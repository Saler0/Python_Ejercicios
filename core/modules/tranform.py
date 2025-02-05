import pandas as pd

from datetime import datetime

class Transform:
    def __init__(self, df):
        self.df = df

    # True if t2-t1 is smaller than 2 days
    def inRecallTimeWindow(t1,t2):
        timeWindowDays = 2.0
        dt1 = datetime.strptime(t1," %Y/ %m/ %d %H: %M: %S")
        dt2 = datetime.strptime(t2," %Y/ %m/ %d %H: %M: %S")
        delta = dt2 - dt1
        days = int(delta.total_seconds ()/86400.0)
        return(days<timeWindowDays)

    def transform_data(self):
        try:
            print(f"\n{self.df.to_string()}")
        except Exception as e:
            print(f"Error en el transform.py {e}", exec_info=True)    