import time
import pyupbit
import datetime
import requests

access = "9wburk8kjhwvHy0Hq5ZVgwM6pNux1Q9BUgJyQoI0"
secret = "BL6GmlFYpaUWu0yit0ayxoeQ160vSeBrzFkj5EjJ"
myToken = "xoxb-2912010894871-2928928134996-vffa16iIEV4YLLe55JwE1iGW"

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
                krw = get_balance("KRW")
                if krw > 5000:
                    buy_result = upbit.buy_market_order("KRW-ETH", krw*0.9995)
                    post_message(myToken,"#crypto", "ETH buy : " +str(buy_result))
                    
        else:
            btc = get_balance("ETH")
            if btc > 0.00008:
                sell_result = upbit.sell_market_order("KRW-ETH", btc*0.9995)
                post_message(myToken,"#crypto", "ETH buy : " +str(sell_result)),

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-BTC", 0.5)
            ma15 = get_ma15("KRW-BTC")
            current_price = get_current_price("KRW-BTC")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    buy_result = upbit.buy_market_order("KRW-BTC", krw*0.9995)
                    post_message(myToken,"#crypto", "BTC buy : " +str(buy_result))
                    
        else:
            btc = get_balance("BTC")
            if btc > 0.00008:
                sell_result = upbit.sell_market_order("KRW-BTC", btc*0.9995)
                post_message(myToken,"#crypto", "BTC buy : " +str(sell_result)),

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-DOGE", 0.5)
            ma15 = get_ma15("KRW-DOGE")
            current_price = get_current_price("KRW-DOGE")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    buy_result = upbit.buy_market_order("KRW-DOGE", krw*0.9995)
                    post_message(myToken,"#crypto", "DOGE buy : " +str(buy_result))
                    
        else:
            btc = get_balance("DOGE")
            if btc > 0.00008:
                sell_result = upbit.sell_market_order("KRW-DOGE", btc*0.9995)
                post_message(myToken,"#crypto", "DOGE buy : " +str(sell_result)),

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-XRP", 0.5)
            ma15 = get_ma15("KRW-XRP")
            current_price = get_current_price("KRW-XRP")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    buy_result = upbit.buy_market_order("KRW-XRP", krw*0.9995)
                    post_message(myToken,"#crypto", "XRP buy : " +str(buy_result))
                    
        else:
            btc = get_balance("XRP")
            if btc > 0.00008:
                sell_result = upbit.sell_market_order("KRW-XRP", btc*0.9995)
                post_message(myToken,"#crypto", "XRP buy : " +str(sell_result)),

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-SAND", 0.5)
            ma15 = get_ma15("KRW-SAND")
            current_price = get_current_price("KRW-SAND")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    buy_result = upbit.buy_market_order("KRW-SAND", krw*0.9995)
                    post_message(myToken,"#crypto", "SAND buy : " +str(buy_result))
                    
        else:
            btc = get_balance("SAND")
            if btc > 0.00008:
                sell_result = upbit.sell_market_order("KRW-SAND", btc*0.9995)
                post_message(myToken,"#crypto", "SAND buy : " +str(sell_result)),         

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-MATIC", 0.5)
            ma15 = get_ma15("KRW-MATIC")
            current_price = get_current_price("KRW-MATIC")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    buy_result = upbit.buy_market_order("KRW-MATIC", krw*0.9995)
                    post_message(myToken,"#crypto", "MATIC buy : " +str(buy_result))
                    
        else:
            btc = get_balance("MATIC")
            if btc > 0.00008:
                sell_result = upbit.sell_market_order("KRW-MATIC", btc*0.9995)
                post_message(myToken,"#crypto", "MATIC buy : " +str(sell_result)),

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-ADA", 0.5)
            ma15 = get_ma15("KRW-ADA")
            current_price = get_current_price("KRW-ADA")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    buy_result = upbit.buy_market_order("KRW-ADA", krw*0.9995)
                    post_message(myToken,"#crypto", "ADA buy : " +str(buy_result))
                    
        else:
            btc = get_balance("ADA")
            if btc > 0.00008:
                sell_result = upbit.sell_market_order("KRW-ADA", btc*0.9995)
                post_message(myToken,"#crypto", "ADA buy : " +str(sell_result)),

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-ONG", 0.5)
            ma15 = get_ma15("KRW-ONG")
            current_price = get_current_price("KRW-ONG")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    buy_result = upbit.buy_market_order("KRW-ONG", krw*0.9995)
                    post_message(myToken,"#crypto", "ONG buy : " +str(buy_result))
                    
        else:
            btc = get_balance("ONG")
            if btc > 0.00008:
                sell_result = upbit.sell_market_order("KRW-ONG", btc*0.9995)
                post_message(myToken,"#crypto", "ONG buy : " +str(sell_result)),        

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-EOS", 0.5)
            ma15 = get_ma15("KRW-EOS")
            current_price = get_current_price("KRW-EOS")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    buy_result = upbit.buy_market_order("KRW-EOS", krw*0.9995)
                    post_message(myToken,"#crypto", "EOS buy : " +str(buy_result))
                    
        else:
            btc = get_balance("EOS")
            if btc > 0.00008:
                sell_result = upbit.sell_market_order("KRW-EOS", btc*0.9995)
                post_message(myToken,"#crypto", "EOS buy : " +str(sell_result)),

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-SXP", 0.5)
            ma15 = get_ma15("KRW-SXP")
            current_price = get_current_price("KRW-SXP")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    buy_result = upbit.buy_market_order("KRW-SXP", krw*0.9995)
                    post_message(myToken,"#crypto", "SXP buy : " +str(buy_result))
                    
        else:
            btc = get_balance("SXP")
            if btc > 0.00008:
                sell_result = upbit.sell_market_order("KRW-SXP", btc*0.9995)
                post_message(myToken,"#crypto", "SXP buy : " +str(sell_result)),

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-GAS", 0.5)
            ma15 = get_ma15("KRW-GAS")
            current_price = get_current_price("KRW-GAS")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    buy_result = upbit.buy_market_order("KRW-GAS", krw*0.9995)
                    post_message(myToken,"#crypto", "GAS buy : " +str(buy_result))
                    
        else:
            btc = get_balance("GAS")
            if btc > 0.00008:
                sell_result = upbit.sell_market_order("KRW-GAS", btc*0.9995)
                post_message(myToken,"#crypto", "GAS buy : " +str(sell_result)),

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-MANA", 0.5)
            ma15 = get_ma15("KRW-MANA")
            current_price = get_current_price("KRW-MANA")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    buy_result = upbit.buy_market_order("KRW-MANA", krw*0.9995)
                    post_message(myToken,"#crypto", "MANA buy : " +str(buy_result))
                    
        else:
            btc = get_balance("MANA")
            if btc > 0.00008:
                sell_result = upbit.sell_market_order("KRW-MANA", btc*0.9995)
                post_message(myToken,"#crypto", "MANA buy : " +str(sell_result)),

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-BORA", 0.5)
            ma15 = get_ma15("KRW-BORA")
            current_price = get_current_price("KRW-BORA")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    buy_result = upbit.buy_market_order("KRW-BORA", krw*0.9995)
                    post_message(myToken,"#crypto", "BORA buy : " +str(buy_result))
                    
        else:
            btc = get_balance("BORA")
            if btc > 0.00008:
                sell_result = upbit.sell_market_order("KRW-BORA", btc*0.9995)
                post_message(myToken,"#crypto", "BORA buy : " +str(sell_result)), 

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-LINK", 0.5)
            ma15 = get_ma15("KRW-LINK")
            current_price = get_current_price("KRW-LINK")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    buy_result = upbit.buy_market_order("KRW-LINK", krw*0.9995)
                    post_message(myToken,"#crypto", "LINK buy : " +str(buy_result))
                    
        else:
            btc = get_balance("LINK")
            if btc > 0.00008:
                sell_result = upbit.sell_market_order("KRW-LINK", btc*0.9995)
                post_message(myToken,"#crypto", "LINK buy : " +str(sell_result)),

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-POWR", 0.5)
            ma15 = get_ma15("KRW-POWR")
            current_price = get_current_price("KRW-POWR")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    buy_result = upbit.buy_market_order("KRW-POWR", krw*0.9995)
                    post_message(myToken,"#crypto", "POWR buy : " +str(buy_result))
                    
        else:
            btc = get_balance("POWR")
            if btc > 0.00008:
                sell_result = upbit.sell_market_order("KRW-POWR", btc*0.9995)
                post_message(myToken,"#crypto", "POWR buy : " +str(sell_result)), 

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-KNC", 0.5)
            ma15 = get_ma15("KRW-KNC")
            current_price = get_current_price("KRW-KNC")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    buy_result = upbit.buy_market_order("KRW-KNC", krw*0.9995)
                    post_message(myToken,"#crypto", "KNC buy : " +str(buy_result))
                    
        else:
            btc = get_balance("KNC")
            if btc > 0.00008:
                sell_result = upbit.sell_market_order("KRW-KNC", btc*0.9995)
                post_message(myToken,"#crypto", "KNC buy : " +str(sell_result)), 

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-TRX", 0.5)
            ma15 = get_ma15("KRW-TRX")
            current_price = get_current_price("KRW-TRX")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("TRX")
                if krw > 5000:
                    buy_result = upbit.buy_market_order("KRW-TRX", krw*0.9995)
                    post_message(myToken,"#crypto", "TRX buy : " +str(buy_result))
                    
        else:
            btc = get_balance("TRX")
            if btc > 0.00008:
                sell_result = upbit.sell_market_order("KRW-TRX", btc*0.9995)
                post_message(myToken,"#crypto", "TRX buy : " +str(sell_result)),
                
        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-XLM", 0.5)
            ma15 = get_ma15("KRW-XLM")
            current_price = get_current_price("KRW-XLM")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("XLM")
                if krw > 5000:
                    buy_result = upbit.buy_market_order("KRW-XLM", krw*0.9995)
                    post_message(myToken,"#crypto", "XLM buy : " +str(buy_result))
                    
        else:
            btc = get_balance("XLM")
            if btc > 0.00008:
                sell_result = upbit.sell_market_order("KRW-XLM", btc*0.9995)
                post_message(myToken,"#crypto", "XLM buy : " +str(sell_result)),
                
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
            target_price = get_target_price("KRW-DAWN", 0.5)
            ma15 = get_ma15("KRW-DAWN")
            current_price = get_current_price("KRW-DAWN")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("DAWN")
                if krw > 5000:
                    buy_result = upbit.buy_market_order("KRW-DAWN", krw*0.9995)
                    post_message(myToken,"#crypto", "DAWN buy : " +str(buy_result))
                    
        else:
            btc = get_balance("DAWN")
            if btc > 0.00008:
                sell_result = upbit.sell_market_order("KRW-DAWN", btc*0.9995)
                post_message(myToken,"#crypto", "DAWN buy : " +str(sell_result)),

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-PUND", 0.5)
            ma15 = get_ma15("KRW-PUND")
            current_price = get_current_price("KRW-PUND")
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("PUND")
                if krw > 5000:
                    buy_result = upbit.buy_market_order("KRW-PUND", krw*0.9995)
                    post_message(myToken,"#crypto", "PUND buy : " +str(buy_result))
                    
        else:
            btc = get_balance("PUND")
            if btc > 0.00008:
                sell_result = upbit.sell_market_order("KRW-PUND", btc*0.9995)
                post_message(myToken,"#crypto", "PUND buy : " +str(sell_result)),

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

        time.sleep(1)
    except Exception as e:
        print(e)
        post_message(myToken,"#crypto", e)
        time.sleep(1)
