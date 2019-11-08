#!/usr/bin/python
from bs4 import BeautifulSoup
import requests
import json
import urllib
import requests

class Object:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
}

iciURL = 'http://www.irvingmasjid.org'
vricURL = 'https://api.masjidapps.com/masjid/publicPrayerTimes/MQ2/NzY1ZjcxZmQtZjE0NS00OGFjLTljYTgtMjBiYmRlYjdkZGRj0'
iantURL = 'https://iant.com'
epicURL = 'https://www.epicmasjid.org'
iaccURL = 'https://planomasjid.org'
icfURL = 'https://us.mohid.co/tx/dallas/icf/masjid/widget/api/index/?m=prayertimings'

iciR = requests.get(iciURL)
vricR = requests.get(vricURL)
iantR = requests.get(iantURL, headers=header).text
epicR = requests.get(epicURL)
iaccR = requests.get(iaccURL)
icfR = requests.get(icfURL)

iciHTML = iciR.text
vricHTML = vricR.text
#iantHTML = urlopen(iantR).read()
epicHTML = epicR.text
iaccHTML = iaccR.text
icfHTML = icfR.text

icisoup = BeautifulSoup(iciHTML, "html.parser")
vricsoup = BeautifulSoup(vricHTML, "html.parser")
iantsoup = BeautifulSoup(iantR, "html.parser")
epicsoup = BeautifulSoup(epicHTML, "html.parser")
iaccsoup = BeautifulSoup(iaccHTML, "html.parser")
icfsoup = BeautifulSoup(icfHTML, "html.parser")


#IRVING MASJID ICI
icfAdhanTimings = icfsoup.findAll('div', attrs={"class": "prayer_azaan_div"})#icfsoup.findAll('body')#, {"class": "prayer_iqama_div"})

print icfAdhanTimings

#print iciIqamahTimingsAsDictionary