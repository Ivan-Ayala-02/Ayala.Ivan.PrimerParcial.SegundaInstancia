def imprimir_separacion_en_consola(longitud:int):
    '''
    imprime una en consola una serie de barras (-----). La longitud de esta debe ser
    especificada para funcionar.
    '''
    if longitud > 0:
        cadena_longitud = ""
        for i in range(longitud):
            cadena_longitud += "-"
        print(cadena_longitud)



def buscar_posicion_elemento_en_lista(elemento:str|int, lista:list) -> int|None:
    '''
    Busca en una lista un elemento del mismo nombre o valor. Si la funcion lo encuentra, 
    esta devolvera la posicion en la que esta ubicada, y en caso de que no exista dicho
    elemento en la lista, esta devolvera un None.
    '''
    posicion_elemento = None

    for i in range(len(lista)):
        if lista[i] == elemento:
            posicion_elemento = i
            break
    
    return posicion_elemento



def convertir_cadena(cadena_original:str, tipo_de_conversion:int) -> str:
    '''
    Toma una cadena y lo convierte segun el numero ingresado en el tipo de conversion:

    0 = Convierte la cadena completa en minusculas.
    1 = Convierte la cadena completa en mayusculas.
    2 = Convierte SOLO la primera letra en mayuscula, el resto se convierte en minusculas.
    '''
    cadena_convertida = ""

    for i in range(len(cadena_original)):

        caracter = cadena_original[i]
        orden_caracter = ord(caracter) # ord: devuelve numero de caracter ascii

        if tipo_de_conversion == 0:
        # rango caracteres mayusculas: 65-89
            if orden_caracter >= 65 and orden_caracter <= 89:
                caracter = chr(orden_caracter + 32) #chr: devuelve el caracter
        
        elif tipo_de_conversion == 1:
        # rango caracteres minusculas: 97-122
            if orden_caracter >= 97 and orden_caracter <= 122:
                caracter = chr(orden_caracter - 32)
        
        elif tipo_de_conversion == 2:
            if i == 0 and (orden_caracter >= 97 and orden_caracter <= 122):
                caracter = chr(orden_caracter - 32)
            elif i == 0 and (orden_caracter >= 65 and orden_caracter <= 89):
                caracter = chr(orden_caracter)
            elif orden_caracter >= 65 and orden_caracter <= 89:
                caracter = chr(orden_caracter + 32)
            
        cadena_convertida += caracter
    
    return cadena_convertida



def convertir_cadenas_a_numeros(cadena_original:str) -> int|None:
    '''
    Convierte una cadena con numeros dentro (Ej: "123") a un int (123). Esta funcion devuelve 
    unicamente numeros, salteando cualquier otra cosa en la cadena. Esta devuelve el entero, o
    en su caso de que no encuentre nada, un None.
    '''
    cadena_numerica = ""

    for i in range(len(cadena_original)):

        caracter = cadena_original[i]
        orden_caracter = ord(caracter) # ord: devuelve numero de caracter ascii
        
        if orden_caracter >= 48 and orden_caracter <= 57:
            # rango caracteres numericos: 48-57
            cadena_numerica += caracter

    if cadena_numerica != "":    
        cadena_numerica = int(cadena_numerica)
        return cadena_numerica
    else:
        cadena_numerica = None



def swapear_listas(lista:list, elemento_i, elemento_j):
    '''
    Cambia de posicion elementos de una lista
    '''
    temporal = lista[elemento_i]
    lista[elemento_i] = lista[elemento_j]
    lista[elemento_j] = temporal




def ordenar_lista(lista:list, tipo_de_ordenamiento:int = 0):
    '''
    Toma una lista y la ordena segun el tipo especificado:
    0: Ordena de forma ascendente
    1: Ordena de forma descendente
    '''

    for i in range(0, len(lista)-1, 1):
        
        for j in range(i+1, len(lista)):

            if tipo_de_ordenamiento == 0:
                if lista[i] > lista[j]:
                    # Ascendente (Menor a mayor)
                    swapear_listas(i, j) # -- Funcion --

            elif tipo_de_ordenamiento == 1:
                if lista[i] < lista[j]:
                    # Descendente (Mayor a menor)
                    swapear_listas(i, j) # -- Funcion --



def sumar_listas(matriz:list) -> int:
    
    acumulador = 0
    filas = len(matriz)
    columnas = len(matriz[0])

    for i in range(len(columnas)):
        for j in range(filas):
            acumulador += filas[i][j]
    
    return acumulador


#----------------------------------------------------------------------------------------

    ''' PRIMER PARCIAL: SEGUNDA INSTANCIA '''

#----------------------------------------------------------------------------------------

def sumar_matriz(matriz:list, tipo_suma:str) -> list|int:
    '''
    Toma una matriz y devuelve una lista o un int con la suma de esta:
    filas = Devuelve una lista con las filas sumadas de las matrices
    columnas = Devuelve una lista con las columnas sumadas de estas
    total = Devuelve un int con la suma total de la matriz
    '''
    acumulador_total_matriz = 0
    lista_matriz = []
    cantidad_filas = len(matriz)
    cantidad_columnas = len(matriz[0])

    if tipo_suma == "filas":

        for i in range(cantidad_filas):
            acumulador_listas = 0

            for j in range(cantidad_columnas):
                elemento_filas = matriz[i][j]
                acumulador_listas += elemento_filas

            lista_matriz += [acumulador_listas]
    
    elif tipo_suma == "columnas":

        for i in range(cantidad_columnas):
            acumulador_listas = 0

            for j in range(cantidad_filas):
                elemento_columnas = matriz[j][i]
                acumulador_listas += elemento_columnas
        
            lista_matriz += [acumulador_listas]

    elif tipo_suma == "total":

        for i in range(cantidad_filas):
            acumulador_listas = 0

            for j in range(cantidad_columnas):
                elemento_filas = matriz[i][j]
                acumulador_total_matriz += elemento_filas

    if acumulador_total_matriz == 0:
        return lista_matriz
    else:
        return acumulador_total_matriz



def operar_listas(lista_a:list, lista_b:list, opcion:str) -> list:
    '''
    Toma dos listas, las opera (segun al opcion ingresada) en la misma posicion en las
    diferentes listas y devuelve una tercer lista con el resultado de la operacion.

    sum = toma un elemento (en en la misma posicion) dentro de cada lista y las suma.
    mult = sum = toma un elemento (...) dentro de cada lista y las multiplica.
    '''
    lista_resultado = []

    for i in range(len(lista_a)):

        if opcion == "sum":
            resultado = lista_a[i] + lista_b[i]
        
        elif opcion == "mult":
            resultado = lista_a[i] * lista_b[i]

        lista_resultado += [resultado]

    return lista_resultado



def operar_lista_con_elemento(lista:list, elemento:int, opcion:str) -> list:
    '''
    Toma una lista y opera con el elemento segun la opcion seleccionada, devolviendo
    una lista con el resultado de estas.

    sum = suma el elemento ingresado en todos los elementos de la lista
    mult = multiplica el elemento ingresado en todos los elementos de la lista
    '''

    lista_resultado = 0

    for i in range(len(lista)):

        if opcion == "sum":
            resultado = lista[i] + elemento

        elif opcion == "mult":
            resultado = lista[i] * elemento

        lista_resultado += [resultado]
    
    return lista_resultado



def imprimir_datos_listas(lista_datos:list|int|str, lista_valores:list|int|str, opcion:int):
    '''
    Toma dos listas e imprime los datos de ambas en orden. Tambien puede imprimir elementos
    especificos al mismo nivel dentro de las dos listas. 

    Opcion 0 = Imprime en la misma posicion de ambas listas TODOS los datos.
    Ejemplo.
    Maria   | 20
    Juan    | 15
    Felipe  | 21

    Opcion 1 = Imprime unicamente un unico valor por pantalla:
    Sol     | 24
    '''

    if opcion == 0:
        for i in range(len(lista_datos)):
            print(f"| {lista_datos[i]:<20} | {lista_valores[i]:<20.2f} |")
    
    if opcion == 1:
        print(f"| {lista_datos:<20} | {lista_valores:<20.2f} |")



def ordenar_lista_y_matriz(lista_datos:list, matriz:list, tipo_ordenamiento:str):
    '''
    Organiza las lista y matriz, esto para que los datos de las columnas sigan siendo coincidentes
    con la lista si esta se modifica. Ingresa por parametro la lista y matriz, asi como el tipo de 
    ordenamiento.

    tipo_ordenamiento:
    "asc" = Ordena de forma ascendente
    "desc" = Ordena de forma descendente
    '''

    for i in range(0, len(lista_datos) - 1, 1):
        for j in range(i+1, len(lista_datos), 1):

            if tipo_ordenamiento == "asc":
                if lista_datos[i] > lista_datos[j]:
                    swapear_listas(lista_datos, i, j)

                    for k in range(len(matriz)):    # Al modificar las demas listas, tambien hay que modificar la matriz
                        swapear_listas(matriz[k], i, j)

            
            elif tipo_ordenamiento == "desc":
                if lista_datos[i] < lista_datos[j]:
                    swapear_listas(lista_datos, i, j)

                    for k in range(len(matriz)):
                        swapear_listas(matriz[k], i, j)




def ordenar_listas(lista_principal:list, lista_secundaria:list, tipo_ordenamiento:str):
    '''
    Toma dos listas, ordena en base a la lista principal y segun el tipo de ordenamiento
    ingresado.

    tipo_ordenamiento:
    "asc" = ordena la lista principal (y a la vez la secundaria) de manera ascendente
    "desc" = ordena la lista principal (y a la vez la secundaria) de manera descendente
    '''
    for i in range(0, len(lista_principal) - 1, 1):

        for j in range(i+1, len(lista_principal), 1):

            if tipo_ordenamiento == "asc":
                if lista_principal[i] > lista_principal[j]:
                    swapear_listas(lista_principal, i, j)
                    swapear_listas(lista_secundaria, i, j)
            
            elif tipo_ordenamiento == "desc":
                if lista_principal[i] < lista_principal[j]:
                    swapear_listas(lista_principal, i, j)
                    swapear_listas(lista_secundaria, i, j)
            





    
