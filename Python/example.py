#Calculamos el saldo actual.
print("Brindame el saldo actual: ")
Saldo = float(input())

#Comenzamos con la condición de si el saldo es menor a 10.000.00 el interes es del 3%, caso contrario sea mayor aumenta a un 4%.
if (Saldo < 10000.00):
    Saldo = Saldo * (1 + 0.03)

else:
    Saldo = Saldo * (1 + 0.04)

#Mostramos la totalidad del saldo mas el interes.
print ("El saldo de la cuenta al finalizar el año es %5.2f" %Saldo)