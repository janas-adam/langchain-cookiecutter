.PHONY: help
help: ## Show this help (usage: make help)
	@echo "Usage: make [target]"
	@echo "Targets:"
	@awk '/^[a-zA-Z0-9_-]+:.*?##/ { \
		helpMessage = match($$0, /## (.*)/); \
		if (helpMessage) { \
			target = $$1; \
			sub(/:/, "", target); \
			printf "  \033[36m%-20s\033[0m %s\n", target, substr($$0, RSTART + 3, RLENGTH); \
		} \
	}' $(MAKEFILE_LIST)


.PHONY: run-app
run-app: ## Run streamlit interface
	streamlit run app/main.py --server.port {{ cookiecutter.app_port }}

black:
	poetry run black .

ruff:
	poetry run ruff check . --fix

.PHONY: lint
lint: ## Format your code
	make black
	make ruff
