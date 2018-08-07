# ProyectoBiMundial-
El  análisis  de  sentimiento  utiliza  el  procesamiento  de  lenguaje  natural,  análisis  de  texto  y  lingüística 
computacional  para  identificar  y  extraer  información  subjetiva;  por  ende,  está  relacionado  con  la 
sociología  en  cuanto  a  las  emociones  y  sentimientos  y
a  que  éstos  son  a  menudo  parte  del  proceso  de 
toma de decisiones de una persona.  
En este sentido, se  ha escogido realizar el análisis de opinión pública utilizando datos de Twitter de los 
países
que participaron en el mundial de futbol 2018

#Objetivo General
Implementar e investigar el funcionamiento de un clasificador de sentimientos utilizando los algoritmos 
de aprendizaje vistos en clase y los datos recolectados de Twitter para identificar tendencias de opinión 
en los 20 países qu
e participaron en el mundial a partir del 28 de junio del 2018.

#Objetivos específicos:

Crear  un  clasificador  de  sentimiento en  inglés  utilizando  datos 
extraídos
de  Twitter  para  minar 
opinión pública en los siguientes 
países
: argentina, belgica, brasil, co
lombia, croacia, dinamarca, 
espania,  francia,  inglaterra,  japon,  mexico,  panama,  polonia,  portugal,  rusia,  senegal,  suecia, 
suiza, tunez, uruguay


Identificar y seleccionar las herramientas necesarias para procesar y analizar datos provenientes 
de Twitter

Método

En este proyecto realizamos una recopilación de datos del mundial mediante los tweets, para ello utilizamos la Api de twitter la cual nos permité recolectar los tweets. A continuacion guardamos los tweets en una base de datos en nuestro caso couchDB en donde filtraremos cada uno de los datos por medio del idioma Inglés y sin emoticones ademas de Hagshtags referidos al mundial 

• Resultados
Los resultados seran presentados en gráficas las cuales se encuentran en las respectivas carpetas, se realizaron analisis de sentimientos para saber que aceptacion tuvo el mundial en cada respectivo pais, aparte de clasificar los tweets por dia y por lugar y por fecha de partido .


• Conclusiones y trabajo futuro
Podemos visualizar que el mundial tuvo una gran acogida por parte de los paises participantes a pesar de que existe una gran diferencia con respecto a la cantidad de tweets tomados por cada país.

Podemos concluir que el analisis de datos nos permite obtener información importante y saber que tendencias son las que estan en auge 

A futuro podemos realizar mas investigaciones sobre la información adquerida y podemos filtrarla de manera más óptimas, el ánalisis de informacion siempre nos permitira realizar mejoras.


• Apéndice: instrucciones de instalación y funcionamiento

Herramientas

    CouchDB
    Phyton (lenguaje de programación)
    VMware Workstation
    Sistema operativo Ubuntu 16.04.1
    
    
    Instalación
CouchDB
1.	Instalar Apache en Ubuntu
sudo apt-get install apache2 -y

2.	Iniciar el servidor web Apache y habilitarlo para iniciar junto a el tiempo de arranque del sistema con el siguiente comando:
sudo systemctl start apache2
sudo systemctl enable apache2
3.	Instalar Apache CouchDB en Ubuntu
sudo apt-get update -y
sudo apt-get install couchdb -y
4.	Una vez instalado, ejecutamos las siguientes líneas para iniciar el servicio y habilitarlo al arranque de Ubuntu 
sudo systemctl start couchdb
sudo systemctl enable couchdb
5.	Accedemos a Apache CouchDB en Ubuntu
http://IP:5984/_utils/


Instalación de librerias :
pip install numpy
install matplotlib
pip install -U textblob
python -m textblob.download_corpora



