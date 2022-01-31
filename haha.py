import time
import pyupbit
import datetime
import requests

access = "opbQhxfIbyYUcCl1XxKzFuUQNIRc19dckDUlYbup"
secret = "DTZPBPXoWRnxrc03jOmWvzk7iNxEUD6tfr15H3K1"
myToken = "xoxb-2912010894871-2928928134996-LisxWzc5nf48zLxO19taoFk9"

def post_message(token, channel, text):
    """슬랙 메시지 전송"""
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    
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
# 시작 메세지 슬랙 전송
post_message(myToken,"#crypto", "autotrade start")

while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-BTC")
        end_time = start_time + datetime.timedelta(days=1)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-ETH", 0.5)
            ma15 = get_ma15("KRW-ETH")
            current_price = get_current_price("KRW-ETH")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("ETH")
                if krw > 5000:
                    buy_result = upbit.buy_market_order("KRW-ETH", krw*0.9995)
                    post_message(myToken,"#crypto", "ETH buy : " +str(buy_result))
                    
        else:
            btc = get_balance("ETH")
            if btc > 0.00008:
                sell_result = upbit.sell_market_order("KRW-ETH", btc*0.9995)
                post_message(myToken,"#crypto", "ETH buy : " +str(sell_result)),

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-SAND", 0.5)
            ma15 = get_ma15("KRW-SAND")
            current_price = get_current_price("KRW-SAND")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("SAND")
                if krw > 5000:
                    buy_result = upbit.buy_market_order("KRW-SAND", krw*0.9995)
                    post_message(myToken,"#crypto", "SAND buy : " +str(buy_result))
                    
        else:
            btc = get_balance("SAND")
            if btc > 0.00008:
                sell_result = upbit.sell_market_order("KRW-SAND", btc*0.9995)
                post_message(myToken,"#crypto", "SAND buy : " +str(sell_result)),

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-AXS", 0.5)
            ma15 = get_ma15("KRW-AXS")
            current_price = get_current_price("KRW-AXS")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("AXS")
                if krw > 5000:
                    buy_result = upbit.buy_market_order("KRW-AXS", krw*0.9995)
                    post_message(myToken,"#crypto", "AXS buy : " +str(buy_result))
                    
        else:
            btc = get_balance("AXS")
            if btc > 0.00008:
                sell_result = upbit.sell_market_order("KRW-AXS", btc*0.9995)
                post_message(myToken,"#crypto", "AXS buy : " +str(sell_result)),                

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-ONG", 0.5)
            ma15 = get_ma15("KRW-ONG")
            current_price = get_current_price("KRW-ONG")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("ONG")
                if krw > 5000:
                    buy_result = upbit.buy_market_order("KRW-ONG", krw*0.9995)
                    post_message(myToken,"#crypto", "ONG buy : " +str(buy_result))
                    
        else:
            btc = get_balance("ONG")
            if btc > 0.00008:
                sell_result = upbit.sell_market_order("KRW-ONG", btc*0.9995)
                post_message(myToken,"#crypto", "ONG buy : " +str(sell_result)),

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-BTC", 0.5)
            ma15 = get_ma15("KRW-BTC")
            current_price = get_current_price("KRW-BTC")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("BTC")
                if krw > 5000:
                    buy_result = upbit.buy_market_order("KRW-BTC", krw*0.9995)
                    post_message(myToken,"#crypto", "BTC buy : " +str(buy_result))
                    
        else:
            btc = get_balance("BTC")
            if btc > 0.00008:
                sell_result = upbit.sell_market_order("KRW-BTC", btc*0.9995)
                post_message(myToken,"#crypto", "BTC buy : " +str(sell_result)),
                
        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-FLOW", 0.5)
            ma15 = get_ma15("KRW-FLOW")
            current_price = get_current_price("KRW-FLOW")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("FLOW")
                if krw > 5000:
                    buy_result = upbit.buy_market_order("KRW-FLOW", krw*0.9995)
                    post_message(myToken,"#crypto", "FLOW buy : " +str(buy_result))
                    
        else:
            btc = get_balance("FLOW")
            if btc > 0.00008:
                sell_result = upbit.sell_market_order("KRW-FLOW", btc*0.9995)
                post_message(myToken,"#crypto", "FLOW buy : " +str(sell_result)),                               

        time.sleep(1)
    except Exception as e:
        print(e)
        post_message(myToken,"#crypto", e)
        time.sleep(1)
