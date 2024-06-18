#Greetings and Rules of the Alus game 
def intro():
    name = input ("What's your name?")
    print ("Hello", name, "Welcome to this Atlas game")
    print("This Atlas Game asks you about places in the Auckland Dsitrict that start with the ending letter of a prompt word from the auckland district that the computer will give you.")
def rule():
    Rule_1 = print("You have to tell suburb names only in Auckland District") 
    Rule_2 = print("You shouldn't repeat the same suburb name again") 
    Rule_3 = print("You should start the name with the ending letter of the previous word")
Answers_1 = ["Albany","Alfriston","Arch Hill","Auckland CBD","Avondale","Balmoral","Bayswater","Bayview","Beach Haven","Belmont","Birkdale","Birkenhead","Blockhouse Bay","Botany Downs","Botany","Browns Bay","Bucklands Beach","Burswood","Campbells Bay","Castor Bay","Chatswood","Clendon Park","Clover Park","Cockle Bay","Conifer Grove","Dannemora","Devonport","Drury","East Tamaki","East Tamaki Heights","Eastern Beach","Eden Terrace","Eden Valley","Ellerslie","Epsom","Fairview Heights","Farm Cove","Favona","Flat Bush","Forrest Hill","Freemans Bay","Gardens","Glen Eden","Glen Innes","Glendene","Glendowie","Glenfield","Golflands","Goodwood Heights","Grafton","Green Bay","Greenhithe","Greenlane","Grey Lynn","Half Moon Bay","Hauraki","Henderson","Herald Island","Herne Bay","Highbrook","Highland Park","Hillcrest""Hillpark","Hillsborough","Hingaia","Hobsonville","Homai","Howick","Huntington Park","Kaurilands","Kelston","Keri Hill","Kingsland","Kohimarama","Konini","Laingholm","Lincoln","Long Bay","Lucas Heights","Lynfield","Mairangi Bay","Mangere","Mangere Bridge","Mangere East","Manukau","Manurewa","Massey","McLaren Park","Meadowbank","Mechanics Bay","Mellons Bay","Middlemore","Milford","Mission Bay","Mission Heights","Morningside","Mount Albert","Mount Eden","Mount Roskill","Mount Wellington","Murrays Bay","Narrow Neck","New Lynn","New Windsor","Newmarket","Newton","Northcote","Northcross","Northpark","One Tree Hill","Onehunga","Opaheke","Orakei","Oranga","Otahuhu","Otara","Oteha","Owairaka","Pahurehure","Pakuranga","Pakuranga Heights","Panmure","Papakura","Papatoetoe","Parnell","Penrose","Pinehill","Point Chevalier","Point England","Ponsonby","Randwick Park","Ranui","Red Hill","Remuera","Rosebank","Rosedale","Rosehill","Rothesay Bay","Royal Heights","Royal Oak","Saint Heliers","Saint Marys Bay","Sandringham","Schnapper Rock","Shamrock Park","Shelly Park","Somerville","Southdown","St Johns","St Lukes","Stanley Point","Stonefields","Sunnyhills","Sunnynook","Sunnyvale","Swanson","Takanini","Takapuna","Tamaki","Te Atatu Peninsula","Te Atatu South","Te Papapa","Three Kings","Titirangi","Torbay Heights","Torbay","Totara Heights","Totara Vale","Unsworth Heights","Viaduct Harbour","Wai o Taiki Bay","Waiake","Waiata Shores","Waikowhai","Waima","Wairau Valley","Waterview","Wattle Downs","Wesley","West Harbour","Western Heights","Western Springs","Westfield","Westgate","Westmere","Weymouth","Whenuapai","Windsor Park","Wiri","Woodlands Park","Wynyard Quarter"]
# Introduction to the user
intro()
rule()
Rules_4 = input("Did you understand the rules of this Atlus game?")
if Rules_4 == "yes":
    print("Let's start the game")
else: 
    print(rule())
# The main games starts from here
Ask_User = input("Do you want to start the game or shall I?")
if Ask_User == "yes":
    print("Ok, Please start !")
else: 
    print(Answers_1[3])