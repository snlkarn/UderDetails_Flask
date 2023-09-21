FROM python:3.9

WORKDIR /myApp
COPY requirements.txt /myApp/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /myApp/
EXPOSE 8080
CMD ["python", "simple_app.py"]