def palindromo(oracion):
    oracion = oracion.replace(" ","")
    if str(oracion)==str(oracion)[::-1]:
      return True
    else:
      return False  
print(palindromo(input("Escriba una oracion  ")))
        




