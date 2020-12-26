import requests
import datetime
from pprint import pprint
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "gP_f_HeBPSnzEdD-huhG9ze41wpqhQee"


end_point = "https://tequila-api.kiwi.com/v2/search"
departure_city = "London"
departure_airport_code = "LON"

today= datetime.datetime.now()
month_period = today+datetime.timedelta(days=6*30)
formatted_day = today.strftime("%d/%m/%Y")
formatted_period = month_period.strftime("%d/%m/%Y")

class FlightSearch:

    def get_destination_code(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def get_prices(self, city):
        global data
        header={
            "apikey": TEQUILA_API_KEY,
        }
        query={
            "fly_from": departure_airport_code,
            "date_from": formatted_day,
            "date_to": formatted_period,
            "fly_to": city,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP",
        }
        response = requests.get(url=end_point, params=query, headers=header)
        try:
            data = response.json()["data"][0]
        except:
            print("There is no flight in specified days")
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0],
                noinfo=False
            )
            return flight_data
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0],
                noinfo=True
            )
            print(f"{flight_data.destination_city}: £{flight_data.price}")
            return flight_data


