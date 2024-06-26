# Defining Greetings and Rules of the Alus game 
# Task done by Rishikesh. only intro was edited by neel
def intro():
    name = input ("What's your name?")
    print("Hello", name, "Welcome to this Atlas game")
    print("This Atlas Game asks you about places in the Auckland Dsitrict that start with the ending letter of a prompt word from the auckland district that the computer will give you.")

def rule():
    Rule_1 = print("You have to tell suburb names only in Auckland District") 
    Rule_2 = print("You shouldn't repeat the same suburb name again") 
    Rule_3 = print("You should start the name with the ending letter of the previous word")
# Task done by Neel
def getLives():
    while True:
        lives = input("How many lives do you want to do this game?")
        try:
            lives  >= 0 - int(lives) 
            if lives >= 0:
                return lives
            else:
                print("Please pick a number for this question.")
        except:
            print("Please input a number(The reason you are seeing this message is because you didn't input a number for this question the first time around).")
# done by neel. only multi list by rishikesh
Starts_with_A_and_ends_with_Y = ["Albany"]
Starts_with_A_and_ends_with_N = ["Alfriston"]
Starts_with_A_and_ends_with_L = ["Arch Hill"]
Starts_with_A_and_ends_with_D = ["Auckland CBD"]
Starts_with_A_and_ends_with_E = ["Avondale"]

Starts_with_B_and_ends_with_L8_ = ["Balmoral"]
Starts_with_B_and_ends_with_R_ = ["Bayswater"]
Starts_with_B_and_ends_with_W = ["Bayview"]
Starts_with_B_and_ends_with_N_ = ["Beach Haven"]
Starts_with_B_and_ends_with_T_ = ["Belmont"]
Starts_with_B_and_ends_with_E_ = ["Birkdale"]
Starts_with_B_and_ends_with_D_ = ["Birkenhead", "Burswood"]
Starts_with_B_and_ends_with_Y_ = ["Blockhouse Bay", "Browns Bay"]
Starts_with_B_and_ends_with_D_ = ["Botany Downs"]
Starts_with_B_and_ends_with_Y_ = ["Botany"]
Starts_with_B_and_ends_with_H_ = ["Bucklands Beach"]

Starts_with_C_and_ends_with_Y_ = ["Campbells Bay","Castor Bay", "Cockle Bay"]
Starts_with_C_and_ends_with_D_ = ["Chatswood"]
Starts_with_C_and_ends_with_K_ = ["Clendon Park","Clover Park"]
Starts_with_C_and_ends_with_E_ = ["Conifer Grove"]

Starts_with_D_and_ends_with_A_ = ["Dannemora"]
Starts_with_D_and_ends_with_T_ = ["Devonport"]
Starts_with_D_and_ends_with_Y_ = ["Drury"]

Starts_with_E_and_ends_with_I_ = ["East Tamaki"]
Starts_with_E_and_ends_with_S_ = [ "East Tamaki Heights"]
Starts_with_E_and_ends_with_H_ = ["Eastern Beach"]
Starts_with_E_and_ends_with_E_ = ["Eden Terrace","Ellerslie"]
Starts_with_E_and_ends_with_Y_ = ["Eden Valley"]
Starts_with_E_and_ends_with_M_ = ["Epsom"]

Starts_with_F_and_ends_with_S_ = ["Fairview Heights"]
Starts_with_F_and_ends_with_E_ = ["Farm Cove"]
Starts_with_F_and_ends_with_A_ = ["Favona"]
Starts_with_F_and_ends_with_H_ = ["Flat Bush"]
Starts_with_F_and_ends_with_L_ = ["Forrest Hill"]
Starts_with_F_and_ends_with_Y_ = ["Freemans Bay"]

Starts_with_G_and_ends_with_S_ = ["Gardens"]
Starts_with_G_and_ends_with_N_ = ["Glen Eden","Grafton","Grey Lynn"]
Starts_with_G_and_ends_with_S_ = ["Glen Innes","Golflands","Goodwood Heights"]
Starts_with_G_and_ends_with_E_ = ["Glendene","Glendowie","Greenhithe","Greenlane"]
Starts_with_G_and_ends_with_D_ = ["Glenfield"]
Starts_with_G_and_ends_with_Y_ = ["Green Bay"]

Starts_with_H_and_ends_with_Y_ = ["Half Moon Bay","Herne Bay"]
Starts_with_H_and_ends_with_I_ = ["Hauraki","Homai"]
Starts_with_H_and_ends_with_N_ = ["Henderson"]
Starts_with_H_and_ends_with_D_ = ["Herald Island"]
Starts_with_H_and_ends_with_K_ = ["Highland Park","Huntington Park","Howick","Hillpark","Highbrook"]
Starts_with_H_and_ends_with_T_ = ["Hillcrest"]
Starts_with_H_and_ends_with_H_ = ["Hillsborough"]
Starts_with_H_and_ends_with_A_ = ["Hingaia"]
Starts_with_H_and_ends_with_E_ = ["Hobsonville"]

Starts_with_K_and_ends_with_S_ = ["Kaurilands"]
Starts_with_K_and_ends_with_N_ = ["Kelston"]
Starts_with_K_and_ends_with_L_ = ["Keri Hill"]
Starts_with_K_and_ends_with_D_ = ["Kingsland"]
Starts_with_K_and_ends_with_A_ = ["Kohimarama"]
Starts_with_K_and_ends_with_I_ = ["Konini"]

Starts_with_L_and_ends_with_M_ = ["Laingholm"]
Starts_with_L_and_ends_with_N_ = ["Lincoln"]
Starts_with_L_and_ends_with_Y_ = ["Long Bay"]
Starts_with_L_and_ends_with_S_ = ["Lucas Heights"]
Starts_with_L_and_ends_with_D_ = ["Lynfield"]

Starts_with_M_and_ends_with__ = ["Mairangi Bay","Mechanics Bay","Mellons Bay","Massey","Mission Bay","Murrays Bay"]
Starts_with_M_and_ends_with__ = ["Mangere","Mangere Bridge","Middlemore","Morningside"]
Starts_with_M_and_ends_with__ = ["Mangere East","Mount Albert"]
Starts_with_M_and_ends_with__ = ["Manukau"]
Starts_with_M_and_ends_with__ = ["Manurewa"]
Starts_with_M_and_ends_with__ = ["McLaren Park","Meadowbank"]
Starts_with_M_and_ends_with__ = ["Milford"]
Starts_with_M_and_ends_with__ = ["Mission Heights"]
Starts_with_M_and_ends_with__ = ["Mount Eden","Mount Wellington"]
Starts_with_M_and_ends_with__ = ["Mount Roskill"]

Starts_with_N_and_ends_with_K_ = ["Narrow Neck","Northpark"]
Starts_with_N_and_ends_with_R_ = ["New Windsor"]
Starts_with_N_and_ends_with_T_ = ["Newmarket"]
Starts_with_N_and_ends_with_N_ = ["Newton", "New Lynn"]
Starts_with_N_and_ends_with_E_ = ["Northcote"]
Starts_with_N_and_ends_with_S_ = ["Northcross"]

Starts_with_O_and_ends_with_L_ = ["One Tree Hill"]
Starts_with_O_and_ends_with_E_ = ["Opaheke"]
Starts_with_O_and_ends_with_I_ = ["Orakei"]
Starts_with_O_and_ends_with_U_ = ["Otahuhu"]
Starts_with_O_and_ends_with_A_ = ["Onehunga","Oranga","Otara","Oteha","Owairaka"]

Starts_with_P_and_ends_with_E_ = ["Pahurehure","Penrose","Papakura","Pakuranga","Panmure","Papatoetoe"]
Starts_with_P_and_ends_with_S_ = ["Pakuranga Heights"]
Starts_with_P_and_ends_with_L_ = ["Pinehill","Parnell"]
Starts_with_P_and_ends_with_R_ = ["Point Chevalier"]
Starts_with_P_and_ends_with_D_ = ["Point England"]
Starts_with_P_and_ends_with_Y_ = ["Ponsonby"]

Starts_with_R_and_ends_with_K_ = ["Randwick Park","Rosebank","Royal Oak"]
Starts_with_R_and_ends_with_I_ = ["Ranui"]
Starts_with_R_and_ends_with_L_ = ["Red Hill","Rosehill"]
Starts_with_R_and_ends_with_A_ = ["Remuera"]
Starts_with_R_and_ends_with_E_ = ["Rosedale"]
Starts_with_R_and_ends_with_Y_ = ["Rothesay Bay"]
Starts_with_R_and_ends_with_S_ = ["Royal Heights"]

Starts_with_S_and_ends_with_S_ = ["Saint Heliers"]
Starts_with_S_and_ends_with_Y_ = ["Saint Marys Bay"]
Starts_with_S_and_ends_with_M_ = ["Sandringham"]
Starts_with_S_and_ends_with_K_ = ["Schnapper Rock","Shamrock Park","Shelly Park"]
Starts_with_S_and_ends_with_E_ = ["Somerville","Sunnyvale"]
Starts_with_S_and_ends_with_N_ = ["Southdown","Swanson"]
Starts_with_S_and_ends_with_S_ = ["St Johns""St Lukes","Stonefields","Sunnyhills"]
Starts_with_S_and_ends_with_K_ = ["Sunnynook"]
Starts_with_S_and_ends_with_T_ = ["Stanley Point"]

Starts_with_T_and_ends_with_I_ = ["Takanini","Tamaki","Titirangi"]
Starts_with_T_and_ends_with_H_ = ["Takapuna","Te Atatu Peninsula","Te Papapa"]
Starts_with_T_and_ends_with_H_ = ["Te Atatu South"]
Starts_with_T_and_ends_with_S_ = ["Three Kings","Torbay Heights","Totara Heights"]
Starts_with_T_and_ends_with_Y_ = ["Torbay"]
Starts_with_T_and_ends_with_E_ = ["Totara Vale"]

Starts_with_U_and_ends_with_S = ["Unsworth Heights"]

Starts_with_V_and_ends_with_R_ = ["Viaduct Harbour"]

Starts_with_W_and_ends_with_Y_ = ["Wai o Taiki Bay","Wairau Valley","Wesley"]
Starts_with_W_and_ends_with_S_ = ["Waiata Shores","Wattle Downs","Western Heights","Western Springs"]
Starts_with_W_and_ends_with_A_ = ["Waima"]
Starts_with_W_and_ends_with_I_ = ["Waikowhai","Whenuapai","Wiri"]
Starts_with_W_and_ends_with_W_ = ["Waterview"]
Starts_with_W_and_ends_with_R_ = ["West Harbour","Wynyard Quarter"]
Starts_with_W_and_ends_with_D_ = ["Westfield"]
Starts_with_W_and_ends_with_E_ = ["Westgate","Westmere","Waiake"]
Starts_with_W_and_ends_with_H_ = ["Weymouth"]
Starts_with_W_and_ends_with_K_ = ["Windsor Park","Woodlands Park"]
# Introduction to the user
# Task done by Rishikesh
intro()
rule()
getLives()        
# The main games starts from here 
# Task done by Rishikesh

# Conclusion 
# Task done by neel