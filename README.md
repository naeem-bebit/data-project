![Python application](https://github.com/naeem-bebit/data-project/workflows/Python%20application/badge.svg)

# Run flask locally

1. Activate the virtual environment

   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

1. Install requirements

   ```bash
   pip3 install -r requirements.txt
   ```

1. Run app locally

   ```bash
   FLASK_APP=src/app.py flask run
   ```

   Or

   ```bash
   python -m flask run
   ```

   Or

   ```bash
   flask run
   ```

   The server will be up on `http://127.0.0.1:5000/`

1. Run tests

   Specify the folder `tests`

   ```bash
   python -m pytest tests
   ```

   Or
   It will look recurcisvely for the `test_*.py` files

   ```bash
   python -m pytest
   ```

   Or

   ```bash
   py.test -v
   ```

1. Flake8 settings

   `.flake8` used by Github Actions `.github/workflows/lint-test.yaml`

## References

- [Flask](https://github.com/pallets/flask)
- [Black](https://github.com/psf/black)
