# python:alpine is 3.{latest}
FROM arm32v7/python:3.6.7-slim 

RUN pip install flask

COPY flaskr /flaskr/
COPY file.csv /

EXPOSE 5000


ENTRYPOINT ["python", "/flaskr/kakebo.py"]
