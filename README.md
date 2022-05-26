## IDENTIFICAR SI ES UN PALINDROMO ##
# El programa esta compuesto por varias funciones que permite identificar si la oracion introducida es un palindromo

# Los palindromos son palabras o frases que se leen igual en un sentido que en otro.
   

# Antes de ponerle un valor a la funcion use el replace para poder eliminar los espacios    
    def palindromo(oracion): 
    oracion = oracion.replace(" ","")

# Para definir la funcion use el bucle if para condicionar si era verdadero o falso he ingrese un texto
     
    if str(oracion)==str(oracion)[::-1]:
      print("La oración sí es un palíndromo")
    else:
      print("La oración no es un palíndromo")}

# Cree otra funcion para que aparezca un error si es escribia alguna clase de numero 
    ``` 
    >>> 
    ```  
    def ingresar_oracion():  
    while True:
        error = False
        oracion = input("Escriba una oración: ")
        for letra in oracion:
# El comando isdigit se usa para identificar si algun valor es un numero
         
    if letra.isdigit() == True:
                print("Ingrese una oración que no contenga números")
                error = True
                break
        if error == False:
            break

    return oracion
  
# Por ultimo cree otra funcion que funcione como un menu y pueda ser mas entendible al momento de la ejecucion 
    ``` 
    >>> 
    ```    
    def menu():
    while True:
        oracion = ingresar_oracion()
        palindromo(oracion)
        while True:
            opc = input("¿Desea ingresar otra oración? si/no: ")
# El comando != funciona para indicar si es diferente a otro valor  
          
    if opc != "si" and opc != "no":
                print("Ingrese alguna de las opciones")
                continue
            elif opc == "si":
                break
            else:
                print("¡Hasta luego!")
# Para finalizar el quit para que cierre el programa
             
    quit()

    menu()

