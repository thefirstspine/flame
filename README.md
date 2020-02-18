# DATA COMPUTING & ANALYSIS

```
 (        (                      *             
 )\ )     )\ )       (         (  `            
(()/(    (()/(       )\        )\))(      (    
 /(_))    /(_))   ((((_)(     ((_)()\     )\   
(_))_|   (_))      )\ _ )\    (_()((_)   ((_)  
| |_     | |       (_)_\(_)   |  \/  |   | __| 
| __|    | |__      / _ \     | |\/| |   | _|  
|_|      |____|    /_/ \_\    |_|  |_|   |___| 
                                               
```

## About Flame

Flame is a collection of data computing & analysis commands on the TFS collected data. These CLIs are served by Google Fire.

## Why developing custom data computing & analysis commands?

We are trying to stick to the GDPR advices and all the data analysis scripts are open source and centralized to increase control on our data treatment process.

## Using with Docker

Build a Docker image:

```bash
docker build -t thefirstspine/flame:latest .
```

Run the image:

```bash
docker run -v '{source-data-storage}:/storage/{identifier}' -d thefirstspine/flame:latest --name flame_container
docker exec -t flame_container python compute-games.py count_game_types
```

Example with Arena:

```bash
docker run -v '/block-storage/arena/data:/storage/arena' thefirstspine/flame:latest
docker exec -t flame_container python compute-games.py count_game_types
```

## Using with python installed on the server

Install dependencies

```bash
pip install -r requirements.txt
```

Run commands

```bash
python compute-games.py count_game_types --path={source-data-storage}
```

Example with Arena:

```bash
python compute-games.py count_game_types --path=/block-storage/arena/data
```

## The commands

- [compute-games.md](compute-games.md)
- [compute-players.md](compute-players.md)
- [compute-sessions.md](compute-sessions.md)
- [influxdb.md](influxdb.md)
