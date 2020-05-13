from flask_restful import Resource, reqparse
from flask import request

# dummy data
trips = [
    {   "customer_name":"Beyonce",
        "customer_id": "u314958",
        "destination": "SchipholAirport"
    },
    {   "customer_name": "Queen Maxima",
        "customer_id": "u035135",
        "destination": "TilburgUniversity"
    },
    {   "customer_name": "Michelle Obama",
        "customer_id": "u51351",
        "destination": "EindhovenUniversity"
    }
]


# resource place trip request
class TripRequest(Resource):
    def get(self, destination):
        for trip in trips:
            if destination == trip["destination"]:
                return trip, 200  # return 200 HTTP status code to indicate success
        return {"message": "Trip not found"}, 404  # return 404 HTTP status code to indicate resource not found

