import requests
from bs4 import BeautifulSoup as bs
import json

isbn = '4774198765'.replace('-', '')
print(isbn)
key = 'AIzaSyDXBxe_sCjrhhFPEGphgTfehrKDs-17aFQ'
base_url = 'https://www.googleapis.com/books/v1/volumes?q=isbn:'

query = base_url + isbn + '&key=' + key
data = requests.get(query)

soup = bs(data.text, 'html5lib')

print(query)
