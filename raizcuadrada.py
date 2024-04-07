x=1.0 #Inniciamos x a la unidad
a=float(input("Dame el valor de a: \n"))

#Se inicia el calculo de la raiz de a
for k in range(1, 10):
    x=(x+a/x)/2
    print("La raiz despues de" ,k, "iteraciones es" ,x)