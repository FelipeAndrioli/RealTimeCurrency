#!/usr/bin/env python3

##Created by Felipe Andrioli

import requests
import json
import time

def RealTimeCurrency(from_currency, to_currency, api_key, current_hour):
    
##    print(from_currency)
##    print(to_currency)
##    print(api_key)

    base_url = r"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"
    main_url = base_url + "&from_currency=" + from_currency + "&to_currency=" + to_currency + "&apikey=" + api_key

    req_ob = requests.get(main_url)
    result = req_ob.json()

##    print(req_ob)
##    print(result)

##    print("Result before parsing the json data: \n", result)

    print(current_hour)

    print("Realtime Currency Exchange Rate for",
            result["Realtime Currency Exchange Rate"]
            ["2. From_Currency Name"], "To",
            result["Realtime Currency Exchange Rate"]
            ["4. To_Currency Name"], "is",
            result["Realtime Currency Exchange Rate"]
            ["5. Exchange Rate"], to_currency)


if __name__ == "__main__":

    from_currency = "USD"
    to_currency = "BRL"

    api_key = "EOV84XG6Q1E4RE1W"
    localtime = time.localtime()
    current_time = time.strftime("%I:%M:%S %p", localtime)

##    RealTimeCurrency(from_currency, to_currency, api_key, current_time)
##    RealTimeCurrency(from_currency, to_currency, api_key, current_time)  

    while True:
        localtime = time.localtime()
        current_time = time.strftime("%I:%M:%S %p", localtime)
        RealTimeCurrency(from_currency, to_currency, api_key, current_time)
##        print(result)
        time.sleep(300)
        
        
