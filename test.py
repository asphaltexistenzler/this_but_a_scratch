print('the boy was flattered,\nnever ever has he been given such a great gift,')
print('never ever has anyone been so generous to him.')
print("He stuttered:\"m... ma... mark, please, i\'ll delete your data on the subject, it will be as if it would\'ve never happened.")
print("\"accept this small gesture of me, \as for now I cant do anything, except for this\" he continued")

#mit Python sind verschiedenste Rechnungen möglich! vom addieren bis hin zum Potenzieren ist alles möglich
print(10+10)
print((20*57)-(-70)**3)
print(9/3)
print(8%3)
print(10**20)

#ebenso sind BRuchrechnungen möglich. um diese auszuführen gilt diese Schreibweise:
from fractions import Fraction
bruch1=Fraction(1,2)
bruch2=Fraction(5,6)
print (bruch1/bruch2)

erg = bruch1+2*bruch2
divmod (erg.numerator, erg.denominator)
(2,1)
print (erg)

#Type Conversions:
#In Python ist möglich durch die verschiedenen Typen verschiedene Operationen durchzuführen,
# die zwei strings z.B "2" und "3" können nicht addiert werden um 5 zu ergeben. Das ergebnis wäre in diesem Fall 23
# Eine Lösung für dieses Problems wäre die Typen Konversion - hier, mithilfe der Int funktion.
print("2"+"3")
print(int("2")+int("3"))

# User-Input der üblicherweise ein String ist kann in Floats umgewandelt werden.
#    -print(float(input("enter a number:"))* 
#    -float(input("enter another number:")))
print(float("spam"*int(input("enter a number")))

#Variablen:
#Variablen spielen in Python wie in jeder anderen Programmiersprache eine große Rolle, um eine Variable zu erstellen schreibe einfach:'X=V'

#x =  123.456
#print(x)

#x=("this is a string")
#print(x+!)

#A=1234*5678
#B=888/4
#C=(3**4)**5
#print ((A+B)*C)

print ("alice + bob")