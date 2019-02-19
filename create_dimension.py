import pandas as pd
from datetime import date
import holidays

lookup_month = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }

fr_holidays=holidays.FRA()

df = pd.DataFrame({"date": pd.date_range('2000-01-01', '2050-12-31')})
df["year"] = df.date.dt.year
df["semester"] = (df.date.dt.quarter + 1) // 2
df["quarter"] = df.date.dt.quarter
df["monthofyear"] = df.date.dt.month
df["name_of_month"] = df["monthofyear"].apply(lambda x: lookup_month[x])
df["week"] = df.date.dt.weekofyear
df["dayofyear"] = df.date.dt.dayofyear
df["dayofweek"] = df.date.dt.dayofweek+1
df["name_of_day"] = df.date.dt.weekday_name
df["holiday"] = df["date"].apply(lambda x: x in fr_holidays)
print(df.head(10))

df.to_csv("lookup_date.csv", index=False)