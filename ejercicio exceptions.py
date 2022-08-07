def readint(prompt, min, max):
  try:
      numero=int(input(prompt))
      if numero<=max and numero >= min:
        return (numero)
      else:
          print ("El valor no esta en el rango permitido")
  except ValueError:
    print("Error de ingreso")
          

v = readint("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)

