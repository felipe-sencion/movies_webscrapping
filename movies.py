import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/list/ls055592025/'
r = requests.get(url)
r.encoding = 'utf-8'
soup = BeautifulSoup(r.text, 'html.parser')
listers = soup.find_all(class_ = 'lister-item mode-detail')

with open('movies.txt', 'w') as f:
    for l in listers:
        titulo = l.find_all(class_ = 'lister-item-header')[0].find('a').text #titulo
        genero = l.find_all(class_ = 'genre')[0].text.strip() #genero
        director = l.find_all(class_ = 'text-muted text-small')[1].text.strip() #director y actores
        year = l.find_all(class_ = 'lister-item-year text-muted unbold')[0].text.strip() #año
        duracion = l.find_all(class_ = 'runtime')[0].text.strip() #tiempo
        presupuesto = l.find_all(class_ = 'text-muted text-small')[2].text.strip() #votos y presupuesto
        calif = l.find_all(class_ = 'ipl-rating-star__rating')[0].text.strip() #calificacion
        print(f'titulo: {titulo}')
        print(f'genero: {genero}')
        try:
            print(f'director: {director.split("Director:")[1].strip().split("|")[0].strip()}')
        except:
            print(f'director: {director.split("Directors:")[1].strip().split("|")[0].strip().upper()}')
        print(f'calificación: {calif}')
        print(f'duración: {duracion}')
        print(f'año: {year}')
        print('actores:', director.split("Stars:")[1].strip().replace("\n", ""))
        try:
            print(f'presupuesto: {presupuesto.split("Gross:")[1].strip()}')
        except:
            print('presupuesto: 0')
        print('*'*50)
        f.write(f'titulo: {titulo.upper()}\n')
        f.write(f'genero: {genero}\n')
        try:
            f.write(f'director: {director.split("Director:")[1].strip().split("|")[0].strip()}\n')
        except:
            f.write(f'director: {director.split("Directors:")[1].strip().split("|")[0].strip()}\n')
        f.write(f'calificación: {calif}\n')
        f.write(f'duración: {duracion}\n')
        f.write(f'año: {year}\n')
        f.write('actores:' + director.split("Stars:")[1].strip().replace("\n", "") + '\n')
        try:
            f.write(f'presupuesto: {presupuesto.split("Gross:")[1].strip()}\n')
        except:
            f.write('presupuesto: 0\n')
        f.write(('*'*50) +'\n')





