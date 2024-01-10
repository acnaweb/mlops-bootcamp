# MLOps Bootcamp

MLOps with MLFlow, Scikit-learn, CI/CD, Azure, FastAPI, Gradio, SHAP, Docker, DVC, Flask, BentoML

### Project Template (Cookiecutter Data Science)

```
cookiecutter https://github.com/khuyentran1401/data-science-template
```


### Configuration File (Hydra)

- https://hydra.cc/

### API Documentation for Python Projects

- https://pdoc.dev/

### Data Versioning (dvc)

- https://dvc.org/


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

- https://docs.kanaries.net/pt/topics/Python/jupyterlab-vs-notebook
- https://github.com/cookiecutter/cookiecutter
