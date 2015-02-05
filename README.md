# README #

### Hub-Of-All-Things - University of Warwick ###

* This repository is the central code repository for the Hub of All Things (University of Warwick) web application.

## How do I use the API? ###

* API documentation is available at: http://hat.onespace.media/api/v1/

### How do I get set up? ###


#### Development Database

The HAT uses PostgreSQL database. For development you could use one locally, e.g.:

    postgres -D /usr/local/var/postgres
    createdb hat
    createuser hat -P

Once you have run all the database initialisation scripts, you should make sure that the configured database user has access to the necessary tables:

	psql hat -c "GRANT ALL ON ALL TABLES IN SCHEMA public to hat;"
	psql hat -c "GRANT ALL ON ALL FUNCTIONS IN SCHEMA public to hat;"
	psql hat -c "GRANT ALL ON ALL SEQUENCES IN SCHEMA public to hat;"

#### Development Server

Make sure you have entered your database configuration in Django configs (e.g. `settings/local.py`)

Setting up then proceeds in a few steps:

	# Setup project dependencies
	pip install -r requirements.txt 
	# Setup base database models (for INSTALLED_APPS, etc.)
	python manage.py syncdb
	# Migrate app models
	python manage.py migrate

Caveat with app model migration: the default oder of migration does not work, but you can get around this by expliitly specifying the order:

	python manage.py migrate things
	python manage.py migrate locations
	python manage.py migrate events
	python manage.py migrate users
	python manage.py migrate

The import system data (curriencies, ethnicities, genders, etc.):
	
	python manage.py system_importer

Finally, load data fixtures (also needs to happen in a specific order):

	python manage.py loaddata hat/fixtures/thing_types.json
	python manage.py loaddata hat/fixtures/things.json
	python manage.py loaddata hat/fixtures/units.json
	python manage.py loaddata hat/fixtures/sensors.json


### Contribution guidelines ###

* TBC

### Where can I see the live proof-of-concept? ###

* http://hat.onespace.media/

### Who do I talk to? ###

* daniel@onespacemedia.com (Daniel Samuels, Lead Developer)
* tom@onespacemedia.com (Thomas Rumbold, Head of Product)
* jamesfoley@onespacemedia.com (James Foley, Developer)
* x.ma@warwick.ac.uk (Xiao Ma, Project Lead @ University of Warwick)

### License

HAT database schema beta by [RCUK HAT Project Universities](http://www.hubofallthings.com/) is licensed under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/)