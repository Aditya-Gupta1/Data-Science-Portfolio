# Scraping Bollywood Actor's Data from IMDB Website
This project aims to demonstrate the scraping of IMDB website to collect information regarding bollywood actors.
## Libraries Required
* BeautifulSoup
* Requests
* Urllib
* Pandas

## About
This project uses the website [https://www.imdb.com/list/ls002913270/](https://www.imdb.com/list/ls002913270/) for scraping information using BeautifulSoup. Data collected can be stored in 2 formats:<br>
1. <u>**Consolidated**</u>:
In this format, the images of all the actors are collected and stored in the `ActorImages` folder. Other information such as actor's name, name of actor's image file and actor's meta data is stored collectively in  `Actors_Data.csv` file.

2. <u>**Distributed**</u>:
In this format, the data is stored in `ActorDataBase` folder. Here, each actor has its own seperate folder containing respective image file and a .txt file of its meta data.

The format has to be specified while calling `make_database` function.