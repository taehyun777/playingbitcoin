import time
import pyupbit
import datetime

access = "opbQhxfIbyYUcCl1XxKzFuUQNIRc19dckDUlYbup"
secret = "DTZPBPXoWRnxrc03jOmWvzk7iNxEUD6tfr15H3K1"

def get_target_price(ticker, k):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_price

def get_start_time(ticker):
    """시작 시간 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=1)
    start_time = df.index[0]
    return start_time

def get_balance(ticker):
    """잔고 조회"""
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == ticker:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0
    return 0

def get_current_price(ticker):
    """현재가 조회"""
    return pyupbit.get_orderbook(ticker=ticker)["orderbook_units"][0]["ask_price"]

# 로그인
upbit = pyupbit.Upbit(access, secret)
print("autotrade start")

# 자동매매 시작
while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-BTC")
        end_time = start_time + datetime.timedelta(days=1)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-BTC", 0.5)
            current_price = get_current_price("KRW-BTC")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-BTC", krw*0.9995)
        else:
            btc = get_balance("ETH")
            if btc > 0.00008:
                upbit.sell_market_order("KRW-ETH", btc*0.9995),

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-ETH", 0.5)
            current_price = get_current_price("KRW-ETH")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-ETH", krw*0.9995)
        else:
            btc = get_balance("ETH")
            if btc > 0.00008:
                upbit.sell_market_order("KRW-ETH", btc*0.9995),

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-SAND", 0.5)
            current_price = get_current_price("KRW-SAND")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-SAND", krw*0.9995)
        else:
            btc = get_balance("SAND")
            if btc > 0.00008:
                upbit.sell_market_order("KRW-SAND", btc*0.9995),

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-MANA", 0.5)
            current_price = get_current_price("KRW-MANA")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-MANA", krw*0.9995)
        else:
            btc = get_balance("MANA")
            if btc > 0.00008:
                upbit.sell_market_order("KRW-MANA", btc*0.9995),

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-FLOW", 0.5)
            current_price = get_current_price("KRW-FLOW")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-FLOW", krw*0.9995)
        else:
            btc = get_balance("FLOW")
            if btc > 0.00008:
                upbit.sell_market_order("KRW-FLOW", btc*0.9995),

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-ATOM", 0.5)
            current_price = get_current_price("KRW-ATOM")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-ATOM", krw*0.9995)
        else:
            btc = get_balance("ATOM")
            if btc > 0.00008:
                upbit.sell_market_order("KRW-ATOM", btc*0.9995),

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-AXS", 0.5)
            current_price = get_current_price("KRW-AXS")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-AXS", krw*0.9995)
        else:
            btc = get_balance("AXS")
            if btc > 0.00008:
                upbit.sell_market_order("KRW-AXS", btc*0.9995),

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-ONG", 0.5)
            current_price = get_current_price("KRW-ONG")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-ONG", krw*0.9995)
        else:
            btc = get_balance("ONG")
            if btc > 0.00008:
                upbit.sell_market_order("KRW-ONG", btc*0.9995),

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-BORA", 0.5)
            current_price = get_current_price("KRW-BORA")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-BORA", krw*0.9995)
        else:
            btc = get_balance("BORA")
            if btc > 0.00008:
                upbit.sell_market_order("KRW-BORA", btc*0.9995)                                          

        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)
