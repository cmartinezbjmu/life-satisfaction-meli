# Life Satisfaction MELI

## Requirements

```
* python 3.8
* Flask 2.1.2
* Install virtual environment manager 'pipenv' (https://pypi.org/project/pipenv/)
* Install docker (https://www.docker.com/get-started)
```

## DotEnv

This API comes batteries included to use .env files in your codebase and already has a .env example file. You have to copy this file to your project root as .env for your project to run.

## Quick Start

### Deploy with Docker Compose

1. Clone the repository with the command "git clone https://github.com/cmartinezbjmu/life-satisfaction-meli.git"

2. Copy `.env.example` to `.env` file and adjust the value for the environment variables 

3. Download the MELI-dataset from https://worksampleprd.s3.amazonaws.com/static/worksample/2022/06/09/meli_dataset.csv and paste this file on `static/csv/`folder

4. Excecute this command:

   ```
   docker compose up
   ```

Now you can see the server running on the IP [http://127.0.0.1:8080](http://127.0.0.1:8080/)

### Run in local environment

Please follow the next steps to run the Flask API in your local machine:
1. Clone the repo
2. Copy `.env.example` to `.env` file and adjust the value for the environment variables 
3. Download the MELI-dataset from https://worksampleprd.s3.amazonaws.com/static/worksample/2022/06/09/meli_dataset.csv and paste this file on `static/csv/`folder
4. Install `pipenv` if not installed (`pip install pipenv`)
5. In the root of the project run `pipenv install` and then `pipenv shell`
6. Run `flask run` and your server should be alive on `localhost:5000`

## Endpoints
#### Get list with countries life satisfaction greater than user set index

`POST`

```
curl --location --request POST 'http://127.0.0.1:8080/api/v1.0/countries/life-satisfaction?index_gt=7' \
--header 'Content-Type: application/json'
```

#### Server status

`GET`

```
curl --location --request GET 'http://127.0.0.1:8080/api/v1.0/ping' \
--header 'Content-Type: application/json'
```

