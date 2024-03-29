# Booking Agent Web App

Project Prompt:

> Fyyur is a musical venue and artist booking site that facilitates the discovery and bookings of shows between local performing artists and venues. This site lets you list new artists and venues, discover them, and list shows with artists as a venue owner.
> 
> Your job is to build out the data models to power the API endpoints for the Fyyur site by connecting to a PostgreSQL database for storing, querying, and creating information about artists and venues on Fyyur.

### Project / Stack Structure

* **SQLAlchemy** - ORM library
* **PostgreSQL** - database
* **Python3** and **Flask** as server language and server framework
* **Flask-Migrate** for creating and running schema migrations
* **HTML**, **CSS**, and **Javascript** with [Bootstrap 3](https://getbootstrap.com/docs/3.4/customize/) for our website's frontend

## Prerequisites and Dependencies
* [Install Flask](http://flask.pocoo.org/docs/1.0/installation/#install-flask) if you haven't already.

  ```
  $ cd ~
  $ sudo pip3 install Flask
  ```
* Install the dependencies:
  ```
  $ pip install -r requirements.txt
  ```


## Installation and Setup

To start and run the local development server,

* Initialize and activate a virtualenv:
  ```
  $ cd YOUR_PROJECT_DIRECTORY_PATH/
  $ virtualenv --no-site-packages env
  $ source env/bin/activate
  ```

* Run the development server:
  ```
  $ export FLASK_APP=myapp
  $ export FLASK_ENV=development # enables debug mode
  $ python3 app.py
  ```

* Navigate to Home page [http://localhost:5000](http://localhost:5000)


## Contributing Authors

C. Tyler Dennis  

## Licensing

This project is released under the [MIT License](https://opensource.org/licenses/MIT)
