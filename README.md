![](https://github.com/naeem-bebit/data-project/actions/workflows/lint-test.yaml/badge.svg)
[![Python application](https://github.com/naeem-bebit/data-project/actions/workflows/lint-test.yaml/badge.svg)](https://github.com/naeem-bebit/data-project/actions/workflows/lint-test.yaml)


# Run flask locally

1. Activate the virtual environment
   
   Install virtualenv if not available
   ```console
   pip install virtualenv
   ```

   ```console
   python3 -m venv env or python -m venv env
   source env/bin/activate
   ```

   Or

   ```console
   . env/bin/activate
   ```
   
   Windows (Command Prompt)
   
   ```console
   virtualenv myenv  ##(name of the env)
   myenv\Scripts\activate
   env\Scripts\activate.bat
   ```
   
   To check Python environment (Windows)
   ```console
   where python
   C:\Users\..\..\env\Scripts\python.exe
   C:\Users\..\AppData\Local\Programs\Python\Python310\python.exe
   C:\Users\..\AppData\Local\Microsoft\WindowsApps\python.exe
   ```
      
   To list all installed packages
   ```console
   pip list
   ```

1. To delete virtual environment
   ```console
   rmdir env /s
   ```

1. To deactivate the virtual environment

   ```console
   deactivate
   ```

1. Install requirements

   ```console
   pip3 install -r requirements.txt
   ```
   
1. Get packages from main Python environment
   ```console
   python -m venv env --system-site-packages
   ```
   
   Check for local Python packages
   ```console
   pip list --local
   ```

1. Setting up the flask development environment

   ```console
   export FLASK_ENV=development
   export FLASK_APP=/src/app.py #optional
   ```

1. Run app locally

   ```console
   FLASK_APP=src/app.py flask run
   ```

   Or

   ```console
   python -m flask run
   ```

   Or

   ```console
   flask run
   flask --app app(name of the file) run --debug #auto reload
   ```

   The server will be up on `http://127.0.0.1:5000/`

1. Run tests

   Specify the folder `tests`

   ```console
   python -m pytest tests
   ```

   Or
   It will look recurcisvely for the `test_*.py` files

   ```console
   python -m pytest
   ```

   Or

   ```console
   py.test -v
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
   
1. Docker verify installation

   ```console
   docker run --name repo alpine/git clone https://github.com/docker/getting-started.git
   cd getting-started
   docker build -t docker101tutorial .
   docker run -d -p 80:80 --name docker-tutorial docker101tutorial
   docker tag docker101tutorial naeem15/docker101tutorial
   docker push naeem15/docker101tutorial
   ```

1. Typescript setting

   ```console
   tsc main.ts --outFile ../js/main.js --watch
   ```

1. Sass
   
   ```console
   sass --watch main.sass ../css/main.css
   ```

1. Conda (windows)

   ```console
   conda create --name env_name python=3.11
   conda activate env_name
   conda deactivate
   ```
## References

- [Flask](https://github.com/pallets/flask)
- [Flask Quick Start](https://flask.palletsprojects.com/en/2.0.x/quickstart/)
- [Black](https://github.com/psf/black)
- [Dockerfile Linter](https://github.com/hadolint/hadolint)
- [Docker Python](https://www.docker.com/blog/tag/python-env-series/)
- [Pre-commit Github Actions](https://github.com/pre-commit/action)
- [Django docker compose](https://docs.docker.com/samples/django/)
- [Hosting REST API Github](https://dev.to/myogeshchavan97/how-to-easily-create-and-host-your-own-rest-api-without-writing-a-single-line-of-code-2np4)
  
