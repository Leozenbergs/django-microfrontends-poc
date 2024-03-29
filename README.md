# django-microfrontends-poc

## Description
A microfrontend by Django SSR prove of concern
> Archtecture inspired by this [article](https://medium.com/zenithec-techware/serve-spa-with-django-1f492f2857ed)

## Dependencies
- python v3
- node.js v16


## installation
``` shell
# django dependencies:
  cd mysite
  # create virtualenv
  python -m virtualenv -p python3 venv
  # install django requirements
  pip install -r requirements.txt
  # make initial migration
  python manage.py migrate

cd ..
# react dependencies:
  cd simple-react
  npm install
```

## Running
For running the project correctly you must build the microfrontend first
``` shell
# build react-app
  cd simple-react
  npm run build
```
And then run the project properly
``` shell
cd ..
  # collect django static files
  cd mysite
  python manage.py collectstatic

  # run django
  python manage.py runserver
```