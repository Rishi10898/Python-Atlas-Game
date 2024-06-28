#Greetings and Rules of the Alus game 
# Task 1 
def intro():
    Greet_1 = input ("What's your name?")
    Greet_2 = print("Hi,", Greet_1, " Welcome.This is an Atlas Game only within Auckland Dsitrict")     
def rule():
    Rule_1 = print("You have to tell suburb names only in Auckland District") 
    Rule_2 = print("You shouldn't repeat the same suburb name again") 
    Rule_3 = print("You should start the name with the ending letter of the previous word")
def rule_1():
    Rules_4 = input("Did you understand the rules of this Atlus game?")
    if Rules_4 == "no":
        print(rule()) 
    else:
        Rules_4 == "yes"
        print()    
Places_in_Auckland = ["Albany"] and ["Alfriston"] and ["Arch Hill"] and ["Auckland CBD"] and ["Avondale"] and ["Balmoral"] and ["Bayswater"] and ["Bayview"] and ["Beach Haven"] and ["Belmont"] and ["Birkdale"] and ["Birkenhead", "Burswood"] and ["Blockhouse Bay", "Browns Bay"] and ["Botany Downs"] and ["Botany"] and ["Bucklands Beach"] and ["Campbells Bay","Castor Bay", "Cockle Bay"] and ["Chatswood"] and ["Clendon Park","Clover Park"] and ["Conifer Grove"] and ["Dannemora"] and ["Devonport"] and ["Drury"] and ["East Tamaki"] and ["East Tamaki Heights"] and ["Eastern Beach"] and ["Eden Terrace","Ellerslie"] and ["Eden Valley"] and ["Epsom"] and ["Fairview Heights"] and ["Farm Cove"] and ["Favona"] and ["Flat Bush"] and ["Forrest Hill"] and ["Freemans Bay"] and ["Gardens"] and ["Glen Eden","Grafton","Grey Lynn"] and ["Glen Innes","Golflands","Goodwood Heights"] and ["Glendene","Glendowie","Greenhithe","Greenlane"] and ["Glenfield"] and ["Green Bay"] and ["Half Moon Bay","Herne Bay"] and ["Hauraki","Homai"] and ["Henderson"] and ["Herald Island"] and ["Highland Park","Huntington Park","Howick","Hillpark","Highbrook"] and ["Hillcrest"] and ["Hillsborough"] and ["Hingaia"] and ["Hobsonville"] and ["Kaurilands"] and ["Kelston"] and ["Keri Hill"] and ["Kingsland"] and ["Kohimarama"] and ["Konini"] and ["Laingholm"] and ["Lincoln"] and ["Long Bay"] and ["Lucas Heights"] and ["Lynfield"] and ["Mairangi Bay","Mechanics Bay","Mellons Bay","Massey","Mission Bay","Murrays Bay"] and ["Mangere","Mangere Bridge","Middlemore","Morningside"] and ["Mangere East","Mount Albert"] and ["Manukau"] and ["Manurewa"] and ["McLaren Park","Meadowbank"] and ["Milford"] and ["Mission Heights"] and ["Mount Eden","Mount Wellington"] and ["Mount Roskill"] and ["Narrow Neck","Northpark"] and ["New Windsor"] and ["Newmarket"] and ["Newton", "New Lynn"] and ["Northcote"] and ["Northcross"] and ["One Tree Hill"] and ["Opaheke"] and ["Orakei"] and ["Otahuhu"] and ["Onehunga","Oranga","Otara","Oteha","Owairaka"] and ["Pahurehure","Penrose","Papakura","Pakuranga","Panmure","Papatoetoe"] and ["Pakuranga Heights"] and ["Pinehill","Parnell"] and ["Point Chevalier"] and ["Point England"] and ["Ponsonby"] and ["Randwick Park","Rosebank","Royal Oak"] and ["Ranui"] and ["Red Hill","Rosehill"] and ["Remuera"] and ["Rosedale"] and ["Rothesay Bay"] and ["Royal Heights"] and ["Saint Heliers"] and ["Saint Marys Bay"] and ["Sandringham"] and ["Schnapper Rock","Shamrock Park","Shelly Park"] and ["Somerville","Sunnyvale"] and ["Southdown","Swanson"] and ["St Johns""St Lukes","Stonefields","Sunnyhills"] and ["Sunnynook"] and ["Stanley Point"] and ["Takanini","Tamaki","Titirangi"] and ["Takapuna","Te Atatu Peninsula","Te Papapa"] and ["Te Atatu South"] and ["Three Kings","Torbay Heights","Totara Heights"] and ["Torbay"] and ["Totara Vale"] and ["Unsworth Heights"] and ["Viaduct Harbour"] and ["Wai o Taiki Bay","Wairau Valley","Wesley"] and ["Waiata Shores","Wattle Downs","Western Heights","Western Springs"] and ["Waima"] and ["Waikowhai","Whenuapai","Wiri"] and ["Waterview"] and ["West Harbour","Wynyard Quarter"] and ["Westfield"] and ["Westgate","Westmere","Waiake"] and ["Weymouth"] and ["Windsor Park","Woodlands Park"]

# Final code of Task 1 
intro()
rule()
rule_1()
# The main games starts from here
# Task 2 
Ask_User = input("Do you want to start the game ?")
if Ask_User ==" no" or "no" or "No" or " No" or "NO":
    import random
    print(random.choice(Places_in_Auckland))
else: 
    input("Ok, Please start !")
# Task 3 
# Task 4