from plyer import notification
from time import sleep

while True:

    notification.notify(

        title = "Drink Water Reminder",
        message = "🚰 Remember to stay hydrated! Take a sip of water now! 💧💦",
        timeout = 10
    )

    sleep(60*60)