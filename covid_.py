import csv


menu= """
Respecto al COVID-19, ¿que quiere saber?
--------------------------------------------
[1]Casos por país
[2]Ranking por país
[3]Máximo de fallecidos 
[4]Comparación de fallecidos
[5]Casos por región
[6]Casos por región y comuna
[7]Internados por region
[8]Evolución de pacientes UCI en el tiempo
[9]Movilidad por comuna
[10]Cambio de movilidad
[11]Salir del programa
--------------------------------------------
"""


#archivos csv a manipular
archivos= ["WHO-COVID-19-global-data.csv",
"Covid-19.csv",
"IndiceDeMovilidad-IM_externo",
"IndiceDeMovilidad-IM_interno",
"UCI_T"]
#funcione
#[1]
def casos_pais(file, country, fecha):
    with open(file, 'r') as covid:
        reader = csv.reader(covid)
        lista_paises = list(reader)

    i=1
    while i < len(lista_paises):
        if str(lista_paises[i][0])== fecha and str(lista_paises[i][2])== country:
            return "los casos del pais: "+str(country)+" son: "+str(lista_paises[i][5])
        else:
            i+=1

#2. Ranking por país [0.5 pts.] Programe la función n_caos_pais(n,fecha,file)
# que retorna los n países con más contagiados para una fecha específica en el
#formato AAAA-MM-DD y un archivo del tipo WHO-COVID-19-global-data.csv .
#hacer una lista de 0 a n, recorrer el archivo y ir cambiando los valores a medida que sean mayores
#a los que ya estan en la lista
#[2]
"""
def n_caos_pais(n,fecha,file):
    i=1
    ranking= []
    pais= []
    #crear cantidades de puestos del ranking
    while i <= n:
        ranking.append(0)
        pais.append("")
        i+=1
    #tener el csv en listas anidadas
    with open(file, 'r') as covid:
        reader = csv.reader(covid)
        lista_paises = list(reader)
    j=1
    while j < len(lista_paises):
        if str(lista_paises[j][0]) == fecha:
            #print(lista_paises[j][0],lista_paises[j][2],lista_paises[j][5])
            k=0
            while k < len(ranking):
                if int(lista_paises[j][5]) > int(ranking[k]):
                    ranking[k] = lista_paises[j][5]
                    pais[k] = lista_paises[j][2]
                    print(pais)
                    k+=1
                else: 
                    k+=1
            j+=1
        else:
            j+=1

    rankingTotal= [ranking, pais]
    return rankingTotal
"""
#[3]
def max_fallecidos(file):
    with open(file, 'r') as covid:
        reader = csv.reader(covid)
        lista_paises = list(reader)
    j=1
    contador= 0
    pais= ""
    while j < len(lista_paises):
        if str(lista_paises[j][0]) == "2020-06-30" and int(lista_paises[j][5]) > contador: 
            contador= int(lista_paises[j][5])
            pais= str(lista_paises[j][2])
        j+=1
    return "el paises con mas contagios es: "+str(pais)+" con: "+ str(contador)+" contagiados"

#[4]
def compara_fallecidos_paises(pais1, pais2, fecha, file):
    with open(file, 'r') as covid:
        reader = csv.reader(covid)
        lista_paises = list(reader)

    c_pais1=0
    c_pais2=0
    
    i= 1
    while i < len(lista_paises):
        if str(lista_paises[i][0]) == fecha:
            if str(lista_paises[i][2]) == pais1:
                c_pais1= int(lista_paises[i][5])
            elif str(lista_paises[i][2])== pais2:
                c_pais2= int(lista_paises[i][5])
            i+=1
        else:
            i+=1   
    if c_pais1 >= c_pais2:
        diferencia= c_pais1 - c_pais2
        return "los contagidos de los respectivos paises son: "+str(c_pais1)+", "+str(c_pais2)+" con una diferencia de:", str(diferencia)        
    
    else:
        diferencia= c_pais2 - c_pais1
        return "los contagidos de los respectivos paises son: "+str(c_pais1)+", "+str(c_pais2)+" con una diferencia de:", str(diferencia)

#[5]

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
        dic = dict.fromkeys([regiones],0)
        i=0
        while i < len(regiones):
            j=1
            contagiadosf=0
            while j < len(co_region):
                if co_region[j][0] == regiones[i]:
                    k=5
                    contagiados= 0
                    while k < len(co_region[j]):
                        if float(co_region[j][k]) > contagiados:
                            contagiados= float(co_region[j][k])
                        k+=1
                        if k == int(len(co_region[j]))-1:
                            contagiadosf+=contagiados
                            break
                    dic_regiones[co_region[j][0]]= contagiados
                            
                else:
                    j+=1        
                    #[5]--->
            i+=1
    return dic_regiones

#[6]
# coding=utf-8

"""

# colores
colors = [
    # nombre, valor hexadecimal (rgb)
    ('negro', '#000000'),
    ('blanco', '#FFFFFF'),
    ('rojo', '#FF0000'),
    ('verde', '#00FF00'),
    ('azul', '#0000FF'),
    ('amarillo', '#FFFF00'),
    ('magenta', '#FF00FF'),
    ('cian', '#00FFFF')
]

with open('colores.csv', 'wb') as f:  # el flag 'b' es requerido en ciertas plataformas
    writer = csv.writer(f)
    writer.writerows(colors)
"""

            

#estrutura del codigo
print(menu)
opcion= int(input("Ingrese su opción:"))
while opcion != 11:
    #derivadas de las funciones segun el archivo que se desea manipular
    if opcion in range(1,11):
        if opcion in [1,2,3,4]:
            file = archivos[0]
            if opcion == 1:
                country = input("ingrese el país especifico: ") 
                country= country.title()
                fecha = input("Ingrese la fecha en formato AAAA-MM-DD: ")
                casosPaises = casos_pais(file, country, fecha)
                print(casosPaises)

            elif opcion == 2:
                n= int(input("Ingrese el limite del ranking: "))
                fecha = input("Ingrese la fecha en formato AAAA-MM-DD: ")
                rkPaises= n_caos_pais(n,fecha, file)
                print(rkPaises)

            elif opcion == 3:
                max_fallecidos_1=max_fallecidos(file)
                print(max_fallecidos_1)
            elif opcion == 4:
                pais1= input("Ingrese el primer pais: ")
                pais1= pais1.title()
                pais2= input("Ingrese el segundo pais: ")
                pais2= pais2.title()
                fecha= input("Ingrese la fecha especifica: ")
                fallecidos= compara_fallecidos_paises(pais1,pais2, fecha, file)
                print (fallecidos)
        elif opcion in [5,6]:
            file = archivos[1]
            if opcion == 5:
                contagiados= contagiados_region(file)
                print(contagiados)

        elif opcion in [7,8]:
            file = archivos[4]

        elif opcion in [9,10]:
            file1 = archivos[2]
            file2 = archivos[3]
    else:
        print("Error intentelo, nuevamente")
    print(menu)
    opcion= int(input("Ingrese su opción:"))