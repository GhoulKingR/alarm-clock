from playsound import playsound
from datetime import datetime
import time


def get(text, ran):
    result = input(text)
    if int(result) in ran:
        return result
    else:
        print(result, "is not in range")
        return get(text, ran)


print("Welcome to alarm clock CLI!\nWhen do you want to set your alarm for")
mainloop = True
while mainloop:
    mainloop = True
    hour = get("Hour: ", ran=range(0, 24))
    minute = get("Minute: ", ran=range(0, 60))

    subloop = True
    while subloop:
        subloop = True
        response = input(
            "That is {}:{} right? (Y/n)".format(hour.zfill(2), minute.zfill(2))
        )

        if response.lower().startswith("y") or len(response) == 0:
            mainloop = False
            subloop = False
        elif response.lower().startswith("n"):
            subloop = False
            print("Alright, let's do that again")
        else:
            print("Invalid response")


while True:
    now = datetime.now()
    current_hour = now.strftime("%H")
    current_minute = now.strftime("%M")

    if current_hour == hour and current_minute == minute:
        print("It's time")
        playsound("alarm.mp3")
        break

    time.sleep(1)
