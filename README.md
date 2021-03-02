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
│    ├── common_operations  - here's the default config file.
│    │    ├── __init__.py  - here's the default config file.
│    │    └── common_operations.py  - here's the default config file.
│    │
│    ├── data  - here's the default config file.
│    │    ├── Contraction.json  - here's the default config file.
│    │    └── TouchnoteReveiws.csv  - here's the default config file.
│    │
│    └── logger  - here's the default config file.
│    │    ├── __init__.py  - here's the default config file.
│    │    ├── APILogger.py  - here's the default config file.
│    │    ├── logger.py  - here's the default config file.
│    │    └── LoggerError.py  - here's the default config file.
│    │
│    └── ModelPredictor  - here's the default config file.
│    │    ├── __init__.py  - here's the default config file.
│    │    └── ModelPredictor.py  - here's the default config file.
│    │
│    └── models  - here's the default config file.
│    │    ├── model_mapping.json  - here's the default config file.
│    │    ├── log_reg.sav  - here's the default config file.
│    │    ├── naive_bayes.sav  - here's the default config file.
│    │    └── svm.sav  - here's the default config file.
│    │
│    └── TextPreprocessor  - here's the default config file.
│    │    ├── __init__.py  - here's the default config file.
│    │    └── TextPreprocessor.py  - here's the default config file.
│    │
│    └── TextClassifier.py  - here's the default config file.
│
│
├──  Touch Note App Review Analysis  
|    |
│    └── models  - here's the default config file.
│    │    ├── model_mapping.json  - here's the default config file.
│    │    ├── log_reg.sav  - here's the default config file.
│    │    ├── naive_bayes.sav  - here's the default config file.
│    │    └── svm.sav  - here's the default config file.
│    │
│    └── data  - here's the default config file.
│    │    ├── __init__.py  - here's the default config file.
│    │    └── TextPreprocessor.py  - here's the default config file.
|    |
│    └── Touch Note App Review Analysis.html  - here's the default config file.
│    └── Touch Note App Review Analysis.ipynb  - here's the default config file.
|
│
├──  data  
│    └── datasets  - here's the datasets folder that is responsible for all data handling.
│    └── transforms  - here's the data preprocess folder that is responsible for all data augmentation.
│    └── build.py  		   - here's the file to make dataloader.
│    └── collate_batch.py   - here's the file that is responsible for merges a list of samples to form a mini-batch.
│
│
├──  engine
│   ├── trainer.py     - this file contains the train loops.
│   └── inference.py   - this file contains the inference process.
│
│
├── layers              - this folder contains any customed layers of your project.
│   └── conv_layer.py
│
│
├── modeling            - this folder contains any model of your project.
│   └── example_model.py
│
│
├── solver             - this folder contains optimizer of your project.
│   └── build.py
│   └── lr_scheduler.py
│   
│ 
├──  tools                - here's the train/test model of your project.
│    └── train_net.py  - here's an example of train model that is responsible for the whole pipeline.
│ 
│ 
└── utils
│    ├── logger.py
│    └── any_other_utils_you_need
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
