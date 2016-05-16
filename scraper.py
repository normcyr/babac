#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import csv
from bs4 import BeautifulSoup
#import urllib2

#username = ""
#password = ""

#r = requests.get('http://cyclebabac.com/wp-login.php', auth=(username, password))

#with open("commande.csv", "rb") as fichiercsv:
#    data = csv.reader(fichiercsv)
#    liste = list(data)

with open('perso.csv', 'rU') as fichiercsv:
  # read the file as a dictionary for each row ({header : value})
  reader = csv.DictReader(fichiercsv)
  data = {}
  for row in reader:
    for header, value in row.items():
      try:
        data[header].append(value)
      except KeyError:
        data[header] = [value]
sku = data["# Babac"]

for ligne in sku:
    r = requests.get('http://cyclebabac.com/fr/', params='?s='+ligne)
    html = r.text
    soup = BeautifulSoup(html, "html.parser")
    title = soup.title
    sku2 = str(soup.find_all("span", attrs={"class": "sku"}))[34:40]
    for text in title.children:
        print(sku2 + "," + text[13:] + "," + "NOTRE PRIX")

#url = 'http://cyclebabac.com/' + '?s=' + noproduit
#response = urllib2.urlopen(url)
#html = response.read()
requests.get('https://api.github.com/user', auth=('user', 'pass'))
