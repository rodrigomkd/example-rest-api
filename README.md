Example REST API
=================

Basic template to develop an API with Flask

Usage
-----

Clone the repo:

    git clone https://github.com/rodrigomkd/example-rest-api
    cd example-rest-api

Create virtualenv:

    virtualenv {env_name} or python3 -m venv {env_name}
    source {env_name}/bin/activate
    pip install -r requirements.txt

Run the server

    python3 api.py

Try the endpoints:

    curl -XGET http://localhost:5000/api/v1/hello-world
    curl -XGET http://localhost:5000/api/v1/message

Swagger docs available at `http://localhost:5000/swagger`


License
-------

MIT, see LICENSE file
