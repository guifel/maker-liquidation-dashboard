UNISWAP_ABI = [
    {
        "name": "TokenPurchase",
        "inputs": [
            {
                "type": "address",
                "name": "buyer",
                "indexed": True
            },
            {
                "type": "uint256",
                "name": "eth_sold",
                "indexed": True
            },
            {
                "type": "uint256",
                "name": "tokens_bought",
                "indexed": True
            }
        ],
        "anonymous": False,
        "type": "event"
    },
    {
        "name": "EthPurchase",
        "inputs": [
            {
                "type": "address",
                "name": "buyer",
                "indexed": True
            },
            {
                "type": "uint256",
                "name": "tokens_sold",
                "indexed": True
            },
            {
                "type": "uint256",
                "name": "eth_bought",
                "indexed": True
            }
        ],
        "anonymous": False,
        "type": "event"
    },
    {
        "name": "AddLiquidity",
        "inputs": [
            {
                "type": "address",
                "name": "provider",
                "indexed": True
            },
            {
                "type": "uint256",
                "name": "eth_amount",
                "indexed": True
            },
            {
                "type": "uint256",
                "name": "token_amount",
                "indexed": True
            }
        ],
        "anonymous": False,
        "type": "event"
    },
    {
        "name": "RemoveLiquidity",
        "inputs": [
            {
                "type": "address",
                "name": "provider",
                "indexed": True
            },
            {
                "type": "uint256",
                "name": "eth_amount",
                "indexed": True
            },
            {
                "type": "uint256",
                "name": "token_amount",
                "indexed": True
            }
        ],
        "anonymous": False,
        "type": "event"
    },
    {
        "name": "Transfer",
        "inputs": [
            {
                "type": "address",
                "name": "_from",
                "indexed": True
            },
            {
                "type": "address",
                "name": "_to",
                "indexed": True
            },
            {
                "type": "uint256",
                "name": "_value",
                "indexed": False
            }
        ],
        "anonymous": False,
        "type": "event"
    },
    {
        "name": "Approval",
        "inputs": [
            {
                "type": "address",
                "name": "_owner",
                "indexed": True
            },
            {
                "type": "address",
                "name": "_spender",
                "indexed": True
            },
            {
                "type": "uint256",
                "name": "_value",
                "indexed": False
            }
        ],
        "anonymous": False,
        "type": "event"
    },
    {
        "name": "setup",
        "outputs": [],
        "inputs": [
            {
                "type": "address",
                "name": "token_addr"
            }
        ],
        "constant": False,
        "payable": False,
        "type": "function",
        "gas": 175875
    },
    {
        "name": "addLiquidity",
        "outputs": [
            {
                "type": "uint256",
                "name": "out"
            }
        ],
        "inputs": [
            {
                "type": "uint256",
                "name": "min_liquidity"
            },
            {
                "type": "uint256",
                "name": "max_tokens"
            },
            {
                "type": "uint256",
                "name": "deadline"
            }
        ],
        "constant": False,
        "payable": True,
        "type": "function",
        "gas": 82605
    },
    {
        "name": "removeLiquidity",
        "outputs": [
            {
                "type": "uint256",
                "name": "out"
            },
            {
                "type": "uint256",
                "name": "out"
            }
        ],
        "inputs": [
            {
                "type": "uint256",
                "name": "amount"
            },
            {
                "type": "uint256",
                "name": "min_eth"
            },
            {
                "type": "uint256",
                "name": "min_tokens"
            },
            {
                "type": "uint256",
                "name": "deadline"
            }
        ],
        "constant": False,
        "payable": False,
        "type": "function",
        "gas": 116814
    },
    {
        "name": "__default__",
        "outputs": [],
        "inputs": [],
        "constant": False,
        "payable": True,
        "type": "function"
    },
    {
        "name": "ethToTokenSwapInput",
        "outputs": [
            {
                "type": "uint256",
                "name": "out"
            }
        ],
        "inputs": [
            {
                "type": "uint256",
                "name": "min_tokens"
            },
            {
                "type": "uint256",
                "name": "deadline"
            }
        ],
        "constant": False,
        "payable": True,
        "type": "function",
        "gas": 12757
    },
    {
        "name": "ethToTokenTransferInput",
        "outputs": [
            {
                "type": "uint256",
                "name": "out"
            }
        ],
        "inputs": [
            {
                "type": "uint256",
                "name": "min_tokens"
            },
            {
                "type": "uint256",
                "name": "deadline"
            },
            {
                "type": "address",
                "name": "recipient"
            }
        ],
        "constant": False,
        "payable": True,
        "type": "function",
        "gas": 12965
    },
    {
        "name": "ethToTokenSwapOutput",
        "outputs": [
            {
                "type": "uint256",
                "name": "out"
            }
        ],
        "inputs": [
            {
                "type": "uint256",
                "name": "tokens_bought"
            },
            {
                "type": "uint256",
                "name": "deadline"
            }
        ],
        "constant": False,
        "payable": True,
        "type": "function",
        "gas": 50455
    },
    {
        "name": "ethToTokenTransferOutput",
        "outputs": [
            {
                "type": "uint256",
                "name": "out"
            }
        ],
        "inputs": [
            {
                "type": "uint256",
                "name": "tokens_bought"
            },
            {
                "type": "uint256",
                "name": "deadline"
            },
            {
                "type": "address",
                "name": "recipient"
            }
        ],
        "constant": False,
        "payable": True,
        "type": "function",
        "gas": 50663
    },
    {
        "name": "tokenToEthSwapInput",
        "outputs": [
            {
                "type": "uint256",
                "name": "out"
            }
        ],
        "inputs": [
            {
                "type": "uint256",
                "name": "tokens_sold"
            },
            {
                "type": "uint256",
                "name": "min_eth"
            },
            {
                "type": "uint256",
                "name": "deadline"
            }
        ],
        "constant": False,
        "payable": False,
        "type": "function",
        "gas": 47503
    },
    {
        "name": "tokenToEthTransferInput",
        "outputs": [
            {
                "type": "uint256",
                "name": "out"
            }
        ],
        "inputs": [
            {
                "type": "uint256",
                "name": "tokens_sold"
            },
            {
                "type": "uint256",
                "name": "min_eth"
            },
            {
                "type": "uint256",
                "name": "deadline"
            },
            {
                "type": "address",
                "name": "recipient"
            }
        ],
        "constant": False,
        "payable": False,
        "type": "function",
        "gas": 47712
    },
    {
        "name": "tokenToEthSwapOutput",
        "outputs": [
            {
                "type": "uint256",
                "name": "out"
            }
        ],
        "inputs": [
            {
                "type": "uint256",
                "name": "eth_bought"
            },
            {
                "type": "uint256",
                "name": "max_tokens"
            },
            {
                "type": "uint256",
                "name": "deadline"
            }
        ],
        "constant": False,
        "payable": False,
        "type": "function",
        "gas": 50175
    },
    {
        "name": "tokenToEthTransferOutput",
        "outputs": [
            {
                "type": "uint256",
                "name": "out"
            }
        ],
        "inputs": [
            {
                "type": "uint256",
                "name": "eth_bought"
            },
            {
                "type": "uint256",
                "name": "max_tokens"
            },
            {
                "type": "uint256",
                "name": "deadline"
            },
            {
                "type": "address",
                "name": "recipient"
            }
        ],
        "constant": False,
        "payable": False,
        "type": "function",
        "gas": 50384
    },
    {
        "name": "tokenToTokenSwapInput",
        "outputs": [
            {
                "type": "uint256",
                "name": "out"
            }
        ],
        "inputs": [
            {
                "type": "uint256",
                "name": "tokens_sold"
            },
            {
                "type": "uint256",
                "name": "min_tokens_bought"
            },
            {
                "type": "uint256",
                "name": "min_eth_bought"
            },
            {
                "type": "uint256",
                "name": "deadline"
            },
            {
                "type": "address",
                "name": "token_addr"
            }
        ],
        "constant": False,
        "payable": False,
        "type": "function",
        "gas": 51007
    },
    {
        "name": "tokenToTokenTransferInput",
        "outputs": [
            {
                "type": "uint256",
                "name": "out"
            }
        ],
        "inputs": [
            {
                "type": "uint256",
                "name": "tokens_sold"
            },
            {
                "type": "uint256",
                "name": "min_tokens_bought"
            },
            {
                "type": "uint256",
                "name": "min_eth_bought"
            },
            {
                "type": "uint256",
                "name": "deadline"
            },
            {
                "type": "address",
                "name": "recipient"
            },
            {
                "type": "address",
                "name": "token_addr"
            }
        ],
        "constant": False,
        "payable": False,
        "type": "function",
        "gas": 51098
    },
    {
        "name": "tokenToTokenSwapOutput",
        "outputs": [
            {
                "type": "uint256",
                "name": "out"
            }
        ],
        "inputs": [
            {
                "type": "uint256",
                "name": "tokens_bought"
            },
            {
                "type": "uint256",
                "name": "max_tokens_sold"
            },
            {
                "type": "uint256",
                "name": "max_eth_sold"
            },
            {
                "type": "uint256",
                "name": "deadline"
            },
            {
                "type": "address",
                "name": "token_addr"
            }
        ],
        "constant": False,
        "payable": False,
        "type": "function",
        "gas": 54928
    },
    {
        "name": "tokenToTokenTransferOutput",
        "outputs": [
            {
                "type": "uint256",
                "name": "out"
            }
        ],
        "inputs": [
            {
                "type": "uint256",
                "name": "tokens_bought"
            },
            {
                "type": "uint256",
                "name": "max_tokens_sold"
            },
            {
                "type": "uint256",
                "name": "max_eth_sold"
            },
            {
                "type": "uint256",
                "name": "deadline"
            },
            {
                "type": "address",
                "name": "recipient"
            },
            {
                "type": "address",
                "name": "token_addr"
            }
        ],
        "constant": False,
        "payable": False,
        "type": "function",
        "gas": 55019
    },
    {
        "name": "tokenToExchangeSwapInput",
        "outputs": [
            {
                "type": "uint256",
                "name": "out"
            }
        ],
        "inputs": [
            {
                "type": "uint256",
                "name": "tokens_sold"
            },
            {
                "type": "uint256",
                "name": "min_tokens_bought"
            },
            {
                "type": "uint256",
                "name": "min_eth_bought"
            },
            {
                "type": "uint256",
                "name": "deadline"
            },
            {
                "type": "address",
                "name": "exchange_addr"
            }
        ],
        "constant": False,
        "payable": False,
        "type": "function",
        "gas": 49342
    },
    {
        "name": "tokenToExchangeTransferInput",
        "outputs": [
            {
                "type": "uint256",
                "name": "out"
            }
        ],
        "inputs": [
            {
                "type": "uint256",
                "name": "tokens_sold"
            },
            {
                "type": "uint256",
                "name": "min_tokens_bought"
            },
            {
                "type": "uint256",
                "name": "min_eth_bought"
            },
            {
                "type": "uint256",
                "name": "deadline"
            },
            {
                "type": "address",
                "name": "recipient"
            },
            {
                "type": "address",
                "name": "exchange_addr"
            }
        ],
        "constant": False,
        "payable": False,
        "type": "function",
        "gas": 49532
    },
    {
        "name": "tokenToExchangeSwapOutput",
        "outputs": [
            {
                "type": "uint256",
                "name": "out"
            }
        ],
        "inputs": [
            {
                "type": "uint256",
                "name": "tokens_bought"
            },
            {
                "type": "uint256",
                "name": "max_tokens_sold"
            },
            {
                "type": "uint256",
                "name": "max_eth_sold"
            },
            {
                "type": "uint256",
                "name": "deadline"
            },
            {
                "type": "address",
                "name": "exchange_addr"
            }
        ],
        "constant": False,
        "payable": False,
        "type": "function",
        "gas": 53233
    },
    {
        "name": "tokenToExchangeTransferOutput",
        "outputs": [
            {
                "type": "uint256",
                "name": "out"
            }
        ],
        "inputs": [
            {
                "type": "uint256",
                "name": "tokens_bought"
            },
            {
                "type": "uint256",
                "name": "max_tokens_sold"
            },
            {
                "type": "uint256",
                "name": "max_eth_sold"
            },
            {
                "type": "uint256",
                "name": "deadline"
            },
            {
                "type": "address",
                "name": "recipient"
            },
            {
                "type": "address",
                "name": "exchange_addr"
            }
        ],
        "constant": False,
        "payable": False,
        "type": "function",
        "gas": 53423
    },
    {
        "name": "getEthToTokenInputPrice",
        "outputs": [
            {
                "type": "uint256",
                "name": "out"
            }
        ],
        "inputs": [
            {
                "type": "uint256",
                "name": "eth_sold"
            }
        ],
        "constant": True,
        "payable": False,
        "type": "function",
        "gas": 5542
    },
    {
        "name": "getEthToTokenOutputPrice",
        "outputs": [
            {
                "type": "uint256",
                "name": "out"
            }
        ],
        "inputs": [
            {
                "type": "uint256",
                "name": "tokens_bought"
            }
        ],
        "constant": True,
        "payable": False,
        "type": "function",
        "gas": 6872
    },
    {
        "name": "getTokenToEthInputPrice",
        "outputs": [
            {
                "type": "uint256",
                "name": "out"
            }
        ],
        "inputs": [
            {
                "type": "uint256",
                "name": "tokens_sold"
            }
        ],
        "constant": True,
        "payable": False,
        "type": "function",
        "gas": 5637
    },
    {
        "name": "getTokenToEthOutputPrice",
        "outputs": [
            {
                "type": "uint256",
                "name": "out"
            }
        ],
        "inputs": [
            {
                "type": "uint256",
                "name": "eth_bought"
            }
        ],
        "constant": True,
        "payable": False,
        "type": "function",
        "gas": 6897
    },
    {
        "name": "tokenAddress",
        "outputs": [
            {
                "type": "address",
                "name": "out"
            }
        ],
        "inputs": [],
        "constant": True,
        "payable": False,
        "type": "function",
        "gas": 1413
    },
    {
        "name": "factoryAddress",
        "outputs": [
            {
                "type": "address",
                "name": "out"
            }
        ],
        "inputs": [],
        "constant": True,
        "payable": False,
        "type": "function",
        "gas": 1443
    },
    {
        "name": "balanceOf",
        "outputs": [
            {
                "type": "uint256",
                "name": "out"
            }
        ],
        "inputs": [
            {
                "type": "address",
                "name": "_owner"
            }
        ],
        "constant": True,
        "payable": False,
        "type": "function",
        "gas": 1645
    },
    {
        "name": "transfer",
        "outputs": [
            {
                "type": "bool",
                "name": "out"
            }
        ],
        "inputs": [
            {
                "type": "address",
                "name": "_to"
            },
            {
                "type": "uint256",
                "name": "_value"
            }
        ],
        "constant": False,
        "payable": False,
        "type": "function",
        "gas": 75034
    },
    {
        "name": "transferFrom",
        "outputs": [
            {
                "type": "bool",
                "name": "out"
            }
        ],
        "inputs": [
            {
                "type": "address",
                "name": "_from"
            },
            {
                "type": "address",
                "name": "_to"
            },
            {
                "type": "uint256",
                "name": "_value"
            }
        ],
        "constant": False,
        "payable": False,
        "type": "function",
        "gas": 110907
    },
    {
        "name": "approve",
        "outputs": [
            {
                "type": "bool",
                "name": "out"
            }
        ],
        "inputs": [
            {
                "type": "address",
                "name": "_spender"
            },
            {
                "type": "uint256",
                "name": "_value"
            }
        ],
        "constant": False,
        "payable": False,
        "type": "function",
        "gas": 38769
    },
    {
        "name": "allowance",
        "outputs": [
            {
                "type": "uint256",
                "name": "out"
            }
        ],
        "inputs": [
            {
                "type": "address",
                "name": "_owner"
            },
            {
                "type": "address",
                "name": "_spender"
            }
        ],
        "constant": True,
        "payable": False,
        "type": "function",
        "gas": 1925
    },
    {
        "name": "name",
        "outputs": [
            {
                "type": "bytes32",
                "name": "out"
            }
        ],
        "inputs": [],
        "constant": True,
        "payable": False,
        "type": "function",
        "gas": 1623
    },
    {
        "name": "symbol",
        "outputs": [
            {
                "type": "bytes32",
                "name": "out"
            }
        ],
        "inputs": [],
        "constant": True,
        "payable": False,
        "type": "function",
        "gas": 1653
    },
    {
        "name": "decimals",
        "outputs": [
            {
                "type": "uint256",
                "name": "out"
            }
        ],
        "inputs": [],
        "constant": True,
        "payable": False,
        "type": "function",
        "gas": 1683
    },
    {
        "name": "totalSupply",
        "outputs": [
            {
                "type": "uint256",
                "name": "out"
            }
        ],
        "inputs": [],
        "constant": True,
        "payable": False,
        "type": "function",
        "gas": 1713
    }
]

