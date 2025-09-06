# Welcome to the Compiler!
import random
produktiv = False
groesse = 50
preis = 20.21
zitat = "11 88 0, da werden wir Sie helfen tun." 
preisAusgabe = "Das kostet", preis, "€." 
zitat = "Aha!" 
zweitesZitat = "Juhuu ich bin ein Zitat!" 
nummer = random.randint(1, 20)
nummerZwei = random.randint(1, 100)
nummern = [random.randint(1, 100) for x in range(5)]
name = "Tim" 
buecher = 50
satz = "Ich heiße", name, "und habe", buecher, "Bücher gebunkert." 
name = "Tim" 
buecher = 50
satz = "Ich heiße " + name + " und habe " + str(buecher) + " Bücher gebunkert." 
print("Jo! Was geht? Ich habe einige Bücher")
print(name + " <- ein toller Name!")
rand = [0 for x in range(5)]
print(rand)
rand = 0
print(rand)
print("Schere")
print("Hallo")
for x in range(5):
	print(f"Ich fange mit Buch {x} an.")
	for xx in range(20):
		print(f"Ich bin bei Seite {xx} vom Buch {x}.")
		for xxx in range(30):
			print(f"Ich bin bei Zeile {xxx} der Seite {xx} vom Buch {x}.")
			
		
	
