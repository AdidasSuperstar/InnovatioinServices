from flask import Flask
from flask_restful import Api

from resources.place_record import PlaceRecord

app = Flask(__name__)
api = Api(app)

api.add_resource(PlaceRecord, '/placerecords/<string:name>')
#define path to the resource

app.run(host='0.0.0.0', port=5000, debug=True)
# In the context of servers, 0.0.0.0 can mean "all IPv4 addresses on the local machine".