from datetime import datetime
from .services import *
from moneywagon.core import make_standard_halfing_eras

# instructions for getting version byte:
# https://github.com/MichaelMure/WalletGenerator.net/wiki/How-to-add-a-new-currency#step-two-find-the-prefixes-for-the-address-format-of-your-currency

# also here: https://github.com/MichaelMure/WalletGenerator.net/blob/master/src/janin.currency.js#L78

crypto_data = {
    'btc': {
        'name': 'Bitcoin',
        'address_version_byte': 0,
        'message_magic': b"\xf9\xbe\xb4\xd9",
        'bip44_coin_type': 0x80000000,
        'private_key_prefix': 128,
        'genesis_date': datetime(2009, 1, 3, 18, 15, 5),
        'supply_data': {
            'method': 'standard',
            'start_coins_per_block': 50,
            'minutes_per_block': 10,
            'full_cap': 21000000,
            'blocks_per_era': 210000,
            'reward_ends_at_block': 6930000
        },
        'services': {
            'current_price': [
                Bitstamp, GDAX, Winkdex, BTCE, BTER, BTCChina, Cryptonator, ChainSo,
                Gemini, CexIO, Poloniex, Bittrex, Huobi, Vircurex, YoBit, Yunbi
            ],
            'address_balance': [
                BlockCypher, Blockr, ChainSo,
                BitEasy, SmartBitAU, BlockExplorerCom, BlockChainInfo, Blockonomics,
                BitpayInsight, CoinPrism, BitGo, LocalBitcoinsChain, Bcoin
            ],
            'historical_transactions': [
                Blockr, BlockExplorerCom, BitGo, SmartBitAU, ChainSo, CoinPrism, BlockSeer,
                BitpayInsight, Blockonomics, LocalBitcoinsChain
            ],
            'single_transaction': [
                BitpayInsight, Blockr, BlockCypher, BlockExplorerCom,
                ChainSo, CoinPrism, SmartBitAU, LocalBitcoinsChain
            ],
            'push_tx': [
                BlockChainInfo, BlockExplorerCom, Blockr, ChainSo, CoinPrism,
                BitpayInsight, LocalBitcoinsChain
            ],
            'unspent_outputs': [
                Blockr, BitpayInsight, BlockExplorerCom, SmartBitAU, BlockChainInfo, CoinPrism, ChainSo,
                BitGo, LocalBitcoinsChain
            ],
            'get_block': [
                BitpayInsight, ChainRadar, Blockr, OKcoin, BlockExplorerCom, ChainSo,
                BitGo, LocalBitcoinsChain
            ],
            "get_optimal_fee": [
                BitGo, BlockCypher, CoinTape, BitcoinFees21
            ]
        },
    },
    'ltc': {
        'name': 'Litecoin',
        'address_version_byte': 48,
        'message_magic': b"\xfb\xc0\xb6\xdb",
        'bip44_coin_type': 0x80000002,
        'private_key_prefix': 176,
        'genesis_date': datetime(2011, 10, 7),
        'supply_data': {
            'method': 'standard',
            'start_coins_per_block': 50,
            'minutes_per_block': 2.5,
            'full_cap': 84000000,
            'blocks_per_era': 840000
        },
        'services': {
            'current_price': [
                BTCE, GDAX, ChainSo, BTER, CexIO, Poloniex, Bittrex, BTCChina,
                Vircurex, Cryptonator, YoBit
            ],
            'address_balance': [
                BlockCypher, Blockr, ChainSo, ProHashing, HolyTransaction, Bcoin
            ],
            'historical_transactions': [
                ProHashing, Blockr, ChainSo
            ],
            'single_transaction': [
                Blockr, BlockCypher
            ],
            'push_tx': [
                Blockr, ChainSo
            ],
            'unspent_outputs': [
                ChainSo, Blockr
            ],
            'get_block': [
                ChainSo, Blockr, OKcoin, ProHashing, HolyTransaction
            ]
        },
    },
    'ppc': {
        'name': 'Peercoin',
        'address_version_byte': 55,
        'message_magic': b"\xe6\xe8\xe9\xe5",
        'bip44_coin_type': 0x80000006,
        'private_key_prefix': 183,
        'proof_of_stake': True,
        'genesis_date': datetime(2012, 8, 19, 18, 12, 4),
        'supply_data': {},
        'services': {
            'current_price': [
                BTCE, ChainSo, Bittrex, BTER, Poloniex, Cryptonator, Vircurex,
                YoBit
            ],
            'address_balance': [
                Blockr, Mintr, HolyTransaction
            ],
            'historical_transactions': [
                Blockr
            ],
            'single_transaction': [
                Mintr, Blockr
            ],
            'push_tx': [
                MultiCoins
            ],
            'unspent_outputs': [
                Blockr
            ],
            'get_block': [
                Mintr, HolyTransaction
            ]
        },
    },
    'doge': {
        'name': 'Dogecoin',
        'message_magic': b"\xc0\xc0\xc0\xc0",
        'address_version_byte': 30,
        'bip44_coin_type': 0x80000003,
        'private_key_prefix': 158,
        'genesis_date': datetime(2013, 12, 6, 10, 25, 40),
        'supply_data': {
            'method': 'per_era',
            'eras': [
                {'start': 1,      'end': 100000, 'reward': 500000}, # reward was random, average used
                {'start': 100001, 'end': 144999, 'reward': 250011}, # reward was random, average used
                {'start': 145000, 'end': 200000, 'reward': 250000},
                ] + make_standard_halfing_eras(
                    start=200000, interval=100000,
                    start_reward=125000, total_eras=4
                ) + [
                {'start': 600001, 'end': None,   'reward': 10000}
            ],
            'minutes_per_block': 1.0,
            'full_cap': None,
        },
        'services': {
            'current_price': [
                Bittrex, Poloniex, Cryptonator, ChainSo, BTER, YoBit
            ],
            'address_balance': [
                BlockCypher, ChainSo, DogeChainInfo, ProHashing, HolyTransaction,
                Bcoin
            ],
            'historical_transactions': [
                BlockCypher, ChainSo, ProHashing
            ],
            'single_transaction': [
                BlockCypher, ChainSo
            ],
            'push_tx': [
                ChainSo
            ],
            'unspent_outputs': [
                DogeChainInfo, ChainSo
            ],
            'get_block': [
                ChainSo, ProHashing, HolyTransaction
            ]
        },
    },
    'nxt': {
        'name': 'Nxt',
        'address_version_byte': None,
        'bip44_coin_type': 0x8000001d,
        'private_key_prefix': None,
        'genesis_date': datetime(2013, 10, 29),
        'services': {
            'current_price': [
                Bittrex, ChainSo, Poloniex, Cryptonator
            ],
            'address_balance': [
                MyNXT, NXTPortal
            ],
            'historical_transactions': [
                NXTPortal
            ],
            'single_transaction': [

            ],
            'push_tx': [

            ],
            'unspent_outputs': [

            ],
            'get_block': [

            ]
        },
    },
    'myr': {
        'name': 'MyriadCoin',
        'address_version_byte': 50,
        'message_magic': b"\xaf\x45\x76\xee",
        'bip44_coin_type': 0x8000005a,
        'private_key_prefix': 178,
        'genesis_date': datetime(2014, 2, 23),
        'supply_data': {
            'method': 'standard',
            'start_coins_per_block': 1000,
            'minutes_per_block': 0.5,
            'full_cap': 2000000000,
            'blocks_per_era': 967680
        },
        'services': {
            'current_price': [
                Poloniex, Bittrex, Cryptonator, ChainSo
            ],
            'address_balance': [
                MYRCryptap, CryptapUS, BirdOnWheels, ProHashing
            ],
            'historical_transactions': [
                MYRCryptap, BirdOnWheels, ProHashing
            ],
            'single_transaction': [
                MYRCryptap, BirdOnWheels
            ],
            'push_tx': [
                MYRCryptap, BirdOnWheels
            ],
            'unspent_outputs': [
                MYRCryptap, BirdOnWheels
            ],
            'get_block': [
                MYRCryptap, BirdOnWheels, ProHashing
            ]
        },
    },
    'vtc': {
        'name': 'Vertcoin',
        'address_version_byte': 71,
        'message_magic': b"\xfa\xbf\xb5\xda",
        'bip44_coin_type': 0x8000001c,
        'private_key_prefix': 199,
        'genesis_date': datetime(2014, 1, 8),
        'supply_data': {
            'method': 'standard',
            'start_coins_per_block': 50,
            'minutes_per_block': 2.5,
            'full_cap': 84000000,
            'blocks_per_era': 840000
        },
        'services': {
            'current_price': [
                Poloniex, Bittrex, Cryptonator, ChainSo, YoBit
            ],
            'address_balance': [
                VertcoinInfo, VTConline, Bcoin
            ],
            'historical_transactions': [
                #Verters,
            ],
            'single_transaction': [
                #Verters
            ],
            'push_tx': [
                #Verters
            ],
            'unspent_outputs': [
                #Verters
            ],
            'get_block': [
                #Verters,
            ]
        },
    },
    'ftc': {
        'name': 'Feathercoin',
        'address_version_byte': 14,
        'message_magic': b"\xfb\xc0\xb6\xdb",
        'bip44_coin_type': 0x80000008,
        'private_key_prefix': 0x8e,
        'genesis_date': datetime(2013, 4, 16),
        'supply_data': {
            'method': 'per_era',
            'minutes_per_block': 2.5,
            'eras': [
                {'start': 0,      'end': 204638, 'reward': 200},
                {'start': 204639, 'end': 2100000, 'reward': 80}
            ] + make_standard_halfing_eras(
                start=2100000, interval=2100000,
                start_reward=40
            ),
            'blocktime_adjustments': [
                [0, 2.632061418725984],
                [204639, 1]
            ],
            'full_cap': 336000000,
            'blocks_per_era': 2100000,
        },
        'services': {
            'current_price': [
                Bittrex, ChainSo, Cryptonator, Vircurex
            ],
            'address_balance': [
                ChainTips, FeathercoinCom2, Bcoin
            ],
            'historical_transactions': [
                ChainTips, ProHashing
            ],
            'single_transaction': [
                ChainTips
            ],
            'push_tx': [
                ChainTips
            ],
            'unspent_outputs': [
                ChainTips
            ],
            'get_block': [
                ChainTips, ProHashing
            ]
        },
    },
    'dash': {
        'name': 'Dash',
        'address_version_byte': 76,
        "message_magic": b"\xbf\x0c\x6b\xbd",
        'bip44_coin_type': 0x80000005,
        'private_key_prefix': 204,
        'genesis_date': datetime(2014, 1, 19, 1, 40, 18),
        'supply_data': {
            'method': 'per_era',
            'eras': [
                {'start': 1,   'end': 5000,  'reward': 500}, # "instamine"
                {'start': 5001, 'end': 20000,  'reward': 144},
                {'start': 20001, 'end': 60000, 'reward': 14}
            ] + make_standard_halfing_eras(
                start=60000, interval=210240,
                start_reward=5, halfing_func=lambda era, reward: reward - ((reward/14) * era)
            ),
            'additional_block_interval_adjustment_points': [
                 100, 500, 1000, 3000, 5000
            ],
            'minutes_per_block': 2.5,
            'full_cap': 18900000,
        },
        'services': {
            'current_price': [
                Bittrex, Poloniex, ChainSo, Cryptonator, YoBit
            ],
            'address_balance': [
                MasterNodeIO, ProHashing, CryptoID, SiampmDashInsight, HolyTransaction,
                DashOrgInsight
            ],
            'historical_transactions': [
                ProHashing, DashOrgInsight, SiampmDashInsight, MasterNodeIO
            ],
            'single_transaction': [
                DashOrgInsight, SiampmDashInsight, MasterNodeIO
            ],
            'push_tx': [
                MasterNodeIO, DashOrgInsight, SiampmDashInsight
            ],
            'unspent_outputs': [
                MasterNodeIO, SiampmDashInsight, DashOrgInsight
            ],
            'get_block': [
                ProHashing, SiampmDashInsight, HolyTransaction, MasterNodeIO,
                DashOrgInsight
            ]
        },
    },
    'rdd': {
        'name': 'Reddcoin',
        'address_version_byte': 61,
        'bip44_coin_type': 0x80000004,
        'private_key_prefix': 0xbd,
        'genesis_date': datetime(2014, 1, 20),
        'proof_of_stake': True,
        'services': {
            'current_price': [
                Bittrex, ChainSo, Cryptonator, YoBit
            ],
            'address_balance': [
                ReddcoinCom, ProHashing
            ],
            'historical_transactions': [
                ReddcoinCom, ProHashing
            ],
            'single_transaction': [
                ReddcoinCom
            ],
            'push_tx': [
                ReddcoinCom
            ],
            'unspent_outputs': [
                ReddcoinCom
            ],
            'get_block': [
                ReddcoinCom, ProHashing
            ]
        },
    },

    'nmc': {
        'name': 'Namecoin',
        'address_version_byte': 52,
        'bip44_coin_type': 0x80000007,
        'private_key_prefix': 0x80,
        'genesis_date': datetime(2011, 4, 18),
        'services': {
            'current_price': [
                Poloniex, Cryptonator, YoBit
            ],
            'address_balance': [
                Bcoin
            ]
        }
    },
    'aur': {
        'name': 'Auroracoin',
        'address_version_byte': 23,
        'bip44_coin_type': 0x80000055,
        'private_key_prefix': 0x97,
        'genesis_date': datetime(2014, 2, 2),
        'services': {
            'current_price': [
                Bittrex, Cryptonator, YoBit
            ],
            'address_balance': [
                CryptoID, ProHashing
            ],
            'historical_transactions': [
                ProHashing
            ],
            'single_transaction': [

            ],
            'push_tx': [

            ],
            'unspent_outputs': [
                CryptoID
            ],
            'get_block': [
            ]
        },
    },

    'emc': {
        'name': 'Emercoin',
        'address_version_byte': 33,
        'bip44_coin_type': None,
        'private_key_prefix': None,
        'genesis_date': datetime(2011, 11, 5),
        'services': {
            'current_price': [
                YoBit, Bittrex, Cryptonator
            ],
            'address_balance': [
                Mintr
            ],
            'historical_transactions': [

            ],
            'single_transaction': [
                Mintr
            ],
            'push_tx': [

            ],
            'unspent_outputs': [

            ],
            'get_block': [
                Mintr
            ]
        },
    },

    'gsm': {
        'name': 'GSMcoin',
        'address_version_byte': 38,
        'bip44_coin_type': None,
        'private_key_prefix': None,
        'genesis_date': datetime(1, 1, 1),
        'services': {
            'current_price': [
                YoBit
            ],
            'address_balance': [
            ],
            'historical_transactions': [

            ],
            'single_transaction': [
            ],
            'push_tx': [

            ],
            'unspent_outputs': [

            ],
            'get_block': [
            ]
        },
    },

    'erc': {
        'name': 'Europecoin',
        'address_version_byte': 33,
        'bip44_coin_type': None,
        'private_key_prefix': None,
        'genesis_date': datetime(1, 1, 1),
        'services': {
            'current_price': [
                Bittrex, Cryptonator
            ],
            'address_balance': [
            ],
            'historical_transactions': [

            ],
            'single_transaction': [
            ],
            'push_tx': [

            ],
            'unspent_outputs': [

            ],
            'get_block': [
            ]
        },
    },

    'tx': {
        'name': 'Transfercoin',
        'address_version_byte': 66,
        'bip44_coin_type': None,
        'private_key_prefix': None,
        'genesis_date': datetime(1, 1, 1),
        'services': {
            'current_price': [
                Bittrex, Cryptonator, YoBit
            ],
            'address_balance': [
                CryptoID
            ],
            'historical_transactions': [

            ],
            'single_transaction': [

            ],
            'push_tx': [

            ],
            'unspent_outputs': [
                CryptoID
            ],
            'get_block': [

            ]
        },
    },

    'maid': {
        'name': 'MaidSafeCoin',
        'address_version_byte': 0,
        'bip44_coin_type': None,
        'private_key_prefix': None,
        'genesis_date': datetime(1, 1, 1),
        'services': {
            'current_price': [
                Bittrex, Poloniex, Cryptonator
            ],
            'address_balance': [

            ],
            'historical_transactions': [

            ],
            'single_transaction': [

            ],
            'push_tx': [

            ],
            'unspent_outputs': [

            ],
            'get_block': [

            ]
        },
    },

    'tips': {
        'name': 'FedoraCoin',
        'address_version_byte': 33,
        'bip44_coin_type': None,
        'private_key_prefix': None,
        'genesis_date': datetime(2013, 12, 21),
        'services': {
            'current_price': [
                Cryptonator
            ],
            'address_balance': [
                CryptoID
            ],
            'historical_transactions': [

            ],
            'single_transaction': [

            ],
            'push_tx': [

            ],
            'unspent_outputs': [
                CryptoID
            ],
            'get_block': [

            ]
        },
    },

    'karm': {
        'name': 'Karma',
        'address_version_byte': 45,
        'bip44_coin_type': None,
        'private_key_prefix': None,
        'genesis_date': datetime(2014, 2, 4),
        'services': {
            'current_price': [

            ],
            'address_balance': [
                CryptoID
            ],
            'historical_transactions': [

            ],
            'single_transaction': [

            ],
            'push_tx': [

            ],
            'unspent_outputs': [
                CryptoID
            ],
            'get_block': [

            ]
        },
    },

    'flap': {
        'name': 'FlappyCoin',
        'address_version_byte': 35,
        'bip44_coin_type': None,
        'private_key_prefix': None,
        'genesis_date': datetime(2014, 2, 14),
        'services': {
            'current_price': [

            ],
            'address_balance': [
                CryptoID
            ],
            'historical_transactions': [

            ],
            'single_transaction': [

            ],
            'push_tx': [

            ],
            'unspent_outputs': [
                CryptoID
            ],
            'get_block': [

            ]
        },
    },

    'pot': {
        'name': 'PotCoin',
        'address_version_byte': 55,
        'bip44_coin_type': 0x80000051,
        'private_key_prefix': None,
        'genesis_date': datetime(2014, 1, 21),
        'supply_data': {
            'method': 'standard',
            'start_coins_per_block': 420,
            'minutes_per_block': 0.666666666,
            'full_cap': 420000000,
            'blocks_per_era': 210000
        },
        'services': {
            'current_price': [
                Bittrex, Cryptonator
            ],
            'address_balance': [
                CryptoID, ProHashing
            ],
            'historical_transactions': [
                ProHashing
            ],
            'single_transaction': [

            ],
            'push_tx': [

            ],
            'unspent_outputs': [
                CryptoID
            ],
            'get_block': [
                ProHashing
            ]
        },
    },

    'bqc': {
        'name': 'BBQcoin',
        'address_version_byte': 85,
        'bip44_coin_type': None,
        'private_key_prefix': 213,
        'genesis_date': datetime(2012, 7, 15),
        'services': {
            'current_price': [
                Cryptonator
            ],
            'address_balance': [

            ],
            'historical_transactions': [

            ],
            'single_transaction': [

            ],
            'push_tx': [

            ],
            'unspent_outputs': [

            ],
            'get_block': [

            ]
        },
    },

    'nvc': {
        'name': 'Novacoin',
        'address_version_byte': 8,
        'bip44_coin_type': 0x80000032,
        'private_key_prefix': 136,
        'genesis_date': datetime(2012, 10, 1),
        'services': {
            'current_price': [
                YoBit, Cryptonator
            ],
            'address_balance': [
                CryptapUS, Bcoin
            ],
            'historical_transactions': [

            ],
            'single_transaction': [

            ],
            'push_tx': [

            ],
            'unspent_outputs': [

            ],
            'get_block': [

            ]
        },
    },

    'uno': {
        'name': 'Unobtanium',
        'address_version_byte': 130,
        'bip44_coin_type': 0x8000005c,
        'private_key_prefix': 224,
        'genesis_date': datetime(2013, 10, 17),
        'supply_data': {
            'method': 'standard',
            'full_cap': 250000,
            'blocks_per_era': 100000,
            'minutes_per_block': 3,
        },
        'services': {
            'current_price': [
                Bittrex, Cryptonator
            ],
            'address_balance': [
                UNOCryptap, CryptoID
            ],
            'historical_transactions': [
                UNOCryptap, CryptoID
            ],
            'single_transaction': [
                UNOCryptap
            ],
            'push_tx': [
                UNOCryptap
            ],
            'unspent_outputs': [
                UNOCryptap, CryptoID
            ],
            'get_block': [
                UNOCryptap
            ]
        },
    },

    'ric': {
        'name': 'Riecoin',
        'address_version_byte': 60,
        'bip44_coin_type': 143,
        'private_key_prefix': 128,
        'genesis_date': datetime(2014, 2, 11, 0, 49, 1),
        'supply_data': {
            'method': 'standard',
            'start_coins_per_block': 50,
            'minutes_per_block': 2.5,
            'blocks_per_era': 840000,
        },
        'services': {
            'current_price': [
                Cryptonator
            ],
            'address_balance': [
                RICCryptap, Bcoin, CryptoID
            ],
            'historical_transactions': [
                RICCryptap
            ],
            'single_transaction': [
                RICCryptap
            ],
            'push_tx': [
                RICCryptap
            ],
            'unspent_outputs': [
                RICCryptap, CryptoID
            ],
            'get_block': [
                RICCryptap
            ]
        },
    },

    'xrp': {
        'name': 'Ripple',
        'genesis_date': datetime(2011, 3, 1),
        'services': {
            'current_price': [
                Bittrex, Poloniex, Cryptonator
            ],
        }
    },

    'hemp': {
        'name': 'Hempcoin',
        'address_version_byte': 40,
        'bip44_coin_type': None,
        'private_key_prefix': None,
        'genesis_date': datetime(1, 1, 1),
        'services': {
            'current_price': [

            ],
            'address_balance': [
                BlockExperts
            ],
            'historical_transactions': [

            ],
            'single_transaction': [
                BlockExperts
            ],
            'push_tx': [

            ],
            'unspent_outputs': [

            ],
            'get_block': [
                BlockExperts
            ]
        },
    },

    'dope': {
        'name': 'Dopecoin',
        'address_version_byte': 8,
        'bip44_coin_type': None,
        'private_key_prefix': None,
        'genesis_date': datetime(1, 1, 1),
        'services': {
            'current_price': [
                Bittrex, Cryptonator
            ],
            'address_balance': [
                BlockExperts
            ],
            'historical_transactions': [

            ],
            'single_transaction': [
                BlockExperts
            ],
            'push_tx': [

            ],
            'unspent_outputs': [

            ],
            'get_block': [
                BlockExperts
            ]
        },
    },

    'dime': {
        'name': 'Dimecoin',
        'address_version_byte': 15,
        'bip44_coin_type': None,
        'private_key_prefix': None,
        'genesis_date': datetime(2014, 12, 23),
        'services': {
            'current_price': [
                YoBit, Cryptonator
            ],
            'address_balance': [
                BlockExperts
            ],
            'historical_transactions': [

            ],
            'single_transaction': [
                BlockExperts
            ],
            'push_tx': [

            ],
            'unspent_outputs': [

            ],
            'get_block': [
                BlockExperts
            ]
        },
    },

    'xcp': {
        'name': 'CounterParty',
        'address_version_byte': 0,
        'bip44_coin_type': 0x80000009,
        'private_key_prefix': 128,
        'genesis_date': datetime(2014, 1, 2),
        'services': {
            'current_price': [
                Bittrex, Poloniex, Cryptonator
            ],
            'address_balance': [
                CoinDaddy1, CoinDaddy2, CounterPartyChain
            ],
            'historical_transactions': [
                CoinDaddy1, CoinDaddy2
            ],
            'single_transaction': [
                CoinDaddy1, CoinDaddy2
            ],
            'push_tx': [
                CoinDaddy1, CoinDaddy2
            ],
            'unspent_outputs': [
                CoinDaddy1
            ],
            'get_block': [
                CoinDaddy1, CoinDaddy2
            ]
        },
    },

    'eth': {
        'name': 'Ethereum',
        'address_version_byte': None,
        'bip44_coin_type': 0x8000003c,
        'private_key_prefix': None,
        'genesis_date': datetime(2015, 7, 30),
        'supply_data': {
            'instamine': 72009990.50
        },
        'services': {
            'current_price': [
                Poloniex, GDAX, Bittrex, CexIO, EtherChain, YoBit, Cryptonator,
                Yunbi
            ],
            'address_balance': [
                Etherscan, EtherChain, ETCchain
            ],
            'historical_transactions': [

            ],
            'single_transaction': [

            ],
            'push_tx': [

            ],
            'unspent_outputs': [

            ],
            'get_block': [

            ]
        },
    },

    'etc': {
        'name': 'Ethereum Classic',
        'address_version_byte': None,
        'bip44_coin_type': 0x8000003d,
        'private_key_prefix': None,
        'genesis_date': datetime(2016, 7, 20),
        'services': {
            'current_price': [
                Poloniex, Bittrex, YoBit, Yunbi
            ],
            'address_balance': [
                ETCchain
            ]
        },
    },

    'xmr': {
        'name': 'Monero',
        'address_version_byte': None,
        'bip44_coin_type': 0x80000080,
        'private_key_prefix': None,
        'genesis_date': datetime(2014, 4, 18),
        'services': {
            'current_price': [
                Bittrex, Poloniex
            ]
        }
    },

    'blk': {
        'name': 'Blackcoin',
        'message_magic': b"\x70\x35\x22\x05",
        'address_version_byte': 25,
        'bip44_coin_type': 0x8000000a,
        'private_key_prefix': 153,
        'genesis_date': datetime(1, 1, 1),
        'services': {
            'current_price': [
                Poloniex
            ],
            'address_balance': [
                HolyTransaction, Bcoin
            ],
            'historical_transactions': [

            ],
            'single_transaction': [

            ],
            'push_tx': [

            ],
            'unspent_outputs': [

            ],
            'get_block': [

            ]
        },
    },

    'xpm': {
        'name': 'Primecoin',
        'address_version_byte': 23,
        'bip44_coin_type': 0x80000018,
        'private_key_prefix': 151,
        'genesis_date': datetime(1, 1, 1),
        'services': {
            'current_price': [
                Poloniex
            ],
            'address_balance': [
                Bcoin
            ],
            'historical_transactions': [

            ],
            'single_transaction': [

            ],
            'push_tx': [

            ],
            'unspent_outputs': [

            ],
            'get_block': [

            ]
        },
    },

    'pivx': {
        'name': 'PivX',
        'address_version_byte': 30,
        'bip44_coin_type': 0x80000077,
        'private_key_prefix': 212,
        'genesis_date': datetime(1, 1, 1),
        'services': {
            'current_price': [
                Bittrex
            ],
            'address_balance': [
                PressTab, CryptoID
            ],
            'historical_transactions': [

            ],
            'single_transaction': [
                CryptoID
            ],
            'push_tx': [

            ],
            'unspent_outputs': [
                CryptoID
            ],
            'get_block': [

            ]
        },
    },
    'zec': {
        'name': 'ZCash',
        'address_version_byte': None,
        'bip44_coin_type': None,
        'private_key_prefix': None,
        'genesis_date': datetime(1, 1, 1),
        'services': {
            'current_price': [
                Bittrex
            ],
            'address_balance': [
                ZChain
            ],
            'historical_transactions': [

            ],
            'single_transaction': [

            ],
            'push_tx': [

            ],
            'unspent_outputs': [

            ],
            'get_block': [

            ]
        },
    },


    # TEMPLATE
    '': {
        'name': '',
        'address_version_byte': None,
        'bip44_coin_type': None,
        'private_key_prefix': None,
        'genesis_date': datetime(1, 1, 1),
        'services': {
            'current_price': [

            ],
            'address_balance': [

            ],
            'historical_transactions': [

            ],
            'single_transaction': [

            ],
            'push_tx': [

            ],
            'unspent_outputs': [

            ],
            'get_block': [

            ]
        },
    }
}
