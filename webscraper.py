#!/usr/bin/python
from bs4 import BeautifulSoup
import requests
import json
import urllib
import requests

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

iciArr = []
#UNUSED: VRIC ALREADY HAS PREFORMED JSON
#vricArr = []
iantArr = []
epicArr = []
iaccArr = []
icfArr = []

#IRVING MASJID ICI
iciIqamahTimings = icisoup.findAll('td', attrs={"class": "jamah"})
iciFprayer = "FajrIqamah\":\""+str(iciIqamahTimings[0].text)
iciDprayer = "DhurIqamah\":\""+str(iciIqamahTimings[1].text)
iciAprayer = "AsrIqamah\":\""+str(iciIqamahTimings[2].text)
iciMprayer = "MaghribIqamah\":\""+str(iciIqamahTimings[3].text)
iciIprayer = "IshaIqamah\":\""+str(iciIqamahTimings[4].text)
iciArr.append(iciFprayer)
iciArr.append(iciDprayer)
iciArr.append(iciAprayer)
iciArr.append(iciMprayer)
iciArr.append(iciIprayer)
iciIqamahJSON = json.dumps(iciArr)
with open('ici.json', 'w') as outfile:
	json.dump(iciArr, outfile)

#VALLEY RANCH ISLAMIC CENTER VRIC
vricResponse = urllib.urlopen(vricURL)
vricJSON = json.loads(vricResponse.read())
vricPrayerJSON = json.dumps(vricJSON)
with open('vric.json', 'w') as outfile:
	json.dump(vricJSON, outfile)

#ISLAMIC ASSOCIATION OF NORTH TEXAS IANT
iantIqamahTimings = iantsoup.findAll('td', attrs={"class": "mit_time"})
iantFprayer = "FajrIqamah\":\""+str(iantIqamahTimings[1].text)
iantDprayer = "DhurIqamah\":\""+str(iantIqamahTimings[3].text)
iantAprayer = "AsrIqamah\":\""+str(iantIqamahTimings[5].text)
iantMprayer = "MaghribIqamah\":\" 10 minutes after "+str(iantIqamahTimings[6].text)
iantIprayer = "IshaIqamah\":\""+str(iantIqamahTimings[9].text)
iantArr.append(iantFprayer)
iantArr.append(iantDprayer)
iantArr.append(iantAprayer)
iantArr.append(iantMprayer)
iantArr.append(iantIprayer)
iantIqamahJSON = json.dumps(iantArr)
with open('iant.json', 'w') as outfile:
	json.dump(iantArr, outfile)

#EAST PLANO ISLAMIC CENTER EPIC
epicIqamahTimings = epicsoup.findAll('td', attrs={"class": "subtext"})
epicFprayer = "FajrIqamah\":\""+str(epicIqamahTimings[1].text)
epicDprayer = "DhurIqamah\":\""+str(epicIqamahTimings[4].text)
epicAprayer = "AsrIqamah\":\""+str(epicIqamahTimings[6].text)
epicMprayer = "MaghribIqamah\":\""+str(epicIqamahTimings[8].text)
epicIprayer = "IshaIqamah\":\""+str(epicIqamahTimings[10].text)
epicArr.append(epicFprayer)
epicArr.append(epicDprayer)
epicArr.append(epicAprayer)
epicArr.append(epicMprayer)
epicArr.append(epicIprayer)
epicIqamahJSON = json.dumps(epicArr)
with open('epic.json', 'w') as outfile:
	json.dump(epicArr, outfile)

#ISLAMIC ASSOCIATION OF COLLIN COUNTY IACC
iaccIqamahTimings = iaccsoup.findAll('td', attrs={"style": "text-align:right"})
iaccFprayer = (str("FajrIqamah\":\""+str(iaccIqamahTimings[0].text)).strip())
iaccDprayer = (str("DhurIqamah\":\""+str(iaccIqamahTimings[2].text)).strip())
iaccAprayer = (str("AsrIqamah\":\""+str(iaccIqamahTimings[3].text)).strip())
iaccMprayer = (str("MaghribIqamah\":\""+str(iaccIqamahTimings[4].text)).strip())
iaccIprayer = (str("IshaIqamah\":\""+str(iaccIqamahTimings[5].text)).strip())
iaccArr.append(iaccFprayer)
iaccArr.append(iaccDprayer)
iaccArr.append(iaccAprayer)
iaccArr.append(iaccMprayer)
iaccArr.append(iaccIprayer)
iaccIqamahJSON = json.dumps(iaccArr)
with open('iacc.json', 'w') as outfile:
	json.dump(iaccArr, outfile)

#ISLAMIC CENTER OF FRISCO ICF
icfIqamahTimings = icfsoup.findAll('div', attrs={"class": "prayer_iqama_div"})#icfsoup.findAll('body')#, {"class": "prayer_iqama_div"})

icfArr.append({'FajrIqamah': str(icfIqamahTimings[1].text)})
icfArr.append({'DhurIqamah': str(icfIqamahTimings[2].text)})
icfArr.append({'AsrIqamah': str(icfIqamahTimings[3].text)})
icfArr.append({'MaghribIqamah': str(icfIqamahTimings[4].text)})
icfArr.append({'IshaIqamah': str(icfIqamahTimings[5].text)})
#icfArr.append("IqamahTimings:", (str("FajrIqamah\":\""+str(icfIqamahTimings[1].text)).strip(), str("DhurIqamah\":\""+str(icfIqamahTimings[2].text)).strip()))
#icfArr.extend(icfDprayer)
#icfArr.extend(icfAprayer)
#icfArr.extend(icfMprayer)
#icfArr.extend(icfIprayer)

icfIqamahJSON = json.dumps(icfArr)
with open('icf.json', 'w') as outfile:
	json.dumps(icfArr, outfile, indent=2)	

icfsoup2 = icfsoup.findAll('div', attrs={"class": "prayer_iqama_div"})
print 
print
#print
print icfIqamahJSON
#print (content)


