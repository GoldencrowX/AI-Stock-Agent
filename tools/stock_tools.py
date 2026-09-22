# import yfinance as yf


# def get_stock_price(symbol: str):
#     """
#     Get stock price using yfinance
#     """

#     stock = yf.Ticker(symbol)

#     data = stock.history(period="1d")

#     if data.empty:
#         return {"error": "Stock not found"}

#     price = data["Close"].iloc[-1]

#     return {
#         "symbol": symbol,
#         "price": float(price)
#     }

import yfinance as yf
import requests


def get_stock_price(symbol: str):
    """
    Get latest stock price
    """

    try:
        stock = yf.Ticker(symbol)

        data = stock.history(period="1d")

        if data.empty:
            return {"error": "Stock not found"}

        price = float(data["Close"].iloc[-1])

        return {
            "symbol": symbol,
            "price": price
        }

    except Exception as e:
        return {
            "error": str(e)
        }


def get_stock_fundamentals(symbol: str):
    """
    Get fundamental data
    """

    try:
        stock = yf.Ticker(symbol)
        info = stock.info

        return {
            "market_cap": info.get("marketCap", "N/A"),
            "pe_ratio": info.get("trailingPE", "N/A"),
            "eps": info.get("trailingEps", "N/A"),
            "revenue": info.get("totalRevenue", "N/A")
        }

    except Exception as e:
        return {
            "error": str(e)
        }


def get_stock_news(symbol: str):
    """
    Get latest stock news
    """

    try:
        url = f"https://query1.finance.yahoo.com/v1/finance/search?q={symbol}"

        r = requests.get(url, timeout=10)

        data = r.json()

        news = []

        if "news" in data:
            for n in data["news"][:5]:

                news.append({
                    "title": n.get("title"),
                    "publisher": n.get("publisher"),
                    "link": n.get("link")
                })

        return news

    except Exception as e:
        return {
            "error": str(e)
        }