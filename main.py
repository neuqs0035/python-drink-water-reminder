from plyer import notification
from time import sleep

while True:

    notification.notify(

        title = "Drink Water Reminder",
        message = "⏰ Hey there! Time for a quick break. \n\n🚰 Don't forget to grab a refreshing drink of water and stay hydrated! \n\nYour body will thank you. 💧💙",
        timeout = 10
    )

    sleep(60*60)