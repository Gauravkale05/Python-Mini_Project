import time
from plyer import notification

while True:
        notification.notify(title="Drink Water",message="Drink a Glass of water", app_name="Drinking water Reminder",timeout=5)
        time.sleep(3600)

