from Telegram.sendmarkdown import SendMarkdown
import os

def check_farm_summary():
    req = os.popen("chia farm summary").read()
    start = req.find("Total chia farmed: ")
    start2 = req.find("Total chia farmed: ") + len("Total chia farmed: ")
    end = req[start2:].find('\n')
    chia = int(req[start2:][:end].strip('\n'))
    text = req[start:][:end].strip('\n')

    return text, chia
    




if __name__ == '__main__':
    text, chia = check_farm_summary()
    if chia > 0:
        SendMarkdown(chat_id="-590191599", text=text, token=os.environ.get("TELEGRAM_API_TOKEN"))