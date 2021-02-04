#!/usr/bin/env bash

# Run application
uvicorn server:app --workers 1 --host=0.0.0.0 --port=80 --timeout-keep-alive=180
