#!/bin/bash
git push heroku master
heroku run ./manage.py collectstatic
