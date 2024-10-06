# LangChain Cookiecutter 🦜
LangChain Cookiecutter is a streamlined project template designed to help you rapidly kickstart your AI/ML applications using LangChain and Streamlit.

## Launch ✨

Go to the desired directory and run:

1. Make sure u have [**cookiecutter**](https://cookiecutter.readthedocs.io/en/stable/) installed
```bash
pip install cookiecutter
```

2. Create your project template
```bash
cookiecutter https://github.com/janas-adam/langchain-cookiecutter.git
```

## Features ⚙️

- **langchain** - framework for apps powered by large language models (LLMs)
- **poetry** - python deps management
- **streamlit** - open-source python framework for data scientists and AI/ML engineers
- **github workflows** - CICD
- **pre-commit** - hooks for code formatting and linting

## cookiecutter parameters explained 👨‍💻

- `project_name`: Name of the project repository (e.g. `LangChain Application`)
- `project_slug`: Slugified project name - it represents simplified project name
- `author_name`: Project author name
- `email`: Email address of the project author
- `description`: Brief summary of what the project is
- `version`: Indicates the current version of the project
- `license`: Specifies the type of license under which project is released 
- `app_port`: The port number on which the streamlit application ll run

## Contributions 🚀
Contributions are kindly welcomed! if you are interested in helping improve this cookiecutter specify an issue and help us enhance the project together!

## License 📝
This project is licensed under the terms of the MIT license.