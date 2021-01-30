#!/Users/NaumaanHassan/Documents/GitHub/naumaanh.github.io/tutorial-env/bin/python3  
# encoding=utf8
from bs4 import BeautifulSoup
import json
import urllib.request
import requests
import datetime
import re
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

timeLastRan = datetime.datetime.now().strftime("Last updated: %B %d, %Y at %I:%M%p")

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
mmURL = 'http://www.makkahmasjid.net'
micURL = 'http://www.micmasjid.com'
myaseenURL = 'http://masjidyaseen.org'
mckinneyURL = 'http://www.mckinneymasjid.org'
mansfURL = 'https://www.mansfieldmasjid.com'
darelimanURL = 'https://www.dareleman.org'
maiURL = 'https://masjidalislam.org/prayer-times/'
dncfwURL = 'https://dncfw.org'
ialfmURL = 'https://us.mohid.co/tx/dallas/ialfm/masjid/widget/api/index/?m=prayertimings'
icopURL = 'https://us.mohid.co/tx/dallas/iccltx/masjid'
iacURL = 'https://www.masjidal-rahman.org/'

iciR = requests.get(iciURL)
vricR = requests.get(vricURL)
iantR = requests.get(iantURL, headers=header).text
epicR = requests.get(epicURL)
iaccR = requests.get(iaccURL)
icfR = requests.get(icfURL)
allenR = requests.get(allenURL, headers=header).text
mmR = requests.get(mmURL)
micR = requests.get(micURL, headers=header).text
myaseenR = requests.get(myaseenURL)
mckinneyR = requests.get(mckinneyURL, headers=header).text
mansfR = requests.get(mansfURL, headers=header).text
darelimanR = requests.get(darelimanURL, headers=header).text
maiR = requests.get(maiURL)
dncfwR = requests.get(dncfwURL, headers=header).text
ialfmR = requests.get(ialfmURL)
icopR = requests.get(icopURL)
iacR = requests.get(iacURL)

iciHTML = iciR.text
vricHTML = vricR.text
#iantHTML = urlopen(iantR).read()
epicHTML = epicR.text
iaccHTML = iaccR.text
icfHTML = icfR.text
#allenHTML = allenR.text
mmHTML = mmR.text
#micHTML = micR.text
myaseenHTML = myaseenR.text
#mckinneyHTML = mckinneyR.text
#mansfHTML = mansfR.text
#maiHTML = maiR.text
#dncfwHTML = dncfwR.text
ialfmHTML = ialfmR.text
icopHTML = icopR.text
iacHTML = iacR.text

icisoup = BeautifulSoup(iciHTML, "html.parser")
vricsoup = BeautifulSoup(vricHTML, "html.parser")
iantsoup = BeautifulSoup(iantR, "html.parser")
epicsoup = BeautifulSoup(epicHTML, "html.parser")
iaccsoup = BeautifulSoup(iaccHTML, "html.parser")
icfsoup = BeautifulSoup(icfHTML, "html.parser")
allensoup = BeautifulSoup(allenR, "html.parser")
#icssoup = BeautifulSoup(icsHTML, "html.parser")
mmsoup = BeautifulSoup(mmHTML, "html.parser")
micsoup = BeautifulSoup(micR, "html.parser")
myaseensoup = BeautifulSoup(myaseenHTML, "html.parser")
mckinneysoup = BeautifulSoup(mckinneyR, "html.parser")
mansfsoup = BeautifulSoup(mansfR, "html.parser")
darelimansoup = BeautifulSoup(darelimanR, "html.parser")
dncfwsoup = BeautifulSoup(dncfwR, "html.parser")
ialfmsoup = BeautifulSoup(ialfmHTML, "html.parser")
icopsoup = BeautifulSoup(icopHTML, "html.parser")
iacsoup = BeautifulSoup(iacHTML, "html.parser")

#Masjid AR RAHMAN ISLAMIC ASSOCIATION OF CARROLLTON IAC
iacTimings = iacsoup.findAll('span')
print(iacTimings)

#ISLAMIC ASSOCIATION OF FORT WORTH DAR UN NOOR
dncfwIqamahTimings = dncfwsoup.findAll('td')
dncfwFprayer = "N/A"#dncfwIqamahTimings[1].text.strip()
dncfwDprayer = "N/A"#dncfwIqamahTimings[3].text.strip()
dncfwAprayer = "N/A"#dncfwIqamahTimings[5].text.strip()
dncfwMprayer = "N/A"#dncfwIqamahTimings[7].text.strip()
dncfwIprayer = "N/A"#dncfwIqamahTimings[9].text.strip()
dncfwJ1aprayer = dncfwIqamahTimings[1].text.strip()#dncfwIqamahTimings[11].text.strip()

#MASJID AL ISLAM
#maiIQamahTimings = maisoup.findAll('html')

#DAR EL IMAAN ARLINGTON 
darelimanIqamahTimings = darelimansoup.findAll('span style')

#MANSFIELD MASJID
mansfIqamahTimingF = mansfsoup.findAll('th')
mansfIqamahTiming = mansfsoup.findAll('td')
#mansF = ((str(mansfIqamahTimingF[1].text)).strip())

#ISLAMIC CENTER OF COPPELL
icopIqamahTimings = icopsoup.findAll('div', attrs={"class": "prayer_iqama_div"})
icopAdhanTimings = icopsoup.findAll('div', attrs={"class": "prayer_azaan_div"})
icopJummahTiming1 = icopsoup.find('div', attrs={"class": "num"})
#print icopIqamahTimings
allICC = {
	'ID': 13,
	'name': "ICC",
	'fullName': "Islamic Center of Coppell",
	'FajrAdhan': icopAdhanTimings[1].text,
	'FajrIqamah': icopIqamahTimings[1].text,
	'DhurAdhan': icopAdhanTimings[2].text,
	'DhurIqamah': icopIqamahTimings[2].text,
	'AsrAdhan': icopAdhanTimings[3].text,
	'AsrIqamah': icopIqamahTimings[3].text,
	'MaghribAdhan': icopAdhanTimings[4].text,
	'MaghribIqamah': icopIqamahTimings[4].text,
	'IshaAdhan': icopAdhanTimings[5].text,
	'IshaIqamah': icopIqamahTimings[5].text,
	'masjidPic': "",
	'URL': 'https://iccmasjid.org/',
	'latitude': 32.969960, 
	'longitude': -96.975986,
}

#Masjid Yaseen
myaseenIqamahTiming = myaseensoup.findAll('td', attrs={"style": "text-align:right"})
allMY = {
	'ID': 12,
	'name': "MY",
	'fullName': "Masjid Yaseen",
	'FajrAdhan': ((str(myaseenIqamahTiming[0].text)).strip()),
	'FajrIqamah': ((str(myaseenIqamahTiming[1].text)).strip()),
	'DhurAdhan': ((str(myaseenIqamahTiming[2].text)).strip()),
	'DhurIqamah': ((str(myaseenIqamahTiming[3].text)).strip()),
	'AsrAdhan': ((str(myaseenIqamahTiming[4].text)).strip()),
	'AsrIqamah': ((str(myaseenIqamahTiming[5].text)).strip()),
	'MaghribAdhan': ((str(myaseenIqamahTiming[6].text)).strip()),
	'MaghribIqamah': ((str(myaseenIqamahTiming[7].text)).strip()),
	'IshaAdhan': ((str(myaseenIqamahTiming[8].text)).strip()),
	'IshaIqamah': ((str(myaseenIqamahTiming[9].text)).strip()),
	'masjidPic': "",
	'URL': "http://masjidyaseen.org/",
	'latitude': 32.983145, 
	'longitude': -96.650791,
}

#ISLAMIC ASSOCIATION OF LEWIVILLE FARMERS MOUND
ialfmIqamahTimings = ialfmsoup.findAll('div', attrs={"class": "prayer_iqama_div"})#icfsoup.findAll('body')#, {"class": "prayer_iqama_div"})
ialfmAdhanTimings = ialfmsoup.findAll('div', attrs={"class": "prayer_azaan_div"})#icfsoup.findAll('body')#, {"class": "prayer_iqama_div"})
allIALFM = {
	'ID': 11,
	'name': "IALFM",
	'fullName': "Islamic Association of Lewisville & Flower Mound",
	'FajrAdhan': ialfmAdhanTimings[1].text,
	'FajrIqamah': ialfmIqamahTimings[1].text,
	'DhurAdhan': ialfmAdhanTimings[2].text,
	'DhurIqamah': ialfmIqamahTimings[2].text,
	'AsrAdhan': ialfmAdhanTimings[3].text,
	'AsrIqamah': ialfmIqamahTimings[3].text,
	'MaghribAdhan': ialfmAdhanTimings[4].text,
	'MaghribIqamah': ialfmIqamahTimings[4].text,
	'IshaAdhan': ialfmAdhanTimings[5].text,
	'IshaIqamah': ialfmIqamahTimings[5].text,
	'masjidPic': "",
	'URL': 'https://www.ialfm.org/',
	'latitude': 33.034412, 
	'longitude': -97.083097,
}

#Mesquite Masjid
micIqamahTimings = micsoup.findAll('div', attrs={"class": "time"})
allMIC = {
	'ID': 10,
	'name': "MIC",
	'fullName': "Mesquite Islamic Center",
	'FajrAdhan': "N/A",
	'FajrIqamah': micIqamahTimings[0].text,
	'DhurAdhan': "N/A",
	'DhurIqamah': micIqamahTimings[1].text,
	'AsrAdhan': "N/A",
	'AsrIqamah': micIqamahTimings[2].text,
	'MaghribAdhan': "N/A",
	'MaghribIqamah': micIqamahTimings[3].text,
	'IshaAdhan': "N/A",
	'IshaIqamah': micIqamahTimings[4].text,
	'masjidPic': "",
	'URL': 'https://www.micmasjid.com/',
	'latitude': 32.796484, 
	'longitude': -96.617984,
}

#MCKINNEY MASJID
mckinneyIqamahTiming = mckinneysoup.findAll('td')
allMIA = {
	'ID': 9,
	'name': "MIA",
	'fullName': "McKinney Islamic Association",
	'FajrAdhan': mckinneyIqamahTiming[4].text.strip(),
	'FajrIqamah': mckinneyIqamahTiming[5].text,
	'DhurAdhan': mckinneyIqamahTiming[7].text.strip(),
	'DhurIqamah': mckinneyIqamahTiming[8].text,
	'AsrAdhan': mckinneyIqamahTiming[10].text.strip(),
	'AsrIqamah': mckinneyIqamahTiming[11].text,
	'MaghribAdhan': mckinneyIqamahTiming[13].text.strip(),
	'MaghribIqamah': mckinneyIqamahTiming[14].text,
	'IshaAdhan': mckinneyIqamahTiming[16].text.strip(),
	'IshaIqamah': mckinneyIqamahTiming[17].text,
	'masjidPic': "",
	'URL': 'https://www.mckinneymasjid.org/',
	'latitude': 33.169022, 
	'longitude': -96.663064
}

# ALLEN MASJID
allenIqamahTimings = allensoup.findAll('td')
allAllen = {
	'ID': 8,
	'name': "IAA",
	'fullName': "Islamic Association of Allen",
	'FajrAdhan': ((str(allenIqamahTimings[1].text)).strip()+' AM'),
	'FajrIqamah': ((str(allenIqamahTimings[2].text)).strip()+' AM'),
	'DhurAdhan': ((str(allenIqamahTimings[4].text)).strip()+' AM'),
	'DhurIqamah': ((str(allenIqamahTimings[5].text)).strip()+' AM'),
	'AsrAdhan': ((str(allenIqamahTimings[7].text)).strip()+' AM'),
	'AsrIqamah': ((str(allenIqamahTimings[8].text)).strip()+' AM'),
	'MaghribAdhan': ((str(allenIqamahTimings[10].text)).strip()+' AM'),
	'MaghribIqamah': ((str(allenIqamahTimings[11].text)).strip()+' AM'),
	'IshaAdhan': ((str(allenIqamahTimings[13].text)).strip()+' AM'),
	'IshaIqamah': ((str(allenIqamahTimings[14].text)).strip()+' AM'),
	'masjidPic': "",
	'URL': 'https://allenmasjid.com/',
	'latitude': 33.097190, 
	'longitude': -96.683529,
}

#MAKKAH MASJID GARLAND
mmIqamahTimings = mmsoup.findAll('td')
allMM = {
	'ID': 7,
	'name': "IDEA",
	'fullName': "Makkah Masjid",
	'FajrAdhan': "N/A",
	'FajrIqamah': mmIqamahTimings[1].text,
	'DhurAdhan': "N/A",
	'DhurIqamah': mmIqamahTimings[3].text,
	'AsrAdhan': "N/A",
	'AsrIqamah': mmIqamahTimings[5].text,
	'MaghribAdhan': "N/A",
	'MaghribIqamah': mmIqamahTimings[7].text,
	'IshaAdhan': "N/A",
	'IshaIqamah': mmIqamahTimings[9].text,
	'masjidPic': "",
	'URL': 'http://www.makkahmasjid.net/',
	'latitude': 32.931817, 
	'longitude': -96.679314
}

#ISLAMIC ASSOCIATION OF NORTH TEXAS IANT
iantIqamahTimings = iantsoup.findAll('td')
allIANT = {
	'ID': 6,
	'name': "IANT",
	'fullName': "Islamic Association of North Texas",
	'FajrAdhan': iantIqamahTimings[0].text,
	'FajrIqamah': iantIqamahTimings[1].text,
	'DhurAdhan': iantIqamahTimings[3].text,
	'DhurIqamah': iantIqamahTimings[4].text,
	'AsrAdhan': iantIqamahTimings[5].text,
	'AsrIqamah': iantIqamahTimings[6].text,
	'MaghribAdhan': iantIqamahTimings[7].text,
	'MaghribIqamah': iantIqamahTimings[8].text,
	'IshaAdhan': iantIqamahTimings[9].text,
	'IshaIqamah': iantIqamahTimings[10].text,
	'masjidPic': "",
	'URL': 'https://iant.com/',
	'latitude': 32.939422, 
	'longitude': -96.730911,
}

#ISLAMIC ASSOCIATION OF COLLIN COUNTY IACC
iaccIqamahTimings = iaccsoup.findAll('td', attrs={"style": "text-align:right"})
allIACC = {
	'ID': 5,
	'name': "IACC",
	'fullName': "Islamic Association of Collin County",
	'FajrAdhan': "N/A",
	'FajrIqamah': ((str(iaccIqamahTimings[0].text)).strip()+' AM'),
	'DhurAdhan': "N/A",
	'DhurIqamah': ((str(iaccIqamahTimings[2].text)).strip()+' PM'),
	'AsrAdhan': "N/A",
	'AsrIqamah': ((str(iaccIqamahTimings[3].text)).strip()+' PM'),
	'MaghribAdhan': "N/A",
	'MaghribIqamah': ((str(iaccIqamahTimings[4].text)).strip()+' PM'),
	'IshaAdhan': "N/A",
	'IshaIqamah': ((str(iaccIqamahTimings[5].text)).strip()+' PM'),
	'masjidPic': "",
	'URL': 'https://planomasjid.org/',
	'latitude': 33.059832, 
	'longitude': -96.751554,
} 

#ISLAMIC CENTER OF FRISCO ICF
icfIqamahTimings = icfsoup.findAll('div', attrs={"class": "prayer_iqama_div"})#icfsoup.findAll('body')#, {"class": "prayer_iqama_div"})
icfAdhanTimings = icfsoup.findAll('div', attrs={"class": "prayer_azaan_div"})#icfsoup.findAll('body')#, {"class": "prayer_iqama_div"})

allICF = {
	'ID': 4,
	'name': "ICF",
	'fullName': "Islamic Center of Frisco",
	'FajrAdhan': icfAdhanTimings[1].text,
	'FajrIqamah': icfIqamahTimings[1].text,
	'DhurAdhan': icfAdhanTimings[2].text,
	'DhurIqamah': icfIqamahTimings[2].text,
	'AsrAdhan': icfAdhanTimings[3].text,
	'AsrIqamah': icfIqamahTimings[3].text,
	'MaghribAdhan': icfAdhanTimings[4].text,
	'MaghribIqamah': icfIqamahTimings[4].text,
	'IshaAdhan': icfAdhanTimings[5].text,
	'IshaIqamah': icfIqamahTimings[5].text,
	'masjidPic': "",
	'URL': 'https://friscomasjid.org/',
	'latitude': 33.172561, 
	'longitude': -96.834773,
}

#EAST PLANO ISLAMIC CENTER EPIC
epicIqamahTimings = epicsoup.findAll('td', attrs={"class": "subtext"})
allEPIC = {
	'ID': 3,
	'name': "EPIC",
	'fullName': "East Plano Islamic Center",
	'FajrAdhan': epicIqamahTimings[0].text,
	'FajrIqamah': epicIqamahTimings[1].text,
	'DhurAdhan': epicIqamahTimings[3].text,
	'DhurIqamah': epicIqamahTimings[4].text,
	'AsrAdhan': epicIqamahTimings[5].text,
	'AsrIqamah': epicIqamahTimings[6].text,
	'MaghribAdhan': epicIqamahTimings[7].text,
	'MaghribIqamah': epicIqamahTimings[8].text,
	'IshaAdhan': epicIqamahTimings[9].text,
	'IshaIqamah': epicIqamahTimings[10].text,
	'masjidPic': "",
	'URL': 'https://epicmasjid.org/',
	'latitude': 33.010194, 
	'longitude': -96.646658,
}

#IRVING MASJID ICI
iciIqamahTimings = icisoup.findAll('td')
iciAdhanTimings = icisoup.findAll('td')
#iciJummahTimings = (icisoup.findAll('td', attrs={"colspan": "6"})[-1])
allICI = {
	'ID': 2,
	'name': "ICI",
	'fullName': "Islamic Center of Irving",
	'FajrAdhan': iciAdhanTimings[0].text,
	'FajrIqamah': iciIqamahTimings[6].text,
	'DhurAdhan': iciAdhanTimings[2].text,
	'DhurIqamah': iciIqamahTimings[7].text,
	'AsrAdhan': iciAdhanTimings[3].text,
	'AsrIqamah': iciIqamahTimings[8].text,
	'MaghribAdhan': iciAdhanTimings[4].text,
	'MaghribIqamah': iciIqamahTimings[9].text,
	'IshaAdhan': iciAdhanTimings[5].text,
	'IshaIqamah': iciIqamahTimings[10].text,
	'masjidPic': "",
	'URL': 'https://irvingmasjid.org/',
	'latitude': 32.843514, 
	'longitude': -97.010609,
}

#VALLEY RANCH ISLAMIC CENTER VRIC
with urllib.request.urlopen(vricURL) as url:
	vricResponse = url.read()
vricJSON = json.loads(vricResponse)

allVRIC = {
	'ID': 1,
	'name': "VRIC",
	'fullName': "Valley Ranch Islamic Center",
	'FajrAdhan': vricJSON['fajrAdhan'],
	'FajrIqamah': vricJSON['fajrIqamah'],
	'DhurAdhan': vricJSON['duhrAdhan'],
	'DhurIqamah': vricJSON['duhrIqamah'],
	'AsrAdhan': vricJSON['asrAdhan'],
	'AsrIqamah': vricJSON['asrIqamah'],
	'MaghribAdhan': vricJSON['maghribAdhan'],
	'MaghribIqamah': vricJSON['maghribIqamah'],
	'IshaAdhan': vricJSON['ishaAdhan'],
	'IshaIqamah': vricJSON['ishaIqamah'],
	'masjidPic': "",
	'URL': 'https://vric.org/',
	'latitude': 32.917265, 
	'longitude': -96.948097,
}
allTime = {
	'ID' : 1, 
	'timeLastRan': timeLastRan,
}
outputer = [allVRIC, allICI, allEPIC, allICF, allIACC, allIANT, allMM, allAllen, allMIA, allMIC, allIALFM, allMY, allICC]
z = json.dumps(outputer)
with open('allData.json', 'w') as outfile:
	json.dump(outputer,outfile, indent=2)

outputer1 = [allTime]
z = json.dumps(outputer1)
with open('allTime.json', 'w') as outfile:
	json.dump(outputer1,outfile, indent=2)	

