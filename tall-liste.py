#Program for å lese inn 5 tall inn i en liste og finne det minste tallet

#Tallliste defineres som en tom liste
talliste=[]

#Utskrift av talliste til nå
print('Lista til nå:',talliste)
print()

#FOR-løkke for å lese inn 5 tall inn i lista tallister
for tallnr in range(1,6,1):
    print("Tall nr",tallnr)
    tall=int(input("Oppgi tall:"))
    #Innlest tall (det som brukeren har oppgitt)blir lagt inn i tallista
    #i lista vår talliste som er tom
    talliste=talliste+[tall]


#Utskrift av listeinnhold og listestørrelse etter fylling
print("Hele lista er",talliste)
listeLengde=len(talliste)
print("Antall elementer i tallista er",listeLengde)


#Finner det minste tall ved bruk av FOR-løkke og IF statements
#Antar det første tallet er det minste
minste_tall=talliste[0]
#Tallnr1 er foreløpig den minste
minste_tall_nummer=1
#Starter med første tall
tallnr=1

for tall in talliste:
    if tall<minste_tall:
        minste_tall=tall
        minste_tall_nummer=tallnr

    tallnr+=1 


print("det minste tallet i lista er:",minste_tall,"og er tallnr:",minste_tall_nummer)
