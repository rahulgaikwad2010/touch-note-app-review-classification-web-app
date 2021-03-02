# Touch Note App Review Analysis

![Touch Note App Review Analysos](https://github.com/rahulgaikwad2010/touch-note-app-review-analysis/blob/main/static/img/touchnote_app.png?raw=true)

An AI solution which cognitively able to detect(classify) reviews in fractions of seconds. hence, fewer human interventions, more precise, uniform results, and most importantly operational efficiency.

## Getting Started

Follow these instructions to get the project up and running on your local machine for development and testing purposes.

### Installing

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

### Usage

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
 
## Version

1.0.0 

## Author

* **Rahul Gaikwad** - *Initial work and development*

## References

* [Sentiment-analysis-on-Google-Play-store-apps-reviews](https://github.com/Hrd2D/Sentiment-analysis-on-Google-Play-store-apps-reviews/blob/master/main.ipynb)
* [Dockerize Flask App](https://www.geeksforgeeks.org/dockerize-your-flask-app/)
