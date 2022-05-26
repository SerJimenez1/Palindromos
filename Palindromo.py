def palindromo(oracion):
    oracion = oracion.replace(" ","")
    if str(oracion)==str(oracion)[::-1]:
      print("La oración sí es un palíndromo")
    else:
      print("La oración no es un palíndromo")

      
def ingresar_oracion():  
    while True:
        error = False
        oracion = input("Escriba una oración: ")
        for letra in oracion:
            if letra.isdigit() == True:
                print("Ingrese una oración que no contenga números")
                error = True
                break
        if error == False:
            break

    return oracion

def menu():
    while True:
        oracion = ingresar_oracion()
        palindromo(oracion)
        while True:
            opc = input("¿Desea ingresar otra oración? si/no: ")
            if opc != "si" and opc != "no":
                print("Ingrese alguna de las opciones")
                continue
            elif opc == "si":
                break
            else:
                print("¡Hasta luego!")
                quit()

menu()






