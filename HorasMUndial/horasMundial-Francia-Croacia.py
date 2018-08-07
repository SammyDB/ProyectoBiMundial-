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
francia=vistas('http://127.0.0.1:5984/francia/_design/tweets/_view/vista_francia15')
croacia=vistas('http://127.0.0.1:5984/croacia/_design/tweets/_view/vista_croacia15')

stmiento=""
contadorhoras=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


def give_emoji_free_text(text):
    allchars = [str for str in text.decode('utf-8')]
    emoji_list = [c for c in allchars if c in emoji.UNICODE_EMOJI]
    clean_text = ' '.join([str for str in text.decode('utf-8').split() if not any(i in str for i in emoji_list)])
    return clean_text

listaHora=[]
listaText=[]

for x in francia['rows']:
    hora=x['key']
    text=x['value']
    listaHora.append(hora)
    listaText.append(text)

for y in rusia['rows']:
    hora=y['key']
    text=y['value']
    listaHora.append(hora)
    listaText.append(text)

for z in croacia['rows']:
    hora=z['key']
    text=z['value']
    listaHora.append(hora)
    listaText.append(text)



for q in range(len(listaText)):
		
		if "07" in listaHora[q]:
			contadorhoras[0]=contadorhoras[0]+1
		elif "08" in listaHora[q]:
			contadorhoras[1]=contadorhoras[1]+1
		elif "09" in listaHora[q]:
			contadorhoras[2]=contadorhoras[2]+1
		elif "10" in listaHora[q]:
			contadorhoras[3]=contadorhoras[3]+1
		elif "11" in listaHora[q]:
			contadorhoras[4]=contadorhoras[4]+1
		elif "12" in listaHora[q]:
			contadorhoras[5]=contadorhoras[5]+1	
		elif "13" in listaHora[q]:
			contadorhoras[6]=contadorhoras[6]+1
		elif "14" in listaHora[q]:
			contadorhoras[7]=contadorhoras[7]+1		
		elif "15" in listaHora[q]:
			contadorhoras[8]=contadorhoras[8]+1				
		elif "16" in listaHora[q]:
			contadorhoras[9]=contadorhoras[9]+1
		elif "17" in listaHora[q]:
			contadorhoras[10]=contadorhoras[10]+1
		elif "18" in listaHora[q]:
			contadorhoras[11]=contadorhoras[11]+1
		elif "19" in listaHora[q]:
			contadorhoras[12]=contadorhoras[12]+1
		elif "20" in listaHora[q]:
			contadorhoras[13]=contadorhoras[13]+1
		elif "21" in listaHora[q]:
			contadorhoras[14]=contadorhoras[14]+1
		elif "22" in listaHora[q]:
			contadorhoras[15]=contadorhoras[15]+1
		elif "23" in listaHora[q]:
			contadorhoras[16]=contadorhoras[16]+1
		elif "24" in listaHora[q]:
			contadorhoras[17]=contadorhoras[17]+1

print contadorhoras
dias=('7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24')
y=np.arange(len(dias))
tweets=contadorhoras
plt.bar(y,tweets,align='center',alpha=0.6)
plt.xticks(y,dias)
plt.xlabel('Horas del dia \n')
plt.ylabel('Cantidad de tweets \n')
plt.title('Tweets por hora \n')
plt.show()
