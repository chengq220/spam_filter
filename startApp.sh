#!/bin/bash


default_dir="$(cd "$(dirname "$0")" && pwd)"
echo $default_dir

#'Run the script to start the front-end application'
echo "Starting the React Application"
#reactApp_dir="$(cd naive-bayes-app)"
reactApp_dir="$default_dir/naive-bayes-app"
cd "$reactApp_dir" && npm start &


#'run the script to start the backend endpoints'
echo "Starting the Djanjo EndPoints"
backend_dir="$default_dir/classifier_backend"
cd "$backend_dir" && python manage.py runserver &


