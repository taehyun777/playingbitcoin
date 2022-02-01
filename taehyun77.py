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

def get_ma15(ticker):
    """15일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=15)
    ma15 = df['close'].rolling(15).mean().iloc[-1]
    return ma15

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
            ma15 = get_ma15("KRW-BTC")
            current_price = get_current_price("KRW-BTC")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-BTC", krw*0.9995)
        else:
            btc = get_balance("BTC")
            if btc > 0.00008:
                upbit.sell_market_order("KRW-BTC", btc*0.9995),

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-ETH", 0.5)
            ma15 = get_ma15("KRW-ETH")
            current_price = get_current_price("KRW-ETH")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("ETH")
                if krw > 5000:
                    upbit.buy_market_order("KRW-ETH", krw*0.9995)
        else:
            btc = get_balance("ETH")
            if btc > 0.00008:
                upbit.sell_market_order("KRW-ETH", btc*0.9995),

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-SAND", 0.5)
            ma15 = get_ma15("KRW-SAND")
            current_price = get_current_price("KRW-SAND")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-SAND", krw*0.9995)
        else:
            btc = get_balance("SAND")
            if btc > 0.00008:
                upbit.sell_market_order("KRW-SAND", btc*0.9995),

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-MANA", 0.5)
            ma15 = get_ma15("KRW-MANA")
            current_price = get_current_price("KRW-MANA")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-MANA", krw*0.9995)
        else:
            btc = get_balance("MANA")
            if btc > 0.00008:
                upbit.sell_market_order("KRW-MANA", btc*0.9995),

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-ATOM", 0.5)
            ma15 = get_ma15("KRW-ATOM")
            current_price = get_current_price("KRW-ATOM")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-ATOM", krw*0.9995)
        else:
            btc = get_balance("ATOM")
            if btc > 0.00008:
                upbit.sell_market_order("KRW-ATOM", btc*0.9995),

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-FLOW", 0.5)
            ma15 = get_ma15("KRW-FLOW")
            current_price = get_current_price("KRW-FLOW")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-FLOW", krw*0.9995)
        else:
            btc = get_balance("FLOW")
            if btc > 0.00008:
                upbit.sell_market_order("KRW-FLOW", btc*0.9995),

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-AXS", 0.5)
            ma15 = get_ma15("KRW-AXS")
            current_price = get_current_price("KRW-AXS")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-AXS", krw*0.9995)
        else:
            btc = get_balance("AXS")
            if btc > 0.00008:
                upbit.sell_market_order("KRW-AXS", btc*0.9995),

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-BTT", 0.5)
            ma15 = get_ma15("KRW-BTT")
            current_price = get_current_price("KRW-BTT")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-BTT", krw*0.9995)
        else:
            btc = get_balance("BTT")
            if btc > 0.00008:
                upbit.sell_market_order("KRW-BTT", btc*0.9995),

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-XRP", 0.5)
            ma15 = get_ma15("KRW-XRP")
            current_price = get_current_price("KRW-XRP")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-XRP", krw*0.9995)
        else:
            btc = get_balance("XRP")
            if btc > 0.00008:
                upbit.sell_market_order("KRW-XRP", btc*0.9995),

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-SOL", 0.5)
            ma15 = get_ma15("KRW-SOL")
            current_price = get_current_price("KRW-SOL")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-SOL", krw*0.9995)
        else:
            btc = get_balance("SOL")
            if btc > 0.00008:
                upbit.sell_market_order("KRW-SOL", btc*0.9995),

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-BORA", 0.5)
            ma15 = get_ma15("KRW-BORA")
            current_price = get_current_price("KRW-BORA")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-BORA", krw*0.9995)
        else:
            btc = get_balance("BORA")
            if btc > 0.00008:
                upbit.sell_market_order("KRW-BORA", btc*0.9995),

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-POWR", 0.5)
            ma15 = get_ma15("KRW-POWR")
            current_price = get_current_price("KRW-POWR")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-POWR", krw*0.9995)
        else:
            btc = get_balance("POWR")
            if btc > 0.00008:
                upbit.sell_market_order("KRW-POWR", btc*0.9995),

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-MATIC", 0.5)
            ma15 = get_ma15("KRW-MATIC")
            current_price = get_current_price("KRW-MATIC")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-MATIC", krw*0.9995)
        else:
            btc = get_balance("MATIC")
            if btc > 0.00008:
                upbit.sell_market_order("KRW-MATIC", btc*0.9995),

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-KNC", 0.5)
            ma15 = get_ma15("KRW-KNC")
            current_price = get_current_price("KRW-KNC")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-KNC", krw*0.9995)
        else:
            btc = get_balance("KNC")
            if btc > 0.00008:
                upbit.sell_market_order("KRW-KNC", btc*0.9995),

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-WEMIX", 0.5)
            ma15 = get_ma15("KRW-WEMIX")
            current_price = get_current_price("KRW-WEMIX")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-WEMIX", krw*0.9995)
        else:
            btc = get_balance("WEMIX")
            if btc > 0.00008:
                upbit.sell_market_order("KRW-WEMIX", btc*0.9995),

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-DOGE", 0.5)
            ma15 = get_ma15("KRW-DOGE")
            current_price = get_current_price("KRW-DOGE")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-DOGE", krw*0.9995)
        else:
            btc = get_balance("DOGE")
            if btc > 0.00008:
                upbit.sell_market_order("KRW-DOGE", btc*0.9995),

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-NEAR", 0.5)
            ma15 = get_ma15("KRW-NEAR")
            current_price = get_current_price("KRW-NEAR")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-NEAR", krw*0.9995)
        else:
            btc = get_balance("NEAR")
            if btc > 0.00008:
                upbit.sell_market_order("KRW-NEAR", btc*0.9995),

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-CVC", 0.5)
            ma15 = get_ma15("KRW-CVC")
            current_price = get_current_price("KRW-CVC")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-CVC", krw*0.9995)
        else:
            btc = get_balance("CVC")
            if btc > 0.00008:
                upbit.sell_market_order("KRW-CVC", btc*0.9995),

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-XTZ", 0.5)
            ma15 = get_ma15("KRW-XTZ")
            current_price = get_current_price("KRW-XTZ")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-XTZ", krw*0.9995)
        else:
            btc = get_balance("XTZ")
            if btc > 0.00008:
                upbit.sell_market_order("KRW-XTZ", btc*0.9995),

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-AERGO", 0.5)
            ma15 = get_ma15("KRW-AERGO")
            current_price = get_current_price("KRW-AERGO")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-AERGO", krw*0.9995)
        else:
            btc = get_balance("AERGO")
            if btc > 0.00008:
                upbit.sell_market_order("KRW-AERGO", btc*0.9995),

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-STX", 0.5)
            ma15 = get_ma15("KRW-STX")
            current_price = get_current_price("KRW-STX")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-STX", krw*0.9995)
        else:
            btc = get_balance("STX")
            if btc > 0.00008:
                upbit.sell_market_order("KRW-STX", btc*0.9995),

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-ADA", 0.5)
            ma15 = get_ma15("KRW-ADA")
            current_price = get_current_price("KRW-ADA")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-ADA", krw*0.9995)
        else:
            btc = get_balance("ADA")
            if btc > 0.00008:
                upbit.sell_market_order("KRW-ADA", btc*0.9995),

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-ENJ", 0.5)
            ma15 = get_ma15("KRW-ENJ")
            current_price = get_current_price("KRW-ENJ")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-ENJ", krw*0.9995)
        else:
            btc = get_balance("ENJ")
            if btc > 0.00008:
                upbit.sell_market_order("KRW-ENJ", btc*0.9995),

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-SXP", 0.5)
            ma15 = get_ma15("KRW-SXP")
            current_price = get_current_price("KRW-SXP")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-SXP", krw*0.9995)
        else:
            btc = get_balance("SXP")
            if btc > 0.00008:
                upbit.sell_market_order("KRW-SXP", btc*0.9995),         
        
        time.sleep(1),
    except Exception as e:
        print(e)
        time.sleep(1)
