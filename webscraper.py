#!/usr/bin/python
# encoding=utf8

from bs4 import BeautifulSoup
import requests
import json
import urllib
import requests
import datetime
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')


timeLastRan = datetime.datetime.now().strftime("Last updated on %I:%M%p on %B %d, %Y")

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
allenURL = 'https://allenmasjid.com'
icsURL = 'https://us.mohid.co/tx/dallas/ics/masjid'
mmURL = 'http://www.makkahmasjid.net'
micURL = 'http://www.micmasjid.com'
myaseenURL = 'http://masjidyaseen.org'
mckinneyURL = 'http://www.mckinneymasjid.org'
mansfURL = 'https://www.mansfieldmasjid.com'
darelimanURL = 'https://www.dareleman.org'
#maiURL = 'https://masjidalislam.org'
dncfwURL = 'https://dncfw.org'
isdURL = 'https://www.dentonmosque.com'
ialfmURL = 'https://us.mohid.co/tx/dallas/ialfm/masjid/widget/api/index/?m=prayertimings'
icopURL = 'https://us.mohid.co/tx/dallas/iccltx/masjid'

iciR = requests.get(iciURL)
vricR = requests.get(vricURL)
iantR = requests.get(iantURL, headers=header).text
epicR = requests.get(epicURL)
iaccR = requests.get(iaccURL)
icfR = requests.get(icfURL)
allenR = requests.get(allenURL, headers=header).text
icsR = requests.get(icsURL)
mmR = requests.get(mmURL)
micR = requests.get(micURL, headers=header).text
myaseenR = requests.get(myaseenURL)
mckinneyR = requests.get(mckinneyURL, headers=header).text
mansfR = requests.get(mansfURL, headers=header).text
darelimanR = requests.get(darelimanURL, headers=header).text
#maiR = requests.get(maiURL)
dncfwR = requests.get(dncfwURL, headers=header).text
isdR = requests.get(isdURL, headers=header).text
ialfmR = requests.get(ialfmURL)
icopR = requests.get(icopURL)


iciHTML = iciR.text
vricHTML = vricR.text
#iantHTML = urlopen(iantR).read()
epicHTML = epicR.text
iaccHTML = iaccR.text
icfHTML = icfR.text
#allenHTML = allenR.text
icsHTML = icsR.text
mmHTML = mmR.text
#micHTML = micR.text
myaseenHTML = myaseenR.text
#mckinneyHTML = mckinneyR.text
#mansfHTML = mansfR.text
#maiHTML = maiR.text
#dncfwHTML = dncfwR.text
ialfmHTML = ialfmR.text
icopHTML = icopR.text

icisoup = BeautifulSoup(iciHTML, "html.parser")
vricsoup = BeautifulSoup(vricHTML, "html.parser")
iantsoup = BeautifulSoup(iantR, "html.parser")
epicsoup = BeautifulSoup(epicHTML, "html.parser")
iaccsoup = BeautifulSoup(iaccHTML, "html.parser")
icfsoup = BeautifulSoup(icfHTML, "html.parser")
allensoup = BeautifulSoup(allenR, "html.parser")
icssoup = BeautifulSoup(icsHTML, "html.parser")
mmsoup = BeautifulSoup(mmHTML, "html.parser")
micsoup = BeautifulSoup(micR, "html.parser")
myaseensoup = BeautifulSoup(myaseenHTML, "html.parser")
mckinneysoup = BeautifulSoup(mckinneyR, "html.parser")
mansfsoup = BeautifulSoup(mansfR, "html.parser")
darelimansoup = BeautifulSoup(darelimanR, "html.parser")
dncfwsoup = BeautifulSoup(dncfwR, "html.parser")
isdsoup = BeautifulSoup(isdR, "html.parser")
ialfmsoup = BeautifulSoup(ialfmHTML, "html.parser")
icopsoup = BeautifulSoup(icopHTML, "html.parser")

#ISLAMIC CENTER OF COPPELL
icopIqamahTimings = icopsoup.findAll('div', attrs={"class": "prayer_iqama_div"})
icopAdhanTimings = icopsoup.findAll('div', attrs={"class": "prayer_azaan_div"})
icopJummahTiming1 = icopsoup.find('div', attrs={"class": "num"})
icopJummahTiming = ((str(icopJummahTiming1.text)).strip())


#ISLAMIC ASSOCIATION OF LEWIVILLE FARMER MOUND
ialfmIqamahTimings = ialfmsoup.findAll('div', attrs={"class": "prayer_iqama_div"})#icfsoup.findAll('body')#, {"class": "prayer_iqama_div"})
ialfmAdhanTimings = ialfmsoup.findAll('div', attrs={"class": "prayer_azaan_div"})#icfsoup.findAll('body')#, {"class": "prayer_iqama_div"})
ialfmJ1a = ialfmIqamahTimings[6].text.strip()
ialfmJ1i = ialfmIqamahTimings[7].text.strip()
#ISLAMIC CENTER OF DENTON
isdIqamahTimings = isdsoup.findAll('td')

#ISLAMIC ASSOCIATION OF FORT WORTH DAR UN NOOR
dncfwIqamahTimings = dncfwsoup.findAll('td')
dncfwFprayer = dncfwIqamahTimings[1].text.strip()
dncfwDprayer = dncfwIqamahTimings[3].text.strip()
dncfwAprayer = dncfwIqamahTimings[5].text.strip()
dncfwMprayer = dncfwIqamahTimings[7].text.strip()
dncfwIprayer = dncfwIqamahTimings[9].text.strip()
dncfwJ1aprayer = dncfwIqamahTimings[11].text.strip()

#MASJID AL ISLAM
#maiIQamahTimings = maisoup.findAll('html')

#DAR EL IMAAN ARLINGTON 
darelimanIqamahTimings = darelimansoup.findAll('td')

#MANSFIELD MASJID
mansfIqamahTimingF = mansfsoup.findAll('th')
mansfIqamahTiming = mansfsoup.findAll('td')
mansF = ((str(mansfIqamahTimingF[1].text)).strip())

#MCKINNEY MASJID
mckinneyIqamahTiming = mckinneysoup.findAll('td')
#	'Mckinneya': mckinneyIqamahTiming[].text,
#	'Mckinneyi': mckinneyIqamahTiming[].text,
Mckinneyf = mckinneyIqamahTiming[4].text.strip()
Mckinneyd = mckinneyIqamahTiming[7].text.strip()
Mckinneya = mckinneyIqamahTiming[10].text.strip()
Mckinneym = mckinneyIqamahTiming[13].text.strip()
Mckinneyi = mckinneyIqamahTiming[16].text.strip()
MckinneyJ1 = mckinneyIqamahTiming[19].text.strip()
MckinneyJ2 = mckinneyIqamahTiming[21].text.strip()


#Masjid Yaseen
myaseenIqamahTiming = myaseensoup.findAll('td', attrs={"style": "text-align:right"})
amyaseenFprayer = ((str(myaseenIqamahTiming[0].text)).strip())
amyaseenDprayer = ((str(myaseenIqamahTiming[2].text)).strip())
amyaseenAprayer = ((str(myaseenIqamahTiming[4].text)).strip())
amyaseenMprayer = ((str(myaseenIqamahTiming[6].text)).strip())
amyaseenIprayer = ((str(myaseenIqamahTiming[8].text)).strip())

myaseenJ1prayer = ((str(myaseenIqamahTiming[10].text)).strip())
myaseenJ2prayer = ((str(myaseenIqamahTiming[11].text)).strip())

imyaseenFprayer = ((str(myaseenIqamahTiming[1].text)).strip())
imyaseenDprayer = ((str(myaseenIqamahTiming[3].text)).strip())
imyaseenAprayer = ((str(myaseenIqamahTiming[5].text)).strip())
imyaseenMprayer = ((str(myaseenIqamahTiming[7].text)).strip())
imyaseenIprayer = ((str(myaseenIqamahTiming[9].text)).strip())


#Mesquite Masjid
micIqamahTimings = micsoup.findAll('div', attrs={"class": "time"})


#MAKKAH MASJID GARLAND
mmIqamahTimings = mmsoup.findAll('td')


#SOUTHLAKE MASJID
icsIqamahTimings = icssoup.findAll('div', attrs={"class": "prayer_iqama_div"})
icsAdhanTimings = icssoup.findAll('div', attrs={"class": "prayer_azaan_div"})
icsJummahTiming = icssoup.findAll('div', attrs={"class": "num"})
icsJ1a = ((str(icsJummahTiming[0].text)).strip())
icsJ1i = ((str(icsJummahTiming[1].text)).strip())

# ALLEN MASJID
allenIqamahTimings = allensoup.findAll('td')
aallenFprayer = ((str(allenIqamahTimings[1].text)).strip()+' AM')
aallenDprayer = ((str(allenIqamahTimings[4].text)).strip()+' PM')
aallenAprayer = ((str(allenIqamahTimings[7].text)).strip()+' PM')
aallenMprayer = ((str(allenIqamahTimings[10].text)).strip()+' PM')
aallenIprayer = ((str(allenIqamahTimings[13].text)).strip()+' PM')

aallenJ1prayer = ((str(allenIqamahTimings[16].text)).strip())
aallenJ2prayer = ((str(allenIqamahTimings[18].text)).strip())

iallenFprayer = ((str(allenIqamahTimings[2].text)).strip()+' AM')
iallenDprayer = ((str(allenIqamahTimings[5].text)).strip()+' PM')
iallenAprayer = ((str(allenIqamahTimings[8].text)).strip()+' PM')
iallenMprayer = ((str(allenIqamahTimings[11].text)).strip()+' PM')
iallenIprayer = ((str(allenIqamahTimings[14].text)).strip()+' PM')

#IRVING MASJID ICI
iciIqamahTimings = icisoup.findAll('td', attrs={"class": "jamah"})
iciAdhanTimings = icisoup.findAll('td', attrs={"class": "begins"})
iciJummahTimings = (icisoup.find('td', attrs={"colspan": "2"}))
iciJJ = ((str(iciJummahTimings.text)))
iciJ4 = iciJJ.replace(u"\u2019", "'")
iciJ3 = iciJ4.replace("1st Jumm'a ", "")
iciJ2 = iciJ3.replace("2nd Jumm'a ", "")
iciJ1 = iciJ2.split(" | ")

print iciJummahTimings

#iciAdhanTimingsAsDictionary = {
#	"FajrAdhan": iciAdhanTimings[0].text,
#	'DhurAdhan': iciAdhanTimings[3].text,
#	'AsrAdhan': iciAdhanTimings[5].text,
#	'MaghribAdhan': iciAdhanTimings[7].text,
#	'IshaAdhan': iciAdhanTimings[9].text,
#}
#iciIqamahTimingsAsDictionary = {
#	"FajrIqamah": iciIqamahTimings[0].text,
#	'DhurIqamah': iciIqamahTimings[1].text,
#	'AsrIqamah': iciIqamahTimings[2].text,
#	'MaghribIqamah': iciIqamahTimings[3].text,
#	'IshaIqamah': iciIqamahTimings[4].text,
#}
#iciIqamahTimingsAsList = [iciIqamahTimingsAsDictionary]
#iciIqamahJSON = json.dumps(iciIqamahTimingsAsList)
#with open('ici.json', 'w') as outfile:
#	json.dump(iciIqamahTimingsAsList, outfile)

#VALLEY RANCH ISLAMIC CENTER VRIC
vricResponse = urllib.urlopen(vricURL)
vricJSON = json.loads(vricResponse.read())
vricAdhanTimingsAsDictionary = {
	'FajrAdhan': vricJSON['fajrAdhan'],
	'DhurAdhan': vricJSON['duhrAdhan'],
	'AsrAdhan': vricJSON['asrAdhan'],
	'MaghribAdhan': vricJSON['maghribAdhan'],
	'IshaAdhan': vricJSON['ishaAdhan'],
}
vricIqamahTimingsAsDictionary = {
	'FajrIqamah': vricJSON['fajrIqamah'],
	'DhurIqamah': vricJSON['duhrIqamah'],
	'AsrIqamah': vricJSON['asrIqamah'],
	'MaghribIqamah': vricJSON['maghribIqamah'],
	'IshaIqamah': vricJSON['ishaIqamah'],
}
#vricIqamahTimingsAsList = [vricIqamahTimingsAsDictionary]
#vricPrayerJSON = json.dumps(vricIqamahTimingsAsList)
#with open('vric.json', 'w') as outfile:
#	json.dump(vricIqamahTimingsAsList, outfile)
	



#ISLAMIC ASSOCIATION OF NORTH TEXAS IANT
iantIqamahTimings = iantsoup.findAll('td')



#EAST PLANO ISLAMIC CENTER EPIC
epicIqamahTimings = epicsoup.findAll('td', attrs={"class": "subtext"})
#epicAdhanTimingsAsDictionary = {
#	
#}
#epicIqamahTimingsAsDictionary = {
#	'FajrIqamah': epicIqamahTimings[1].text,
#	'DhurIqamah': epicIqamahTimings[4].text,
#	'AsrIqamah': epicIqamahTimings[6].text,
#	'MaghribIqamah': epicIqamahTimings[8].text,
#	'IshaIqamah': epicIqamahTimings[10].text,
#}
#epicIqamahTimingsAsList = [epicIqamahTimingsAsDictionary]
#epicIqamahJSON = json.dumps(epicIqamahTimingsAsList)
#with open('epic.json', 'w') as outfile:
#	json.dump(epicIqamahTimingsAsList, outfile)

#ISLAMIC ASSOCIATION OF COLLIN COUNTY IACC
iaccIqamahTimings = iaccsoup.findAll('td', attrs={"style": "text-align:right"})
iaccFprayer = ((str(iaccIqamahTimings[0].text)).strip()+' AM')
iaccDprayer = ((str(iaccIqamahTimings[2].text)).strip()+' PM')
iaccAprayer = ((str(iaccIqamahTimings[3].text)).strip()+' PM')
iaccMprayer = ((str(iaccIqamahTimings[4].text)).strip()+' PM')
iaccIprayer = ((str(iaccIqamahTimings[5].text)).strip()+' PM')
iaccJ1prayer = ((str(iaccIqamahTimings[6].text)).strip())
iaccJ2prayer = ((str(iaccIqamahTimings[7].text)).strip())

#iaccIqamahTimingsAsDictionary = {
#	'FajrIqamah': iaccFprayer,
#	'DhurIqamah': iaccDprayer,
#	'AsrIqamah': iaccAprayer,
#	'MaghribIqamah': iaccMprayer,
#	'IshaIqamah': iaccIprayer,
#}

#iaccIqamahTimingsAsList = [iaccIqamahTimingsAsDictionary]
#iaccIqamahJSON = json.dumps(iaccIqamahTimingsAsList)
#with open('iacc.json', 'w') as outfile:
#	json.dump(iaccIqamahTimingsAsList, outfile)

#ISLAMIC CENTER OF FRISCO ICF
icfIqamahTimings = icfsoup.findAll('div', attrs={"class": "prayer_iqama_div"})#icfsoup.findAll('body')#, {"class": "prayer_iqama_div"})
icfAdhanTimings = icfsoup.findAll('div', attrs={"class": "prayer_azaan_div"})#icfsoup.findAll('body')#, {"class": "prayer_iqama_div"})
icfJ1a = ((str(icfIqamahTimings[6].text)).strip())
icfJ1i = ((str(icfIqamahTimings[7].text)).strip())
icfJ2a = ((str(icfIqamahTimings[8].text)).strip())
icfJ2i = ((str(icfIqamahTimings[9].text)).strip())

#icfIqamahTimingsAsDictionary = {
#	'FajrIqamah': icfIqamahTimings[1].text,
#	'DhurIqamah': icfIqamahTimings[2].text,
#	'AsrIqamah': icfIqamahTimings[3].text,
#	'MaghribIqamah': icfIqamahTimings[4].text,
#	'IshaIqamah': icfIqamahTimings[5].text,
#}
#icfIqamahTimingsAsList = [icfIqamahTimingsAsDictionary]
#icfIqamahJSON = json.dumps(icfIqamahTimingsAsList)
#with open('icf.json', 'w') as outfile:
#	json.dump(icfIqamahTimingsAsList, outfile)	

