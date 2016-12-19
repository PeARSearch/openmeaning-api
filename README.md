# openmeaning-api

* Open virtualenv and install requirements:

`source env/bin/activate`

`pip install -r requirements.txt`

`python manage.py migrate`

`python manage.py createsuperuser`

* Populate the database with vectors

`python populate_db.py`

* Run the server:

`python manage.py runserver`

* Visit http://127.0.0.1:8000/.
