# openmeaning-api

The openmeaning api lets users access vectors in json format from
openmeaning.org, using the word that the vector represents. The code in this
repo lets PeARS team setup the server with a database of vectors, taken from a
.dm file.

## Install

* Open virtualenv and install requirements:

`source env/bin/activate`

`pip install -r requirements.txt`

`python manage.py migrate`

`python manage.py createsuperuser`

* Populate the database with vectors

`python populate_db.py`

##Try it out

* Run the server:

`python manage.py runserver`

* Visit http://127.0.0.1:8000/ and click on e.g.
  http://127.0.0.1:8000/vectors/. Single vectors can be accessed via urls of
  the type http://127.0.0.1:8000/vectors/the/, where the word to be queried
  forms the last part of the url. 
  
  Vectors can also be queried via e.g. curl: 

`curl -u admin:password123 http://127.0.0.1:8000/vectors/the/`
