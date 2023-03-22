print("base ^ expoente:")
base=int(input("Base: "))
expoente=int(input("Expoente: "))

potencia=1

for count in range(expoente):
    potencia *= base
    count += 1

print(base,"^",expoente,"=",potencia)