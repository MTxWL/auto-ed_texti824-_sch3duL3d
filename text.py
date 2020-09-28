import random, schedule, time
from twilio.rest import Client
from twlo_credentials import external_number, tw_sid, tw_token
from secret_number import number

MORNING = [
    "Wake up, grab a brush and put a little (makeup),shake up",
    "Good morning!",
    "You overslept for work..."
]

AFTERNOON = [
    "Feed Tina.",
    "Call your grandma.",
    "Buy groceries."
]

NIGHT = [
    "Go to bed before midnight",
    "Read your Suworow.",
    "Drink water."
]

def txt_send(txt_morn=MORNING):
    account = tw_sid
    token = tw_token
    client = Client(account, token)
    txt = txt_morn[random.randint(0, len(txt_morn)-1)]

    client.messages.create(to=number,
                           from_=external_number,
                           body=txt
                           )

schedule.every().day.at("7:49").do(txt_send, MORNING)

schedule.every().day.at("15:03").do(txt_send, AFTERNOON)

schedule.every().day.at("23:27").do(txt_send, NIGHT)

while True:
    schedule.run_pending()
    time.sleep(1)

