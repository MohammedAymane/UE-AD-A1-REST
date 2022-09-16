from datetime import datetime
from flask import Flask, render_template, request, jsonify, make_response
import json
from werkzeug.exceptions import NotFound

app = Flask(__name__)

PORT = 3202
HOST = '0.0.0.0'

with open('{}/databases/times.json'.format("."), "r") as jsf:
   schedule = json.load(jsf)["schedule"]

@app.route("/", methods=['GET'])
def home():
   return "<h1 style='color:blue'>Welcome to the Showtime service!</h1>"


#create showtime endpoints according to the API specification
@app.route("/", methods=['GET'])
def get_showtimes():
   return make_response(jsonify("Welcom to the showtimes endpoint"),200)

# get all showtimes
@app.route("/showtimes", methods=['GET'])
def getAllShowtimes():
   return make_response(jsonify(schedule),200)

# get showtime by date
@app.route("/showtimes/<string:date>", methods=['GET'])
def get_showtime(date):
   for showtime in schedule:
       if showtime["date"] == date:
           return make_response(jsonify(showtime),200)
   raise NotFound("Showtime with date {} not found".format(date))

   # get showtime by movie id
@app.route("/showtimes/movie/<string:movie_id>", methods=['GET'])
def get_showtimeByMovieId(movie_id):
   dates = []
   for showtime in schedule:
       if movie_id in showtime["movies"]:
         # convert 20151130 to 2015-11-30
           dates.append(datetime.strptime(showtime["date"], '%Y%m%d'))
           return make_response(jsonify(dates),200)
   raise NotFound("Showtime with movie id {} not found".format(movie_id))

   # get showtime by theatre id
   

if __name__ == "__main__":
   print("Server running in port %s"%(PORT))
   app.run(host=HOST, port=PORT)
