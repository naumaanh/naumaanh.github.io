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

iciR = requests.get(iciURL)
vricR = requests.get(vricURL)
iantR = requests.get(iantURL, headers=header).text
epicR = requests.get(epicURL)
iaccR = requests.get(iaccURL)
icfR = requests.get(icfURL)
allenR = requests.get(allenURL, headers=header).text
icsR = requests.get(icsURL)

iciHTML = iciR.text
vricHTML = vricR.text
#iantHTML = urlopen(iantR).read()
epicHTML = epicR.text
iaccHTML = iaccR.text
icfHTML = icfR.text
#allenHTML = allenR.text
icsHTML = icsR.text

icisoup = BeautifulSoup(iciHTML, "html.parser")
vricsoup = BeautifulSoup(vricHTML, "html.parser")
iantsoup = BeautifulSoup(iantR, "html.parser")
epicsoup = BeautifulSoup(epicHTML, "html.parser")
iaccsoup = BeautifulSoup(iaccHTML, "html.parser")
icfsoup = BeautifulSoup(icfHTML, "html.parser")
allensoup = BeautifulSoup(allenR, "html.parser")
icssoup = BeautifulSoup(icsHTML, "html.parser")


#SOUTHLAKE MASJID
icsIqamahTimings = icssoup.findAll('prayer_iqama_div')
icsAdhanTimings = icssoup.findAll('prayer_azaan_div')

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
	'FajrBody': "Fajr: ",
	'Body': "Fajr: ",
	'VRICa' : vricJSON['fajrAdhan'],
	'IANTa' : iantIqamahTimings[2].text,
	'EPICa' : epicIqamahTimings[0].text,
	'ICFa': icfAdhanTimings[1].text,
	'Allena' : aallenFprayer,
	'Alleni' : iallenFprayer,
	'ICFi' : icfIqamahTimings[1].text,
	'ICFa' : icfAdhanTimings[1].text,

}
allDhur = {
	'ID': 2,
	'VRICi': vricJSON['duhrIqamah'],
	'ICIi': iciIqamahTimings[1].text,
	'ICIa': iciAdhanTimings[3].text,
	'ICFi': icfIqamahTimings[2].text,
	'IACCi': iaccDprayer,
	'IANTi': iantIqamahTimings[7].text,
	'EPICi': epicIqamahTimings[4].text,
	'DhurBody': "Dhur: ",
	'Body': "Dhur: ",
	'VRICa': vricJSON['duhrAdhan'],
	'IANTa': iantIqamahTimings[6].text,
	'EPICa': epicIqamahTimings[3].text,
	'ICFa': icfAdhanTimings[2].text,
	'Allena' : aallenDprayer,
	'Alleni' : iallenDprayer,
	'ICFi' : icfIqamahTimings[2].text,
	'ICFa' : icfAdhanTimings[2].text,

}
allAsr = {
	'ID': 3,
	'VRICi': vricJSON['asrIqamah'],
	'ICIi': iciIqamahTimings[2].text,
	'ICIa': iciAdhanTimings[5].text,
	'ICFi': icfIqamahTimings[3].text,
	'IACCi': iaccAprayer,
	'IANTi': iantIqamahTimings[11].text,
	'EPICi': epicIqamahTimings[6].text,
	'AsrBody': "Asr: ",
	'Body': "Asr: ",
	'VRICa': vricJSON['asrAdhan'],
	'IANTa': iantIqamahTimings[10].text,
	'EPICa': epicIqamahTimings[5].text,
	'ICFa': icfAdhanTimings[3].text,
	'Allena' : aallenAprayer,
	'Alleni' : iallenAprayer,
	'ICFi' : icfIqamahTimings[3].text,
	'ICFa' : icfAdhanTimings[3].text,

}
allMaghrib = {
	'ID': 4,
	'VRICi': vricJSON['maghribIqamah'],
	'ICIi': iciIqamahTimings[3].text,
	'ICFi': icfIqamahTimings[4].text,
	'ICIa': iciAdhanTimings[7].text,
	'IACCi': iaccMprayer,
	'IANTi': iantIqamahTimings[15].text,
	'EPICi': epicIqamahTimings[8].text,
	'MaghribBody': "Maghrib: ",
	'Body': "Maghrib: ",
	'VRICa': vricJSON['maghribAdhan'],
	'IANTa': iantIqamahTimings[14].text,
	'EPICa': epicIqamahTimings[7].text,
	'ICFa': icfAdhanTimings[4].text,
	'Allena' : aallenMprayer,
	'Alleni' : iallenMprayer,
	'ICFi' : icfIqamahTimings[4].text,
	'ICFa' : icfAdhanTimings[4].text,

}
allIsha = {
	'ID': 5,
	'VRICi': vricJSON['ishaIqamah'],
	'ICIi': iciIqamahTimings[4].text,
	'ICIa': iciAdhanTimings[9].text,
	'ICFi': icfIqamahTimings[5].text,
	'IACCi': iaccIprayer,
	'IANTi': iantIqamahTimings[19].text,
	'EPICi': epicIqamahTimings[10].text,
	'IshaBody': "Isha: ",
	'Body': "Isha: ",
	'VRICa': vricJSON['ishaAdhan'],
	'IANTa': iantIqamahTimings[18].text,
	'EPICa': epicIqamahTimings[9].text,
	'ICFa': icfAdhanTimings[5].text,
	'Allena' : aallenIprayer,
	'Alleni' : iallenIprayer,
	'ICFi' : icfIqamahTimings[5].text,
	'ICFa' : icfAdhanTimings[5].text,

}


outputer = [allFajr, allDhur, allAsr, allMaghrib, allIsha]
z = json.dumps(outputer)
with open('allData.json', 'w') as outfile:
	json.dump(outputer,outfile, indent=2)	