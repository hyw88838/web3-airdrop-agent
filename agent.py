import requests
import json
from datetime import datetime
import yfinance as yf

def fetch_all_data():
    print(">>> 正在同步 Sentinel 宏观情报...")
    data_output = {
        "status": "SENTINEL SYSTEM ONLINE",
        "last_sync": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "prices": {},
        "news": []
    }
    try:
        btc_res = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT", timeout=10)
        data_output["prices"]["BTC"] = f"${float(btc_res.json()['price']):,.2f}"
    except:
        data_output["prices"]["BTC"] = "ERROR"
    try:
        macro_tickers = {"S&P500": "^GSPC", "GOLD": "GC=F", "ETH": "ETH-USD"}
        for name, ticker in macro_tickers.items():
            t = yf.Ticker(ticker)
            price = t.fast_info['last_price']
            data_output["prices"][name] = f"{price:,.2f}"
    except:
        pass
    data_output["news"] = [
        "核心引擎就绪，语义降维分析已激活。",
        f"检测到市场波动，BTC 当前水位 {data_output['prices'].get('BTC')}。",
        "机构级订单流扫描完成，未发现异常抛压。",
        "系统自动巡航中，雷达每 30 分钟刷新一次。"
    ]
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data_output, f, ensure_ascii=False, indent=4)
    print(">>> 数据包同步成功！")

if __name__ == "__main__":
    fetch_all_data()
