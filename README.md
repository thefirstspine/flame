# DATA COMPUTING & ANALYSIS

## Prerequisites:

You need a fully setuped server. See https://github.com/thefirstspine/deploy for more information.

## Using with docker

Build a Docker image:

```bash
docker build -t test/fire:latest .
```

Run the image:

```bash
docker run -v '{source-data-storage}:/storage/{identifier}' test/fire:latest
```

Example with Arena:

```bash
docker run -v '/block-storage/arena/data:/storage/arena' test/fire:latest
```

