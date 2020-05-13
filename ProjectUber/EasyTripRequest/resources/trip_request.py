from flask_restful import Resource, reqparse
from flask import request

# dummy data
trips = [
    {   "customer_name":"Beyonce",
        "customer_id": "u314958",
        "destination": "Schiphol Airport"
    },
    {   "customer_name": "Queen Maxima",
        "customer_id": "u035135",
        "destination": "Tilburg University"
    },
    {   "customer_name": "Michelle Obama",
        "customer_id": "u51351",
        "destination": "Eindhoven University"
    }
]


# resource place trip request
class TripRequest(Resource):
    def get(self, trip_name):
        for trip in trips:
            if trip_name == trip["destination"]:
                return trip, 200  # return 200 HTTP status code to indicate success
        return {"message": "Trip not found"}, 404  # return 404 HTTP status code to indicate resource not found

