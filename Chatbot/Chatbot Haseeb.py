print("ChatBot: hvad er dit navn")
user_name = input()

print("Tak for det "+user_name)

#print("ChatBot: Jeg bor i et hus, kan du gætte prisen?")


house = {
    "bedrooms": 3,
    "bathrooms": 2,
    "city": "Vancouver",
    "price": 10,
    "date_sold": (1, 3, 2015),
}

condo = {
    "bedrooms": 2,
    "bathrooms": 1,
    "city": "Burnaby",
    "price": 699999,
    "date_sold": (27, 8, 2011),
}

realsvar=False
print("ChatBot: Jeg bor i et hus, kan du gætte prisen?")
while(not realsvar): 
    if int(input())==house["price"]:
        print("korrect")
        realsvar=True

    else: 
        print("forkert, prøv igen")
        realsvar=False
    

print("GODT lavet, nu er det tid til endnu en quiz")

gg=False
print("ChatBot: Er du klar?")
inputstring= str(input())
while(not gg):
    if inputstring=="ja" or inputstring=="jeg er klar nu":
        print("ChatBot: så kan vi begynde :)))")
        gg=True
    
    else: 
        print("ChatBot: Okay, så venter vi til du er klar")
        gg=False
    


print("ChatBot: Kan du gætte det rigtige tal?")
rl=False
while(not rl): 
    if str(input())=="ti":
        print("korrect")
        rl=True

    else: 
        print("forkert, prøv igen")
        rl=False


if str(input())=="Hvor meget koster condoen?":
    print(condo["price"])
    




#HOW TO SAVE TO CLOUD AFTER CHANGES TO CODE

#git init 
#git add -A
#git status 
#git commit -m 'navn på commit'
#git push -u origin master