__author__ = 'elikary'

'''


 QUITO
==============
'''
import couchdb
import sys
import urllib2
import json
import textblob
from pylab import *

from couchdb import view

URL = 'localhost'
db_name = 'croacia'


'''========couchdb'=========='''
server = couchdb.Server('http://'+URL+':5984/')  #('http://245.106.43.184:5984/') poner la url de su base de datos
try:
    print db_name
    db = server[db_name]
    print 'success'

except:
    sys.stderr.write("Error: DB not found. Closing...\n")
    sys.exit()



url = 'http://127.0.0.1:5984/croacia/_design/tweets/_view/vista_croacia15'
req = urllib2.Request(url)
f = urllib2.urlopen(req)

d = json.loads(f.read())

archivo = open("/home/usrkap/Desktop/sam.txt","a") #opens file with name of "test.txt"
cont_positives = 0
cont_negatives = 0
cont_neutrals = 0
cont_total = 0


for x in d['rows']:
    a = x['value']
    texto_tweet = textblob.TextBlob(a)

    auc = ''

    if texto_tweet.sentiment.polarity > 0:
        aux = a + ';positive'
        cont_positives = cont_positives + 1
    elif texto_tweet.sentiment.polarity < 0:
        aux = a + ';negative'
        cont_negatives = cont_negatives + 1
    else:
        aux = a + ';neutral'
        cont_neutrals = cont_neutrals + 1

    archivo.write(str((aux.encode("utf-8") + "\n")))
    cont_total = cont_total + 1

archivo.close()

print ("total: " + str(cont_total))
print ("positives: " + str(cont_positives))
print ("negatives: " + str(cont_negatives))
print ("neutrals: " + str(cont_neutrals))


# make a square figure and axesfigure(1, figsize=(8,8))# tamanio de figura
ax = axes([0, 0, 0.9, 0.9])# donde esta la figura ancho alto etc..
#----------------------------------------------------------------------
labels = 'Positivos ', 'Negativos', 'Neutrales '#nomre de los datos
fracs = [cont_positives,cont_negatives,cont_neutrals]#datos a graficar
#----------------------------------------------------------------------
explode=(0, 0.1, 0)#exposicion de uno de los datos segun donde se encuentra
#tipo de grafico(datos,exposicion, titulos de los datos, nose,sombras true o false
pie(fracs, explode=explode,labels=labels, autopct='%10.0f%%', shadow=True)
legend()
title('Evaluacion de Sentimientos Tweets Croacia 15', bbox={'facecolor':'0.6', 'pad':5})

savefig("tweets_sentiments_ny.png")
show()#mostrar grafico


f.close()
