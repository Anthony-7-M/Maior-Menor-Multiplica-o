print("Olá! Este programa foi feito pelo António, mas podes só chamar-me Tó :)")
print("Ainda é só o início, por isso, este programa apenas foi concebido para fazer uma simples coisa: De duas multiplicações, qual será o número mais alto?")

a=float(input("Qual é o primeiro número?"))
b=float(input("Qual é o segundo número?"))
c=float(input("Qual é o terceiro número?"))
d=float(input("Qual é o quarto número?"))

m1=a*b
m2=c*d
maxi=max(m1,m2)

if(m1>m2):
    print("Multiplicando o 1.º número com o 2.º e o 3.º com o 4.º, a maior multiplicação é a 1.ª, sendo o seu valor igual a:",maxi)
else:
    print("Multiplicando o 1.º número com o 2.º e o 3.º com o 4.º, a maior multiplicação é a 2.ª, sendo o seu valor igual a:",maxi)