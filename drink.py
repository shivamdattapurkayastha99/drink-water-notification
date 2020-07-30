import time
from plyer import notification
if __name__ == "__main__":
    notification.notify(
        title=" please drink water",
        message="3.7l/day",
        app_icon="",
        timeout=5
    )
