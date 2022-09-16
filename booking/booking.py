from flask import Flask, render_template, request, jsonify, make_response
import requests
import json
from werkzeug.exceptions import NotFound

app = Flask(__name__)

PORT = 3201
HOST = '0.0.0.0'

with open('{}/databases/bookings.json'.format("."), "r") as jsf:
   bookings = json.load(jsf)["bookings"]


# create booking endpoints according to the API specification
# get all bookings 
@app.route("/bookings", methods=['GET'])
def get_bookings():
   return make_response(jsonify(bookings),200)

# get booking by user id
@app.route("/bookings/<string:user_id>", methods=['GET'])
def get_booking(user_id):
   for booking in bookings:
       if booking["userid"] == user_id:
           return make_response(jsonify(booking),200)
   raise NotFound("Booking with id {} not found".format(user_id))

# post booking for a user
@app.route("/bookings", methods=['POST'])
def post_booking():
   booking = request.json
   # check if booking already exists
   for b in bookings:
       if b["userid"] == booking["userid"]:
           raise NotFound("Booking with id {} already exists".format(booking["userid"]))
   bookings.append(booking)
   return make_response(jsonify(booking),201)


@app.route("/", methods=['GET'])
def home():
   return "<h1 style='color:blue'>Welcome to the Booking service!</h1>"


if __name__ == "__main__":
   print("Server running in port %s"%(PORT))
   app.run(host=HOST, port=PORT)
