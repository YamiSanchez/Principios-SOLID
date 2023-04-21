import csv

def generate(list):
        #LSP porque si se desea guardar otros datos en el archivo, únicamente se tendría modificar el campo 
        #de fields sin modificar el funcionamiento de todo el código
        fields = ["preference_key", "movie_title", "star_cast", "rating", "year", "place", "vote", "link"]
        with open("movie_results.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            for movie in list:
                writer.writerow({**movie})