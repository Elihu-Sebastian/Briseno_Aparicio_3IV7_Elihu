#derivado a que es necesario poder almacenar diferentes fuente de datos
#en python se utiliza la variabñe diccionario
#un diccionario es capaz de poder almacenar diferentes tipos de datos en formato de lista

#primero vamos a crear una lista de alumnos
alumnos = []

#vamos acrear una funcion que se encargue de registrar alumnos
def registrar_alumno():
    boleta = input("Ingresa la boleta del alumno: ")
    nombre = input("Ingresa el nombre del alumno: ")
    appat = input("Ingresa el apellido paterno del alumno: ")
    apmat = input("Ingresa el apellido materno del alumno: ")
    fecnac = input("Ingresa la fecha aa/bb/cc del alumno: ")
    
    
    calificaciones = []
    #vamos a solicitar 3 calificacions
    for i in range(1,4) :
        calificacionparcial = float(input("Ingrese la calificaion del parcial :"))
        calificaciones.append(calificacionparcial)

#defino al alumno
    alumno = {"boleta" : boleta, 
              "nombre" : nombre, 
              "apellidopaterno" : appat , 
              "apellidomaterno" : apmat, 
              "fechadenacimiento" : fecnac, 
              "calificaciones" : calificaciones ,
}

    alumnos.append(alumno)
    print("el alumno se registro correctamente")

#Funcion para poder consultar los datos del arreglo de alumnos(lista) 

def consultar_alumnos() :
    if not alumnos :
        print("No hay registro")
    else :
        print("Lista de Alumnos: \n")
        for alumno in alumnos :
            print(f"Boleta : {alumno['boleta']}, Nombre: {alumno['nombre']} {alumno['apellidopaterno']} {alumno['apellidomaterno']} Fecha de nacimiento : {alumno['fechadenacimiento']} Calificaciones : {alumno['calificaciones']} \n")

#funcion para buscar y editar alumno
def editar_alumno():
    boleta = input("ingresar la boleta del alumno que desea editar")
    for alumno in alumnos :
        if alumno["boleta"]== boleta :
            alumno["nombre"]= input("Ingresa el nuevo nombre o presiona Enter para mantener el actual") or alumno["nombre"]
            alumno["apellidopaterno"]= input("Ingresa el nuevo apellido paterno o presiona Enter para mantener el actual") or alumno["apelidopaterno"]
            alumno["apellidomaterno"]= input("Ingresa el nuevo apellido materno o presiona Enter para mantener el actual") or alumno["apellidomaterno"]
            alumno["fechadenacimiento"]= input("Ingresa el nueva fecha o presiona Enter para mantener el actual") or alumno["fechadenacimiento"]
            #editamos las calificacioes
    for i in range(3) :
        nueva_calificacion = input("Ingresa la nueva calificacion o presione Enter para mantener el actual")
        if nueva_calificacion :
            alumno["calificacion"][i] = float(nueva_calificacion)
            
#vamos aeleminar
def eleminar_alumno() :
   
    return
    print("no hay mas alumnos")
#vamos a crear un menu
def main() :
    while True:
        print("Menu de Gestion de Proximos Extras")
        print("1- Registrar alumno")
        print("2- Consultar alumno")
        print("3- Editar alumno")
        print("4- Eleminar alumno")
        print("5- Salir")
       
        opcion = input("Seleccione una opcion")
       
        if opcion =="1" :
            registrar_alumno()
        elif opcion =="2" :
            consultar_alumnos()
        elif opcion =="3" :
            editar_alumno()
        elif opcion =="4" :
            eleminar_alumno()
        elif opcion =="5" :
            print("Ayos")
            break
        else :
            print("opcon no vaslida")
            
main()