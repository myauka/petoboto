import re
import requests

def data_retrieval():
    api = 'https://api.kuna.io/v3/tickers?symbols=btcuah,ltcuah,dashuah,trxuah,' \
         'ethuah,bchuah,zecuah,uniuah,usdtuah,xlmuah,wavesuah,linkuah,usdcuah,' \
         'eosuah,bnbuah,xrpuah,xemuah,daiuah'
    try:
        inquiry = requests.get(api).json()
    except:
        return 'Bad Request'

    data = {'UAH':{}}

    for i in range(len(inquiry)):
        currency_name = re.sub('uah', '', inquiry[i][0]).upper()
        data['UAH'][currency_name] = str(inquiry[i][7])
    return data

data = data_retrieval()