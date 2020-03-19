import os
from web3 import Web3
from pymaker import Address
from pymaker.numeric import Rad, Wad
from pymaker.auctions import Flipper
from pycoingecko import CoinGeckoAPI

RPC_URL = os.environ.get(
    'RPC_URL', 'https://mainnet.infura.io/v3/115df92e3d34432fb25fb50b758d0d05')
FLIPPER_CONTRACT = os.environ.get(
    'FLIPPER_CONTRACT', '0xd8a04F5412223F513DC55F839574430f5EC15531')

w3 = Web3(Web3.HTTPProvider(RPC_URL))
gecko = CoinGeckoAPI()

COLLATERAL = "ETH"


def format(val) -> str:
    if isinstance(val, Wad):
        return str(val)[:-16]
    elif isinstance(val, Rad):
        return str(val)[:-42]
    elif isinstance(val, Address):
        return str(val)[0:8]
    elif isinstance(val, float):
        return str(round(val, 2))
    else:
        return str(val)


def print_price_info(bid: Wad, lot: Rad, eth_price: float) -> str:
    price = float(bid) / float(lot)
    discount = 100 * (price - eth_price) / eth_price
    return f"{format(price)} ({ '+' if discount > 0 else ''}{format(discount)}%)"


def main():
    print()
    if not w3.isConnected():
        raise Exception("RPC not connected")

    print(f'Current block {w3.eth.blockNumber}')

    flipper = Flipper(web3=w3, address=Address(FLIPPER_CONTRACT))
    current_block = w3.eth.blockNumber
    eth_price = gecko.get_price(ids='ethereum', vs_currencies='usd')['ethereum']['usd']
    logs = flipper.past_logs(6 * 60 * 4 * 20)

    print(f"Found {len(logs)} logs")
    auctions: dict() = {}

    for log in logs:
        if isinstance(log, Flipper.KickLog):
            auctions[str(log.id)] = [log]
        elif isinstance(log, Flipper.TendLog) or isinstance(log, Flipper.DentLog) or isinstance(log, Flipper.DealLog):
            if str(log.id) in auctions:
                auctions[str(log.id)].append(log)
        else:
            raise Exception("Unknown event")

    print(f"There is {len(auctions)} auctions")
    for id, auction in auctions.items():

        # Kick
        print(
            f"Auction {id} start at {auction[0].block} by {format(auction[0].usr)} for {format(auction[0].lot)} {COLLATERAL}, raise target {format(auction[0].tab)} DAI")

        # Bids
        for i, event in enumerate(auction):
            if isinstance(event, Flipper.TendLog):
                print(
                    f"    Tend bid by {format(event.guy)} raised {format(event.bid)} DAI, price {print_price_info(event.bid, event.lot, eth_price)}")
            elif isinstance(event, Flipper.DentLog):
                print(
                    f"    Dent bid by {format(event.guy)} for {format(event.lot)} {COLLATERAL}, price {print_price_info(event.bid, event.lot, eth_price)}")
            else:
                continue

        # Deal/Status
        if isinstance(auction[-1], Flipper.DealLog):
            # Last log is a deal
            last_bid = auction[-2]
            if isinstance(last_bid, Flipper.TendLog) or isinstance(last_bid, Flipper.DentLog):
                print(
                    f"    Deal won by {format(last_bid.guy)} lot of {format(last_bid.lot)} {COLLATERAL} for {format(last_bid.bid)} DAI, price {print_price_info(last_bid.bid, last_bid.lot, eth_price)}")
            elif isinstance(last_bid, Flipper.KickLog):
                print(f"Auction with no bid, won by the kicker")
        elif isinstance(last_bid, Flipper.TendLog) or isinstance(last_bid, Flipper.DentLog):
            # Last log is a Tend/Dent
            last_bid = auction[-2]
            print(
                f"    Auction pending, block to tick {last_bid.block + 720 - current_block}")
        elif isinstance(last_bid, Flipper.KickLog):
            # Last log is a kick
            print(f"    Auction just kick")


main()
