## FTNIJA

=========

**FTNIJA** is a stock market watcher that looks for the trending and currency exchange and how they are doing. It was made with python, and django framework

# REQUIREMENT

asgiref==3.5.2

beautifulsoup4==4.11.1

dj-database-url==0.5.0

Django==4.0.5

django-heroku==0.3.1

gunicorn==20.1.0

jsonfield==3.1.0

matplotlib==3.5.2

psycopg2==2.9.3

python-decouple==3.6

pytz==2022.1

requests==2.28.0

selenium==4.3.0

sqlparse==0.4.2

whitenoise==6.2.0

<<<<<<< HEAD

=======
>>>>>>> e89ae76523031e83c79aaaee953f7d9cd25424fa
`selenium installation is not necessary because it was not used in this project`

# INSTALLATION

Run pip install -r requirements.txt (Python 2), or pip3 install -r requirements.txt (Python 3)
$ pip install -r requirements.txt
or
$ pip3 install -r requirements.txt

**It will be better for this project to be executed in a virtual environment**

## SUMMARY

This web application, automate the process of monitoring the equity and balance. Majorly currency market.
I tried using selenium for automating but it has an draw back because it might not work on most browser.
The site that was provided to scrape was does not have a view source page, that made it harder to create a bot to scrape and or login to the site. I solved that problem by getting data from other sisters platform. The home page of this web sites displays the data stored in the database.
When the ``lunch bot`` button is clicked you are taken to the automation process where the page is reloaded every ``Five minutes``.
Every time the automated  site is reloaded, the previous data gets stored in the database replacing the previous one.
The web site `https://trade.mql5.com/trade?servers=` was build with MQL5 programming language

# LANGUAGE

Python 3.9.6
was used for this project,
Bootstrap 5.2.0
Was used for styling
``there was no javascript used in this project``
