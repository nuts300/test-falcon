#!/bin/sh
# For development
gunicorn -b :8001 --reload 'sample.app:get_app()'