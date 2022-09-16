from flask import Flask, render_template, request, jsonify, make_response
import requests
import json
from werkzeug.exceptions import NotFound

app = Flask(__name__)

PORT = 3203
HOST = '0.0.0.0'

with open('{}/databases/users.json'.format("."), "r") as jsf:
   users = json.load(jsf)["users"]

# create user endpoints according to the API specification
# get all users
@app.route("/users", methods=['GET'])
def get_users():
   return make_response(jsonify(users),200)

# get user by id
@app.route("/users/<string:user_id>", methods=['GET'])
def get_user(user_id):
   for user in users:
       if user["id"] == user_id:
           return make_response(jsonify(user),200)
   raise NotFound("User with id {} not found".format(user_id))

# post user
@app.route("/users", methods=['POST'])
def post_user():
   user = request.json
   # check if user already exists
   for u in users:
       if u["id"] == user["id"]:
           raise NotFound("User with id {} already exists".format(user["id"]))
   users.append(user)
   return make_response(jsonify(user),201)


   # remove user
@app.route("/users/<string:user_id>", methods=['DELETE'])
def delete_user(user_id):
   for user in users:
       if user["id"] == user_id:
           users.remove(user)
           return make_response(jsonify(user),200)
   raise NotFound("User with id {} not found".format(user_id))

   # update user
@app.route("/users/<string:user_id>", methods=['PUT'])
def put_user(user_id):
   user = request.json
   for u in users:
       if u["id"] == user_id:
           users.remove(u)
           users.append(user)
           return make_response(jsonify(user),200)
   raise NotFound("User with id {} not found".format(user_id))


   # get bookings for a user by user id using the booking service
@app.route("/users/<string:user_id>/bookings", methods=['GET'])
def get_user_bookings(user_id):
   # check if user exists
   for user in users:
       if user["id"] == user_id:
           # get bookings for user
           r = requests.get("http://localhost:3201/bookings/{}".format(user_id))
           return make_response(r.json(),200)
   raise NotFound("User with id {} not found".format(user_id))
   

# get movies for a user by user booking using the booking and movie services
@app.route("/users/<string:user_id>/movies", methods=['GET'])
def get_user_movies(user_id):
   # check if user exists
   for user in users:
       if user["id"] == user_id:
           # get bookings for user
           r = requests.get("http://localhost:3201/bookings/{}".format(user_id))
           booking = r.json()
           # get movies for all bookings
           movies = []
           
           for b in booking["dates"]:
               for s in b["movies"]:
                  movies.append(requests.get("http://localhost:3200/movies/"+s).json())
           return make_response(jsonify(movies),200)
   raise NotFound("User with id {} not found".format(user_id))



@app.route("/", methods=['GET'])
def home():
   return "<h1 style='color:blue'>Welcome to the User service!</h1>"





if __name__ == "__main__":
   print("Server running in port %s"%(PORT))
   app.run(host=HOST, port=PORT)
