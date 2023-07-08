import pandas as pd

#leer html

web = input("Proporcionar Dominio: ")
data = pd.read_html(web)

tablas = len(data)

for i in range(0,tablas-1):
    with open("tablas.txt", "a") as file_object:
        file_object.write("\ntabla {}\n".format(i))
        file_object.write("{}".format(data[i]))







