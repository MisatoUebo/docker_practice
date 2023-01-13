#!/bin/sh

cd mysql
rm -drf mysql_data

cd logs
rm -rf *

cd ../../

cd app/src
rm -drf __pycache__

cd models
rm -drf __pycache__