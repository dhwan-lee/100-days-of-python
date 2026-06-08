import requests_cache
from datetime import datetime, timedelta
from data_manager import DataManager
from pprint import pprint
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager

requests_cache.install_cache(
    "flight_cache",
    urls_expire_after={
        "*.sheety.co*": requests_cache.DO_NOT_CACHE,
        "*": 3600,
    }
)

# ==================== Set the Dates ====================
 
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=6 * 30)

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
pprint(sheet_data)

# # ==================== Do a Flight Search ====================

flight_search = FlightSearch()
# Create an instance of the NotificationManager
notification_manager = NotificationManager()

# flights = flight_search.check_flights(
#     origin_city_code="YVR",
#     destination_city_code="CDG",
#     from_time=tomorrow,
#     to_time=six_month_from_today
# )

# pprint(flights)

# ==================== Search all the destinations ====================

# Set your origin airport (London Heathrow)
ORIGIN_CITY_IATA = "YVR"

for destination in sheet_data:
    pprint(f"Getting flights for {destination['city']}...")
    flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    cheapest_flight = find_cheapest_flight(flights, return_date=six_month_from_today.strftime("%Y-%m-%d"))
    pprint(f"{destination['city']}: GBP {cheapest_flight.price}")

    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        pprint(f"Lower price flight found to {destination['city']}!")
        data_manager.update_lowest_price(destination["id"], cheapest_flight.price)
        # notification_manager.send_sms(
        #     message_body=f"Low price alert! Only GBP {cheapest_flight.price} to fly "
        #                  f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
        #                  f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        # )
        # SMS not working? Try whatsapp instead.
        notification_manager.send_whatsapp(
            message_body=f"Low price alert! Only GBP {cheapest_flight.price} to fly "
                         f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                         f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        )