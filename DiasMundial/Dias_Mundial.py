import re
import couchdb
import sys
import urllib2
import json
import textblob
import emoji
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from couchdb import view
from textblob import TextBlob


def vistas(url):
    req = urllib2.Request(url)
    f = urllib2.urlopen(req)
    d = json.loads(f.read())
    return d

rusia=vistas('http://127.0.0.1:5984/rusia/_design/tweets/_view/vista_rusia15')
rusia=vistas('http://127.0.0.1:5984/rusia/_design/tweets/_view/vista_rusia14')
rusia=vistas('http://127.0.0.1:5984/rusia/_design/tweets/_view/vista_rusia11')
rusia=vistas('http://127.0.0.1:5984/rusia/_design/tweets/_view/vista_rusia10')
francia=vistas('http://127.0.0.1:5984/francia/_design/tweets/_view/vista_francia15')
croacia=vistas('http://127.0.0.1:5984/croacia/_design/tweets/_view/vista_croacia15')
belgica=vistas('http://127.0.0.1:5984/belgica/_design/belgica10/_view/vista_belgica10')
francia=vistas('http://127.0.0.1:5984/francia/_design/tweets/_view/vista_francia')
belgica=vistas('http://127.0.0.1:5984/belgica/_design/belgica14/_view/vista_belgica14')
inglaterra=vistas('http://127.0.0.1:5984/inglaterra/_design/tweets/_view/vista_inglaterra14')


stmiento=""
contadorfecha=[0,0,0,0]


def give_emoji_free_text(text):
    allchars = [str for str in text.decode('utf-8')]
    emoji_list = [c for c in allchars if c in emoji.UNICODE_EMOJI]
    clean_text = ' '.join([str for str in text.decode('utf-8').split() if not any(i in str for i in emoji_list)])
    return clean_text

listafecha=[]
listaText=[]

for x in francia['rows']:
    hora=x['key']
    text=x['value']
    listafecha.append(hora)
    listaText.append(text)

for x in belgica['rows']:
    hora=x['key']
    text=x['value']
    listafecha.append(hora)
    listaText.append(text)


for y in rusia['rows']:
    hora=y['key']
    text=y['value']
    listafecha.append(hora)
    listaText.append(text)

for z in croacia['rows']:
    hora=z['key']
    text=z['value']
    listafecha.append(hora)
    listaText.append(text)

for z in inglaterra['rows']:
    hora=z['key']
    text=z['value']
    listafecha.append(hora)
    listaText.append(text)



for q in range(len(listaText)):
		
		if "10" in listafecha[q]:
			contadorfecha[0]=contadorfecha[0]+1
		elif "11" in listafecha[q]:
			contadorfecha[1]=contadorfecha[1]+1
		elif "14" in listafecha[q]:
			contadorfecha[2]=contadorfecha[2]+1
		elif "15" in listafecha[q]:
			contadorfecha[3]=contadorfecha[3]+1
		
print contadorfecha
dias=('10','11','14','15')
y=np.arange(len(dias))
tweets=contadorfecha
plt.bar(y,tweets,align='center',alpha=0.6)
plt.xticks(y,dias)
plt.xlabel('Horas del dia \n')
plt.ylabel('Cantidad de tweets \n')
plt.title('Tweets por dia \n')
plt.show()
