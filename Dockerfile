FROM python:3.7 

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt 

EXPOSE 5000

RUN python -m nltk.downloader popular

ENTRYPOINT [ "python" ] 

CMD [ "run.py" ] 