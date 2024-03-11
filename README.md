# MLOps Bootcamp

## Install


```sh
make install

``` 

## Info


MLOps with MLFlow, Scikit-learn, CI/CD, Azure, FastAPI, Gradio, SHAP, Docker, DVC, Flask, BentoML.


### Experiment Tutorial


- https://dagshub.com/acnaweb/experiment-tutorial.git


### Project Template (Cookiecutter Data Science)

```
cookiecutter https://github.com/khuyentran1401/data-science-template
```

### Configuration File (Hydra)

- https://hydra.cc/

### API Documentation for Python Projects

- https://pdoc.dev/

### Data Versioning (Dvc)

- https://dvc.org/

#### Commands

```
dvc init
dvc add data
dvc commit -m "A change"
dvc pull
```
#### Dvc Pipelines

```sh
dvc repro
```

#### Dvc Remote S3 (MinIO)

- Add remote

```sh
dvc remote add -d minio s3://dvc/datasets -f
dvc remote modify minio endpointurl http://127.0.0.1:9000

```

- Auth (method 1 - setup env vars)

> - AWS_ACCESS_KEY_ID=
> - AWS_SECRET_ACCESS_KEY=

- Auth (method 2 - modify remove)

```sh
dvc remote modify minio access_key_id <access_key>
dvc remote modify minio secret_access_key <secret_access>
```sh

- Push datasets

```sh
dvc push
```

### Model 

#### Dataset

The dataset is collected from [Kaggle Speed Dating Experiment](https://www.kaggle.com/annavictoria/speed-dating-experiment)

#### How to run 
```
make train
make predict
```
#### Files in this src

* [preprocessors.py](./src/preprocessors.py): Classes for preprocessing
* [pipeline.py](./src/pipeline.py): Pipeline of estimator and transformers for both numerical and categorical values 
* [train_pipeline.py](./src/train_pipeline.py): for training 
* [predict.py](./src/predict.py): for preprediction
* [preprocessing.py](./src/config/preprocessing.py): to save information about the dataset, variables, and pipeline's name


#### Model

Decision Tree Classifier

#### Result

Achieve perfect accuracy score


## References

- https://stackoverflow.com/questions/67635688/installation-dvc-on-minio-storage

