#DIP porque se le quitó a movie_fetcher la dependencia de request
import requests

#SRP porque este modulo solo tiene la responsabilidad de obtener los datos de la url
def obtain_data():
        url = 'http://www.imdb.com/chart/top'
        response = requests.get(url)
        return response