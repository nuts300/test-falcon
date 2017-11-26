#!/bin/sh
# For development
gunicorn --reload 'sample.app:get_app()'