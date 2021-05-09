#base image 
FROM python
COPY . /projectcloud
WORKDIR /projectcloud
RUN pip install nltk

RUN pip install stopwords
CMD python pyfile.py