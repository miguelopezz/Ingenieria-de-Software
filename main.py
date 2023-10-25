import os
import csv
import pandas


def cargar_csv(file_name):
    df = pandas.read_csv(file_name, sep = ',')
    print(df)
    return(df)

def cargar_excell(file_name):
    df = pandas.read_excel(file_name)
    print(df)
    return df

def menu1():
    os.system('clear')
    print("""
- · MENU DE OPCIONES · -
          
-> 1: Cargar datos csv
-> 2: Cargar datos excel
-> 0: Salir del programa
""")
    option = int(input(": "))

    if option == 1:
        file_name = str(input("file_name: "))
        os.system('clear')
        df = cargar_csv(file_name)
        menu2(df)
        

    if option == 2:
        file_name = str(input("file_name: "))
        os.system('clear')
        df = cargar_excell(file_name)
        menu2(df)
        
    
        
def menu2(df):
    print("""
- · MENU DE OPCIONES · -
          
-> 1: Seleccionar columna
-> 2: Mostrar columna
-> 3: Hacer modelo regresion lineal
-> 0: Salir del programa
""")
    
    option = int(input(": "))

    if option == 1:
        columnas = []
        for i in range(len(df.columns)):
            columna = df.columns[i]
            columnas.append(columna)
            print("->", i, ":", columna)

        op_columna = int(input("Opcion (0-" + (str(len(df.columns)-1))+ "): "))

        selected_col = df[columnas[op_columna]]
        print("\n Columna seleccionada:")
        print("\n\t",df.columns[op_columna])
        print(selected_col)


        

    


if __name__ == '__main__':
    menu1()
