
#IMPORTS
import bs4
import codecs
import googlemaps
import os
import sys
import zipfile

#GET NAME OF FILE
name = sys.argv[1]

#EXTRACT KMZ
with zipfile.ZipFile(name, "r") as zipper:
	zipper.extractall("")

#OPEN FILE
data = codecs.open('doc.kml', encoding = 'utf-8').read()
os.remove('doc.kml')

#PARSING XHTML
doc = bs4.BeautifulSoup(data,'html.parser')
name = doc.find('placemark').find('name').text
coords = doc.find('placemark').find('point').find('coordinates').text.split(',')
coords = (float(coords[1]), float(coords[0]))

#GETTING ELEVATION
client = googlemaps.Client(key = open('Data\elevation key.txt').read())
elevation = googlemaps.elevation.elevation(client, locations = coords)[0]['elevation']

#PRINT RESULT
print("Name: " + name)
print("Elevation: " + str(elevation))

input()