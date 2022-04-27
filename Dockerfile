# FROM python:3
# ENV API_ENV 1
# RUN mkdir /code
# WORKDIR /Users/admin/Desktop/API_ENV/ecommerce
# COPY requirements.txt /code/
# RUN pip install -r requirements.txt
# RUN pip install --upgrade pip
# COPY . /Users/admin/Desktop/API_ENV/ecommerce/



# — — — — — Dockerfile
# We Use an official Python runtime as a parent image
FROM python:3.8
# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# Copy Requirements Text To Docker
COPY requirements.txt .
# create root directory for our project in the container
RUN mkdir /ecommerce_storee
# Set the working directory to /music_service
WORKDIR /ecommerce_storee
# Copy the current directory contents into the container at /music_service
ADD . /ecommerce_storee/
# Install any needed packages specified in requirements.txt
# RUN pip install -r requirements.txt
# RUN pip install --upgrade pip
# copu run folder with a name
COPY manage.py manage.py
EXPOSE 8000

CMD ["python", "./manage.py"]
# For Server
# CMD exec gunicorn ecommerce.wsgi:application — bind 0.0.0.0:8000




# To Build
# docker build -t ecommerce_storee

# To RUN
# docker run -p 8000:8000 ecommerce_storee