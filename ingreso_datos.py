from validaciones import *
from funciones import *
from datos import *

def ingreso_usuario() -> str:
    '''
    Inicia un input para ingresar un usuario y lo valida, este no retorna nada hasta
    haberlo validado correctamente.
    '''
    usuario = input("Ingrese usuario: ")
    usuario = convertir_cadena(usuario, 2)

    while validar_elemento_dentro_de_lista(usuario, usuarios_vip) == False:
        usuario = input("[ERROR] Ingrese un usuario valido: ")
        usuario = convertir_cadena(usuario, 2)
    
    return usuario

def ingreso_empresa() -> str:
    '''
    Inicia un input para ingresar una empresa y lo valida, este no retorna nada hasta
    haberlo validado correctamente.
    '''
    empresa_elegida = input("Ingrese empresa (APPLE, TESLA, NVIDIA): ")
    empresa_elegida = convertir_cadena(empresa_elegida, 1)

    while validar_elemento_dentro_de_lista(empresa_elegida, empresas) == False:
        empresa_elegida = input("[ERROR] Ingrese empresa valida (APPLE, TESLA, NVIDIA): ")
        empresa_elegida = convertir_cadena(empresa_elegida, 2)


def ingreso_acciones_comprar() -> str:
    '''
    Inicia un input para ingresar un la cantidad de acciones a comprar y lo valida, este no
    retorna nada hasta haberlo validado correctamente.
    '''
    cantidad_acciones = input("Ingrese la cantidad de acciones a comprar (0-500): ")
    cantidad_acciones = convertir_cadenas_a_numeros(cantidad_acciones)
    rango_acciones = validar_numero_dentro_de_rango(cantidad_acciones, 0, 500)

    while (cantidad_acciones == None) or (rango_acciones == False):
        cantidad_acciones = input("[ERROR] Ingrese la cantidad valida de acciones a comprar (Solo numeros y en un rango de 0 a 500): ")
        cantidad_acciones = convertir_cadenas_a_numeros(cantidad_acciones)
        rango_acciones = validar_numero_dentro_de_rango(cantidad_acciones, 0, 500)