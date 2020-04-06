import json
import sys
from typing import List

import time
from web3 import Web3
from pymaker import Address
from pymaker.numeric import Rad, Wad
from pymaker.auctions import Flipper, LogNote

from uniswap import UNISWAP_ABI

# IMPORTANT: Require the pymaker library: https://github.com/makerdao/pymaker and web3 py
# add them to the python path.

SKIP_BID_DETAILS = False

START_BLOCK = 8928180   # w3.eth.blockNumber - 15000

UNISWAP_EXCHANGE = ""

ilk = sys.argv[1]

if ilk == 'ETH-mainnet':
    RPC_URL = "https://parity0.mainnet.makerfoundation.com:8545"
    MAKER_OSM = "0x81FE72B5A8d1A857d176C3E7d5Bd2679A9B85763"
    FLIPPER_CONTRACT = "0xd8a04F5412223F513DC55F839574430f5EC15531"
    COLLATERAL = "ETH"
    UNISWAP_EXCHANGE = "0x2a1530C4C41db0B0b2bB646CB5Eb1A67b7158667"
elif ilk == 'BAT-mainnet':
    RPC_URL = "https://parity0.mainnet.makerfoundation.com:8545"
    MAKER_OSM = "0xB4eb54AF9Cc7882DF0121d26c5b97E802915ABe6"
    FLIPPER_CONTRACT = "0xaA745404d55f88C108A28c86abE7b5A1E7817c07"
    COLLATERAL = "BAT"
    UNISWAP_EXCHANGE = "0x2E642b8D59B45a1D8c5aEf716A84FF44ea665914"
elif ilk == 'USDC-mainnet':
    RPC_URL = "https://parity0.mainnet.makerfoundation.com:8545"
    MAKER_OSM = "0x77b68899b99b686F415d074278a9a16b336085A0"
    FLIPPER_CONTRACT = "0xE6ed1d09a19Bd335f051d78D5d22dF3bfF2c28B1"
    COLLATERAL = "USDC"
    UNISWAP_EXCHANGE = "0x97deC872013f6B5fB443861090ad931542878126"
elif ilk == 'ETH-kovan':
    RPC_URL = "https://parity0.kovan.makerfoundation.com:8545"
    FLIPPER_CONTRACT = "0xB40139Ea36D35d0C9F6a2e62601B616F1FfbBD1b"
    MAKER_OSM = "0x75dD74e8afE8110C8320eD397CcCff3B8134d981"
    COLLATERAL = "ETH"
elif ilk == 'BAT-kovan':
    RPC_URL = "https://parity0.kovan.makerfoundation.com:8545"
    FLIPPER_CONTRACT = "0xC94014A032cA5fCc01271F4519Add7E87a16b94C"
    MAKER_OSM = "0x5C40C9Eb35c76069fA4C3A00EA59fAc6fFA9c113"
    COLLATERAL = "BAT"
elif ilk == 'USDC-kovan':
    RPC_URL = "https://parity0.kovan.makerfoundation.com:8545"
    FLIPPER_CONTRACT = "0x45d5b4A304f554262539cfd167dd05e331Da686E"
    MAKER_OSM = "0x4c51c2584309b7BF328F89609FDd03B3b95fC677"
    COLLATERAL = "USDC"
else:
    raise IOError("Need network (i.g: 'ETH-mainnet')")


OSM_ABI = json.load(open('./lib/pymaker/pymaker/abi/OSM.abi'))
w3 = Web3(Web3.HTTPProvider(RPC_URL))
csv = open("data.csv", "a")
csv.write("id,start_block,end_block,lot,tab,n_bids,final_lot,final_bid,final_price,discount_OSM,ETH_price_OSM,discount_uniswap,ETH_price_uniswap,winner,dealer\n")
END_BLOCK = w3.eth.blockNumber

if 'mainnet' in RPC_URL:
    uniswap = w3.eth.contract(address=UNISWAP_EXCHANGE, abi=UNISWAP_ABI)


def get_OSM_price_at_block(block: int) -> float:
    OSM_contract = w3.eth.contract(address=MAKER_OSM, abi=OSM_ABI)
    logs = OSM_contract.events.LogValue().createFilter(
        fromBlock=block - 2000, toBlock=block).get_all_entries()
    if len(logs) == 0:
        return sys.float_info.min

    price = w3.fromWei(
        w3.toInt(logs[-1].args.val), "ether")
    return float(price)


def get_uniswap_price(block: int) -> float:
    if 'mainnet' not in RPC_URL:
        return 1
    else:
        return uniswap.functions.getEthToTokenInputPrice(10**18).call(block_identifier=block) * 10 ** -18


def format(val) -> str:

    def pad(val, pad=5):
        while len(val.split(".")[0]) < pad:
            val = " " + val

        return val

    if isinstance(val, Wad):
        return pad(str(val)[:-16])
    elif isinstance(val, Rad):
        return pad(str(val)[:-42])
    elif isinstance(val, Address):
        return str(val)[0:12]
    elif isinstance(val, float):
        return pad(str(round(val, 2)), 3)
    else:
        return str(val)


def print_price_info(bid: Wad, lot: Rad, block: int) -> str:
    OSM_eth_price = get_OSM_price_at_block(block)
    uniswap_price = get_uniswap_price(block)
    price = float(bid) / float(lot)
    OSM_discount = 100 * ((price - OSM_eth_price) / OSM_eth_price)
    uniswap_discount = 100 * ((price - uniswap_price) / uniswap_price)

    # timestamp = w3.eth.getBlock(block).timestamp
    return OSM_eth_price, uniswap_price, f"{format(price)} OSM({ '+' if OSM_discount > 0 else '-'}{format(abs(OSM_discount))}%) UNS({ '+' if OSM_discount > 0 else '-'}{format(abs(uniswap_discount))}%)"


def print_auction_details(auction: List[LogNote], current_block: int):

    # Kick
    print(
        f"Auction {auction[0].id} start at {auction[0].block} by {format(auction[0].usr)} for {format(auction[0].lot)} {COLLATERAL}, raise target {format(auction[0].tab)} DAI")

    start_time = w3.eth.getBlock(auction[0].block).timestamp

    if not SKIP_BID_DETAILS:
        # Bids
        for i, event in enumerate(auction):
            if isinstance(event, Flipper.TendLog):
                print(
                    f"    Tend bid by {format(event.guy)} at block {format(event.block)} raised {format(event.bid)} DAI, price {print_price_info(event.bid, event.lot, event.block)[2]}")
            elif isinstance(event, Flipper.DentLog):
                print(
                    f"    Dent bid by {format(event.guy)} at block {format(event.block)}    for {format(event.lot)} {COLLATERAL},  price {print_price_info(event.bid, event.lot, event.block)[2]}")
            else:
                continue

    # Deal/Status
    if isinstance(auction[-1], Flipper.DealLog):
        # Deal

        # Last log is a deal/auction finished
        last_bid = auction[-2]
        if isinstance(last_bid, Flipper.TendLog) or isinstance(last_bid, Flipper.DentLog):
            # They was at least one bid during the auction

            price_OSM, price_uniswap, price_print = print_price_info(
                last_bid.bid, last_bid.lot, last_bid.block)
            print(
                f"    Deal won by {format(last_bid.guy)} at block {auction[-1].block} lot of {format(last_bid.lot)} {COLLATERAL},  price {price_print}")
            final_price = float(last_bid.bid) / float(last_bid.lot)
            discount_OSM = (price_OSM - final_price) / price_OSM
            discount_uniswap = (price_uniswap - final_price) / price_uniswap
            n_bids = len(auction) - 2
            # Write to CSV file, columns:
            # id,start_block,end_block,lot,tab,n_bids,final_lot,final_bid,final_price,discount_OSM,ETH_price_OSM,discount_uniswap,ETH_price_uniswap,winner,dealer
            csv.write(
                f"{auction[0].id},{auction[0].block},{auction[-1].block},{auction[0].lot},{format(auction[0].tab)},{n_bids},{last_bid.lot},{last_bid.bid},{final_price},{discount_OSM},{price_OSM},{discount_uniswap},{price_uniswap},{last_bid.guy},{auction[-1].usr}\n")
        elif isinstance(last_bid, Flipper.KickLog):
            print(f"Auction with no bid, won by the kicker")
    elif isinstance(auction[-1], Flipper.TendLog) or isinstance(auction[-1], Flipper.DentLog):
        # Last log is a Tend/Dent
        last_bid = auction[-2]
        print(
            f"    Auction pending, block to tick {(start_time + 6*60*60  - time.time())/60} min")
    elif isinstance(auction[-1], Flipper.KickLog):
        # Last log is a kick
        print(f"Auction just kick")


def main():
    if not w3.isConnected():
        raise Exception("RPC not connected")

    print(f'Current block {w3.eth.blockNumber}')

    flipper = Flipper(web3=w3, address=Address(FLIPPER_CONTRACT))
    current_block = w3.eth.blockNumber

    # Fetch logs
    logs: List[LogNote] = []
    block = START_BLOCK
    block_batch = 5000
    while block < END_BLOCK:
        print(f"Fetch logs from block {block} to {block + block_batch}")
        new_logs = flipper.past_logs_block_range(
            block, min(block + block_batch, current_block))
        logs += new_logs
        block += block_batch
        print(f"Found {len(new_logs)} logs")

    auctions: dict() = {}

    # Process logs
    for log in logs:
        if isinstance(log, Flipper.KickLog):
            auctions[str(log.id)] = [log]
        elif isinstance(log, Flipper.TendLog) or isinstance(log, Flipper.DentLog) or isinstance(log, Flipper.DealLog):
            if str(log.id) in auctions:
                auctions[str(log.id)].append(log)
        else:
            raise Exception("Unknown event")

    print(f"Found {len(logs)} logs for {len(auctions)} auctions")
    print("==================================")

    # Print details for each auction
    for id, auction in auctions.items():
        print_auction_details(auction, current_block)


main()
