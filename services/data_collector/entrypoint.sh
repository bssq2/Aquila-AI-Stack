#!/usr/bin/env sh
set -eu

# If the first argument is pytest (i.e. we’re running the test suite)
# start the API in the background so that the tests can hit it.
if [ "$1" = "pytest" ] || [ "$1" = "pytest-quiet" ] || [ "$1" = "pytest -q" ]; then
  uvicorn src.main:app --host 0.0.0.0 --port 6000 &
  # give uvicorn a brief moment to come up
  sleep 2
fi

# hand off to whatever command was passed to the container
exec "$@"