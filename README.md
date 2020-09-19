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

```
python -m flask run
```

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
