# dungeon_and_dragons
A simple helper for DD games, taking form of an API

## Installation

First, clone this project
```
$ git clone git@github.com:MaxAdau/ddhelper.git
$ cd ddhelper
```
Then, check your python's version, you should use python3.4 for this project to run
```
$ ls -l /usr/bin/python*
```
It is a good idea to install a virtual environment dedicated for this project.
Virtualenv python's package will help you to do so.
```
# Install virtualenv
$ [sudo] python3.4 -m  pip install virtualenv
# Create a virtualenv linked to python3.4
$ virtualenv --python=/usr/bin/python3.4 <path/to/new/virtualenv/>
# Activate the created virtualenv
$ source <path/to/new/virtualenv/>/bin/activate
```
Install dependencies
```
$ pip install -r requirements
```
Run the application
```
$ python app.py
```
