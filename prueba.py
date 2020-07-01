import csv
file ="Covid-19.csv"
def contagiados_region(file):
    with open(file, 'r') as covid:
        reader = csv.reader(covid)
        co_region = list(reader)
        regiones= ["Arica y Parinacota",
        "Tarapacá",
        "Antofagasta",
        "Atacama",
        "Coquimbo",
        "Valparaíso",
        "Metropolitana",
        "O’Higgins",
        "Maule",
        "Ñuble",
        "Biobío",
        "Araucanía",
        "Los Ríos",
        "Los Lagos",
        "Aysén",
        "Magallanes"]
        dic_regiones= {}
        i=0
        while i < len(regiones):
            i+=1
            print(i)
            print(regiones[i])

print(contagiados_region(file))