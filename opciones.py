from funciones import *

def mostrar_menu():
    print(
'''
Menu de Opciones

1.  Registrar una transacción
2.  Cantidad total de acciones adquiridas por usuario. 
3.  Promedio de acciones adquiridas de cada empresa entre todos los usuarios 
4.  Usuarios ordenados alfabéticamente de la Z-A junto con el total invertido en las 
    distintas empresas. 
5.  Inversión total acumulada por toda la cartera de usuarios 
6.  Por cada usuario, la empresa en la que compró más acciones. 
7.  Acción con mayor inversión total (USD) en toda la cartera. 
8.  Porcentaje de inversión por usuario respecto a la inversión total acumulada. 
9.  Listado de los usuarios cuya inversión total supere la inversión promedio
10. Determinar cuál es la empresa que más dinero recaudó.
11. Listado ordenado descendentemente de todos los usuarios cuya cantidad de acciones de 
    Tesla supere el número promedio de acciones de Tesla.

''')



# Opcion 1 -----------
def registrar_transaccion(usuario:str, empresa:str, acciones_adquiridas:int, lista_usuarios:list, lista_empresas:list, lista_precios:list, matriz_acciones_usuarios:list):

    '''if empresa == "APPLE":
        pos_en_list_empresa = 0
    elif empresa == "TESLA":
        pos_en_list_empresa = 1
    elif empresa == "NVIDIA":
        pos_en_list_empresa = 2'''

    pos_en_list_empresa = buscar_posicion_elemento_en_lista(empresa, lista_empresas)
    pos_en_list_usuario = buscar_posicion_elemento_en_lista(usuario, lista_usuarios) # -- Funcion --

    matriz_acciones_usuarios[pos_en_list_empresa][pos_en_list_usuario] += acciones_adquiridas
    precio_por_unidad = lista_precios[pos_en_list_empresa]
    total_invertido = precio_por_unidad * acciones_adquiridas

    imprimir_separacion_en_consola(30) # -- Funcion --
    print(f'''Listado de Informacion

{"Usuario":20}:{usuario}
{"Accion":20}:{empresa}
{"Precio por unidad":20}:{precio_por_unidad:.2f} USD
{"Cantidad adquirida":20}:{acciones_adquiridas}
{"Total invertido":20}:{total_invertido:.2f} USD''')
    imprimir_separacion_en_consola(30) # -- Funcion --

    # {:25} Hace que la cadena ocupe (En este caso) 25 caracteres. Esta por defecto esta alineada a la izquierda.
    #:.2f Se usa para valores numericos, esta se asegura que tengas 2 decimales.



# Opcion 2 -----------
def mostrar_cantidad_de_acciones_por_usuario(lista_usuarios:list, lista_empresas:list, matriz_acciones_usuarios:list):
    '''
    Cantidad de acciones por cada usuario, mas el total de estas
    '''
    imprimir_separacion_en_consola(30) # -- Funcion --
    for i in range(len(lista_usuarios)):
        acumulador_acciones = 0
        print(f"{"Usuario":8}: {lista_usuarios[i]}")
        
        for j in range(len(matriz_acciones_usuarios)):
            nombre_empresa = lista_empresas[j]
            acciones_empresa = matriz_acciones_usuarios[j][i]
            print(f"{nombre_empresa:8}: {acciones_empresa}")
            acumulador_acciones += matriz_acciones_usuarios[j][i]
        
        print(f"{"Total":8}: {acumulador_acciones}")
        imprimir_separacion_en_consola(30) # -- Funcion --



# Opcion 3 -----------
def promedio_acciones_adquiridas(lista_empresas:list, matriz_acciones_usuarios:list):

    lista_promedios_empresa = []

    for i in range(len(matriz_acciones_usuarios)):
        acumulador_acciones = 0

        for j in range(len(matriz_acciones_usuarios[i])):
            acumulador_acciones += matriz_acciones_usuarios[i][j]

        promedio_acciones_empresa = acumulador_acciones / len(matriz_acciones_usuarios[i])
        lista_promedios_empresa += [promedio_acciones_empresa]   
        print(f"Promedio de acciones de {lista_empresas[i]:10}: {promedio_acciones_empresa:.2f}")

    print()



# Opcion 4 -----------
def ordenar_usuarios_descendiente(opcion:int, lista_usuarios:list, lista_empresas:list, lista_valor_acciones_empresa:list, matriz_acciones_usuarios:list):
    
    # Ordenar listas
    for i in range(0, len(lista_usuarios)-1, 1):
        for j in range(i+1, len(lista_usuarios)):

            if lista_usuarios[i] < lista_usuarios[j]:

                swapear_listas(lista_usuarios, i, j)
                # Ordenamiento descendente

                for k in range(len(matriz_acciones_usuarios)):
                    '''
                    Itera por las filas de la matriz acciones de usuario.
                    Es decir, a su vez que cambia de posicion los nombres 
                    tambien va cambiando de posicion las acciones en sus 
                    respectivas listas.
                    '''
                    swapear_listas(matriz_acciones_usuarios[k], i, j)
                



    # Imprimir la inversion total de los usuarios en cada empresa
    for i in range(len(lista_usuarios)):

            print(f"Usuario: {lista_usuarios[i]}")

            for j in range(len(matriz_acciones_usuarios)):

                nombre_empresa = lista_empresas[j]
                valor_individual_accion = lista_valor_acciones_empresa[j]
                cantidad_acciones_empresa = matriz_acciones_usuarios[j][i]
                inversion_total = valor_individual_accion * cantidad_acciones_empresa

                print(f"{nombre_empresa:7}: {inversion_total:.2f} USD")
            print()


    


# Opcion 5 -----------
def inversion_total(lista_valor_acciones:list, matriz_acciones_usuarios:list):
    
    total_invertido_global = 0

    for i in range(len(matriz_acciones_usuarios)):
        acumulador_acciones_empresa = 0

        for j in range(len(matriz_acciones_usuarios[i])):
            acumulador_acciones_empresa += matriz_acciones_usuarios[i][j]

        total_invertido_empresa = acumulador_acciones_empresa * lista_valor_acciones[i]
        total_invertido_global += total_invertido_empresa
    
    print(f"La inversino total acumulada entre todos los usuarios es de: {total_invertido_global:.2f} USD\n")



# Opcion 6 -----------
def empresa_comrpo_mas_acciones(lista_usuarios:list, lista_empresas:list, matriz_acciones_usuarios:list):

    for i in range(len(lista_usuarios)):
        empresa_con_mas_acciones = 0
        pos_en_list_empresa = 0

        for j in range(len(matriz_acciones_usuarios)):
            if matriz_acciones_usuarios[j][i] > empresa_con_mas_acciones:
                empresa_con_mas_acciones = matriz_acciones_usuarios[j][i]
                pos_en_list_empresa = j
            
        print(f"{"Usuario":25}: {lista_usuarios[i]}")
        print(f"{"Empresa con mas acciones":25}: {lista_empresas[pos_en_list_empresa]}")
        print(f"{"Cantidad de acciones":25}: {matriz_acciones_usuarios[pos_en_list_empresa][i]}\n")



# Opcion 7 -----------
def accion_con_mayor_inversion(lista_empresas:list, lista_valor_acciones:list, matriz_acciones_usuarios:list):
    accion_mayor_inversion = 0
    pos_empresa = 0
    pos_accion = 0

    for i in range(len(matriz_acciones_usuarios)):

        for j in range(len(matriz_acciones_usuarios[i])):
            if matriz_acciones_usuarios[i][j] > accion_mayor_inversion:
                accion_mayor_inversion = matriz_acciones_usuarios[i][j]
                pos_empresa = i
                pos_accion = j
    
    cantidad_invertida = lista_valor_acciones[pos_empresa] * accion_mayor_inversion

    print(f"{"Empresa con mayor inversion":28}: {lista_empresas[pos_empresa]}")
    print(f"{"Accion con mayor inversion":28}: {matriz_acciones_usuarios[pos_empresa][pos_accion]}")
    print(f"{"Cantidad en USD invertida":28}: {cantidad_invertida}\n")



# Opcion 8 -----------
def porcentaje_inversion_usuario_comparado_al_total(lista_usuarios:list, lista_valor_acciones:list, matriz_acciones_usuarios:list):

    total_invertido_global = 0

    for i in range(len(matriz_acciones_usuarios)):
        acumulador_acciones_empresa = 0

        for j in range(len(matriz_acciones_usuarios[i])):
            acumulador_acciones_empresa += matriz_acciones_usuarios[i][j]

        total_invertido_empresa = acumulador_acciones_empresa * lista_valor_acciones[i]
        total_invertido_global += total_invertido_empresa

    for i in range(len(lista_usuarios)):
        accion_usuario = 0
        total_invertido_usuario = 0

        for j in range(len(matriz_acciones_usuarios)):
            accion_usuario = matriz_acciones_usuarios[j][i]
            total_invertido_usuario += accion_usuario * lista_valor_acciones[j]
        
        porcentaje_inversion_usuario = total_invertido_usuario * 100 / total_invertido_global

        print(f"{"Usuario":24}: {lista_usuarios[i]}")
        print(f"{"Porcentaje de inversion":24}: {porcentaje_inversion_usuario:.2f}%\n")



# Opcion 9 -----------
def usuarios_superan_inversion_promedio(lista_usuarios:list, lista_valor_acciones:list, matriz_acciones_usuarios:list):

    total_invertido_global = 0

    for i in range(len(matriz_acciones_usuarios)):
        acumulador_acciones_empresa = 0

        for j in range(len(matriz_acciones_usuarios[i])):
            acumulador_acciones_empresa += matriz_acciones_usuarios[i][j]

        total_invertido_empresa = acumulador_acciones_empresa * lista_valor_acciones[i]
        total_invertido_global += total_invertido_empresa

    promedio_inversiones = total_invertido_global / len(lista_usuarios)
    print(f"Promedio de inversiones : {promedio_inversiones:.2f} USD\n")

    for i in range(len(lista_usuarios)):
        accion_usuario = 0
        total_invertido_usuario = 0

        for j in range(len(matriz_acciones_usuarios)):
            accion_usuario = matriz_acciones_usuarios[j][i]
            total_invertido_usuario += accion_usuario * lista_valor_acciones[j]
        
        if total_invertido_usuario > promedio_inversiones:
            print(f"{"Usuario":9} : {lista_usuarios[i]}")
            print(f"{"Inversion":9} : {total_invertido_usuario:.2f} USD\n")



#----------------------------------------------------------------------------------------

    ''' PRIMER PARCIAL: SEGUNDA INSTANCIA '''

#----------------------------------------------------------------------------------------

'''
10. Determinar cuál es la empresa que más dinero recaudó.
11. Listado ordenado descendentemente de todos los usuarios cuya cantidad de acciones de 
    Tesla supere el número promedio de acciones de Tesla.
'''

# Opcion 10 ----------
def empresa_mas_recaudacion(lista_nombres_empresas:list, lista_precios_acciones:list, matriz_acciones_usuarios:list):
    
    lista_acciones_totales_empresas = sumar_matriz(matriz_acciones_usuarios, "filas")
    lista_recaudacion_empresas = operar_listas(lista_precios_acciones, lista_acciones_totales_empresas, "mult")

    ordenar_listas(lista_recaudacion_empresas, lista_nombres_empresas, "desc")

    nombre_empresa = lista_nombres_empresas[0]
    cantidad_reacudacion = lista_recaudacion_empresas[0]

    print(f"Empresa con mayor recaudacion")
    print(f"{nombre_empresa} : {cantidad_reacudacion:.2f} USD\n")


# Opcion 11 ----------
def mostrar_usuarios_tesla_acciones_mayor_promedio(lista_nombres_empresas:list, lista_valor_acciones:list, lista_nombres_usuarios:list, matriz_acciones_usuario:list):

    tesla = buscar_posicion_elemento_en_lista("TESLA", lista_nombres_empresas)
    lista_acciones_totales_empresas = sumar_matriz(matriz_acciones_usuario, "filas")
    promedio_acciones_tesla = lista_acciones_totales_empresas[tesla] / lista_valor_acciones[tesla]

    ordenar_lista_y_matriz(lista_nombres_usuarios, matriz_acciones_usuario, "desc")     

    print(f"| {"Usuario":<20} | {"Acciones Tesla":<20} |")
    imprimir_separacion_en_consola(47)
    print(f"{"| Prom. acciones tesla":<20} | {promedio_acciones_tesla:<20.2f} |")
    imprimir_separacion_en_consola(47)

    for i in range(len(lista_nombres_usuarios)):
        if matriz_acciones_usuario[tesla][i] > promedio_acciones_tesla:
            imprimir_datos_listas(lista_nombres_usuarios[i], matriz_acciones_usuario[tesla][i], 1) 
    print("")

