import csv
import requests
from bs4 import BeautifulSoup

# goal: scrape top 50 TV shows on IMDb in Comedy using requests & BeautifulSoup #
# make CSV file with rank, name, length, genre(s), & rating #

with open('C:\\Users\\Rebecca\\github\\imdbScrape\\imdbScrape.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['Rank', 'Name', 'Length', 'Genre(s)', 'Rating'])

    URL = "https://www.imdb.com/search/title/?genres=comedy&sort=user_rating,desc&title_type=tv_series,mini_series&num_votes=5000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=f85d9bf4-1542-48d1-a7f9-48ac82dd85e7&pf_rd_r=XH37R4RB191T4K7RVQYZ&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=toptv&ref_=chttvtp_gnr_5"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    shows = soup.find_all('div', class_="lister-item mode-advanced")

    for show in shows:
        header = show.find('h3', class_='lister-item-header')

        rank = header.find('span', class_='lister-item-index unbold text-primary')
        showName = header.find('a')
        length = show.find('span', class_='runtime')
        genres = show.find('span', class_='genre')
        rating = show.find('div', class_='inline-block ratings-imdb-rating')
        rating = rating.find('strong')

        if None in (rank, showName, length, genres, rating):
            continue

        writer.writerow([rank.text.strip(), showName.text.strip(), length.text.strip(), genres.text.strip(), rating.text.strip()])
