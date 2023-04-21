#DIP porque se le quitó a movie_fetcher la dependencia de request
from bs4 import BeautifulSoup

#SRP porque este modulo solo tiene la responsabilidad de obtener la variable soup
def obtain_soup(response):
    soup = BeautifulSoup(response.text, 'lxml')
    return soup
    

   