from flight_data import FlightData
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

flight_search = FlightSearch()
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(sheet_data)

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

print(sheet_data)
cities = [value["iataCode"] for value in sheet_data]

for i in cities:
    x = 0

    price = flight_search.get_prices(i)
    notification = NotificationManager(price.price, price.origin_city,price.origin_airport,price.destination_city,
                                       price.return_date, price.out_date, price.destination_airport, price.noinfo)

    if price.noinfo and price.price < sheet_data[x]["lowestPrice"]:
        notification.check_prices()
    x += 1
