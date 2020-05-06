# vendr Django App

This is a minimal Django app built using the Django rest framework.
It uses U.S. Census data and relies on a SQL database for storing
U.S. cities ranked by population. It was developed using PostgreSQL.

These can then be retrieved by accessing `/apps/v1/cities` and `/apps/v1/cities/<id>`

Unit tests are included in the "api/tests" folder and pylint-django was used to 
ensure PEP compliance. You can run the tests with `$ pylint api.tests

The `requirements-dev.txt` will get you going with the dependencies needed.
