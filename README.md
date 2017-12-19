# Memo Saver App RESTful API

A simple RESTful API that allows the user to add text memos or pictures of written notes and view all.

## Features

### Record a Memo

* Add Plain Text Content
* Attach an image (Optional)
* With: The name of the participant in the meeting.
* Date: Date when the meeting took place.

### List All Memos

* Display All Memos in reverse chronological order, grouped by day.

## Setup

### Min. Requirements:
Python 3

```
# Get the latest code from github
git clone https://github.com/balrampariyarath/memoapp.git

# Go to the project directory
cd memoapp/

# Install Requirements.txt
pip install requirements.txt

# Migrate Database
python3 manage.py migrate

# Point MEDIA_ROOT in settings.py to location of memoapp/photos/ (upload folder)

# Run Tests
python3 manage.py test

# Run Server
python3 manage.py test
```

URL - http://localhost:8000/

## Docker Setup

TODO

API available at: http://localhost:8000/api/memos/


## API v1 Methods

| Sl.No | Method Name | Method Type | Parameters | URL | 
|-|:--:|--:|--:|--:|
| 1 | add | POST | desc (Text), image (Optional), date (YYYY-MM-DD) and person (Text) | http://your_server_ip/api/memos/add |
| 2.a | history | GET |  | http://your_server_ip/api/memos/history |
| 2.b | history | GET | ordering=+-date | http://your_server_ip/api/memos/history/?ordering=-date |
| 2.c | history | GET | search=name  | http://your_server_ip/api/memos/history/?search=name |
| 2.d | history | GET | search=date  | http://your_server_ip/api/memos/history/?search=date |

## Libraries Used
* Django - v2.0
* djangorestframework - v3.1.2
* Pillow - 2017.3
