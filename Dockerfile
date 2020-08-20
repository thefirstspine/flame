FROM python:3.6

# Install postgresql server
RUN apt update &&\
    apt install -y sudo postgresql-11

# Set the workdir, copy all files
RUN mkdir /app
WORKDIR /app
COPY ./app /app

# Install dependencies
RUN pip install -r requirements.txt

# Entrypoint
ADD entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
