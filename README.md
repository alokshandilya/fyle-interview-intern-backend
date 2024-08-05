# Fyle Backend Challenge

## Table of Contents

- [Fyle Backend Challenge](#fyle-backend-challenge)
  - [Table of Contents](#table-of-contents)
  - [Setup](#setup)
  - [Some Aliases to make life easier](#some-aliases-to-make-life-easier)
    - [Start Server](#start-server)
  - [Starting point](#starting-point)
  - :star2: [Ending point](#ending-point)
- [Docker Setup](#docker-setup)
  - [Build the image](#build-the-image)
  - :star2: [Pull my image](#pull-my-image)
  - [Run the image](#run-the-image)
  - :star2: [Final Screenshot](#final-screenshot)

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

## Starting point

![5_of_18](https://github.com/user-attachments/assets/9b9dcab6-eefe-4a17-a989-81a0bb37d232)

- $5$ tests are passing

- task detail : [link](./Application.md)

## Ending point

![20240804_22h50m02s_grim](https://github.com/user-attachments/assets/c41cf2ec-8d21-42ff-8de3-06fa006f969e)

![20240805_06h04m08s_grim](https://github.com/user-attachments/assets/bca25ce8-6caa-45be-993b-105ea9ea59e6)

![20240805_06h05m46s_grim](https://github.com/user-attachments/assets/b4003462-16dd-4169-9580-b1cd048eb18f)


# Docker Setup

- Docker documentation _[here](https://docs.docker.com/get-started/)_

## Build the image


```sh
docker buildx build -t fyle-intern .
# for pushing to docker hub, you need to login first via `docker login`
docker tag fyle-intern alokshandilya/fyle-intern:latest
docker push alokshandilya/fyle-intern:latest  # optional
```

- replace `alokshandilya` with your username

## Pull my image

> :star2: if you want my image _(~190MB)_ instead of building it yourself, you can pull it from [here](https://hub.docker.com/r/alokshandilya/fyle-intern) via `docker pull alokshandilya/fyle-intern:latest`

```sh
docker pull alokshandilya/fyle-intern:latest
```

## Run the image

```sh
docker run -it -p 5000:7755 fyle-intern
# or if you pulled my image then
docker run -it -p 5000:7755 alokshandilya/fyle-intern:latest
```

- visit `http://localhost:5000/` or `http://127.0.0.1:5000/` in your browser or postman instance
    - you can choose any port in place of `5000`, be consistent with the `docker run` command

## Final Screenshot

![20240805_06h50m36s_grim](https://github.com/user-attachments/assets/637de76e-0b2c-4c5e-8ea2-d35837ed4265)
