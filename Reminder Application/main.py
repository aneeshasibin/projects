import time
from plyer import notification
if __name__=="__main__":
        while True:
               notification.notify(
                       title="please drink water now!!",
                       message="The National Academies of Sciences, Engineering, and medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids for men. About 11.5 cups (2.7 liters) of fluids for women.",
                       app_icon="D:\Projects\Reminder Application\icon.ico",
                       timeout=2
                )
               time.sleep(60*60)