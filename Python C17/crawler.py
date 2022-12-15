from bs4 import BeautifulSoup
import schedule
import json
import requests
import time

def main():
    page = requests.get("https://www.autovit.ro")
    soup = BeautifulSoup(page.content, "html.parser")

    cars = []

    for section in soup.find_all("section",{"class": "ooa-af2m8r e2nxjc60"}):

        car_title = section.find("h2", {"class": "e1lmj3dz0 ooa-16u688i er34gjf0"}).text

        car_price = section.find("div", {"class": "ooa-80vtuv er34gjf0"}).span.text

        #used to get year and km
        car_caract = section.find("ul", {"class": "ooa-zzhv62 e16henwp0"})

        car_year = car_caract.find_all("li")[0].text.replace(" ", "")

        car_km = car_caract.find_all("li")[1].text

        car = {
            "title": car_title,
            "price": car_price,
            "year": car_year,
            "km": car_km,
        }
        cars.append(car)

    with open("cars.json", "r+") as f:
        # get cars from file
        try:
            jsoncars = json.load(f)
        except:
            jsoncars = []
        jsoncars.append(cars)
        f.seek(0)
        json.dump(jsoncars, f, indent=4)

main()

#automate this to run once a day
def job():
    print("I'm working...")
    main()

schedule.every().day.at("00:00").do(job)
#schedule.every(10).minutes.do(job)

while True:
    print("Waiting...")
    schedule.run_pending()
    # sleep for 1 second
    time.sleep(5)




