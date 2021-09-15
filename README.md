![Python application](https://github.com/naeem-bebit/data-project/workflows/Linter%20&%20test/badge.svg)

# Run flask locally

1. Activate the virtual environment

   ```console
   $ python3 -m venv env
   $ source env/bin/activate
   ```

   Or

   ```console
   $ . env/bin/activate
   ```

1. To deactivate the virtual environment

   ```console
   $ deactivate
   ```

1. Install requirements

   ```console
   $ pip3 install -r requirements.txt
   ```

1. Setting up the flask development environment

   ```console
   $ export FLASK_ENV=development
   $ export FLASK_APP=/src/app.py
   ```

1. Run app locally

   ```console
   $ FLASK_APP=src/app.py flask run
   ```

   Or

   ```console
   $ python -m flask run
   ```

   Or

   ```console
   $ flask run
   ```

   The server will be up on `http://127.0.0.1:5000/`

1. Run tests

   Specify the folder `tests`

   ```console
   $ python -m pytest tests
   ```

   Or
   It will look recurcisvely for the `test_*.py` files

   ```console
   $ python -m pytest
   ```

   Or

   ```console
   $ py.test -v
   ```

1. Flake8 settings

   `.flake8` used by Github Actions `.github/workflows/lint-test.yaml`

1. `pipreqs` for requirements

1. Docker build and docker run

   ```console
   docker build -t flask_app:v1 .
   docker run flask_app
   docker container run -d -p 5000:5000 flask_app:v1
   ```

1. Check for Dockerfile Linter

   ```console
   docker run --rm -i hadolint/hadolint < Dockerfile
   ```

1. Docker debug

   ```console
   docker container prune # to remove existing containers.
   docker-compose build --no-cache # to rebuild docker images.
   docker-compose up --build --force-recreate
   docker stop $(docker ps -aq) # to stop all running dockers
   docker ps # to list of all running dockers
   docker run -p 5000:5000 docker_image # to run on port 5000
   ```

1. Typescript setting

   ```console
   $ tsc main.ts --outFile ../js/main.js --watch
   ```

1. Sass
   ```console
   $ sass --watch main.sass ../css/main.css
   ```

## References

- [Flask](https://github.com/pallets/flask)
- [Black](https://github.com/psf/black)
- [Dockerfile Linter](https://github.com/hadolint/hadolint)
- [Docker Python](https://www.docker.com/blog/tag/python-env-series/)
- [Pre-commit Github Actions](https://github.com/pre-commit/action)
