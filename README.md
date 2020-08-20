# Data computing with Flame

## About Flame

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

Flame is a containerized  collection of data computing & analysis commands on the TFS collected data. These CLIs are served by Google Python Fire.

More on Google Python Fire: https://github.com/google/python-fire

## Synopsis

```
+----------------------+                  +----------------------+
| FRONTAL SERVICE      |                  | VOLUME               |
|                      |  1/ Writes       |                      |
| Net service that     |----------------->| External volume      |
| provide APIs (Arena, |                  | mounted on the       |
| website, etc.)       |                  | service.             |
+----------------------+                  +----------------------+
                                                      |
                                                      | 2/ Copy
                                                      |
                                                      v
+----------------------+                  +----------------------+                  +----------------------+
| STATS ARCHIVES       |                  | VOLUME               |                  | FLAME CONTAINER      |
|                      |  4/ Fetch        |                      |  3/ Computes     |                      |
| Archive the          |----------------->| Copy of the volume,  |<---------------->| Performs analysis on |
| computed data for    |                  | not written nor read |                  | the copied volume    |
| further use.         |                  | by the ser^ice.      |                  | and write results.   |
+----------------------+                  +----------------------+                  +----------------------+
```

## Usage

Flame is thinked to run along with docker: run an image on a mounted volume.

### Prepare the environment

The machine that will run the flame container should have docker installed. Run this to install it:

`apt-get update && apt-get -y install docker-ce docker-ce-cli containerd.io`

### Run the docker image

`docker run --name <some-flame> -e FLAME_<SOME_CONFIG>=<some-value> -v </local-volume-mount-point>:/flame-volume thefirstspine/flame:<tag> <the-command>`

For the `latest` version of flame, use the latest tag. The desired volume to compute should be mounted to the `/flame-volume` path.

Example : `docker run --name my-flame-container -v /block-storage/arena:/flame-volume thefirstspine/flame:latest python compute-games.py count_game_type`

### Getting output

The command will simply print on the standard output the result of the command.

### Docker environment variables configuration

Based on the environment variables passed to the container, some features will be activated or not. Here’s a list of all available features:

| Variable key | Explaination | Example |
| --- | --- | --- |
| `FLAME_POSTGRESQL_DUMP_FILE` | If set, Flame will import this dump file during the startup. It should be in the mounted volume. The path must be relative to the root of the mounted volume. | `FLAME_POSTGRESQL_DUMP_FILE=/data/mydump.sql` |

### Notes

- Auto remove the running container using the `--rm` flag.
- Output to a file: `docker run --rm -a STDOUT … > myoutput.json`

## Available commands

The computing commands are available inside collections served by Google Python Fire.

To run a command: `<collection> <command> <options>`

For instance: `compute-games.py get_game --game_id=123`

### Collection games.py

All the computations related with the games.

Required volume: `volume-thefirstspine-arena-<country>`

| Command | Description | Options |
| --- | --- | --- |
| `get_game <game_id>` | Get a game instance data | <ul><li>`String outputs_to`<br>Indicates the output format of the command. Must be python (default) or json.</li></ul> |
| `count_game_types` | Get the number of played games by types | <ul><li>`String outputs_to`<br>Indicates the output format of the command. Must be python (default) or json.</li></ul> |
| `count_games_per_hour` | Get the games played per hour | <ul><li>`String outputs_to`<br>Indicates the output format of the command. Must be python (default) or json.</li></ul> |
| `count_games_per_weekday` | Get the games played per weekday | <ul><li>`String outputs_to`<br>Indicates the output format of the command. Must be python (default) or json.</li></ul> |
| `count_destroyed_cards_per_type` | Get the destroyed cards per type | <ul><li>`String outputs_to`<br>Indicates the output format of the command. Must be python (default) or json.</li></ul> |

### Collection players.py

The commands under this collection are related with the player data (e.g. wizards files)

Required volume: `volume-thefirstspine-arena-<country>`

| Command | Description | Options |
| --- | --- | --- |
| `get_player <game_id>` | Get a player data | <ul><li>`String outputs_to`<br>Indicates the output format of the command. Must be python (default) or json.</li></ul> |
| `ranks` | Ranks the players according to their victories | <ul><li>`String outputs_to`<br>Indicates the output format of the command. Must be python (default) or json.</li></ul> |
| `get_points <player_id>` | Get the points of a player | <ul><li>`String outputs_to`<br>Indicates the output format of the command. Must be python (default) or json.</li></ul> |

### Collection sessions.py

All the Solid Pancake sessions. It requires a dump file to be imported with the `FLAME_POSTGRESQL_DUMP_FILE` environment variable.

Required volume: `volume-thefirstspine-solid-pancake-<country>`

| Command | Description | Options |
| --- | --- | --- |
| `get_sessions <offset> <limit>` | Get the sessions in the Solid Pancake service tracking | <ul><li>`String outputs_to`<br>Indicates the output format of the command. Must be python (default) or json.</li></ul> |
| `get_events <offset> <limit>` | Get the last events in the Solid Pancake service tracking | <ul><li>`String outputs_to`<br>Indicates the output format of the command. Must be python (default) or json.</li></ul> |
| `count_active_sessions_per_product_and_version` | Get the sessions in the Solid Pancake service tracking | <ul><li>`String outputs_to`<br>Indicates the output format of the command. Must be python (default) or json.</li></ul> |
| `get_sessions_with_events` | Get the sessions with events in the Solid Pancake service tracking | <ul><li>`String outputs_to`<br>Indicates the output format of the command. Must be python (default) or json.</li></ul> |
| `count_sessions_per_product` | Count the sessions per product | <ul><li>`String outputs_to`<br>Indicates the output format of the command. Must be python (default) or json.</li></ul> |
