#!/bin/sh
gunicorn --reload 'sample.app:get_app()'