calificacion = int(input("Introduce tu calificacion de la AZ-900: "))

# preguntamos si la calificacion es menor a 700
if calificacion < 700 :
    print("Veez, por no estudiar") # si es menor a 700, muestra esto
elif calificacion > 1000 :
    print("Mientes no puedes sacar mas de 1000")   
else: # si no se cumple el if anterior pasa a esta linea 
    print("Eres un crack, pasaste") # se ejcuta si ninguno de los if se cumple     


edad = int(input("introduce tu edad: "))
if edad >= 18 and edad <= 100 :
    print("Bienvenido al mamitas")
elif edad > 100: 
    print("si vienes acompañado de tus abuelitos si te podemos fiar")
elif edad < 0 :
    print("Ni que fueras viajero  del tiempo")
else: 
    print("No puedes llevarte esos cigarros ")    
    
    
#en python no hay switch case     