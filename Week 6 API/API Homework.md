

```python
# Dependencies
import requests
import json
import pandas as pd
import numpy as np
import seaborn as sm
import openweathermapy.core as owm
import random 
from pprint import pprint
import matplotlib.pyplot as plt

from scipy.stats import sem
from config import api_key
from config import gkey
from citipy import citipy

weather_url = ("http://api.openweathermap.org/data/2.5/weather?appid=" + api_key + "&lat=")
goog_url = "https://maps.googleapis.com/maps/api/geocode/json"
```


```python
#generate random 500 random cities
cities_raw = []
citiespy = []

#Get convert random coordinates into nearest city
while len(cities_raw) < 1000:
    y = random.randint(-9000, 9000)
    z = random.randint(-18000, 18000)
    orig_city = (citipy.nearest_city(float(y/100), float(z/100)))
    if orig_city not in cities_raw:
        cities_raw.append(orig_city)

#Convert nearest city into city name
for city in cities_raw:
    name = city.city_name
    if name not in citiespy:
        citiespy.append(name)
len(citiespy)
```




    996




```python
#Convert unique cities back into geographic coordinates through Google API:
latitudes = []
longitudes = []
x=0

for city in citiespy:
    target_city = citiespy[x]
    params = {"address": target_city, "key": gkey}
    goog_city = requests.get(goog_url, params=params).json()
    try:
        lat = goog_city["results"][0]["geometry"]["location"]["lat"]
        latitudes.append(lat)
    except IndexError:
        pass
    try:
        lng = goog_city["results"][0]["geometry"]["location"]["lng"]
        longitudes.append(lng)
    except IndexError:
        pass
    x=x+1

len(longitudes)
```




    988




```python
#Fill in lists from API call
cities = []
cloudiness = []
country = []
date = []
humidity = []
max_temp = []
min_temp = []
wind_speed = []
lati = []
longi = []
counter = 1
x=0

while len(country) < 500:
    url = weather_url + str(latitudes[x]) + "&lon=" + str(longitudes[x])
    response = requests.get(url).json()
    try:
        country.append(response['sys']['country'])
        cities.append(response['name'])
        cloudiness.append(response['clouds']['all'])
        date.append(response['dt'])
        humidity.append(response['main']['humidity'])
        max_temp.append(response['main']['temp_max'])
        min_temp.append(response['main']['temp_min'])
        wind_speed.append(response['wind']['speed'])
        lati.append(response['coord']['lat'])
        longi.append(response['coord']['lon'])
    except KeyError:
        pass
    x=x+1
    print(f"Getting weather info for city# {counter}: {response['name']}")
    counter = counter + 1
```

    Getting weather info for city# 1: Bambous Virieux
    Getting weather info for city# 2: Bissora
    Getting weather info for city# 3: Makui
    Getting weather info for city# 4: Ushuaia
    Getting weather info for city# 5: Guizikeng
    Getting weather info for city# 6: Salekhard
    Getting weather info for city# 7: Luanda
    Getting weather info for city# 8: Flagstaff
    Getting weather info for city# 9: Kodiak
    Getting weather info for city# 10: Lorengau
    Getting weather info for city# 11: Walmer
    Getting weather info for city# 12: Margate
    Getting weather info for city# 13: Punta Arenas
    Getting weather info for city# 14: Bluff
    Getting weather info for city# 15: Gore
    Getting weather info for city# 16: Tiksi
    Getting weather info for city# 17: Coahuayana
    Getting weather info for city# 18: Mahebourg
    Getting weather info for city# 19: Busselton
    Getting weather info for city# 20: Albany
    Getting weather info for city# 21: Samarai
    Getting weather info for city# 22: De Waterkant
    Getting weather info for city# 23: Wanaka
    Getting weather info for city# 24: Narsaq
    Getting weather info for city# 25: Lipin Bor
    Getting weather info for city# 26: Tasiilaq
    Getting weather info for city# 27: Williamsburg
    Getting weather info for city# 28: Sao Filipe
    Getting weather info for city# 29: Atuona
    Getting weather info for city# 30: 
    Getting weather info for city# 31: Nybyen
    Getting weather info for city# 32: 
    Getting weather info for city# 33: Hilo
    Getting weather info for city# 34: Bredasdorp
    Getting weather info for city# 35: Puerto Ayora
    Getting weather info for city# 36: San Francisco County
    Getting weather info for city# 37: Ambon
    Getting weather info for city# 38: Mar del Plata
    Getting weather info for city# 39: Fort Dauphin
    Getting weather info for city# 40: Dongsheng
    Getting weather info for city# 41: Tulsa County
    Getting weather info for city# 42: Kruisfontein
    Getting weather info for city# 43: Almeirim
    Getting weather info for city# 44: Tabonuea Village
    Getting weather info for city# 45: Arraial do Cabo
    Getting weather info for city# 46: 
    Getting weather info for city# 47: Kapaa
    Getting weather info for city# 48: Cidreira
    Getting weather info for city# 49: Vaini
    Getting weather info for city# 50: Thinadhoo
    Getting weather info for city# 51: Bonavista
    Getting weather info for city# 52: Kenai
    Getting weather info for city# 53: Aguelmous
    Getting weather info for city# 54: Olho d’Agua
    Getting weather info for city# 55: Geraldton
    Getting weather info for city# 56: Kutum
    Getting weather info for city# 57: Zarzis
    Getting weather info for city# 58: Tura
    Getting weather info for city# 59: Chateauroux
    Getting weather info for city# 60: Municipio de Champerico
    Getting weather info for city# 61: Zheleznyaki
    Getting weather info for city# 62: Ittoqqortoormiit
    Getting weather info for city# 63: Hermanus
    Getting weather info for city# 64: State Circus
    Getting weather info for city# 65: Canitas de Felipe Pescador
    Getting weather info for city# 66: Barentu
    Getting weather info for city# 67: Neepawa
    Getting weather info for city# 68: Grande Riviere Sud Est
    Getting weather info for city# 69: Tulsa County
    Getting weather info for city# 70: Leawood
    Getting weather info for city# 71: Acapulco de Juarez
    Getting weather info for city# 72: Hithadhoo
    Getting weather info for city# 73: Nóutigos
    Getting weather info for city# 74: Tulsa County
    Getting weather info for city# 75: Khatanga
    Getting weather info for city# 76: 
    Getting weather info for city# 77: New York
    Getting weather info for city# 78: Barrow
    Getting weather info for city# 79: Sokol’niki
    Getting weather info for city# 80: Sortland
    Getting weather info for city# 81: Lompoc
    Getting weather info for city# 82: Saint-Philippe
    Getting weather info for city# 83: Baruun-Urt
    Getting weather info for city# 84: Dossor
    Getting weather info for city# 85: New Norfolk
    Getting weather info for city# 86: Nsanje
    Getting weather info for city# 87: Rikitea
    Getting weather info for city# 88: Belle Mare
    Getting weather info for city# 89: Beghleti
    Getting weather info for city# 90: Lakes Entrance
    Getting weather info for city# 91: Falefa
    Getting weather info for city# 92: Tiznit
    Getting weather info for city# 93: Hobart
    Getting weather info for city# 94: Puerto Armuelles
    Getting weather info for city# 95: Baoro
    Getting weather info for city# 96: Chokurdakh
    Getting weather info for city# 97: Victoria
    Getting weather info for city# 98: Weirton Heights
    Getting weather info for city# 99: McConnell AFB
    Getting weather info for city# 100: Bhainsdehi
    Getting weather info for city# 101: Yonabaru
    Getting weather info for city# 102: Entuziastov
    Getting weather info for city# 103: Buttonville
    Getting weather info for city# 104: Pangnirtung
    Getting weather info for city# 105: Upernavik
    Getting weather info for city# 106: Mombetsu
    Getting weather info for city# 107: Chah Bahar
    Getting weather info for city# 108: Surquillo
    Getting weather info for city# 109: Fiamah
    Getting weather info for city# 110: Avarua
    Getting weather info for city# 111: Tautira
    Getting weather info for city# 112: North Grosvenor Dale
    Getting weather info for city# 113: Langsa
    Getting weather info for city# 114: Curvelo
    Getting weather info for city# 115: Batagay
    Getting weather info for city# 116: Gigmoto
    Getting weather info for city# 117: Saudarkrokur
    Getting weather info for city# 118: 
    Getting weather info for city# 119: Andenes
    Getting weather info for city# 120: Vinukonda
    Getting weather info for city# 121: Macabuboni
    Getting weather info for city# 122: Biltine
    Getting weather info for city# 123: Capitan Pablo Lagerenza
    Getting weather info for city# 124: Kaohsiung
    Getting weather info for city# 125: Les Îles-de-la-Madeleine
    Getting weather info for city# 126: San Juan
    Getting weather info for city# 127: Turukhansk
    Getting weather info for city# 128: Qaanaaq
    Getting weather info for city# 129: Bilibino
    Getting weather info for city# 130: Yellowknife
    Getting weather info for city# 131: Los Angeles
    Getting weather info for city# 132: Kirovsk
    Getting weather info for city# 133: Kelyun’ya
    Getting weather info for city# 134: Gamvik
    Getting weather info for city# 135: London
    Getting weather info for city# 136: Cremona
    Getting weather info for city# 137: Eenhana
    Getting weather info for city# 138: Funafuti
    Getting weather info for city# 139: Mayenne
    Getting weather info for city# 140: Carnarvon
    Getting weather info for city# 141: Khorixas
    Getting weather info for city# 142: Ust-Nera
    Getting weather info for city# 143: Mason
    Getting weather info for city# 144: Utuloa
    Getting weather info for city# 145: Bhairab Bazar
    Getting weather info for city# 146: Krasnovishersk
    Getting weather info for city# 147: Belaya Gora
    Getting weather info for city# 148: Ubaporanga
    Getting weather info for city# 149: Kanel
    Getting weather info for city# 150: San Cristobal de Las Casas
    Getting weather info for city# 151: Bhanvad
    Getting weather info for city# 152: Fortuna
    Getting weather info for city# 153: Teofilo Otoni
    Getting weather info for city# 154: Petropavlovsk-Kamchatskiy
    Getting weather info for city# 155: Chumikan
    Getting weather info for city# 156: Catalina Foothills
    Getting weather info for city# 157: Talnakh
    Getting weather info for city# 158: Curup
    Getting weather info for city# 159: Basoko
    Getting weather info for city# 160: Beverly Hills
    Getting weather info for city# 161: Kukumu
    Getting weather info for city# 162: Francke
    Getting weather info for city# 163: Myoma
    Getting weather info for city# 164: Haines Junction
    Getting weather info for city# 165: Poti
    Getting weather info for city# 166: Dudinka
    Getting weather info for city# 167: San Jose
    Getting weather info for city# 168: Port Alfred
    Getting weather info for city# 169: Yelch - New Village
    Getting weather info for city# 170: Souillac
    Getting weather info for city# 171: Nemuro
    Getting weather info for city# 172: Gongzhuling
    Getting weather info for city# 173: Savannah Bight
    Getting weather info for city# 174: China Grove
    Getting weather info for city# 175: Saskylakh
    Getting weather info for city# 176: Washington, D. C.
    Getting weather info for city# 177: Vila Velha
    Getting weather info for city# 178: Markivka
    Getting weather info for city# 179: Lebu
    Getting weather info for city# 180: Tual
    Getting weather info for city# 181: Kahului
    Getting weather info for city# 182: Ponta do Sol
    Getting weather info for city# 183: Tuktoyaktuk
    Getting weather info for city# 184: Yaosai
    Getting weather info for city# 185: Dikson
    Getting weather info for city# 186: Mariental
    Getting weather info for city# 187: Rudnik
    Getting weather info for city# 188: Zhovtneve
    Getting weather info for city# 189: Maragogi
    Getting weather info for city# 190: Sokoto
    Getting weather info for city# 191: Spasskoye-Lutovinovo
    Getting weather info for city# 192: Ulladulla
    Getting weather info for city# 193: Kashechewan
    Getting weather info for city# 194: Sastamala
    Getting weather info for city# 195: Mariinsk
    Getting weather info for city# 196: San Rafael
    Getting weather info for city# 197: Kayasula
    Getting weather info for city# 198: Beringovskiy
    Getting weather info for city# 199: Ammon
    Getting weather info for city# 200: Racine
    Getting weather info for city# 201: Ribeira Grande
    Getting weather info for city# 202: Caras
    Getting weather info for city# 203: Shimoda
    Getting weather info for city# 204: Slatina
    Getting weather info for city# 205: Clyde River
    Getting weather info for city# 206: Ihlowerfehn
    Getting weather info for city# 207: Ancud
    Getting weather info for city# 208: Knysna
    Getting weather info for city# 209: Araguaina
    Getting weather info for city# 210: Redding
    Getting weather info for city# 211: Ólafsvík
    Getting weather info for city# 212: Pitimbu
    Getting weather info for city# 213: Sibolga
    Getting weather info for city# 214: Souran
    Getting weather info for city# 215: Anloga
    Getting weather info for city# 216: Bartlesville
    Getting weather info for city# 217: Ambilobe
    Getting weather info for city# 218: Dolinsk
    Getting weather info for city# 219: Ilulissat
    Getting weather info for city# 220: Worthington
    Getting weather info for city# 221: Lokossa
    Getting weather info for city# 222: Paamiut
    Getting weather info for city# 223: Koror State
    Getting weather info for city# 224: Sokolo
    Getting weather info for city# 225: Ponta Delgada (São José)
    Getting weather info for city# 226: Mogadishu
    Getting weather info for city# 227: Esperance
    Getting weather info for city# 228: Parish of Saint George
    Getting weather info for city# 229: Gialo
    Getting weather info for city# 230: Kayes
    Getting weather info for city# 231: Huanren
    Getting weather info for city# 232: Ust-Tsilma
    Getting weather info for city# 233: Mandalgovi
    Getting weather info for city# 234: Birjand
    Getting weather info for city# 235: Aş Şalālah al Jadīdah
    Getting weather info for city# 236: Tuatapere
    Getting weather info for city# 237: Kamsack
    Getting weather info for city# 238: Ventspils
    Getting weather info for city# 239: Morondava
    Getting weather info for city# 240: Blake
    Getting weather info for city# 241: Buraydah
    Getting weather info for city# 242: Anadyr
    Getting weather info for city# 243: Roald
    Getting weather info for city# 244: Sitka
    Getting weather info for city# 245: Bambanglipuro
    Getting weather info for city# 246: Medley
    Getting weather info for city# 247: Mandera
    Getting weather info for city# 248: Donggang
    Getting weather info for city# 249: Kota Belud
    Getting weather info for city# 250: Taungdwingyi
    Getting weather info for city# 251: Gary
    Getting weather info for city# 252: Kalabo
    Getting weather info for city# 253: Price
    Getting weather info for city# 254: East La Mirada
    Getting weather info for city# 255: Manaquiri
    Getting weather info for city# 256: Nioro Rufis
    Getting weather info for city# 257: Saldanha
    Getting weather info for city# 258: Broome
    Getting weather info for city# 259: Hamilton
    Getting weather info for city# 260: Baao
    Getting weather info for city# 261: Muisne
    Getting weather info for city# 262: Thunder Bay
    Getting weather info for city# 263: Fukien
    Getting weather info for city# 264: Safotu
    Getting weather info for city# 265: Zalantun
    Getting weather info for city# 266: Praia da Vitoria
    Getting weather info for city# 267: Nicoya
    Getting weather info for city# 268: Ahuimanu
    Getting weather info for city# 269: Oakland
    Getting weather info for city# 270: Pathein
    Getting weather info for city# 271: Ciudad Camargo
    Getting weather info for city# 272: Hue
    Getting weather info for city# 273: Karatau
    Getting weather info for city# 274: Anau
    Getting weather info for city# 275: Aklavik
    Getting weather info for city# 276: Teseney
    Getting weather info for city# 277: Acajutla
    Getting weather info for city# 278: Lumut
    Getting weather info for city# 279: Iqaluit
    Getting weather info for city# 280: Peabiru
    Getting weather info for city# 281: Shrewsbury
    Getting weather info for city# 282: Tlacote el Bajo
    Getting weather info for city# 283: Constitucion
    Getting weather info for city# 284: Jyväskylä
    Getting weather info for city# 285: Villa Tupac Amaru
    Getting weather info for city# 286: Payson
    Getting weather info for city# 287: Arlit
    Getting weather info for city# 288: Marion
    Getting weather info for city# 289: Ancun
    Getting weather info for city# 290: Naidong
    Getting weather info for city# 291: Alyangula
    Getting weather info for city# 292: Buttonville
    Getting weather info for city# 293: Atikokan
    Getting weather info for city# 294: Weining
    Getting weather info for city# 295: Coquimbo
    Getting weather info for city# 296: Llanos De Aridane (Los)
    Getting weather info for city# 297: Kloulklubed
    Getting weather info for city# 298: Seymchan
    Getting weather info for city# 299: San Patricio County
    Getting weather info for city# 300: Palmerston
    Getting weather info for city# 301: Sermersooq
    Getting weather info for city# 302: Severo-Kurilsk
    Getting weather info for city# 303: Kununurra
    Getting weather info for city# 304: Wulan
    Getting weather info for city# 305: Nelson Bay
    Getting weather info for city# 306: San Fernando de Monte Cristi
    Getting weather info for city# 307: Traralgon
    Getting weather info for city# 308: Msanga
    Getting weather info for city# 309: Kavieng
    Getting weather info for city# 310: Baykalovsk
    Getting weather info for city# 311: Bougouni
    Getting weather info for city# 312: Mutsu
    Getting weather info for city# 313: Antonio Enes
    Getting weather info for city# 314: Atasu
    Getting weather info for city# 315: Richards Bay
    Getting weather info for city# 316: Assaizal
    Getting weather info for city# 317: Sakaiminato
    Getting weather info for city# 318: Nazarovo
    Getting weather info for city# 319: Bonthe
    Getting weather info for city# 320: Sandur
    Getting weather info for city# 321: Paihia
    Getting weather info for city# 322: Thanh pho Bac Lieu
    Getting weather info for city# 323: Hambantota
    Getting weather info for city# 324: Udachnyy
    Getting weather info for city# 325: Mount Gambier
    Getting weather info for city# 326: Vestmannaeyjar
    Getting weather info for city# 327: Bandarbeyla
    Getting weather info for city# 328: Mopipi
    Getting weather info for city# 329: Gualeguay
    Getting weather info for city# 330: Aleksandrov Gay
    Getting weather info for city# 331: Shubarkuduk
    Getting weather info for city# 332: Itacoatiara
    Getting weather info for city# 333: Angra dos Reis
    Getting weather info for city# 334: Mil’kovo
    Getting weather info for city# 335: Petropavlovka
    Getting weather info for city# 336: Welkom
    Getting weather info for city# 337: Akron
    Getting weather info for city# 338: Meaford
    Getting weather info for city# 339: Sao Joao da Barra
    Getting weather info for city# 340: Cherdyn
    Getting weather info for city# 341: Ploemeur
    Getting weather info for city# 342: Zhuanghe
    Getting weather info for city# 343: Xinmin
    Getting weather info for city# 344: Stromness
    Getting weather info for city# 345: San Quintin
    Getting weather info for city# 346: Paradip Garh
    Getting weather info for city# 347: Kailua
    Getting weather info for city# 348: Katsuura
    Getting weather info for city# 349: Capim Grosso
    Getting weather info for city# 350: Dingle
    Getting weather info for city# 351: Omboue
    Getting weather info for city# 352: Barishal
    Getting weather info for city# 353: Lubbock
    Getting weather info for city# 354: Taunggyi
    Getting weather info for city# 355: Chicago
    Getting weather info for city# 356: Medellin
    Getting weather info for city# 357: Stanica Zelenikovo
    Getting weather info for city# 358: Baie-Comeau
    Getting weather info for city# 359: Fairbanks
    Getting weather info for city# 360: Saint Paul
    Getting weather info for city# 361: Tamatangga
    Getting weather info for city# 362: Alugan
    Getting weather info for city# 363: Umea
    Getting weather info for city# 364: Carutapera
    Getting weather info for city# 365: Cleora
    Getting weather info for city# 366: Concarneau
    Getting weather info for city# 367: Chegdomyn
    Getting weather info for city# 368: Beloha
    Getting weather info for city# 369: Yulara
    Getting weather info for city# 370: Kokstad
    Getting weather info for city# 371: Rawannawi Village
    Getting weather info for city# 372: Maylands
    Getting weather info for city# 373: Longyearbyen
    Getting weather info for city# 374: Atar
    Getting weather info for city# 375: Vista Alegre
    Getting weather info for city# 376: Marondera
    Getting weather info for city# 377: Teriberka
    Getting weather info for city# 378: Verkhnyaya Inta
    Getting weather info for city# 379: Alta Floresta
    Getting weather info for city# 380: Sheridan
    Getting weather info for city# 381: Imbituba
    Getting weather info for city# 382: Krasnosel’kup
    Getting weather info for city# 383: Svarstad
    Getting weather info for city# 384: Ewa Beach
    Getting weather info for city# 385: Nizhniy Bestyakh
    Getting weather info for city# 386: Serui
    Getting weather info for city# 387: Georgiyevka
    Getting weather info for city# 388: Farakka
    Getting weather info for city# 389: Makakilo
    Getting weather info for city# 390: Ōhama
    Getting weather info for city# 391: Maroantsetra
    Getting weather info for city# 392: Kamenka
    Getting weather info for city# 393: Muzhi
    Getting weather info for city# 394: Diamantina
    Getting weather info for city# 395: Vadamadurai
    Getting weather info for city# 396: Ipeko
    Getting weather info for city# 397: Maungatapere
    Getting weather info for city# 398: Adrar
    Getting weather info for city# 399: Jinjiang
    Getting weather info for city# 400: Lokoja
    Getting weather info for city# 401: Safotu
    Getting weather info for city# 402: Swellendam
    Getting weather info for city# 403: Baykit
    Getting weather info for city# 404: Northern Province
    Getting weather info for city# 405: Pelabuhanratu
    Getting weather info for city# 406: Bargaal
    Getting weather info for city# 407: Kaeo
    Getting weather info for city# 408: Schaumburg
    Getting weather info for city# 409: Sesheke
    Getting weather info for city# 410: Puerto Escondido
    Getting weather info for city# 411: Bang Krathum
    Getting weather info for city# 412: Sumenep
    Getting weather info for city# 413: Nouadhibou
    Getting weather info for city# 414: Taoudenni
    Getting weather info for city# 415: 
    Getting weather info for city# 416: Tsiombe
    Getting weather info for city# 417: Egvekinot
    Getting weather info for city# 418: Eriko Village
    Getting weather info for city# 419: Daru
    Getting weather info for city# 420: Vila Franca do Campo
    Getting weather info for city# 421: Kiama
    Getting weather info for city# 422: Ouargla
    Getting weather info for city# 423: Seattle
    Getting weather info for city# 424: Rorvik
    Getting weather info for city# 425: Lagoa
    Getting weather info for city# 426: Kamaishi
    Getting weather info for city# 427: Hardrock
    Getting weather info for city# 428: Mount Hagen
    Getting weather info for city# 429: Vardo
    Getting weather info for city# 430: Tezu
    Getting weather info for city# 431: Elizabeth City
    Getting weather info for city# 432: Luderitz
    Getting weather info for city# 433: Orebro
    Getting weather info for city# 434: Yauya
    Getting weather info for city# 435: Poronaysk
    Getting weather info for city# 436: Pyt-Yakh
    Getting weather info for city# 437: Klaksvik
    Getting weather info for city# 438: Hami
    Getting weather info for city# 439: Borough of Torbay
    Getting weather info for city# 440: Te Anau
    Getting weather info for city# 441: Proletariy
    Getting weather info for city# 442: Havre-Saint-Pierre
    Getting weather info for city# 443: Lubukbergalung
    Getting weather info for city# 444: Springbok
    Getting weather info for city# 445: Le Vauclin
    Getting weather info for city# 446: Binika
    Getting weather info for city# 447: Weragampita
    Getting weather info for city# 448: Norman Wells
    Getting weather info for city# 449: Atambua
    Getting weather info for city# 450: Bilma
    Getting weather info for city# 451: Pacific Grove
    Getting weather info for city# 452: New York
    Getting weather info for city# 453: Puerto Colombia
    Getting weather info for city# 454: Malaya Vishera
    Getting weather info for city# 455: Ahipara
    Getting weather info for city# 456: Deputatskiy
    Getting weather info for city# 457: Blue Springs
    Getting weather info for city# 458: Nanortalik
    Getting weather info for city# 459: Lavrentiya
    Getting weather info for city# 460: Novopokrovka
    Getting weather info for city# 461: Parish of Saint Mary
    Getting weather info for city# 462: Sinegorskiy
    Getting weather info for city# 463: Gazanjyk
    Getting weather info for city# 464: Turayf
    Getting weather info for city# 465: Wichita
    Getting weather info for city# 466: Yichun
    Getting weather info for city# 467: Port Victoria
    Getting weather info for city# 468: Minns
    Getting weather info for city# 469: Tonkino
    Getting weather info for city# 470: Piney Point Village
    Getting weather info for city# 471: Teguise
    Getting weather info for city# 472: Poum
    Getting weather info for city# 473: Caravelas
    Getting weather info for city# 474: Pangody
    Getting weather info for city# 475: Beachburg
    Getting weather info for city# 476: Issia
    Getting weather info for city# 477: Evensk
    Getting weather info for city# 478: Lakatoro
    Getting weather info for city# 479: Biscarrosse
    Getting weather info for city# 480: Eyl
    Getting weather info for city# 481: Bom Sucesso
    Getting weather info for city# 482: Pleasanton
    Getting weather info for city# 483: Pasighat
    Getting weather info for city# 484: Walvis Bay
    Getting weather info for city# 485: Vyartsilya
    Getting weather info for city# 486: Lufilufi
    Getting weather info for city# 487: Port Blair
    Getting weather info for city# 488: Saint George
    Getting weather info for city# 489: Svetlyy
    Getting weather info for city# 490: Oranjemund
    Getting weather info for city# 491: Uvat
    Getting weather info for city# 492: Zharkent
    Getting weather info for city# 493: Andra
    Getting weather info for city# 494: Nome
    Getting weather info for city# 495: Cabo San Lucas
    Getting weather info for city# 496: Carauari
    Getting weather info for city# 497: San Miguel de Tucuman
    Getting weather info for city# 498: Khandbari
    Getting weather info for city# 499: Haapiti
    Getting weather info for city# 500: Visby
    Getting weather info for city# 501: Kavaratti
    Getting weather info for city# 502: Tigil
    Getting weather info for city# 503: Mugur-Aksy
    Getting weather info for city# 504: Barra do Garcas
    Getting weather info for city# 505: Jeddah
    Getting weather info for city# 506: Tabaquite
    


```python
#Convert lists to dataframe
weather_data = {
    "City": cities,
    "Latitude": lati, 
    "Longitude": longi,
    "Cloudiness": cloudiness,
    "Country": country,
    "Date": date,
    "Humidity": humidity,
    "Max Temperature": max_temp,
    "Min Temperature": min_temp,
    "Wind Speed": wind_speed}

weather_df = pd.DataFrame(weather_data)
weather_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>City</th>
      <th>Cloudiness</th>
      <th>Country</th>
      <th>Date</th>
      <th>Humidity</th>
      <th>Latitude</th>
      <th>Longitude</th>
      <th>Max Temperature</th>
      <th>Min Temperature</th>
      <th>Wind Speed</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bambous Virieux</td>
      <td>20</td>
      <td>MU</td>
      <td>1528426800</td>
      <td>78</td>
      <td>-20.34</td>
      <td>57.76</td>
      <td>296.150</td>
      <td>296.150</td>
      <td>2.60</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bissora</td>
      <td>8</td>
      <td>GW</td>
      <td>1528428928</td>
      <td>80</td>
      <td>12.23</td>
      <td>-15.45</td>
      <td>298.377</td>
      <td>298.377</td>
      <td>5.02</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Makui</td>
      <td>0</td>
      <td>ID</td>
      <td>1528428928</td>
      <td>95</td>
      <td>-6.37</td>
      <td>105.83</td>
      <td>301.477</td>
      <td>301.477</td>
      <td>5.82</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Ushuaia</td>
      <td>75</td>
      <td>AR</td>
      <td>1528423200</td>
      <td>56</td>
      <td>-54.80</td>
      <td>-68.30</td>
      <td>278.150</td>
      <td>278.150</td>
      <td>6.70</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Guizikeng</td>
      <td>75</td>
      <td>TW</td>
      <td>1528426800</td>
      <td>63</td>
      <td>25.17</td>
      <td>121.44</td>
      <td>307.150</td>
      <td>306.150</td>
      <td>7.20</td>
    </tr>
  </tbody>
</table>
</div>




```python
weather_df.to_csv("igot500citiesbutnullvalueaintone.csv")
```


```python
#Latitude vs Max Temperature (F) plot
plt.figure(figsize=(10, 5))
plt.scatter(weather_df['Latitude'], weather_data['Max Temperature'], marker = 'o', edgecolors="black", facecolors='blue')
plt.title("Latitude vs Temperature")
plt.ylabel("Maximum Temperature (Fahrenheit)")
plt.xlabel("Latitude")
plt.grid(True)

plt.savefig("Images/latvtemp.png")

plt.show()
```


![png](output_6_0.png)



```python
#Latitude vs Humidity (%) plot
plt.figure(figsize=(10, 5))
plt.scatter(weather_df['Latitude'], weather_data['Humidity'], marker = 'o', edgecolors="black", facecolors='blue')
plt.title("Latitude vs Humidity")
plt.ylabel("Humidity (Percent)")
plt.xlabel("Latitude")
plt.grid(True)

plt.savefig("Images/latvhumidity.png")

plt.show()
```


![png](output_7_0.png)



```python
#Latitude vs Cloudiness (%) plot
plt.figure(figsize=(10, 5))
plt.scatter(weather_df['Latitude'], weather_data['Cloudiness'], marker = 'o', edgecolors="black", facecolors='blue')
plt.title("Latitude vs Cloudiness")
plt.ylabel("Cloudiness (Percent)")
plt.xlabel("Latitude")
plt.grid(True)
           
plt.savefig("Images/latvcloud.png")
           
plt.show()
```


![png](output_8_0.png)



```python
#Latitude vs Wind Speed (mph) plot
plt.figure(figsize=(10, 5))
plt.scatter(weather_df['Latitude'], weather_data['Wind Speed'], marker = 'o', edgecolors="black", facecolors='blue')
plt.title("Latitude vs Wind Speed")
plt.ylabel("Wind Speed (mph)")
plt.xlabel("Latitude")
plt.grid(True)

plt.savefig("Images/latvwind.png")

plt.show()
```


![png](output_9_0.png)



```python
'''Three observations 
1. The maximum temperature of a city increases the closer it is to the equator

2. There is very little correlation between latitude and cloudiness. There is also minimal correlation between 
latitude and wind speed. 

3. Cities avoe the equator look to be slightly less humid on average than those below the equator. 
'''
```


```python
Your final notebook must:

Randomly select at least 500 unique (non-repeat) cities based on latitude and longitude.
Perform a weather check on each of the cities using a series of successive API calls. 
Include a print log of each city as it's being processed with the city number, city name, and requested URL.
Save both a CSV of all data retrieved and png images for each scatter plot.
```


```python
As final considerations:

You must include a written description of three observable trends based on the data. 
You must use proper labeling of your plots, including aspects like: Plot Titles (with date of analysis) and Axes Labels.
You must include an exported markdown version of your Notebook called  README.md in your GitHub repository.
```


```python
In building your script, pay attention to the cities you are using in your query pool. 
Are you getting coverage of the full gamut of latitudes and longitudes? 
Or are you simply choosing 500 cities concentrated in one region of the world? 
Even if you were a geographic genius, simply rattling 500 cities based on your human selection would create a 
biased dataset. Be thinking of how you should counter this. (Hint: Consider the full range of latitudes).
```
