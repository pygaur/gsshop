#!/bin/bash

NAME="src"                                   # Name of the application
DJANGODIR=/gs/gsshop/gsshop/src            # Django project directory
SOCKFILE=/gs/gsshop/gsshop/src/run/gunicorn.sock   # we will communicate using this unix socket
USER=gs                                      # The user to run as
GROUP=gs                                   # The group to run as
NUM_WORKERS=4                                   # How many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=src.settings.production          # Which settings file should Django use
DJANGO_WSGI_MODULE=src.wsgi                  # WSGI module name

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source /gs/gsshop/gsshop_env/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
exec gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user $USER \
  --bind=unix:$SOCKFILE


