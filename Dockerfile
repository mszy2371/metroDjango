FROM python:3.10-slim
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app
WORKDIR /app
EXPOSE 8000
ENTRYPOINT ["python", "metroproject/manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
