FROM python:3

COPY requirements.txt /temp/requirements.txt
COPY hackathon /hackathon
WORKDIR /hackathon
EXPOSE 8000

RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password hackathon-user

USER hackathon-user

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]