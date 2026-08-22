#escritura en archivo 
with open ("lecturas.txt","w") as archivo:
    archivo.write("75.2\n")
    archivo.write("75.1\n")

#leer un archivo 
with open("lecturas.txt", "r") as archivo:
    contenido= archivo.read()
    print(contenido)