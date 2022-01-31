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

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-MANA", 0.5)
            ma15 = get_ma15("KRW-MANA")
            current_price = get_current_price("KRW-MANA")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("MANA")
                if krw > 5000:
                    buy_result = upbit.buy_market_order("KRW-MANA", krw*0.9995)
                    post_message(myToken,"#crypto", "MANA buy : " +str(buy_result))
                    
        else:
            btc = get_balance("MANA")
            if btc > 0.00008:
                sell_result = upbit.sell_market_order("KRW-MANA", btc*0.9995)
                post_message(myToken,"#crypto", "MANA buy : " +str(sell_result)),

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-ATOM", 0.5)
            ma15 = get_ma15("KRW-ATOM")
            current_price = get_current_price("KRW-ATOM")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("ATOM")
                if krw > 5000:
                    buy_result = upbit.buy_market_order("KRW-ATOM", krw*0.9995)
                    post_message(myToken,"#crypto", "ATOM buy : " +str(buy_result))
                    
        else:
            btc = get_balance("ATOM")
            if btc > 0.00008:
                sell_result = upbit.sell_market_order("KRW-ATOM", btc*0.9995)
                post_message(myToken,"#crypto", "ATOM buy : " +str(sell_result)),

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-GAS", 0.5)
            ma15 = get_ma15("KRW-GAS")
            current_price = get_current_price("KRW-GAS")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("GAS")
                if krw > 5000:
                    buy_result = upbit.buy_market_order("KRW-GAS", krw*0.9995)
                    post_message(myToken,"#crypto", "GAS buy : " +str(buy_result))
                    
        else:
            btc = get_balance("GAS")
            if btc > 0.00008:
                sell_result = upbit.sell_market_order("KRW-GAS", btc*0.9995)
                post_message(myToken,"#crypto", "GAS buy : " +str(sell_result)),

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-WEMIX", 0.5)
            ma15 = get_ma15("KRW-WEMIX")
            current_price = get_current_price("KRW-WEMIX")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("WEMIX")
                if krw > 5000:
                    buy_result = upbit.buy_market_order("KRW-WEMIX", krw*0.9995)
                    post_message(myToken,"#crypto", "WEMIX buy : " +str(buy_result))
                    
        else:
            btc = get_balance("WEMIX")
            if btc > 0.00008:
                sell_result = upbit.sell_market_order("KRW-WEMIX", btc*0.9995)
                post_message(myToken,"#crypto", "WEMIX buy : " +str(sell_result)),

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-SOL", 0.5)
            ma15 = get_ma15("KRW-SOL")
            current_price = get_current_price("KRW-SOL")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("SOL")
                if krw > 5000:
                    buy_result = upbit.buy_market_order("KRW-SOL", krw*0.9995)
                    post_message(myToken,"#crypto", "SOL buy : " +str(buy_result))
                    
        else:
            btc = get_balance("SOL")
            if btc > 0.00008:
                sell_result = upbit.sell_market_order("KRW-SOL", btc*0.9995)
                post_message(myToken,"#crypto", "SOL buy : " +str(sell_result)),

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-ADA", 0.5)
            ma15 = get_ma15("KRW-ADA")
            current_price = get_current_price("KRW-ADA")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("ADA")
                if krw > 5000:
                    buy_result = upbit.buy_market_order("KRW-ADA", krw*0.9995)
                    post_message(myToken,"#crypto", "ADA buy : " +str(buy_result))
                    
        else:
            btc = get_balance("ADA")
            if btc > 0.00008:
                sell_result = upbit.sell_market_order("KRW-ADA", btc*0.9995)
                post_message(myToken,"#crypto", "ADA buy : " +str(sell_result)),

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-MATIC", 0.5)
            ma15 = get_ma15("KRW-MATIC")
            current_price = get_current_price("KRW-MATIC")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("MATIC")
                if krw > 5000:
                    buy_result = upbit.buy_market_order("KRW-MATIC", krw*0.9995)
                    post_message(myToken,"#crypto", "MATIC buy : " +str(buy_result))
                    
        else:
            btc = get_balance("MATIC")
            if btc > 0.00008:
                sell_result = upbit.sell_market_order("KRW-MATIC", btc*0.9995)
                post_message(myToken,"#crypto", "MATIC buy : " +str(sell_result)),

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-AERGO", 0.5)
            ma15 = get_ma15("KRW-AERGO")
            current_price = get_current_price("KRW-AERGO")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("AERGO")
                if krw > 5000:
                    buy_result = upbit.buy_market_order("KRW-AERGO", krw*0.9995)
                    post_message(myToken,"#crypto", "AERGO buy : " +str(buy_result))
                    
        else:
            btc = get_balance("AERGO")
            if btc > 0.00008:
                sell_result = upbit.sell_market_order("KRW-AERGO", btc*0.9995)
                post_message(myToken,"#crypto", "AERGO buy : " +str(sell_result)),

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-LINK", 0.5)
            ma15 = get_ma15("KRW-LINK")
            current_price = get_current_price("KRW-LINK")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("LINK")
                if krw > 5000:
                    buy_result = upbit.buy_market_order("KRW-LINK", krw*0.9995)
                    post_message(myToken,"#crypto", "LINK buy : " +str(buy_result))
                    
        else:
            btc = get_balance("LINK")
            if btc > 0.00008:
                sell_result = upbit.sell_market_order("KRW-LINK", btc*0.9995)
                post_message(myToken,"#crypto", "LINK buy : " +str(sell_result)),

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-HUNT", 0.5)
            ma15 = get_ma15("KRW-HUNT")
            current_price = get_current_price("KRW-HUNT")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("HUNT")
                if krw > 5000:
                    buy_result = upbit.buy_market_order("KRW-HUNT", krw*0.9995)
                    post_message(myToken,"#crypto", "HUNT buy : " +str(buy_result))
                    
        else:
            btc = get_balance("HUNT")
            if btc > 0.00008:
                sell_result = upbit.sell_market_order("KRW-HUNT", btc*0.9995)
                post_message(myToken,"#crypto", "HUNT buy : " +str(sell_result))                            

        time.sleep(1)
    except Exception as e:
        print(e)
        post_message(myToken,"#crypto", e)
        time.sleep(1)
