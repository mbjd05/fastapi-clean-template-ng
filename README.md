# fastapi-clean-template-ng

## Description

_Example Application Interface using FastAPI framework in Python 3_

This example showcases Repository Pattern in Hexagonal Architecture _(also known as Clean Architecture)_. Here we have two Entities - Books and Authors, whose relationships have been exploited to create CRUD endpoint in REST under OpenAPI standard.

## About this fork

All actual work was done for Python 3.8 by [0xTheProDev](https://github.com/0xTheProDev), in his amazing [fastapi-clean-example](https://github.com/0xTheProDev/fastapi-clean-example). I just did the following to update it to 3.12:
- Update dependencies to Python 3.12 versions.
- remove outdated dependencies and install their newer equivalents (pydantic => pydantic-settings).
- Make pipfile install on Windows (the pipfile no longer tries to install the unsupported `uvloop` as a dep to `uvicorn` on Windows).
- Install `winloop` instead of `uvloop` on windows for when no hot-reload is needed.
- Add platform agnostic `run.py` entrypoint script with hot-reloading by default and an optional `--no reload` flag, which automatically picks the optimal event loop to use depending on current platform and 'reload choice'
- update installation instructions to clarify the process for Windows

## Installation

- Install all the project dependency using [Pipenv](https://pipenv.pypa.io):

  ```sh
  $ pipenv install --dev
  ```
  - If you're on Windows, install `uvicorn` manually afterwards, without uvloop, which doesn't run on Windows. (run.py will use `winloop` instead):
 
    ```sh
    $  pipenv run pip install uvicorn --no-binary uvicorn
    ```
    
- Run the server:
  ```sh
  $ pipenv run python run.py
  ```

- You can also open a shell inside virtual environment:

  ```sh
  $ pipenv shell
  ```

- Open `localhost:8000/docs` for API Documentation

- Open `localhost:8000/graphql` for GraphQL Documentation

_*Note:* In case you are not able to access `pipenv` from you `PATH` locations, replace all instances of `pipenv` with `python3 -m pipenv`._

## Testing

For Testing, `unittest` module is used for Test Suite and Assertion, whereas `pytest` is being used for Test Runner and Coverage Reporter.

- Run the following command to initiate test:
  ```sh
  $ pipenv run pytest
  ```
- To include Coverage Reporting as well:
  ```sh
  $ pipenv run pytest --cov-report xml --cov .
  ```

## License

&copy; MIT License
