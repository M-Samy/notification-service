#!/usr/bin/env bash

# Run application
gunicorn server:app -w 4 -b 0.0.0.0:80 --timeout=180 --limit-request-line=0
