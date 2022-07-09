To access the webiste go to https://jlb838.uk
Alternativley to install the set up on your own machine follow the instructions below
These instructions are designed to run on unix systems however I have only tested them on ubuntu and WSL 2
To install make sure you have the following installed
Python 3.8.10
pip 20.0.2
1. Extract the zip folder to somewhere you want to use it and navigate to that directory using the command line 
2. run sudo apt-get install libpq-dev python-dev
3. run sudo apt-get -y install postgresql postgresql-contrib
4. run sudo su - postgres
5. run createuser james
6. run createdb reccomender_db --owner james
7. run psql -c "ALTER USER james WITH PASSWORD 'helloworld10'"
8. run exit
9. run pip install -r requirements.txt
10. run python3 manage.py collectstatic
11. run python3 manage.py makemigrations
12. run python3 manage.py migrate
13. run python3 manage.py runserver
The server will now run at http://127.0.0.1:8000/
