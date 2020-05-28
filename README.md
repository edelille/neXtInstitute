# neXtInstitute


This web app uses Django Python web framework. To install and run this webapp locally.

## Running the server locally

1. Make sure Python 3.8 is up and running through command line, using the following link

  https://www.python.org/downloads/

2.a. To run the app on windows, run the following commands in command prompt (windows):

```bash
git clone https://github.com/lamn18/neXtInstitute.git
cd neXtInstitute
.\env\py3.8env\Scripts\activate
pip3 install -r requirements.txt
py manage.py migrate
py manage.py runserver
```

2.b. Additionally, to run the server on a linux machine, run these set of commands (linux/macOs):

```bash
git clone https://github.com/lamn18/neXtInstitute.git
cd neXtInstitute
source env\py3.8env\Scripts\activate
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver
```

3. After running the following commands, you can find the local development server in your browser at localhost:8000 by default
