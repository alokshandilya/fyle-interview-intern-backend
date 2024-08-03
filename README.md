# Fyle Backend Challenge

## Setup

- setup python 3.8 and install dependencies
- install [pyenv](https://github.com/pyenv/pyenv)

``` sh
pyenv install 3.8  # defaults to 3.8.19
pyenv local 3.8
python -m venv .venv
source .venv/bin/activate  # for fish shell, use .venv/bin/activate.fish
pip install -r requirements.txt
```

- task details [here](./Application.md)

## Some Aliases to make life easier

``` sh
alias rest='rm core/store.sqlite3 -f && export FLASK_APP=core/server.py && flask db upgrade -d core/migrations'
alias resttest='rm core/store.sqlite3 -f && export FLASK_APP=core/server.py && flask db upgrade -d core/migrations && pytest -vvv -s tests/'
```
- `rest` to reset the database, will be helpful to test via `postman`
- `resttest` to reset the database and run tests

### Start Server

```sh
bash run.sh
```

- for test coverage report

```sh
# pytest --cov
# open htmlcov/index.html
```