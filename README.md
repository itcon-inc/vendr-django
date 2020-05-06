# vendr Django App

This is a minimal Django app built using the Django rest framework.
It uses U.S. Census data and relies on a SQL database for storing
U.S. cities ranked by population.

These can then be retrieved by accessing "/cities" and "/cities/<id>"

Unit tests are included in the "api/tests" folder and pylint-django was used to 
ensure PEP compliance.

The `requirements-dev.txt` will get you going with the dependencies needed.
