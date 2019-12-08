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
allenURL = 'https://allenmasjid.com'
icsURL = 'https://us.mohid.co/tx/dallas/ics/masjid'
mmURL = 'http://www.makkahmasjid.net'
micURL = 'http://www.micmasjid.com'
myaseenURL = 'http://masjidyaseen.org'
mckinneyURL = 'http://www.mckinneymasjid.org'
mansfURL = 'https://www.mansfieldmasjid.com'
darelimanURL = 'https://www.dareleman.org'
maiURL = 'https://masjidalislam.org'
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
maiR = requests.get(maiURL)
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
maiHTML = maiR.text
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
maisoup = BeautifulSoup(maiHTML, "html.parser")
dncfwsoup = BeautifulSoup(dncfwR, "html.parser")
isdsoup = BeautifulSoup(isdR, "html.parser")
ialfmsoup = BeautifulSoup(ialfmHTML, "html.parser")
icopsoup = BeautifulSoup(icopHTML, "html.parser")

#ISLAMIC CENTER OF COPPELL
icopIqamahTimings = icopsoup.findAll('div', attrs={"class": "prayer_iqama_div"})
icopAdhanTimings = icopsoup.findAll('div', attrs={"class": "prayer_azaan_div"})


#ISLAMIC ASSOCIATION OF LEWIVILLE FARMER MOUND
ialfmIqamahTimings = ialfmsoup.findAll('div', attrs={"class": "prayer_iqama_div"})#icfsoup.findAll('body')#, {"class": "prayer_iqama_div"})
ialfmAdhanTimings = ialfmsoup.findAll('div', attrs={"class": "prayer_azaan_div"})#icfsoup.findAll('body')#, {"class": "prayer_iqama_div"})


#ISLAMIC CENTER OF DENTON
isdIqamahTimings = isdsoup.findAll('td')

#ISLAMIC ASSOCIATION OF FORT WORTH DAR UN NOOR
dncfwIqamahTimings = dncfwsoup.findAll('td')
dncfwFprayer = dncfwIqamahTimings[1].text.strip()
dncfwDprayer = dncfwIqamahTimings[3].text.strip()
dncfwAprayer = dncfwIqamahTimings[5].text.strip()
dncfwMprayer = dncfwIqamahTimings[7].text.strip()
dncfwIprayer = dncfwIqamahTimings[9].text.strip()

#MASJID AL ISLAM
maiIQamahTimings = maisoup.findAll('html')

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

#Masjid Yaseen
myaseenIqamahTiming = myaseensoup.findAll('td', attrs={"style": "text-align:right"})
amyaseenFprayer = ((str(myaseenIqamahTiming[0].text)).strip())
amyaseenDprayer = ((str(myaseenIqamahTiming[2].text)).strip())
amyaseenAprayer = ((str(myaseenIqamahTiming[4].text)).strip())
amyaseenMprayer = ((str(myaseenIqamahTiming[6].text)).strip())
amyaseenIprayer = ((str(myaseenIqamahTiming[8].text)).strip())

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

# ALLEN MASJID
allenIqamahTimings = allensoup.findAll('td')
aallenFprayer = ((str(allenIqamahTimings[1].text)).strip()+' AM')
aallenDprayer = ((str(allenIqamahTimings[4].text)).strip()+' PM')
aallenAprayer = ((str(allenIqamahTimings[7].text)).strip()+' PM')
aallenMprayer = ((str(allenIqamahTimings[10].text)).strip()+' PM')
aallenIprayer = ((str(allenIqamahTimings[13].text)).strip()+' PM')

iallenFprayer = ((str(allenIqamahTimings[2].text)).strip()+' AM')
iallenDprayer = ((str(allenIqamahTimings[5].text)).strip()+' PM')
iallenAprayer = ((str(allenIqamahTimings[8].text)).strip()+' PM')
iallenMprayer = ((str(allenIqamahTimings[11].text)).strip()+' PM')
iallenIprayer = ((str(allenIqamahTimings[14].text)).strip()+' PM')
#IRVING MASJID ICI

iciIqamahTimings = icisoup.findAll('td', attrs={"class": "jamah"})
iciAdhanTimings = icisoup.findAll('td')

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
iantIqamahTimings = iantsoup.findAll('td')#, attrs={"class": "i_labels a_left"})
#iantAdhanTimingsAsDictionary = {
#	'FajrAdhan': iantIqamahTimings[0].text+" AM",
#	'DhurAdhan': iantIqamahTimings[2].text+" PM",
#	'AsrAdhan': iantIqamahTimings[4].text+" PM",
#	'MaghribAdhan': iantIqamahTimings[6].text+" PM",
#	'IshaAdhan': iantIqamahTimings[8].text+" PM",
#}
#iantIqamahTimingsAsDictionary = {
#	'FajrIqamah': iantIqamahTimings[1].text+"AM",
#	'DhurIqamah': iantIqamahTimings[3].text+"PM",
#	'AsrIqamah': iantIqamahTimings[5].text+"PM",
#	'MaghribIqamah': '10 minutes after '+iantIqamahTimings[6].text+"PM",
#	'IshaIqamah': iantIqamahTimings[9].text+"PM",
#}
#iantIqamahTimingsAsList = [iantIqamahTimingsAsDictionary]
#iantIqamahJSON = json.dumps(iantIqamahTimingsAsList)
#with open('iant.json', 'w') as outfile:
#	json.dump(iantIqamahTimingsAsList, outfile)



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

#####################################################################################################
#####################################################################################################
#####################################################################################################
###############______Code to actually create 5 layer JSON____________________########################
#####################################################################################################
#####################################################################################################
#####################################################################################################
#####################################################################################################
#####################################################################################################



allFajr = {
	'ID': 1,
	'VRICi': vricJSON['fajrIqamah'],
	'ICIi': iciIqamahTimings[0].text,
	'ICIa': iciAdhanTimings[0].text,
	'ICFi': icfIqamahTimings[1].text,
	'IACCi': iaccFprayer,
	'IANTi': iantIqamahTimings[3].text,
	'EPICi': epicIqamahTimings[1].text,
	'Body': "Fajr: ",
	'VRICa' : vricJSON['fajrAdhan'],
	'IANTa' : iantIqamahTimings[2].text,
	'EPICa' : epicIqamahTimings[0].text,
	'ICFa': icfAdhanTimings[1].text,
	'Allena' : aallenFprayer,
	'Alleni' : iallenFprayer,
	'ICSi' : icsIqamahTimings[1].text,
	'ICSa' : icsAdhanTimings[1].text,
	'MMi' : mmIqamahTimings[1].text,
	'Mici' : micIqamahTimings[0].text,
	'MYaseena' : amyaseenFprayer,
	'MYaseeni' : imyaseenFprayer,
	'Mckinneya': Mckinneyf,
	'Mckinneyi': mckinneyIqamahTiming[5].text,
	'Mansfi': mansF,
	'Darelimaani': darelimanIqamahTimings[1].text,
	'dncfwi': dncfwFprayer,
	'isda': isdIqamahTimings[5].text,
	'isdi': isdIqamahTimings[6].text,
	'ialfmi': ialfmIqamahTimings[1].text,
	'ialfma': ialfmAdhanTimings[1].text,
	'icopi': icopIqamahTimings[1].text,
	'icopa': icopAdhanTimings[1].text,
}
allSunrise = {
	'ID': 2,
	'VRICi': vricJSON['sunrise'],
	'ICIi': vricJSON['sunrise'],
	'ICIa': "",
	'ICFi': vricJSON['sunrise'],
	'IACCi': vricJSON['sunrise'],
	'IANTi': vricJSON['sunrise'],
	'EPICi': vricJSON['sunrise'],
	'Body': "      Sunrise ",
	'VRICa' : "",
	'IANTa' : "",
	'EPICa' : "",
	'ICFa': "",
	'Allena' : "",
	'Alleni' : vricJSON['sunrise'],
	'ICSi' : vricJSON['sunrise'],
	'ICSa' : "",
	'MMi' : vricJSON['sunrise'],
	'Mici' : vricJSON['sunrise'],
	'MYaseena' : "",
	'MYaseeni' : vricJSON['sunrise'],
	'Mckinneya': "",
	'Mckinneyi': vricJSON['sunrise'],
	'Mansfi': vricJSON['sunrise'],
	'Darelimaani': vricJSON['sunrise'],
	'dncfwi': vricJSON['sunrise'],
	'isda': "",
	'isdi': vricJSON['sunrise'],
	'ialfmi': vricJSON['sunrise'],
	'ialfma': "",
	'icopi': vricJSON['sunrise'],
	'icopa': "",
}
allDhur = {
	'ID': 3,
	'VRICi': vricJSON['duhrIqamah'],
	'ICIi': iciIqamahTimings[1].text,
	'ICIa': iciAdhanTimings[3].text,
	'ICFi': icfIqamahTimings[2].text,
	'IACCi': iaccDprayer,
	'IANTi': iantIqamahTimings[7].text,
	'EPICi': epicIqamahTimings[4].text,
	'Body': "Dhur: ",
	'VRICa': vricJSON['duhrAdhan'],
	'IANTa': iantIqamahTimings[6].text,
	'EPICa': epicIqamahTimings[3].text,
	'ICFa': icfAdhanTimings[2].text,
	'Allena' : aallenDprayer,
	'Alleni' : iallenDprayer,
	'ICSi' : icsIqamahTimings[2].text,
	'ICSa' : icsAdhanTimings[2].text,
	'MMi' : mmIqamahTimings[3].text,
	'Mici' : micIqamahTimings[1].text,
	'MYaseena' : amyaseenDprayer,
	'MYaseeni' : imyaseenDprayer,
	'Mckinneya': Mckinneyd,
	'Mckinneyi': mckinneyIqamahTiming[8].text,
	'Mansfi': mansfIqamahTiming[1].text,
	'Darelimaani': darelimanIqamahTimings[3].text,
	'dncfwi': dncfwDprayer,
	'isda': isdIqamahTimings[11].text,
	'isdi': isdIqamahTimings[12].text,
	'ialfmi': ialfmIqamahTimings[2].text,
	'ialfma': ialfmAdhanTimings[2].text,
	'icopi': icopIqamahTimings[2].text,
	'icopa': icopAdhanTimings[2].text,
}
allAsr = {
	'ID': 4,
	'VRICi': vricJSON['asrIqamah'],
	'ICIi': iciIqamahTimings[2].text,
	'ICIa': iciAdhanTimings[5].text,
	'ICFi': icfIqamahTimings[3].text,
	'IACCi': iaccAprayer,
	'IANTi': iantIqamahTimings[11].text,
	'EPICi': epicIqamahTimings[6].text,
	'Body': "Asr: ",
	'VRICa': vricJSON['asrAdhan'],
	'IANTa': iantIqamahTimings[10].text,
	'EPICa': epicIqamahTimings[5].text,
	'ICFa': icfAdhanTimings[3].text,
	'Allena' : aallenAprayer,
	'Alleni' : iallenAprayer,
	'ICSi' : icsIqamahTimings[3].text,
	'ICSa' : icsAdhanTimings[3].text,
	'MMi' : mmIqamahTimings[5].text,
	'Mici' : micIqamahTimings[2].text,
	'MYaseena' : amyaseenAprayer,
	'MYaseeni' : imyaseenAprayer,
	'Mckinneya': Mckinneya,
	'Mckinneyi': mckinneyIqamahTiming[11].text,
	'Mansfi': mansfIqamahTiming[3].text,
	'Darelimaani': darelimanIqamahTimings[7].text,
	'dncfwi': dncfwAprayer,
	'isda': isdIqamahTimings[14].text,
	'isdi': isdIqamahTimings[15].text,
	'ialfmi': ialfmIqamahTimings[3].text,
	'ialfma': ialfmAdhanTimings[3].text,
	'icopi': icopIqamahTimings[3].text,
	'icopa': icopAdhanTimings[3].text,

}
allMaghrib = {
	'ID': 5,
	'VRICi': vricJSON['maghribIqamah'],
	'ICIi': iciIqamahTimings[3].text,
	'ICFi': icfIqamahTimings[4].text,
	'ICIa': iciAdhanTimings[7].text,
	'IACCi': iaccMprayer,
	'IANTi': iantIqamahTimings[15].text,
	'EPICi': epicIqamahTimings[8].text,
	'Body': "Maghrib: ",
	'VRICa': vricJSON['maghribAdhan'],
	'IANTa': iantIqamahTimings[14].text,
	'EPICa': epicIqamahTimings[7].text,
	'ICFa': icfAdhanTimings[4].text,
	'Allena' : aallenMprayer,
	'Alleni' : iallenMprayer,
	'ICSi' : icsIqamahTimings[4].text,
	'ICSa' : icsAdhanTimings[4].text,
	'MMi' : mmIqamahTimings[7].text,
	'Mici' : micIqamahTimings[3].text,
	'MYaseena' : amyaseenMprayer,
	'MYaseeni' : imyaseenMprayer,
	'Mckinneya': Mckinneym,
	'Mckinneyi': mckinneyIqamahTiming[14].text,
	'Mansfi': mansfIqamahTiming[5].text,
	'Darelimaani': darelimanIqamahTimings[9].text,
	'dncfwi': dncfwMprayer,
	'isda': isdIqamahTimings[17].text,
	'isdi': isdIqamahTimings[18].text,
	'ialfmi': ialfmIqamahTimings[4].text,
	'ialfma': ialfmAdhanTimings[4].text,
	'icopi': icopIqamahTimings[4].text,
	'icopa': icopAdhanTimings[4].text,

}
allIsha = {
	'ID': 6,
	'VRICi': vricJSON['ishaIqamah'],
	'ICIi': iciIqamahTimings[4].text,
	'ICIa': iciAdhanTimings[9].text,
	'ICFi': icfIqamahTimings[5].text,
	'IACCi': iaccIprayer,
	'IANTi': iantIqamahTimings[19].text,
	'EPICi': epicIqamahTimings[10].text,
	'Body': "Isha: ",
	'VRICa': vricJSON['ishaAdhan'],
	'IANTa': iantIqamahTimings[18].text,
	'EPICa': epicIqamahTimings[9].text,
	'ICFa': icfAdhanTimings[5].text,
	'Allena' : aallenIprayer,
	'Alleni' : iallenIprayer,
	'ICSi' : icsIqamahTimings[5].text,
	'ICSa' : icsAdhanTimings[5].text,
	'MMi' : mmIqamahTimings[9].text,
	'Mici' : micIqamahTimings[4].text,	
	'MYaseena' : amyaseenIprayer,
	'MYaseeni' : imyaseenIprayer,
	'Mckinneya': Mckinneyi,
	'Mckinneyi': mckinneyIqamahTiming[17].text,
	'Mansfi': mansfIqamahTiming[7].text,
	'Darelimaani': darelimanIqamahTimings[11].text,
	'dncfwi': dncfwIprayer,
	'isda': isdIqamahTimings[20].text,
	'isdi': isdIqamahTimings[21].text,
	'ialfmi': ialfmIqamahTimings[5].text,
	'ialfma': ialfmAdhanTimings[5].text,
	'icopi': icopIqamahTimings[5].text,
	'icopa': icopAdhanTimings[5].text,


}

outputer = [allFajr, allSunrise, allDhur, allAsr, allMaghrib, allIsha]
z = json.dumps(outputer)
with open('allData.json', 'w') as outfile:
	json.dump(outputer,outfile, indent=2)	
