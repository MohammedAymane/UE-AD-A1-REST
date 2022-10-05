<div align="center" id="top"> 
  <img src="./.github/app.gif" alt="UE AD A1 REST" />

  &#xa0;

  <!-- <a href="https://ueada1rest.netlify.app">Demo</a> -->
</div>

<h1 align="center">UE AD A1 REST</h1>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/{{YOUR_GITHUB_USERNAME}}/ue-ad-a1-rest?color=56BEB8">

  <img alt="Github language count" src="https://img.shields.io/github/languages/count/{{YOUR_GITHUB_USERNAME}}/ue-ad-a1-rest?color=56BEB8">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/{{YOUR_GITHUB_USERNAME}}/ue-ad-a1-rest?color=56BEB8">

  <img alt="License" src="https://img.shields.io/github/license/{{YOUR_GITHUB_USERNAME}}/ue-ad-a1-rest?color=56BEB8">

  <!-- <img alt="Github issues" src="https://img.shields.io/github/issues/{{YOUR_GITHUB_USERNAME}}/ue-ad-a1-rest?color=56BEB8" /> -->

  <!-- <img alt="Github forks" src="https://img.shields.io/github/forks/{{YOUR_GITHUB_USERNAME}}/ue-ad-a1-rest?color=56BEB8" /> -->

  <!-- <img alt="Github stars" src="https://img.shields.io/github/stars/{{YOUR_GITHUB_USERNAME}}/ue-ad-a1-rest?color=56BEB8" /> -->
</p>

<!-- Status -->

<!-- <h4 align="center"> 
	🚧  UE AD A1 REST 🚀 Under construction...  🚧
</h4> 

<hr> -->

<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0; 
  <a href="#sparkles-features">Features</a> &#xa0; | &#xa0;
  <a href="#rocket-technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#dart_check_mark-Structure Of the project">Structure of the project</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="#memo-license">License</a> &#xa0; | &#xa0;
  <a href="https://github.com/{{YOUR_GITHUB_USERNAME}}" target="_blank">Author</a>
</p>

<br>

## :dart: About ##

This is a simple microservice application to manage movies reservation implemented using Flask and REST technology
## :sparkles: Features ##

:heavy_check_mark: CRUD for movies reservation


## :rocket: Technologies ##

The following tools were used in this project:

- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Docker](https://www.docker.com/)

## :white_check_mark: Requirements ##

Before starting :checkered_flag:, you need to have [Git](https://git-scm.com), [Python](https://www.python.org/), [Pipe](https://pypi.org/project/pip/) and [Docker](https://www.docker.com/) installed.


## :dart: Structure Of the project ##

The application is divided into 4 microservies (Booking, Showtime, User and Movie). 
Each folder contains a :
  - python implementation of the microservice with Flask using the REST Architecture
  - A json file as a database.
  - A Requirement file and a Dockerfile to create a docker image for the service
  - The OpenApi specification for the service
```
UE-AD-A1-REST
│   README.md
│   docker-compose.yml
│   file.py
│   LICENSE
│   requirements.txt  
│
└───booking
│   │   booking.py
│   │   Dockerfile
│   │   requirements.txt
│   │   UE-archi-distribuees-Booking-1.0.0-resolved.yaml
│   │
│   └───database
│       │   bookings.json
│
│   
└───movie
│   │   movie.py
│   │   Dockerfile
│   │   requirements.txt
│   │   UE-archi-distribuees-Movie-1.0.0-resolved.yaml
│   │
│   └───database
│       │   movies.json
│
│   
└───showtime
│   │   showtime.py
│   │   Dockerfile
│   │   requirements.txt
│   │   UE-archi-distribuees-Showtime-1.0.0-resolved.yaml
│   │
│   └───database
│       │   times.json
│
│   
└───user
│   │   user.py
│   │   Dockerfile
│   │   requirements.txt
│   │   UE-archi-distribuees-User-1.0.0-resolved.yaml
│   │
│   └───database
│       │   user.json
```

## :checkered_flag: Starting ##

```bash
# Clone this project
$ git clone https://github.com/MohammedAymane/UE-AD-A1-REST

# Access
$ cd ue-ad-a1-rest

# Install dependencies
$ pip -r requirements.txt

# Run a specific microservice (movie for example)
$ cd movie
$ python movie.py
$ pymon movie.py (in developpment mode)


# The movie service will initialize in the <http://localhost:3200>
```
## :checkered_flag: Containerizing the application ##
```bash
# Creating the containers
$ cd movie
$ docker build .

# Running the containers
$ cd UE-AD-A1-REST
$ docker-compose up

```

## :memo: License ##

This project is under license from MIT.


Authors : OUGGADI Mohammed-Aymane - MAKNI Sonda

&#xa0;

<a href="#top">Back to top</a>
