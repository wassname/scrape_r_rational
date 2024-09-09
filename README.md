# rrational

scrapping reddit.com/r/rational and analytics

see https://raw.githubusercontent.com/NightMachinery/.shells/master/scripts/python/reddit/subreddit2org.py

Project status: WIP

Project plan:

- [x] Init
- [ ] Fill out README
- [x] Scrape r/rational
- [x] use [statistics](https://github.com/wassname/scrape_r_rational/blob/main/nbs/links.csv)
- [ ] Use llm to get reccomendations, sentiment, karma etc
- [x] share


## Install requirements

This project uses [poetry](https://python-poetry.org/) for requirement and is set up for torch using cuda.
~~~
poetry install
~~~

## How to get data

TODO document how to get the data


## How to run

This project uses [just](https://github.com/casey/just)

~~~
just --list
~~~


## Project Organization

Note this project uses

- [Justfile](https://github.com/casey/just): Command runner with commands like `just data` or `just train`
- data: [data directory ](https://cookiecutter-data-science.drivendata.org/#directory-structure)
    - ./10_raw            <- The original, immutable data dump.
    - ./20_interim        <- Intermediate data that has been transformed.
    - ./30_processed      <- The final, canonical data sets for modeling.
- nbs: jupyter notebooks. Name with creator's initials, a number (for ordering), and short `-` delimited description, e.g.  `jqp-1.0-initial-data-exploration`.
- pyproject.toml:   defines poetry project dependencies and build configuration
- rrational:    Source code for use in this project.

