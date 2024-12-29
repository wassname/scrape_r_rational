# rrational



scrapping reddit.com/r/rational and analytics

- This project has data from r/rational in **markdown** that you can browse, see [./data/cache2/](./data/cache2/) for the data.

- This project also has an html **table** you can see/download at https://wassname.github.io/scrape_r_rational/

![screenshot](docs/image.png)


## Project plan:

- [x] Init
- [x] Fill out README
- [x] Scrape r/rational
- [x] use [statistics](https://github.com/wassname/scrape_r_rational/blob/main/nbs/links.csv)
- [x] Use llm to get reccomendations, sentiment, karma etc
- [x] share
- [x] comment md to html
- [x] comment expand
- [x] threads where it's mentioned
- [x] better tittles and data cleaning
- [x] github pages


## Install requirements

This project uses [poetry](https://python-poetry.org/) for requirement and is set up for torch using cuda.
~~~
poetry install
~~~

Then 
~~~
cp .env.example .env
~~~
Then fill out the api keys


## How to run

First run <nbs/mjc_001_download.ipynb> to update the data in <data/cache2/>

Then run <nbs/mjc_004_process.ipynb> to analyse the data and output <index.html>

use nb 05 to run an llm from openrouter (costs around $50) and the results are... OK


