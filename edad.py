#ingresar edad
Edad=int(input("ingressar edad: "))

if Edad>=0 and Edad<4:
   print("Es un bebé")
   if Edad>3 and Edad<13:
       print("Es un niño")
       if Edad>11 and Edad<19:
           print("Es un adolecente")
           if Edad>18 and Edad<66:
               print("Es un adulto")
               if Edad>65 and Edad<121:
                   print("Es un adulto mayor")
               else:
                   ("No valido")
