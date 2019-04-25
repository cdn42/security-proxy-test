FROM python:3
COPY app/ /app/
ADD requirements.txt /app/
RUN mkdir /app/files
RUN pip install -r /app/requirements.txt
EXPOSE 9000

CMD [ "python", "/app/flask_app.py" ]