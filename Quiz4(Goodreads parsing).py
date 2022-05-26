import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import randint

file = open('myBooks.csv', 'w')
f_obj = csv.writer(file)
f_obj.writerow(['Title', 'Author', 'Rating', 'IMG_URL'])

page = 1

while page < 15:
    url = 'https://www.goodreads.com/review/list/57424153-ana?ref=nav_mybooks&shelf=read&page=' + str(page)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    sub_soup = soup.find('tbody', id='booksBody')
    all_books = sub_soup.find_all('tr', class_='bookalike review')

    for each in all_books:
        img_url = each.img.attrs.get('src')
        title = each.find('td', class_='field title').a.text.strip()
        book_title = title.replace
        author = each.find('td', class_='field author').a.text
        rating = each.find('td', class_='field avg_rating').div.text.strip()
        f_obj.writerow([title, author, rating, img_url])
    page += 1
    sleep(randint(10, 20))





