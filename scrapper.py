import socket
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

try:
  url = input('Enter: ')
  html = urllib.request.urlopen(url).read()
  soup = BeautifulSoup(html, 'html.parser')

  print(soup.prettify())
except:
  print("err")