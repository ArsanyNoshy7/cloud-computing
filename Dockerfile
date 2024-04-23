FROM python:3.9-slim
WORKDIR /app

COPY cloudass.py  /app/
COPY paragraphs.txt /app/

RUN pip install nltk
ENV NLTK_DATA /usr/local/share/nltk_data

RUN python -c "import nltk; nltk.download('stopwords')"
EXPOSE 80

ENV NAME dockerfile
CMD ["python", "cloudass.py"]