FROM python:3.8-buster

RUN pip install pipenv
COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy --ignore-pipfile

ENV PYTHONUNBUFFERED=1

WORKDIR /apidir

RUN useradd --system apiuser && \
    mkdir api && \
    chown -R apiuser api

USER apiuser

COPY api api

CMD ["python3", "api/app.py"]