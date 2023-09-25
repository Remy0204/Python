print("ChatBot: hvad er dit navn")
user_name = input()

print("Tak for det "+user_name+"""
      """)

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

def huspris():
    realsvar=False
    print("ChatBot: Jeg bor i et hus, hvad er prisen af dette hus?")
    while(not realsvar): 
        if int(input(user_name+": "))==house["price"]:
            print("KORRECT")
            realsvar=True

        else: 
            print("forkert, prøv igen")
            realsvar=False


def gætteleg():
    gg=False
    rl = False
    print("ChatBot: Er du klar?")
    while(not gg):
        inputstring = str(input(user_name+": ").lower())
        if inputstring =="ja" or inputstring =="jeg er klar nu":
            print("""ChatBot: så kan vi begynde :)))
                  """)
            print("ChatBot: Kan du gætte det rigtige tal?")
            gg=True
        elif inputstring =="nej": 
            print("ChatBot: Okay, så venter vi til du er klar")
        else:
            print("Det skal betyde hvad??")
        
    while(not rl): 
        if str(input())=="ti":
            print("KORRECT")
            rl=True

        else: 
            print("forkert, prøv igen")
            rl=False

def spørgsmål():
    
    
    
    
    
    responses = {
       'hvor meget koster condoen': 'ChatBot: Condoen koster  + str(condo["price"]) + dkk'

   }
    
    #Svaret = input("Bot: Har du et spørgsmål")
   #if str(input("Bot: Har du et spørgsmål? "))=="Hvor meget koster condoen?":
    #if str(Svaret.lower()) == "Hvor meget koster condoen":
       #print("ChatBot: Condoen koster " + str(condo["price"])+ " dkk")
    #elif Svaret.lower()==
    #if str(input("Bot: Har du flere spørgsmål? "))=="Hvor meget koster condoen?":
       #print("ChatBot: Condoen koster ikke " + str(condo["price"])+ " dkk")

#Koden skal fungere sådan at, hvis man et spørgsmål kan man skrive det til chatbotten, og så svarer den ud for en kendt liste af spørgsmål den kender. Svarede kommer også fra en liste længere oppe

    


while True:
    print("Hva vil du?")
    print("""
          1. hus quiz
          2. gætteleg
          3. spørgsmål
          """)
    Svar = input(user_name+": ")
    if Svar.lower() == "hus quiz" or Svar.lower() == "1":
        huspris()
    elif Svar.lower() == "gætteleg" or Svar.lower() == "2":
        gætteleg()
    elif Svar.lower() == "spørgsmål" or Svar.lower() == "3":
        spørgsmål()


#HOW TO SAVE TO CLOUD AFTER CHANGES TO CODE

#git init 
#git add -A
#git status 
#git commit -m 'navn på commit'
#git push -u origin master