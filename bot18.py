import yfinance as yf
import pandas as pd
import requests
from ta.momentum import RSIIndicator

TOKEN="8766895345:AAHVDXN3aosDJuuj8J3EzUbZl6HQjYUz3YQ"
CHAT_ID="7692977482"

def send(msg):
    url=f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url,data={"chat_id":CHAT_ID,"text":msg})

stocks=[
"SOFI","RKLB","IONQ","OPEN","UPST",
"RIOT","MARA","FUBO","NIO","LCID"
]

results=[]

for stock in stocks:

    try:

        data=yf.download(stock,period="5d",interval="1h",progress=False)

        if len(data)<10:
            continue

        data["RSI"]=RSIIndicator(data["Close"]).rsi()

        price=float(data["Close"].iloc[-1])
        prev=float(data["Close"].iloc[-5])

        change=((price-prev)/prev)*100

        rsi=float(data["RSI"].iloc[-1])

        if change>3 and rsi<70:

            results.append({
                "stock":stock,
                "price":price,
                "change":change
            })

    except:
        pass

if len(results)==0:

    send("לא נמצאו הזדמנויות היום")

else:

    df=pd.DataFrame(results)
    df=df.sort_values("change",ascending=False)

    top=df.head(5)

    send("🚀 מניות חמות:")

    for i,row in top.iterrows():

        send(f"""
מניה: {row['stock']}
מחיר: {round(row['price'],2)}$
עלייה: {round(row['change'],2)}%
""")
