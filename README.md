# DATA COMPUTING & ANALYSIS

## About Flame

Flame is a collection of data computing & analysis commands on the TFS collected data. These CLIs are served by Google Fire.

## Why developing custom data computing & analysis commands?

We are trying to stick to the GDPR advices and all the data analysis scripts are open source and centralized to increase control on our data treatment process.

## Using with docker

Build a Docker image:

```bash
docker build -t test/flame:latest .
```

Run the image:

```bash
docker run -v '{source-data-storage}:/storage/{identifier}' test/flame:latest
```

Example with Arena:

```bash
docker run -v '/block-storage/arena/data:/storage/arena' test/flame:latest
```

