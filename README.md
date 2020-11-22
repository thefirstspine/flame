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

<iframe src="https://viewer.diagrams.net/?highlight=0000ff&edit=_blank&layers=1&nav=1#R7Vxpd9pYEv01OWfmQ%2FpoxfAREMbyaDFmlb70kYQstCE1CLT8%2BrlPCwhDnHRP3J1M7BMHqd5%2B6756VYXkT%2BwwzMY7I97I0doOPjHUOvvECp8Yhu7csfggkryS9FiuEjg7d11XOgumbmHXQqqWHty1vb%2BomERRkLjxpdCKtlvbSi5kxm4XpZfVXqLgctTYcOwrwdQygmvp0l0nm0raZe7O8gfbdTbNyHSnV5WERlO5Xsl%2BY6yjtCViR5%2FY4S6KkuoqzIZ2QMBrcKna3X%2Bh9DSxnb1NvqUBG7mLx5eH5TRnxsbCNKeJJH2uJ3s0gkO94E9MJ0B%2Fg5cI3RJcg2hXlnT%2BOJCpDj4xLMfc3ZlmW9RxyGe6cxMoi6io6QbzqXqqatRQJHmDr70G3PVttEs2kRNtjWB0lg520WG7tskiKNyd60hRFENIQ%2BjZSZLX3DEOGJwdbJIwqEvtzE1WpPlvfH2n1Z2RayFr3%2BTNzTbZ5a1G5FZr%2BiM352blXdNun%2Bwi3x6eQGugakoaDjE1wk3NbbS1T%2FC0dVqreR8ddpb9hiLpep8lxs6xkzcqdqt6BPfWCDVlxnYU2lgPKuzswEjc4%2BU2MOrd5JzqnZo%2BRW5JmGbnszXt633PdanLLqoV1a3OtMVFaxpnUUnmP0Fs%2Bu67Mnt9iAPXMkp2%2F3DEptu0PpH8a8Ru07rF8h%2BN2N1v5DXd%2Bd7EvqDkn%2BVf94p%2BgpEYZMH27mjvruhi7OPq%2BHpxM8KJQWzvXEzFJiBiPJx39tNZ1KaBEbjOFtcWsC3LTicNUdza2G9OJGtrptbhYAB5YJh2MDAs3ylJ2aryUv7UTWsm0kTJ%2B9iw3K0zK7nKQuCG5VHafApu6AC5wMVuunfNEP%2BvSwTKj98JDK5l73%2FbH51mAk%2FR3k3c6GItwCrBxgukVxUSMu6ptF9DYEZJEoVv8Y20sLM3CdKUUpcWjG0sWHr2Azq1aNNyATrUO1GqMfEtTk0rFH9JNhlxZZLBBxjl%2B91hm2A9r4n1DkTgGf6fJULjQn%2Bnsy0%2BQKcf59rf7bB99%2FPqtiPWYajfqPNPl7t0y%2BhXJK3O2fdzyzpfOxc7Rkgs%2B9bck4%2BdXW7yX9LA%2FVzHJdv50Y7LaxfsikZQfVyBXynjS%2FCdgPoGzb8GuYL%2BirDlkP1GSrWYUOqd7Ve3zD3RODPIwF9m%2BPSgMHo%2B4MxldrAKyjUenilLiI4Su2bXOc%2FKOX%2B0Qusoe%2F1UHvaKdWi54sMmMcd8oYaK9zR9jNYPz6nqdo8a%2Bxhoq%2Bd4HS48k6ETk%2BELKezlet47WLncavd80c56WOTmsBpHH8tHfZkF5nJxWD%2FIR3nKZVIuOvaY3ptbuWMs%2BZ3FKBtrPO%2BJ4YZaP%2FQ7Ut7DbK1Dq%2Bxgso9bieE36KewxveevpKPrfLzXLaPvu69se6Zz6vTbiq7XayAzvWxllhscFiP7zlpyRdia24W0%2FON1QBr8NtzK0zmObbGKJvyhckuco1ZhGR%2B%2BpQ%2F6KvJ8fn%2BeSSxCtoFKakrzfoH%2FeHZF91GLzHB%2FWq960Ku1lmIqSz0jxarb9Em0pfB1niY9ERPpJXtgIMs1gXKndP6wzzsHddD0YGOcosJjibWTjBGHcZYLthJ2OOepmIqCn1H9uaMKKAPF%2FWZwF%2BPnXOfHtfVx4vQyqu%2By%2BtiTsnF3JUKlNVyc3zP6ysxK%2Bs3dYsRrcxGZF6UFd4fLEYH1lRP3D7nGjBFG0qfOrnk%2BZkqjFilGO2lmXxQCotXPD%2F%2Fz1QEf58eBhvMyClHmfYz2ZscVMHP0PNeETTUHhVy0aewkr08s1LJw71nsWQ1xhLobMv2qC%2Fm6lR0LPaZN0tW6bE5Tjti4XAa8xzqXhIay2wvLXuptlTi9YPfkWe1bPVIo01HX%2BmBGfZ8XUiK9cPj0WDm7faNLKlR7GA33WG83GSSQFpmsYkdo636HSvs0WY4eV32h8kEBzWk4%2FV4kausAtR6O31KJ8bqObBC1FkGlOq12z1vLGazsbaPG3sWH7ATg1a7I9kRaMur3qjUFu4pYzjwsSsVaBxs5zJFmHCKm3JKzmVgVw58HUWYH%2FDLKYWTSdBMWc%2FTGHl6C1OKhoax9mCvz6D1MNibQuSpwsbTx3qoMiXOiYmzVGMCyp5FWSOztgu0iQOwFHN%2F9k9zn7Xan9fDGstnyhCiXD7jj90dHPQldrsQ59h1B%2F2qLIZF4DoEOzC0hV2FM%2BoA30lHabXTx%2FeFMb7PwVpeDfmjGc5b7Vr8mIrHJy9LYQ0jcQxcfKrGzmfUWZ%2BXBIeRPJlWBZlVp8BWEA%2FyzMnVmU%2B4mkneJFcEi2l2bqkfYUTLnshLs3kiDz%2F4euarz2NvM9jrnCRowM5KYQd4pbYJitfnlWKyB%2B4H%2FKKeA6sGLIdcqsw0Cm1gaUaUKvRpOb%2Ficcnt11gDu4M%2B%2B6VwTiqcRdgCh5ZgI5Qpl8uFVSjDfo5rCjaXgb1IZM8Hl31WLnxygoDzE0bx5nvZc2CT55xcTFxxHJA%2By%2F0hz%2Ba54o0SYpc%2FcCY4j2ATOAbczZRhyuCalolMGDnSbASuzlEmQwcybIhWKIS7034BOw25w6rDlIUctkXkr%2B0H9seMeD8KZcPLwngljo0tK2308GJ%2BjSxfo74aLhh9ycNTOa9VdWVOHSu%2BHmrn9a%2FWMTyYSPXEtLXuPTywQGPuU3hdx%2FWS91%2BXGWEvNr24wrWlt8pGP6IOdCBEVKudr62USFs95trKb%2Fhybtc6W0S3e%2B01wPLCrwCrwV5Y3kkBS8AqYLg4pAoVFkIWfJyGBNFJoQoWDe0Qa8HJHj5LDUzICZjfRnr0gXSJ9GzaZ0sb4fnY%2FxaQdijJc2jYCF4UHE7y%2BvDNRhy4C004B1yD73NHgc1WBHBbGDHwNyjYbHiOPn3Dh4Odprhrf6Pee7%2Bcr2Ed5EIs4FfA1xhliouzDrZaHfY56AF%2BMey3MIIecGbChqg4A0XBKspzcObnsOPEt4PPRyKL0U17Tc7KX9VeS4xFGD7sbZ%2B8tIy7nhwStJN%2F3yX10ft66oO9kfpg3yv10WQ63kp9kARG%2FO2LPz1hYZhND9SboDC911nzfzofdOtZh9fJ7SpzSB5l2LiJPY2NMoeb7oz4Mol4IxV8mUmuhS9uELSSRKN%2BZ9Dp3GTd24r8Ohf%2FKVgbtX6k2ZoU1YYc2bt2ygytWGlr1em1bgajzUtsVe8yBTTP5CoFdD4Yl%2FxGCzMYvUcchsm2NqIw3gu2TPsMEQjNRBy%2Bo1zNvy1VROqKAsa6SBWdxsa6045VHr5zcmjn%2BkoJrK0eoKw8GLA21hjjcKxSO2OrOt5D5WiuBi%2B2sBivCp%2BFmT5ixgGwqWqVbsZjoLETxxgvYp3ZUJgRJeccECEJx8o5IjK4x3CjNcjKJFYOt5oHarj3cT8i5TjuquSVheNlPWyjOIHTpxF3uj7%2BKZccsXBPSIhOUMhJ2EO0gHse90QjCINGdOMM%2FZVZjsALjoPT9KdmSQLWsw4mcF3nqULSlJg1AgS4rGLTHw8U4AjIX%2BoPDoGG4O5Gf27THxwMj6RIcQ9uqbMJULD%2B0qrnzaoz3CN8dP73VTeznBHXxmGaWZKkLlxOzOXKdaKUQiMha4YQNyPoqLOFB0c%2BJekaaaaR1eXSTKZIKCxBx3BXWYRUJCxDCEYxxJVVQjmB%2B1QoBdykGVwxb8JXoRt2d04VxLVC3bwM7QonKVNDhZObQyor0xKeiHCYY4gLLA77DuQk1IPrltblj2ROWJOYE1nJZbRFGw7j7eEOk1QoI%2BEToTcnCRbmq6Uy5qWQsWfiHnrA%2FCzMD2H5bIJw0iJr46q1WST1R8JITp07OdGHMrPKuWjlGkUaQVGBvmApRntlSNKA%2Fl5FMKWWfclZyRy48zIwwz7JtEIka2DkPC1gRegyTetpJPgqJKHUF8JeUt%2FB3IFxI1vKkMnYSyIllalcrIuEDlOKJulHWZjsEQ4T3HPIsir1q1VzLUY09MbJ0xT6E0l4QSGoQ2iMNgTHQsYcgD1CD6wb%2BplwMkPm3mcJnsCBV%2FKU4AGuUDwpRx8Ya4QdBV0BS3V2L5NUHcoojJPLZN8LPm27FbdMJuN1pncQHwbkCwiKWH%2BZpAAxJjCu7IQwKRBYptAjWev%2BzM8%2BwhrwYNiuR1JcGnSKvTQl%2B2TitPrL4dZj%2FTJF1v%2FGLiTsKsPTb96FF7ai7QBn2zo8kLVVEFhBtwkAq3MMV%2B%2FinjSll18%2F09c%2BIXfDeeHezXm59STF3%2Bwoc%2BwP5ig3j7f8VI4y9wV1%2FECO8vWjDx%2BO8oej%2FOEofzjKH47yh6P84Sj%2FPzvK3%2B6e%2FKCO8t21C%2Fjx5tb3eRC4zkv%2FbG%2B4NGHLByW%2BOyWaCOyno0QTFF%2B%2FmLCPje0FWZq3EOpXFfpkko75LwR9JP7F%2BBRNdkZz3b37N7khqFIE688vRugGedXw9NQ4dMRyhDB2cLST8sHxVyWXnexLmpEuaCbOXpVVUyWF22gXGsFlcVqbXVLOkTdE6sIA9LV3n%2BvnvW%2B2xxGQfHaxD7Z1e6o1dlmY7Izt%2FgWtmvYgVFMhjXbry%2B7bzc1TLPj5FbIMz5%2FgfHV9hnbt7uPAqGF1t4HbGvgliIykPaHXL5LcB0ZoVwmQxEDLXeudkkr%2FX3inhKz5L6USrp7l%2F%2FY8zZe%2FuOy%2Bysfc%2BDa3e%2BPsZd7r7GVvfZv7sat%2BlV31RF7P2v3024pj%2Frlt5dxt%2BiNG%2B91k1dH9Muks%2Fa77%2BfqsmibRrsxx%2FbovG724gf37zo5JqjHa5e%2F6utGN1PkVw75Ip84rOr3j60bk5dLTX%2BmoXoQ7%2F60TdvRf"></iframe>

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
| `FLAME_DB_URL` | The database Flame should connect to. | `FLAME_DB_URL=mongodb://localhost:27017/database` `FLAME_DB_URL=postgresql://localhost:5432/database` |

### Notes

- Auto remove the running container using the `--rm` flag.
- Output to a file: `docker run --rm -a STDOUT … > myoutput.json`

## Available commands

The computing commands are available inside collections served by Google Python Fire.

To run a command: `<collection> <command> <options>`

For instance: `games.py get_game --game_id=123`

### Collection games.py

All the computations related with the games.

Required database: `games`

| Command | Description | Options |
| --- | --- | --- |
| `count_game_types` | Get the number of played games by types | <ul><li>`String outputs_to`<br>Indicates the output format of the command. Must be python (default) or json.</li></ul> |

### Collection players.py

The commands under this collection are related with the player data (e.g. wizards files)

Required database: `wizards`

| Command | Description | Options |
| --- | --- | --- |
| `ranks` | Ranks the players according to their victories | <ul><li>`String outputs_to`<br>Indicates the output format of the command. Must be python (default) or json.</li></ul> |

### Collection sessions.py

All the Solid Pancake sessions.

Required database: `solid-pancake>`

| Command | Description | Options |
| --- | --- | --- |
| `count_active_sessions_per_product_and_version` | Get the sessions in the Solid Pancake service tracking | <ul><li>`String outputs_to`<br>Indicates the output format of the command. Must be python (default) or json.</li></ul> |
| `count_sessions_per_product` | Count the sessions per product | <ul><li>`String outputs_to`<br>Indicates the output format of the command. Must be python (default) or json.</li></ul> |
