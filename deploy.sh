#!/bin/bash
git push heroku master
foreman run python manage.py collectstatic --noinput
