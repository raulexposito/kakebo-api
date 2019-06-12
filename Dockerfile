FROM python:3.7.2-slim

COPY flaskr /flaskr/
COPY requirements.txt /

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5005

WORKDIR "/flaskr/"

ENTRYPOINT ["gunicorn", "-w", "4", "-b", ":5005", "kakebo:app"]
