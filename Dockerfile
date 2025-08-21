FROM python:3.11-slim

WORKDIR /app


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN python -m nltk.downloader -d /usr/local/share/nltk_data vader_lexicon
ENV NLTK_DATA=/usr/local/share/nltk_data

COPY ./app/ .
COPY ./data/ .

EXPOSE 8080

CMD ["python","main.py"]