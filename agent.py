import yfinance as yf
import json
from datetime import datetime
import os

def get_terminal_data():
    print(">>> 正在接入全球宏观数据源...")
    
    # 1. 抓取行情 (利用 yfinance)
    # 这里的参数对应：BTC, 以太坊, 标普500, 黄金
    tickers = {
        "BTC": "BTC-USD",
        "ETH": "ETH-USD",
        "S&P500": "^GSPC",
        "GOLD": "GC=F"
    }
    
    market_data = {}
    for label, symbol in tickers.items():
        try:
            ticker = yf.Ticker(symbol)
            price = ticker.fast_info['last_price']
            change = ticker.fast_info['year_to_date_change'] # 简单模拟涨跌
            market_data[label] = f"{price:,.2f}"
        except:
            market_data[label] = "FETCH_ERROR"

    # 2. 模拟情报流 (这里可以根据行情动态生成)
    feeds = [
        f"核心引擎就绪。当前 BTC 支撑位确认于 {market_data['BTC']}",
        "检测到机构级订单流流入，波动率指数扫描中...",
        f"宏观同步完成：标普500 报 {market_data['S&P500']}，黄金报 {market_data['GOLD']}",
        "语义降维分析已激活：市场情绪处于 '谨慎乐观' 状态。"
    ]

    # 3. 封装成 JSON
    output = {
        "status": "SENTINEL SYSTEM ONLINE",
        "update_time": datetime.now().strftime("%H:%M:%S"),
        "prices": market_data,
        "raw_feeds": feeds
    }

    # 4. 写入文件
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=4)
    
    print(">>> 终端数据包已更新完毕。")

if __name__ == "__main__":
    get_terminal_data()
