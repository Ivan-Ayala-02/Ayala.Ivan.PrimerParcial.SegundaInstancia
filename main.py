#from datos import *
#from funciones import *
#from validaciones import *
from opciones import *
from ingreso_datos import *

continuar_menu = "si"

while continuar_menu == "si":
    
    mostrar_menu()
    opcion = ingreso_opcion()

    match opcion:

        case 1:
            usuario = ingreso_usuario()
            empresa_elegida = ingreso_empresa()
            cantidad_acciones =  ingreso_acciones_comprar()
            registrar_transaccion(usuario, empresa_elegida, cantidad_acciones, usuarios_vip, empresas, valor_acciones, acciones_usuarios_vip)

        case 2:   
            mostrar_cantidad_de_acciones_por_usuario(usuarios_vip, empresas, acciones_usuarios_vip)

        case 3:
            promedio_acciones_adquiridas(empresas, acciones_usuarios_vip)

        case 4:
            ordenar_usuarios_descendiente(usuarios_vip, empresas, valor_acciones, acciones_usuarios_vip)

        case 5:
            inversion_total(valor_acciones, acciones_usuarios_vip)

        case 6:
            empresa_comrpo_mas_acciones(usuarios_vip, empresas, acciones_usuarios_vip)

        case 7:
            accion_con_mayor_inversion(empresas, valor_acciones, acciones_usuarios_vip)

        case 8:
            porcentaje_inversion_usuario_comparado_al_total(usuarios_vip, valor_acciones, acciones_usuarios_vip)

        case 9:
            usuarios_superan_inversion_promedio(usuarios_vip, valor_acciones, acciones_usuarios_vip)
        
        #----------------------------------------------------------------------------------------

            ''' PRIMER PARCIAL: SEGUNDA INSTANCIA '''

        #----------------------------------------------------------------------------------------

        case 10:
            empresa_mas_recaudacion(empresas, valor_acciones, acciones_usuarios_vip)

        case 11:
            mostrar_usuarios_tesla_acciones_mayor_promedio(empresas, valor_acciones, usuarios_vip, acciones_usuarios_vip)
    
    continuar_menu = ingreso_continuar_menu()
