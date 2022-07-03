import requests

key_btc = "https://api.binance.com/api/v3/avgPrice?symbol=BTCUSDT"
key_eth = "https://api.binance.com/api/v3/avgPrice?symbol=ETHUSDT"
key_bnb = "https://api.binance.com/api/v3/avgPrice?symbol=BNBUSDT"
key_xrp = "https://api.binance.com/api/v3/avgPrice?symbol=XRPUSDT"
key_ada = "https://api.binance.com/api/v3/avgPrice?symbol=ADAUSDT"


def get_real_time_price(key: str):
    result = requests.get(key)
    result = result.json()
    result = result['price']
    return result


BTC_price = get_real_time_price(key_btc)
ETH_price = get_real_time_price(key_eth)
BNB_price = get_real_time_price(key_bnb)
XRP_price = get_real_time_price(key_xrp)
ADA_price = get_real_time_price(key_ada)

print("Price tags on the top 5 crypto currencies in 2022:")
print(f"Current price of BTC {float(BTC_price):.2f}$")
print(f"Current price of ETH {float(ETH_price):.2f}$")
print(f"Current price of BNB {float(BNB_price):.2f}$")
print(f"Current price of XRP {float(XRP_price):.2f}$")
print(f"Current price of ADA {float(ADA_price):.2f}$")
