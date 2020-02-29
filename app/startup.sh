#!/usr/bin/env bash

ENV=$1

if [ $ENV == 'local' ]; then
    /start-reload.sh
elif [ $ENV == 'production' ]; then
    /start.sh
fi
