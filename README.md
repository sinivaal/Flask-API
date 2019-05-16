# Simple Flask API

This is a simple GET capable API for a database built with Python microframework Flask.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You will need a database that your API can make a call to. Also Python 3 needs to be installed.

```
*Python 3 installed.
*Database with PostgreSQL and some tables with data.
```

### Installing

Start with making a virtual enviroment in your desired directory:

[Good guide](https://realpython.com/python-virtual-environments-a-primer/) for staring with venv tool.

```
python3 -m venv env
```
Then activate your virtual enviroment:
```
source env/bin/activate
```
and clone the repository to your project folder:

```
git clone https://github.com/sinivaal/Flask-API.git
```

Then install the dependencies using python:

```
python -m pip install -r requirements.txt
```

Finally start your Flask server:
```
python run.py
```

Navigate to :
```
http://0.0.0.0:5000/
```

## Built With

* [Flask](http://flask.pocoo.org/) - Python microframework
* [Psycopg2](http://initd.org/psycopg/) - PostgreSQL database adapter


## Authors

* **Sinivaal** - *Initial work* - [sinivaal](https://github.com/sinivaal)


## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details

## Acknowledgments

* Hat tip to anyone who will use the code

