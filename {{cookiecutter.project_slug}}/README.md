## Pre-requisites

Before getting started, please ensure that you have the following dependencies installed on your system:

- [langchain](https://www.langchain.com/)
- [streamlit](https://streamlit.io/)
- [poetry](https://python-poetry.org/)

## Getting Started

To set up and run the app, please follow these steps:

1. Move to the directory where `pyproject.toml` is located:

   ```shell
   cd {{ cookiecutter.project_slug }}
   ```
2. Define your environment variables:

   ```shell
   cp .end.sample .env
   ```

3. Install pre-commit hooks (required):

   ```shell
   pre-commit install
   ```
   
4. Install the dependencies:

   ```shell
   poetry install
   ```

   If you don't want to install the dev packages,
   you can use the following command instead:
   ```shell
   poetry install --without dev
   ```

5. Activate the virtual environment:

   ```shell
   poetry shell
   ```

6. All necessary commands to start with the project can be found in Makefile.
   To see all available commands, run the following command:

   ```shell
   make help
   ```

7. Start application:

   ```shell
   make run-app
   ```

8. Here u go! Open `http://localhost:{{ cookiecutter.app_port }}` to see the app running.


<p style="text-align: center; font-size: 20px">enjoy ! 🚀</p>