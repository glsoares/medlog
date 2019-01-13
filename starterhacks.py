"""
MedLog @ StarterHacks 2019
Lindsay Lee, Alisa Neang, Giselle Soares, Sarah Sohn 
"""

#LIST OF SIDE EFFECTS
sf1 = "Constipation"
sf2 = "Skin Tash/Dermatitis"
sf3 = "Diarrhea"
sf4 = "Dizziness"
sf5 = "Drowsiness"
sf6 = "Dry mouth"
sf7 = "Headache"
sf8 = "Imsomnia"
sf9 = "Nausea"
sf10 = "Suicidal Thoughts"
sf11 = "Abnormal Heart Rhythms"
sf12 = "Anxiety"
sf13 = "Loss of Appetite"
sf14 = "Increase of Appetite"
sf15 = "Cold Symptoms (stuffy nose, sneezing, sore throat)"
sf16 = "Irritability"
sf17 = "Fatigue"
sf18 = "Poor Balance/Coordination"

#LIST OF FOODS/DRINKS THAT SHOULD NOT BE MIXED WITH THE MEDICATION 
int1 = "alcohol"
int2 = "marijuana"
int3 = "caffeine"
int4 = "excessive caffeine"
int5 = "beets"
int6 = "spinach"
int7 = "kale"
int8 = "citrus juices"
int9 = "grapefruit juice"
int10 = "tobacco products"

#brand name ADDERALL
drug1 = "AMPHETAMINE"
drug2 = "DEXTROAMPHETAMINE"
drug3 = "ADDERALL"
drug4 = "CONCERTA"
#brand name XANAX
drug5 = "XANAX"
drug6 = "NIRAVAM"
drug7 = "ALPRAZOLAM"
#brand name ELAVIL 
drug8 = "ELAVIL"
drug9 = "ENDEP"
drug10 = "VANATRIP"
drug11 = "AMITIPTYLINE"
#brand name ABILIFY
drug12 = "ABILIFY"
drug13 = "ARIPIPRAZOLE"
#brand name NUVIGIL
drug14 = "NUVIGIL"
drug15 = "ARMODAFINIL"
#brand name SAPHRIS 
drug16 = "SAPHRIS"
drug17 = "SYCREST"
drug18 = "ASENAPINE"
#brand name STRATTERA
drug19 = "STRATTERA"
drug20 = "AXETRA"
drug21 = "AXEPTA"
drug22 = "ATTERA"
drug23 = "TOMOXETIN"
drug24 = "ATTENTIN"
drug25 = "STRAMOX"
drug26 = "ATOMOXETINE"
#brand name REXULTI 
drug27 = "BREXIPIPRAZOLE"
drug28 = "REXULTI"
#brand name ZOLOFT
drug29 = "ZOLOFT"
drug30 = "SERTRALINE"
#brand name PROZAC 
drug31 = "PROZAC"
drug32 = "SARAFEM"
drug33 = "FLUOXETINE"
#brand name CELEXA
drug34 = "CELEXA"
drug35 = "CITALOPRAM"
#brand name LEXAPRO 
drug36 = "LEXAPRO"
drug37 = "CIPRALEX"
drug38 = "ESCITALOPRAM"
#brand name PAXIL
drug39 = "PAXIL"
drug40 = "PEXEVA"
drug41 = "BRISDELLE"
drug42 = "PAROXETINE"
#brand name LUVOX
drug43 = "LUVOX"
drug44 = "FLUVOXAMINE"

# Program asks for user's medication and lists interactions with food and possible side effects
# Program repeats until user is finished inputting the medications they take
# Prints name of drug, foods/drinks to avoid, and possible side effects 
while True:
    user_input = input("Enter medication name. Enter NO to Quit ").upper()
    if user_input == drug1 or user_input == drug2 or user_input == drug3 or user_input == drug4:
        print (user_input)
        print ("Avoid consuming: "+ int1, int2, int3, int5, int6, int7, int8, sep=', ')
        print ("Possible side effects: ", sf1, sf9, sf3, sf4, sf5, sf17, sf8, sf6, sf15, sep='\n')
    elif user_input == drug5 or user_input == drug6 or user_input == drug7:
        print(user_input)
        print("Avoid consuming: "+ int1, int9, int2, int10, int4, sep=', ')
        print("Possible side effects: ", sf13, sf9, sf3, sf6, sf4, sf5, sf12, sf2, sf2, sep='\n')
    elif user_input == drug8 or user_input == drug9 or user_input == drug10 or user_input == drug11:
        print(user_input)
        print("Avoid consuming: "+ int1, int2, int10, sep=', ')
        print("Possible side effects: ", sf16, sf1, sf17, sf15, sf14, sf7, sf5, sf4, sf12, sep= '\n')
    elif user_input == drug12 or user_input == drug13:    
        print(user_input)
        print("Avoid consuming: "+ int1, int2, int9, sep=', ')
        print("Possible side effects: ", sf17, sf5, sf8, sf4, sf2, sf7, sf3, sf1, sf6, sf13, sf14, sep='\n')
    elif user_input == drug14 or user_input == drug15:
        print (user_input)
        print("Avoid consuming: "+ int1, int4, sep=', ')
        print("Possible side effects: ", sf4, sf7, sf5, sf9, sf17, sf7, sf8, sf1, sep='\n')
    elif user_input == drug16 or user_input == drug17 or user_input == drug18:
        print(user_input)
        print("Avoid consuming: "+ int1, int2, sep=', ')
        print("Possible side effects: ", sf5, sf4, sf1, sf6, sf8, sep='\n')
    elif user_input == drug19 or user_input == drug20 or user_input == drug21 or user_input == drug22 or user_input == drug23 or user_input == drug24 or user_input == drug25 or user_input == drug26:
        print(user_input)
        print("Avoid consuming: "+ int1, sep=', ')
        print("Possible side effects: ", sf5, sf4, sf16, sf8, sf18, sf3, sf1, sf7, sf9, sf6, sep='\n')
    elif user_input == drug27 or user_input == drug28:
        print(user_input)
        print("Avoid consuming: "+ int1, int2, int9, sep=', ')
        print("Possible side effects: ", sf5, sf4, sf6, sf1, sf10, sf16, sep='\n')
    elif user_input == drug29 or user_input == drug30:
        print(user_input)
        print("Avoid consuming: "+ int9, sep=', ')
        print("Possible side effects: ", sf5, sf4, sf8, sf9, sf1, sf6, sep='\n')
    elif user_input == drug31 or user_input == drug32 or user_input == drug33:
        print(user_input)
        print("Avoid consuming: "+ int2, sep=', ')
        print("Possible side effects: ", sf7, sf5, sf4, sf8, sf9, sf1, sf6, sep='\n')
    elif user_input == drug34 or user_input == drug35:
        print(user_input)
        print("Avoid consuming: "+ int1, int9, sep=', ')
        print("Possible side effects: ", sf7, sf9, sf3, sf6, sf12, sf4, sf8, sep='\n')
    elif user_input == drug36 or user_input == drug37 or user_input == drug38:
        print(user_input)
        print("Avoid consuming: "+ int1, int9, sep=', ')
        print("Possible side effects: ", sf8, sf6, sf13, sf9, sf4, sf5, sf16, sf2, sep='\n')
    elif user_input == drug39 or user_input == drug40 or user_input == drug41 or user_input == drug42:
        print(user_input)
        print("Avoid consuming: ", int1)
        print("Possible side effects: ", sf8, sf9, sf12, sf16, sep='\n')
    elif user_input == drug43 or user_input == drug44:
        print(user_input)
        print("Avoid consuming: " + int1, int9, int2, int10, int4, sep=', ')
        print("Possible side effects: ", sf9, sf1, sf7, sf12, sf8, sf5, sf4, sf13, sf14, sf15, sf6, sep='\n')
    elif user_input == "NO":
        break
    else:
        print ("Medication not found. Check spelling and try again. If still not found, contact support.")
        
