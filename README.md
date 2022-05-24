## IDENTIFICAR SI ES UN PALINDROMO ##
# El programa esta compuesto por una funcion que me permite identificar si la oracion introducida es un palindromo
# Los palindromos son palabras o frases que se leen igual en un sentido que en otro.
    ``` 
    >>> 
    ```   
    def palindromo(oracion):
# Antes de ponerle un valor a la funcion use el replace para poder eliminar los espacios    
    ``` 
    >>> 
    ```   
    oracion = oracion.replace(" ","")
# Para definir la funcion use el bucle if para condicionar si era verdadero o falso 
    ``` 
    >>> 
    ```   
    if str(oracion)==str(oracion)[::-1]:
      return True
    else:
      return False  
# Y poe ultimo utilice un print y un input para que imprimiera "Escriba una oracion " 
    ``` 
    >>> 
    ```   
    print(palindromo(input("Escriba una oracion  ")))