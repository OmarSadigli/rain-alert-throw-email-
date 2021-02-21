import requests
import smtplib

my_email = "sadigliomar98@gmail.com"
password = "omar1907"
api_key = "295ff48ee721a48eb63604f1c5af461a"
my_lat = 40.593849
my_lon = 49.665161
hourly = "hourly"

parameters = {
    "lat": my_lat,
    "lon": my_lon,
    "exclude": "current,minutely,daily",
    "appid": api_key
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()

condition_codes = [data["hourly"][i]["weather"][0]["id"] for i in range(0, 12)]
print(condition_codes)
will_rain = False
for condition in condition_codes:
    if condition < 700:
        will_rain = True

if will_rain:
    connection = smtplib.SMTP_SSL("smtp.gmail.com")
    connection.login(my_email, password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="sadigliomar@outlook.com",
        msg="It is gonna be rain today"
    )