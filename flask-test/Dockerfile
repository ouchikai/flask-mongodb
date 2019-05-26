FROM python:3.6

WORKDIR /usr/local/app

COPY style.css ./static/

COPY ["layout.html", "result.html", "toppage.html", "./templates/"]

COPY testapp.py .

RUN  pip install flask \
    flask_pymongo \
    python-dateutil

EXPOSE 5000    

CMD [ "python", "testapp.py" ]