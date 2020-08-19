FROM python:3.6

# Set the workdir, copy all files
WORKDIR /app
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Install postgresql server
RUN apt update &&\
    apt install -y postgresql postgresql-contrib
