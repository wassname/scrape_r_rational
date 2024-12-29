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

use <nbs/mjc_005_allm.ipynb> to run an llm from openrouter (costs around $50) and the results are... OK

## More info:

Reddit Discussion: https://old.reddit.com/r/rational/comments/1hoonrc/v2_table_which_stories_have_been_linked_most/

Table Columns

- 'Title': LLM's opinion about the title
- **'⬆️': Sum of comment score for associated links**
- 'Comments': number of comments with the link in that we found and assocated with this row
- '⭐Qual': LLM's opinion about the users opinion of quality of the fiction out of 10
- '⭐Rat': LLM's opinion about the users opinion of the rating of the fiction
- '⭐Writ': LLM on writing style
- '⭐Plot': LLM on plot
- '⭐Char': LLM on characters
- '⭐World': LLM  on wordbuilding
- **'Tags': LLM's opinion about the tags**
- 'First Link': Date of the first link
- 'Last Link': Date of the last link
- 'Links': Number of associated links
- 'URLs': List of associated links
- 'Reviews Summary': An LLM was asked to summarize user reviews
- **'Threads': Links to all the threads!!**
- **'Comments': Links to all the comments!!**
- 'Similar': LLM's opinion about similar fictions
- 'Description': LLM's description
- 'Recommendations': LLM on why a r/rational user would reccomend
- 'Disrecommendations': LLM
- 'Why': LLM
- 'Reviews': An LLM was asked to quote user reivews... it made some of them up


You can see the actuall prompt in <nbs/mjc_005_allm.ipynb>, search for `class FictionInfo`
