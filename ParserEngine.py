
import requests


# 下載 yahoo 股市
def GetYahooStock():
    response = requests.get(url="https://tw.stock.yahoo.com/")
    print(response.text)
    print('獨立的 ParserEngine 負責下載網址進行分析')

