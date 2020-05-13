from flask_restful import Resource, reqparse
from flask import request

# dummy data
driverRecords = [
    {
        "name": "Iwan",
        "rating": 4.5,
        "ranking": 5,
        "address": {
            "postcode": "5211 DA",
            "street": "Sint Janssingel",
            "houseNo": 92,
            "city": "Den Bosch"
        },
        "licenseplate" : "4BJW994",
        "vehicle": "Mercedes"

    },
    {
        "name": "Amber",
        "rating": 2.0,
        "ranking": 10,
        "address": {
            "postcode": "5812 JE",
            "street": "Rufford Oak",
            "houseNo": 5,
            "city": "London"
        },
        "licenseplate": "BVVX003",
        "vehicle": "Volkswagen"

    }
]



# resource place record
class PlaceRanking(Resource):

    def get(self, name):
        for record in driverRecords:
            if name == record["name"]:
                return record["ranking"], 200  # return 200 HTTP status code to indicate success
        return {"message": "Ranking not found"}, 404 # return 404 HTTP status code to indicate resource not found

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument('ranking', type=int, help='Rate to charge for this resource')
        args = parser.parse_args(strict=True)

        for record in driverRecords:
            if name == record["name"]:
                record["ranking"] = args["ranking"]
                return record, 200

        return {"message": "Driver record not found"}, 404

    def delete(self, name):
        to_be_deleted = None
        for record in driverRecords:
            if name == record["name"]:
                to_be_deleted = record
                ranking_to_be_deleted = record["ranking"]
                break

        if to_be_deleted:
            driverRecords.remove(to_be_deleted[ranking_to_be_deleted])
            return " The ranking of {} is deleted.".format(name), 200
        return {"message": "Driver record not found"}, 404

    def post(self, name):
        return 404



# resource collection ranking records
class PlaceRankings(Resource):
    def post(self):
        return 404

    def get(self):
        for record in driverRecords:
            return record["ranking"],200

    def put(self):
        return {"message": "Not possible to update multiple Driver records"}, 404

    def delete(self):
        for record in driverRecords:
            to_be_deleted = record
            driverRecords.remove(to_be_deleted)
        return {"message": "All driver records have been deleted"},200

