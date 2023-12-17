# About

This is the readme file of MAD2 Project of Sep-23 Term

# Testing Application

## Requirements

- Application zip file
- Python 3.10
- OS: Windows with WSL running on Ubuntu 22.04
- Browser Firefox/Chrome
- Terminal

- WSL Setup
- Installation of redis-server and redis service should be running
  $ sudo install redis-server
  $ sudo system start redis-server
  $ sudo status redis-server   -> make sure that redis-server is running and online
- MailHog
  $ sudo apt-get -y install golang-go
  $ go get github.com/mailhog/MailHog
  $ ~/go/bin/MailHog

- Host PC Setup
- Open browser and run http://localhost:8025
- This should bring up the mail interface

## Project Setup

- Unzip Project file
- Open the terminal to the unziped folder
- python -m venv env
- $ source ./env/source/bin
- $ pip install -r requirements.txt
- $ node ci
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
- Open Firefox
- Run with http://localhost:3000
- Follow onscreen instructions
- By default only admin user is crated(pass:admin)
- Signup to create regular user and manager


--- END OF FILE ---
