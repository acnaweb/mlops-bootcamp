export IMAGE_NAME=mlops_bootcamp

# Local development
install:
	python -m venv venv; \
	. venv/bin/activate; \
	pip install --upgrade pip; \
	pip install pre-commit; \
	pip install -e .[interactive]; \
	pre-commit install; \
	git config --bool flake8.strict true; \
	mkdir data models; \
	dvc init; \
	dvc config core.autostage true; \

formatter:
	black src

# Continuous Integration
typing: formatter
	mypy src

lint:
	flake8  src

build:
	python setup.py install

test:
	pytest

# Containter

c_build:
	docker build -t ${IMAGE_NAME} .

c_run:
	docker run --env-file .env -d ${IMAGE_NAME} 

# Continuous Deployment/Delivery
coverage:
	echo "run coverage"

deploy_staging:
	echo "deploy staging"

deploy_production:
	echo "deploy production"

smoke_test:
	echo "smoke test"	

run:
	python main.py --action action1 --param1 "valor qualquer"

docs_view:
	pdoc --http : src

docs_save:
	pdoc --html --output-dir ./docs src

train:
	python src/train_pipeline.py

predict:
	python src/predict.py