from twilio.rest import Client
from flight_data import FlightData
ACCOUNT_SID = "AC2d558aa54b39737b6fcc9f5164a70b90"
AUT_TOKEN = "be4ac7c90ddcb8dc7c59f73dcecf5e22"
FROM = "+13345092276"
TO = "+306970548924"


class NotificationManager(FlightData):
    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date,
                 return_date,noinfo):
        super().__init__(price, origin_city, origin_airport, destination_city, destination_airport, out_date,
                         return_date,noinfo)

    def check_prices(self):
        client = Client(ACCOUNT_SID, AUT_TOKEN)

        message = client.messages \
            .create(
            body=f"LOW PRICES ALERT!!!\n Only £{self.price} to fly from London-{self.destination_airport}"
                 f" to {self.destination_city}-{self.origin_airport}, from {self.out_date} to {self.return_date}.",
            from_=FROM,
            to=TO,
        )

        print(message.status)
