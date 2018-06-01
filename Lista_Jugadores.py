import urllib,urllib2
import requests
import json
import unicodedata
import html5lib
from bs4 import BeautifulSoup as bs
import pprint
import warnings
import pandas as pd
from pprint import pprint as pp

warnings.filterwarnings("ignore")


def check_word(cadena):
    s = ''.join((c for c in unicodedata.normalize('NFD', unicode(cadena)) if unicodedata.category(c) != 'Mn'))
    try:
        return s.decode()
    except:
        s.encode('ascii', errors='replace')


#### Paginas interesantes
## http://www.football-lineups.com/tourn/World_Cup_Russia_2018/
## http://www.goal.com/en-us/world-cup/table/70excpe1synn9kadnbppahdn7
## http://especiales.marca.com/mundial-rusia-2018/selecciones/listas.html

############################################
# Obtenemos la lista de selecciones (enlaces)
url_lista_alineaciones = 'http://especiales.marca.com/mundial-rusia-2018/selecciones/listas.html'
s = requests.Session()
html_lista = s.get(url_lista_alineaciones).text
bs_lista = bs(html_lista,"html.parser")

Teams_links=[]
for team in bs_lista.find_all('a'):
    if 'img' in team.__str__():
        Teams_links.append(str(team.get('href')))

print Teams_links
print len(Teams_links)
s.close()
############################################


s = requests.Session()
url_seleccion = 'http://especiales.marca.com/mundial-rusia-2018/selecciones/' + Teams_links[0]

html2 = s.get(url_lista_alineaciones).text

html3 = s.get(url_seleccion).text
bs_seleccion = bs(html3,"html.parser")

#print html2
# print bs_lista.find_all('li',attrs={'class':'seleccion'})[0].find_all('li',attrs={'class': 'jugador'})[2].find_all('li',attrs={'class':'nombre'})[0].text
# Nombre del equipo
# print bs_lista.find_all('li',attrs={'class':'seleccion'})[0].find_all('h2')[0].text
# print bs_seleccion.find

Selecciones = {}
Listas = bs_lista.find_all('li',attrs={'class':'seleccion'})
info_seleccion = bs_seleccion.find_all('p',attrs={'class':'opinion2'})[3].text

print check_word(info_seleccion)
print type(info_seleccion)

##### Generamos diccionario de links {'Alemania': 'alemania.html', 'Arabia-Saudi': 'arabia-saudi.html',....}
nombre_equipos=[str(check_word(i.find_all('a')[0].get('alt'))) for i in Listas]
equipos_links = {}
for equipo,link in zip(nombre_equipos,Teams_links):
    equipos_links[equipo] = link
#####


for team,link in zip(Listas,Teams_links):
    seleccion = str(check_word(team.find_all('h2')[0].text))
    Selecciones[seleccion]={'Jugadores':{}}
    # Once ideal
    url_seleccion = 'http://especiales.marca.com/mundial-rusia-2018/selecciones/' + link
    html_seleccion = s.get(url_seleccion).text
    bs_seleccion = bs(html_seleccion, "html.parser")
    info_seleccion = bs_seleccion.find_all('p', attrs={'class': 'opinion2'})[3].text
    # info_once_ideal = check_word(info_seleccion)
    print info_once_ideal
    for player in team.find_all('li',attrs={'class': 'jugador'}):
        # conseguimos info del html
        jugador = str(check_word(player.find_all('li',attrs={'class':'nombre'})[0].text))
        demarcacion = str(check_word(player.find_all('li',attrs={'class':'demarcacion'})[0].text))
        club =  str(check_word(player.find_all('li',attrs={'class':'equipo'})[0].text))
        # dorsal = str(check_word(player.find_all('li',attrs={'class':'dorsal'})[0].text))

        ## Comprobacion titularidad
        if jugador in info_once_ideal:
            titular = 1
        else:
            titular = 0


        # almacenamos info
        info_player = {'demarcacion':demarcacion, 'club':club,'titular':titular}
        Selecciones[seleccion]['Jugadores'][jugador]= info_player


# print Selecciones.keys()
# print len(Selecciones)
pp(Selecciones)



