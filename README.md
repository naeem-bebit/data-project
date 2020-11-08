![Python application](https://github.com/naeem-bebit/data-project/workflows/Python%20application/badge.svg)

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

## References

- [Flask](https://github.com/pallets/flask)
- [Black](https://github.com/psf/black)
