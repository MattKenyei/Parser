import requests
from bs4 import BeautifulSoup

url = 'https://www.goodreads.com/search?q=python'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Finding all books
books = soup.find_all('div', {'class': 'bookContainer'})

for book in books:
    # element with title of book
    title = book.find('a', {'class': 'bookTitle'}).text.strip()

    # finding authors
    authors = [author.text for author in book.find_all('a', {'class': 'authorName'})]

    # finding rating
    rating = book.find('span', {'class': 'minirating'}).text.strip()

    # Findint count of reviews
    reviews_count = book.find('a', {'class': 'reviews'}).text.strip().split()[0]

    print(f'Title: {title}')
    print(f'Authors: {authors}')
    print(f'Rating: {rating}')
    print(f'Reviews count: {reviews_count}')
    print('\n')
