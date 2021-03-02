# Touch Note App Review Analysis

![Touch Note App Review Analysos](https://github.com/rahulgaikwad2010/touch-note-app-review-analysis/blob/main/static/img/touchnote_app.png?raw=true)

An AI solution which cognitively able to detect(classify) reviews in fractions of seconds. hence, fewer human interventions, more precise, uniform results, and most importantly operational efficiency.

# Table Of Contents
-  [Project Structure Overview](#project-structure-overview)
-  [Model Training Part](#model-training-part)
-  [Run python app](#run-python-app)
-  [Dockerizing an application](#dockerizing-an-application)
-  [Version](#version)
-  [Author](#author)
-  [References](#references)



### Project Structure Overview
```
├──  TextClassifier
│    │
│    ├── common_operations          - this package contains common operation tasks.
│    │    ├── __init__.py
│    │    └── common_operations.py  - this file reads config and convert to dictionary.
│    │
│    ├── data                       - here's the default config file.
│    │    ├── Contraction.json      - here's the default config file.
│    │    └── TouchnoteReveiws.csv  - here's the default config file.
│    │
│    └── logger                     - here's the default config file.
│    │    ├── __init__.py           - here's the default config file.
│    │    ├── APILogger.py          - here's the default config file.
│    │    ├── logger.py             - here's the default config file.
│    │    └── LoggerError.py        - here's the default config file.
│    │
│    └── ModelPredictor             - here's the default config file.
│    │    ├── __init__.py           - here's the default config file.
│    │    └── ModelPredictor.py     - here's the default config file.
│    │
│    └── models                     - here's the default config file.
│    │    ├── model_mapping.json    - here's the default config file.
│    │    ├── log_reg.sav           - here's the default config file.
│    │    ├── naive_bayes.sav       - here's the default config file.
│    │    └── svm.sav               - here's the default config file.
│    │
│    └── TextPreprocessor           - here's the default config file.
│    │    ├── __init__.py           - here's the default config file.
│    │    └── TextPreprocessor.py   - here's the default config file.
│    │
│    └── TextClassifier.py          - here's the default config file.
│
│
├──  Touch Note App Review Analysis                        - this folder contains model training related data, models & notebook.
|    |
│    └── models                                            - this folder holds exported models.
│    │    ├── log_reg.sav                                  - Logistic Regression Model.
│    │    ├── naive_bayes.sav                              - Naive Bayes Model
│    │    └── svm.sav                                      - SVM Model.
│    │
│    └── data                                              - this folder contains data used for model training.
│    │    ├── Contraction.json                             - here's the file for text preprocessing.
│    │    └── google_play_store_apps_reviews_training.csv  - Training Dataset.
|    |
│    ├── Touch Note App Review Analysis.ipynb              - Data Analysis & Model Training Notebook.
│    └── Touch Note App Review Analysis.html               - Exported version in HTML.
|
│
├──  static                  - this folder contains bootstrap 4 files.
│    └── asset
│    └── img
│    └── js
│    └── style
│    └── index.js            - here's the file for frond-end form submission to flask app and vice versa.
│
│
├── templates                - this folder contains front-end html files.
│   └── index.html
│
│
├── Dockerfile               - here's the docker file used to create docker image.
├── README.md                - here's the ReadMe of an application.
├── config.ini               - here's the specific config file for the application.
├── requirements.txt         - here's the python package requirement txt.
└── run.py                   - here's runnable of an application.
```

### Model Training Part


### Run python app

A step by step series of examples that tell you how to get a development env running

```
pip install -r requirements.txt
```

If successfully installed, Change values in config file.
```
[Path]
ModelMappingFilePath = .\models\model_mapping.json
etc..
```

Now, you can run project as follows
```
python run.py
```

You can run a test as follows
```
C:\Users\Alice> python run.py
 * Serving Flask app "run" (lazy loading)
 * Environment: production
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```

### Dockerizing an application

##### Docker file
```
FROM python:3.7 
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt 
EXPOSE 5000
RUN python -m nltk.downloader popular
ENTRYPOINT [ "python" ] 
CMD [ "run.py" ] 
```

##### Build the Docker image

Make sure you are in root directory of the project and run the following command.

```
docker build --tag touchnote-review-analysis-app .
```

The above command will create an app with the tag touchnote-review-analysis-app

##### Run the docker image we just created

```
docker run --name touchnote-review-analysis-app -p 5000:5000 touchnote-review-analysis-app
```
 
##### Create a new image from a container’s changes

```
docker commit container-id user-name/touchnote-review-analysis-app:latest
```

##### Before pushing to docker hub repo login into docker hub using docker account

```
docker login
```

##### Push an image to a registry

```
docker push user-name/touchnote-review-analysis-app:latest
```

Progress bars are shown during docker push, which show the uncompressed size. The actual amount of data that’s pushed will be compressed before sending, so the uploaded size will not be reflected by the progress bar.

## Version

1.0.0 

## Author

* **Rahul Gaikwad** - Initial work and development

## References

* [Sentiment-analysis-on-Google-Play-store-apps-reviews](https://github.com/Hrd2D/Sentiment-analysis-on-Google-Play-store-apps-reviews/blob/master/main.ipynb)
* [Dockerize Flask App](https://www.geeksforgeeks.org/dockerize-your-flask-app/)
