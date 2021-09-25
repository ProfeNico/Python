print("-------------------------------------------")
print("Creditos Mandell")
print("-------------------------------------------")

varNombre = input("Ingrese su Nombre: ")
varApellido = input("Ingrese su Apellido: ")
varEdad = input("Ingrese su Edad: ")
varMontoSolicitud = input("Ingrese su monto Credito: ")
varSalario = input("Ingrese su Sueldo Mensual: ")

if varMontoSolicitud > varSalario:
    print("Credito supera su sueldo!!")
else:
    print("Credito Aprobado!!")
    print("Si no paga!!")
    print("Le matamos al perrito")
    print("Le matamos al gatito")