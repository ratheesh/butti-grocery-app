# About

This is the Readme File of MAD2 Project of Sep-23 Term that I submitted as a part of Diploma in Programming course pursued at IIT Madras

# Screenshots
Screenshots of the application features is available in the [Wiki](https://github.com/ratheesh/butti-grocery-app/wiki/Application-Screenshots) Section.

# Images for testing
Product image for testing are placed in testing/images/products

# Testing Application
## Requirements

- Application zip file
- Python 3.10
- OS: Windows with WSL running on Ubuntu 22.04
- Browser Firefox/Chrome
- Terminal

- WSL Setup
- `redis-server` installation and setup
``` bash
  $ sudo install redis-server
  $ sudo system start redis-server
  $ sudo status redis-server   # make sure that redis-server is running and online
```
- MailHog service setup and execution
``` bash
  $ sudo apt-get -y install golang-go
  $ go get github.com/mailhog/MailHog
  $ ~/go/bin/MailHog
```
- Host PC Setup
- Open browser and goto `http://localhost:8025`
- This should bring up the mail interface

## Project Setup
- Unzip Project file
- Open the terminal to the unziped folder
- python -m venv env
- $ source ./env/source/bin
- $ pip install -r requirements.txt
- $ npm install ci
- Open 3 terminal windows
- Terminal 1
  - $ cd backend
  - $ python main.py
- Terminal 2
  - $ cd backend
  - $ celery -A main.celery worker -E -B --loglevel INFO
- Terminal 3
  - $ npm run dev

## Run the Application
- Open Firefox and launch the applicaiton with URL http://localhost:3000
- Follow onscreen instructions for using application
- By default only admin user is created(username: admin pass:admin)
- Signup to create manager and regular user

# License
MIT
