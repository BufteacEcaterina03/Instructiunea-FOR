n=int(input("Introduceti numarul: "))
suma=0
for a in range (1,n) :
    if (a%3==0) and (a%5==0):
        suma+=a

print("Suma nr ce se impart la 3 si 5 este: ", suma)