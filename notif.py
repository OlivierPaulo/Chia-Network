from Telegram.sendmarkdown import SendMarkdown
import os
import pandas as pd

def check_farm_summary():
    req = os.popen("chia farm summary").read()
    #req = "Farming status: Farming\nTotal chia farmed: 0.0\nUser transaction fees: 0.0\nBlock rewards: 0.0\nLast height farmed: 0\nPlot count: 1\nTotal size of plots: 101.368 GiB\nEstimated network space: 731.175 PiB\nExpected time to win: 4 years and 3 months\nNote: log into your key using 'chia wallet show' to see rewards for each key\n"
    start = req.find("Total chia farmed: ")
    start2 = req.find("Total chia farmed: ") + len("Total chia farmed: ")
    end = req[start2:].find('\n')
    chia = float(req[start2:start2+end])
    text = req[start:start2+end].replace(".", ",")

    return text, chia

def read_data():
    return pd.read_csv("data/chia.csv")

if __name__ == '__main__':
    df = read_data()
    text, chia = check_farm_summary()
    if chia > float(df.loc[0, 'number_of_chia']):
        SendMarkdown(chat_id="-590191599", text=text, token=os.environ.get("TELEGRAM_API_TOKEN"))
        df.loc[0, 'number_of_chia'] = float(chia)
        df.to_csv("data/chia.csv", index=False)