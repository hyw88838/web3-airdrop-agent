import requests
import json
from datetime import datetime

def fetch_data():
    print(">>> 正在启动数据抓取引擎...")
    
    # 1. 抓取实时 BTC 价格 (使用币安公开接口)
    try:
        btc_res = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT", timeout=10)
        btc_price = f"${float(btc_res.json()['price']):,.2f}"
    except Exception as e:
        print(f"价格抓取失败: {e}")
        btc_price = "CONNECTION_ERROR"

    # 2. 模拟宏观情报流 (后期你可以自己加爬虫抓取真正的福克斯新闻)
    news_feeds = [
        "核心引擎待命... 语义降维分析已激活。",
        f"检测到亚洲市场流动性注入，BTC 当前水位 {btc_price}。",
        "机构订单流在 $64,500 附近出现堆叠信号。",
        "系统自动巡航已激活，雷达每 60 秒扫描一次。"
    ]

    # 3. 封装数据
    terminal_data = {
        "status": "系统就绪 (ONLINE)",
        "last_sync": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "btc_price": btc_price,
        "raw_feeds": news_feeds
    }

    # 4. 保存为 data.json 供前端读取
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(terminal_data, f, ensure_ascii=False, indent=4)
    
    print(">>> 数据已成功存入 data.json")

if __name__ == "__main__":
    fetch_data()
