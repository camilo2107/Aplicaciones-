4
import math
print("/////////////////////////////////")
print("//Ingrese los datos solicitados//")
print("/////////////////////////////////")
terrenos = int(input("Ingrese las zonas a analizar: "))
if terrenos >=0 :

    cant_ant = 0
    ant_vi = 11700
    tipo_a = 0
    tipo_b = 0
    tipo_c = 0
    tipo_d = 0
    tipo_e = 0
    a = 2600 
    b = 19000 
    c = 1500 
    d = 19600 
    e = 6500 
    contador=0
    for i in range(terrenos):
      contador1 = []
      print("/////////////////////////////////////////////")
      contador+=+1
      print("/////////////////////",contador,"/////////////////////")
      contador1.append(contador)
      print("/////////////////////////////////////////////")
      areazona = float(input("Digite cada area endonde se desean instalar las antenas: "))
      canti_atn = float(input("Cantidad de antenas previamente instaladas: "))
      tipo_ant = input("Tipo de antenas previamente instaladas: ")
      
      if ((tipo_ant == "a" or tipo_ant == "b" or tipo_ant == "c" 
      or tipo_ant == "d" or tipo_ant =="e")):

       if tipo_ant == "a":
        tipo_a+= max (0, math.ceil((areazona - ant_vi * canti_atn )/a)) 
   
       elif tipo_ant == "b":
        tipo_b+= max (0, math.ceil((areazona - ant_vi * canti_atn )/b)) 
        
       elif tipo_ant == "c":
        tipo_c+= max (0, math.ceil((areazona - ant_vi * canti_atn)/c)) 
       
       elif tipo_ant == "d":
        tipo_d+= max (0, math.ceil((areazona - ant_vi * canti_atn)/d)) 
        
 
       elif tipo_ant == "e":
        tipo_e+= max (0, math.ceil((areazona - ant_vi * canti_atn)/e))

           
cant_ant= tipo_a + tipo_b + tipo_c + tipo_d + tipo_e
       

if cant_ant > 0:
    print("///////////////")
    print("///Resultado///") 
    print("///////////////")
    print(cant_ant)
    print("a ""{:.2f}%".format(tipo_a / cant_ant * 100))
    print("b ""{:.2f}%".format(tipo_b / cant_ant * 100))
    print("c ""{:.2f}%".format(tipo_c / cant_ant * 100))
    print("d ""{:.2f}%".format(tipo_d / cant_ant * 100))
    print("e ""{:.2f}%".format(tipo_e / cant_ant * 100))
   
    
else: 
    print("///////////////")
    print("///Resultado///") 
    print("///////////////")
    print(cant_ant)
    print("a 0.00%")
    print("b 0.00%")
    print("c 0.00%")
    print("d 0.00%")
    print("e 0.00%")
    

    