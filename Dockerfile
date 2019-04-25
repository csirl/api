FROM python:3.6.5-slim

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY api api
WORKDIR /api

#ENTRYPOINT ["gunicorn", "-w", "4", "-t", "1480", "-b", "0.0.0.0:5000", "api:create_app()"]

CMD ["python3", "app.py"]