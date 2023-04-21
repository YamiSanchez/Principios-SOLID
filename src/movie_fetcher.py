from services import movie_service
from services import obtain_soup
from services import lista_service
from services import CSV_service

def main():
    #ISP porque ninguna clase depende de métodos que no usa 
    #OCP porque si se quiere cambiar la url de donde se obtienen las peliculas, este código
    #no se modifica, se modificaría solamente el de movie_service 
    response = movie_service.obtain_data()
    soup = obtain_soup.obtain_soup(response)
    list = lista_service.list_movies(soup)
    csv = CSV_service.generate(list)
    #LSP porque si se desea 
    return csv

    

if __name__ == '__main__':
    main()
