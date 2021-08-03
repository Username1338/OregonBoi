import time, sys, random, os

#What would this game be without a 25% chance to die of dysentary?

#Features to implement!
#-----------------------------
#Add more encounters


#Buglist
#------------------
#Fix scoreboard overwriting names
#Ammo fell off the wagon despite there being no ammo


#(FIXED) Fix bug where you can sell infinite amount of supplies to shop
#(FIXED) Fix shop bug where you can go into infinite debt lol
#(FIXED) save corruption issue - FIX BY SPLITTING ENTRIES WITH /, NOT \n
#(FIXED)Fix hard and nightmare modes - FIX BY TWEAKING DIFFICULTY SCALE, USE * TO INCREASE BOTTOM PROBABILITY RATHER THAN DIVIDE TOP PROBABILITY. SAME PROBABILITY EFFECT BUT NO CRASHING FROM RAND() ON FLOAT VALUES FROM DIVISION

#Completed Features
#-------------------
#Karma system that affects the ending & how NPC's treat you
#Water tablets so you don't die of dysentary
#Add CharacterEvents to the main story func, one check per turn
#Randomized illness to random characters, one check per turn, 
#maybe give the illness like, a 2-5% chance of occuring idk
#Add medicine to the shop to cure 'Sick' and 'Gravely Injured' status conditions
#Scaled probability of events based on Difficulty variable
#Starving to death should probably have consequences other than a text warning


Karma = 0
Starving = 'No'
Money = 0
Difficulty = 0
Food = 0
Ammo = 0
Miles = 10
Town = 0
Medicine = 0
Location = ''
PlayerName = ''
Character_1 = ""
Character_2 = ""
Character_3 = ""
Character_4 = ""
Water_Tablets = 'No'
Reputation = ''
ShopMessage = ''

#Health status 
#-----------
Char1Health = 'Healthy'
Char2Health = 'Healthy'
Char3Health = 'Healthy'
Char4Health = 'Healthy'
#------------
#Random tokens
FoodToken = 0
CriticalToken1 = 0
CriticalToken2 = 0
CriticalToken3 = 0
CriticalToken4 = 0
InjuredToken1 = 0
InjuredToken2 = 0
InjuredToken3 = 0
InjuredToken4 = 0
DesperateToken = 0

def CharacterSelect():
  global Character_1
  global Character_2
  global Character_3
  global Character_4
  Character_1 = input("\nCharacter 1's name: ")
  Character_2 = input("\nCharacter 2's name: ")
  Character_3 = input("\nCharacter 3's name: ")
  Character_4 = input("\nCharacter 4's name: ")

def GameOver():
  print("\nAll characters have died\nGame over")
  os.system("exit")
  time.sleep(300)

def TokenCheck():
  global InjuredToken1
  global InjuredToken2
  global InjuredToken3
  global InjuredToken4
  global Char1Health
  global Char2Health
  global Char3Health
  global Char4Health
  if InjuredToken1 >= 1:
    InjuredToken1 = InjuredToken1 - 1
  else:
    InjuredToken1 = 0
    if Char1Health == 'Injured':
      Char1Health = "Healthy"
  if InjuredToken2 >= 1:
    InjuredToken2 = InjuredToken2 - 1
  else:
    InjuredToken2 = 0
    if Char2Health == 'Injured':
      Char2Health = "Healthy"
  if InjuredToken3 >= 1:
    InjuredToken3 = InjuredToken3 - 1
  else:
    InjuredToken3 = 0
    if Char3Health == 'Injured':
      Char3Health = "Healthy"
  if InjuredToken4 >= 1:
    InjuredToken4 = InjuredToken4 - 1
  else:
    InjuredToken4 = 0
    if Char4Health == 'Injured':
      Char4Health = "Healthy"


def Die():
  global Character_1
  global Character_2
  global Character_3
  global Character_4
  global Char1Health
  global Char2Health
  global Char3Health
  global Char4Health
  CharDeath = random.randint(1,4)
  if CharDeath == 1 and Char1Health != "Dead":
    Char1Health = "Dead"
    print("\n",Character_1,"has died.")
    time.sleep(3)
  elif CharDeath == 2 and Char2Health != "Dead":
    Char2Health = "Dead"
    print("\n",Character_2,"has died.")
    time.sleep(3)
  elif CharDeath == 3 and Char3Health != "Dead":
    Char3Health = "Dead"
    print("\n",Character_3,"has died.")
    time.sleep(3)
  elif CharDeath == 4 and Char4Health != "Dead":
    Char4Health = "Dead"
    print("\n",Character_4,"has died.")
    time.sleep(3)
  if Char1Health == "Dead" and Char2Health == "Dead" and Char3Health == "Dead" and Char4Health == "Dead":
    GameOver()

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

def FoodCheck():
    global Food
    global FoodToken
    Food = Food - 4
    if Food < 0:
      Food = 0
      FoodToken = FoodToken + 1
    if FoodToken > 10:
      Die()
    if Food > 4:
      FoodToken = 0

def Hunt():
    global Food
    global Ammo
    HuntChance = random.randint(1,10)
    if HuntChance <5:
        CharacterEvents()
        print("\nThe hunt could have gone better, but we got some food.")
    elif HuntChance == 5:
        print("\nThe hunt went well, these supplies should last for about a week.")
    elif HuntChance > 5 and HuntChance < 10:
        print("\nThe hunt went excellent, we should have weeks worth of food here.")
    elif HuntChance == 10:
        print("\nThe hunt went perfect, we easily have a month's worth of food here.")
    Ammo = Ammo - 5 * HuntChance
    Food = Food + 15 * HuntChance
    Starving = "No"
    if Ammo <0:
      Ammo = 0
    

def TroubleCheck():
    global Ammo
    global Difficulty
    global Food
    Default_Probability = 150/Difficulty
    round(Difficulty)
    TroubleProbability = random.randint(1,Default_Probability)
    if TroubleProbability <= 3:
        sys.stdout.flush()
        time.sleep(1)
        if TroubleProbability == 1:
            sys.stdout.write("| How fortunate!")
            time.sleep(1)
            sys.stdout.write("- We found an abandoned wagon that had some ammo in it.\n")
            time.sleep(1)
            Ammo = Ammo + 10 * Difficulty
        elif TroubleProbability == 2:
            sys.stdout.write("| How unfortunate")
            time.sleep(1)
            sys.stdout.write("- Some of your food has spoiled.\n")
            time.sleep(1)
            Food = Food - 20 * Difficulty
        elif TroubleProbability == 3:
            sys.stdout.write("| How unfortunate")
            time.sleep(1)
            sys.stdout.write("- Some ammo fell off the wagon when you weren't looking.\n")
            time.sleep(1)
            Ammo = Ammo - 10 * Difficulty
            if Ammo <0:
              Ammo = 0

def DoWeNeedFood():
    global Food
    global Ammo
    global Starving
    if Food > 4:
      Starving = "No"
    if Starving == "Yes":
      print("| You are starving and will struggle to your next destination, if you make it.")
    if Food < 5 and Starving == "No":
      if Ammo > 0:
        print(Ammo,"X Ammo\n",Food,"X Food")
        Choice = input("\nYour food supply is running low, would you like to hunt?\nY/N: ")
        if Choice == 'Y' or Choice == 'y':
          if Ammo < 10:
            print("\nNot enough ammo")
            Starving = "Yes"
          else:
            Hunt()
        if Choice == 'N' or Choice == 'n':
          print("\nWe elected not to hunt, and continued on our way.")

def HiddenShop():
  global Char1Health
  global Char2Health
  global Char3Health
  global Char4Health
  global Money
  global Karma
  global Difficulty
  clear()
  print("\nCurrent party status:\n",Character_1,"-",Char1Health,"\n",Character_2,"-",Char2Health,"\n",Character_3,"-",Char3Health,"\n",Character_4,"-",Char4Health,"\n")
  print("Welcome to the hidden shop!\n\nPlayer money: $",Money,"\n1. Party Revive - $1000/-1 Reputation\n\n2. Good Luck Charm - $1500/-3 Reputation\n\n3. Manipulate reputation +++ - $5000\n\n4. Exit Shop")
  ShopSelect = int(input("\n\nEnter selection: "))
  if ShopSelect == 1:
    Char1Health = 'Healthy'
    Char2Health = 'Healthy'
    Char3Health = 'Healthy'
    Char4Health = 'Healthy'
    Money = Money - 1000
    Karma = Karma -1
    print("\nParty revive purchased.")
    time.sleep(1)
    clear()
    HiddenShop()
  if ShopSelect == 2:
    Difficulty = 1
    Money = Money - 1500
    Karma = Karma - 3
    print("\nGood luck charm purchased")
    time.sleep(1)
    clear()
    HiddenShop()
  if ShopSelect == 3:
    Money = Money - 5000
    Karma = Karma + 50
    print("Your reputation has been improved significantly.")
    time.sleep(1)
    clear()
    HiddenShop()
  if ShopSelect == 4:
    print("Leaving hidden shop...\nReturning to normal shop")
    time.sleep(1)
    Shop()
  else:
    print("Leaving hidden shop...\nReturning to normal shop")
    time.sleep(1)

def KarmaStatus():
  global Reputation
  global Karma
  global ShopMessage
  global Location
  if Karma >=10:
    Reputation = "Saint"
    ShopMessage = "\nWelcome to the",Location,"shop!\nOh, it's you! Please, take some supplies for the road, free of charge!\n\n"
  elif Karma >=5 and Karma < 10:
    Reputation = "Hero"
    ShopMessage = "\nWelcome to the",Location,"shop!\nI've heard stories about you! I'll give you a special discount for your good deeds.\n\n"
  elif Karma >=0 and Karma < 5:
    Reputation = "Citizen"
    ShopMessage = "\nWelcome to the",Location,"shop!\n"
  elif Karma < 0 and Karma >=-3:
    Reputation = "Untrustworthy"
    ShopMessage = "\nWelcome to the",Location,"shop!\nI'm keeping my eye on you.\n\n"
  elif Karma < -3 and Karma >=-6:
    Reputation = "Shunned"
    ShopMessage = "\nWelcome to the",Location,"shop!\nOh. I suppose I can sell to you. Make it quick.\n"
  elif Karma <-6 and Karma >-9:
    Reputation = "Outlaw"
    ShopMessage = "\nI don't serve your kind here. Get out.\n\n"
  elif Karma <=-10:
    Reputation = "Wanted - Dead or Alive"
    ShopMessage = "\nYou need to leave. Now.\n\n"

def Shop():
    global Money
    global Food
    global Ammo
    global Location
    global Water_Tablets
    global Reputation
    global Medicine
    KarmaStatus()
    if Water_Tablets == "Yes":
      WeBoughtThemAlready = "(Purchased)"
    elif Water_Tablets == "No":
      WeBoughtThemAlready = "(Not yet purchased)"
    clear()
    print("\nCurrent party status:\n",Character_1,"-",Char1Health,"\n",Character_2,"-",Char2Health,"\n",Character_3,"-",Char3Health,"\n",Character_4,"-",Char4Health,"\n")
    print("\nReputation: ",Reputation)
    if Karma >=10:
      print("\nWelcome to the",Location,"shop!\nOh, it's you! Please, take some supplies for the road, free of charge!\n\n")
      Food = Food + 150
      Ammo = Ammo + 150
      Medicine = Medicine + 8
      Water_Tablets = 'Yes'
    elif Karma >=5 and Karma < 10:
      print("\nWelcome to the",Location,"shop!\nI've heard stories about you! I'll give you a special discount for your good deeds.\n\n")
    elif Karma >=0 and Karma < 5:
      print("\nWelcome to the",Location,"shop!\n")
    elif Karma < 0 and Karma >=-3:
      print("\nWelcome to the",Location,"shop.\nI'm keeping my eye on you.\n\n")
    elif Karma < -3 and Karma >=-6:
      print("\nWelcome to the",Location,"shop.\nOh god, it's you.\nI need you to leave before you scare my customers away.\nShoo.\n")
    elif Karma <-6 and Karma >=-9:
      print("\nI don't serve your kind here. Get out.\n\n")
    elif Karma <=-10:
      print("\nYou need to leave. Now.\n\n")
    if Karma >-6:
      print("\n\nPlayer money: $",Money,"\n1. Small food supply (5) - $100 (Current supply:",Food,")\n\n2. Large food supply (30) - $300\n\n3. Ammo - $5 (Current supply:",Ammo,")\n\n4. Water Purification Tablets - $100",WeBoughtThemAlready,"\n\n5. Medicine - $50 (Current supply:",Medicine,")\n\n6. Exit Shop")
      ShopSelect = int(input("\n\nEnter selection: "))
      if ShopSelect == 1:
          Amount = int(input("\nHow many would you like to buy?: "))
          if Amount < 0:
            Food = Food + 5 * Amount
            if Food < 0:
              print("\nNot enough food to sell.")
              time.sleep(1)
              Food = Food + 5 * abs(Amount)
              clear()
              Shop()
            else:
              Price = 100 * abs(Amount)
              print("\nSold",abs(Amount),"X Small food supply for $",Price)
              time.sleep(1)
              Money = Money + Price
              clear()
              Shop()
          Money = Money - 100 *Amount
          if Money < 0:
            print("\nNot enough money..")
            Money = Money + 100 * Amount
          else:
            Food = Food + 5 * Amount
            print("\n\n",Amount,"X Small food supply purchased!\n\n")
          time.sleep(1)
          clear()
          Shop()
      elif ShopSelect == 2:
        Amount = int(input("\nHow many would you like to buy?: "))
        if Amount < 0:
          Food = Food + 30 * Amount
          if Food < 0:
            print("\nNot enough food to sell.")
            time.sleep(1)
            Food = Food + 30 * abs(Amount)
            clear()
            Shop()
          else:
            Price = 300 * abs(Amount)
            print("\nSold",abs(Amount),"X Large food supply for $",Price)
            time.sleep(1)
            Money = Money + Price
            clear()
            Shop()
        Money = Money - 300 * Amount
        if Money < 0:
          Money = Money + 300 * Amount
          print("\nNot enough money..")
        else:
          Food = Food + 30 * Amount
          print("\n\n",Amount,"X Large food supply purchased!\n\n")
        time.sleep(1)
        clear()
        Shop()
      elif ShopSelect == 3:
        Amount = int(input("\nHow many would you like to buy?: "))
        if Amount < 0:
          Ammo = Ammo + 1 * Amount
          if Ammo < 0:
            print("\nNot enough ammo to sell.")
            time.sleep(1)
            Ammo = Ammo + 1 * abs(Amount)
            clear()
            Shop()
          else:
            Price = 5 * abs(Amount)
            print("\nSold",abs(Amount),"X Ammo for $",Price)
            Money = Money + Price
            time.sleep(1)
            clear()
            Shop()
        Money = Money - 5 * Amount
        if Money < 0:
          Money = Money + 5*Amount
          print("\nNot enough money")
        else:
          Ammo = Ammo + 1 * Amount
          print("\n\n",Amount,"X","Ammo purchased!\n\n")
        time.sleep(1)
        clear()
        Shop()
      elif ShopSelect == 4:
        time.sleep(1)
        Money = Money - 100
        if Money < 0:
          Money = Money + 100
          print("Not enough money..")
        else:
          Water_Tablets = "Yes"
          print("\n\nWater tablets purchased!")
        clear()
        Shop()
      elif ShopSelect == 5:
        Amount = int(input("\nHow many would you like to buy?: "))
        if Amount < 0:
          Medicine = Medicine + 1 * Amount
          if Medicine < 0:
            print("\nNot enough medicine to sell.")
            time.sleep(1)
            Medicine = Medicine + 1 * abs(Amount)
            clear()
            Shop()
          else:
            Price = 50 * abs(Amount)
            print("\nSold",abs(Amount),"X Medicine for $",Price)
            time.sleep(1)
            Money = Money + Price
            clear()
            Shop()
        Money = Money - 50 * Amount
        if Money < 0:
          Money = Money + 50 * Amount
          print("\nNot enough money..")
        else:
          Medicine = Medicine + 1 * Amount
          print("\n\n",Amount,"X Medicine purchased!\n\n")
        time.sleep(1)
        clear()
        Shop()
      elif ShopSelect == 1337:
        Money = 9999
        clear()
        Shop()
      elif ShopSelect == 6:
        clear()
        save()
      elif ShopSelect == 7:
        HiddenShop()
      else:
        print("Invalid, please try again...")
        clear()
        Shop()
    else:
      print("\n\n1. Leave\n2. Rob store")
      ShopSelect = int(input("\n\nEnter selection: "))
      if ShopSelect == 1:
        clear()
        save()
      elif ShopSelect == 2:
        FoodGamble1 = random.randint(1,200)
        AmmoGamble1 = random.randint(1,150)
        MedicineGamble1 = random.randint(1,5)
        MoneyGamble1 = random.randint(500,1000)
        FoodGamble = FoodGamble1 * Difficulty
        AmmoGamble = AmmoGamble1 * Difficulty
        MedicineGamble = MedicineGamble1 * Difficulty
        MoneyGamble = MoneyGamble1 * Difficulty
        DiceRoll = random.randint(1,6)
        if DiceRoll ==1:
          for i in range (3):
            CharacterEvents()
          print("\nThe shop owner began shooting immediately, which prompted the local sherriff to bolt over. \n\nWe took heavy fire and had to leave a party member behind.")
          time.sleep(3)
          Die()
          time.sleep(2)
          save()
        elif DiceRoll >=2:
          print("\nSuccess!")
          time.sleep(2) 
          print("\nWe got",FoodGamble,"X Food,",AmmoGamble,"X Ammo, $",MoneyGamble,"and",MedicineGamble,"X Medicine!")
          Food = Food + FoodGamble
          Ammo = Ammo + AmmoGamble
          Money = Money + MoneyGamble
          time.sleep(6)
          save()
      else:
        print("Try again")
        clear()
        Shop()

def MedFunc():
  global Char1Health
  global Char2Health
  global Char3Health
  global Char4Health
  global Character_1
  global Character_2
  global Character_3
  global Character_4
  global Medicine
  if Char1Health == 'Gravely Injured' or Char1Health == 'Sick':
    print("\nWould you like to use medicine to cure",Character_1,"?")
    print("\nX",Medicine,"Medicine")
    UseMeds = input("\n(Y/N): ")
    if UseMeds == "Y" or UseMeds == "y" and Medicine >=1:
      print("\n",Character_1,"has recovered and is healthy again.")
      Char1Health = 'Healthy'
  if Char2Health == 'Gravely Injured' or Char2Health == 'Sick':
    print("\nWould you like to use medicine to cure",Character_2,"?")
    print("\nX",Medicine,"Medicine")
    UseMeds = input("\n(Y/N): ")
    if UseMeds == "Y" or UseMeds == "y" and Medicine >=1:
      print("\n",Character_2,"has recovered and is healthy again.")
      Char2Health = 'Healthy'
  if Char3Health == 'Gravely Injured' or Char3Health == 'Sick':
    print("\nWould you like to use medicine to cure",Character_3,"?")
    print("\nX",Medicine,"Medicine")
    UseMeds = input("\n(Y/N): ")
    if UseMeds == "Y" or UseMeds == "y" and Medicine >=1:
      print("\n",Character_3,"has recovered and is healthy again.")
      Char3Health = 'Healthy'
  if Char4Health == 'Gravely Injured' or Char4Health == 'Sick':
    print("\nWould you like to use medicine to cure",Character_4,"?")
    print("\nX",Medicine,"Medicine")
    UseMeds = input("\n(Y/N): ")
    if UseMeds == "Y" or UseMeds == "y" and Medicine >=1:
      print("\n",Character_4,"has recovered and is healthy again.")
      Char4Health = 'Healthy'

def CharacterEvents():
  global Difficulty
  global Character_1
  global Character_2
  global Character_3
  global Character_4
  global Char1Health
  global Char2Health
  global Char3Health
  global Char4Health
  global InjuredToken1
  global InjuredToken2
  global InjuredToken3
  global InjuredToken4
  global Medicine
  Default_Probability = 50/Difficulty
  round(Difficulty)
  injuries = ("broken","sprained","bruised","hurt","rolled")
  part = ("arm","knee","neck","ankle","foot","wrist",)
  injured = random.choice(injuries)
  bodypart = random.choice(part)
  EventChance = random.randint(1,Default_Probability)
  if EventChance < 5:
    CharacterHurt = random.randint(1,4)
    if CharacterHurt == 1:
      CharacterHurt = Character_1
      if Char1Health != 'Dead':
        if Char1Health == 'Gravely Injured':
          DiceRoll = random.randint(1,6)
          if DiceRoll <=3:
            print("|",CharacterHurt,"has",injured,"their",bodypart,", causing further complications from their previous injuries.\n\n",CharacterHurt,"has died.")
            Char1Health = 'Dead'
          else:
            print("|",CharacterHurt,"has",injured,"their",bodypart,", and is in agonizing pain from their prior injuries.\n\nThey need medicine NOW.")
        if Char1Health == 'Injured':
          print("|",CharacterHurt,"has",injured,"their",bodypart,", furthering the damage of their previous injuries.\nThey will need medicine fast.")
          Char1Health = 'Gravely Injured'
          MedFunc()
        else:
          Char1Health = 'Injured'
          InjuredToken1 = 7
          print("|",CharacterHurt,"has",injured,"their",bodypart,"and will need rest.")
    if CharacterHurt == 2:
      CharacterHurt = Character_2
      if Char2Health != 'Dead':
        if Char1Health == 'Gravely Injured':
          DiceRoll = random.randint(1,6)
          if DiceRoll <=3:
            print("|",CharacterHurt,"has",injured,"their",bodypart,", causing further complications from their previous injuries.\n\n",CharacterHurt,"has died.")
            Char2Health = 'Dead'
          else:
            print("|",CharacterHurt,"has",injured,"their",bodypart,", and is in agonizing pain from their prior injuries.\n\nThey need medicine NOW.")
        if Char2Health == 'Injured':
          print("|",CharacterHurt,"has",injured,"their",bodypart,", furthering the damage of their previous injuries.\nThey will need medicine fast.")
          Char2Health = 'Gravely Injured'
          MedFunc()
        else:
          Char2Health = 'Injured'
          InjuredToken2 = 7
          print("|",CharacterHurt,"has",injured,"their",bodypart,"and will need rest.")
    if CharacterHurt == 3:
      CharacterHurt = Character_3
      if Char3Health != 'Dead':
        if Char1Health == 'Gravely Injured':
          DiceRoll = random.randint(1,6)
          if DiceRoll <=3:
            print("|",CharacterHurt,"has",injured,"their",bodypart,", causing further complications from their previous injuries.\n\n",CharacterHurt,"has died.")
            Char3Health = 'Dead'
          else:
            print("|",CharacterHurt,"has",injured,"their",bodypart,", and is in agonizing pain from their prior injuries.\n\nThey need medicine NOW.")
        if Char3Health == 'Injured':
          print("|",CharacterHurt,"has",injured,"their",bodypart,", furthering the damage of their previous injuries.\nThey will need medicine fast.")
          Char3Health = 'Gravely Injured'
          MedFunc()
        else:
          Char3Health = 'Injured'
          InjuredToken2 = 7
          print("|",CharacterHurt,"has",injured,"their",bodypart,"and will need rest.")
    if CharacterHurt == 4:
      CharacterHurt = Character_4
      if Char4Health != 'Dead':
        if Char1Health == 'Gravely Injured':
          DiceRoll = random.randint(1,6)
          if DiceRoll <=3:
            print("|",CharacterHurt,"has",injured,"their",bodypart,", causing further complications from their previous injuries.\n\n",CharacterHurt,"has died.")
            Char4Health = 'Dead'
          else:
            print("|",CharacterHurt,"has",injured,"their",bodypart,", and is in agonizing pain from their prior injuries.\n\nThey need medicine NOW.")
        if Char4Health == 'Injured':
          print("|",CharacterHurt,"has",injured,"their",bodypart,", furthering the damage of their previous injuries.\nThey will need medicine fast.")
          Char4Health = 'Gravely Injured'
          MedFunc()
        else:
          Char4Health = 'Injured'
          InjuredToken2 = 7
          print("|",CharacterHurt,"has",injured,"their",bodypart,"and will need rest.")
    time.sleep(3)

def AreWeTHATDesperate():
  global Ammo
  global Food
  global Money
  global Karma
  global DesperateToken
  if Food < 30 and Ammo < 20:
    DesperateToken = DesperateToken + 1
    if DesperateToken == 5:
      if Karma >=-5:
        print("\n",Food,"X Food\n",Ammo,"X Ammo")
        print("| Our supplies are running dangerously low, and we might not make it to the next town.\nHowever, we noticed a few other wagons on the trail...\nWe could really use those supplies. I mean REALLY use those supplies, right? Right??")
      elif Karma < -5 and Karma >= -7:
        print("\n",Food,"X Food\n",Ammo,"X Ammo")
        print("| Our supplies are running low, and we see a few wagons with minimal security travelling. We could use those supplies more, right? ")
      elif Karma < -7:
        print("\n",Food,"X Food\n",Ammo,"X Ammo")
        print("| Our supplies have run out once again, and all these other wagons have plenty.\nShall we?")
      Choice = input("\nY/N: ")
      DesperateToken = 0
      if Choice == "Y" or Choice == "y":
        DiceRoll = random.randint(1,6)
        FoodGained = 20*DiceRoll
        AmmoGained = 10*DiceRoll
        if DiceRoll ==2:
          for i in range(5):
            CharacterEvents()
          print("\nThey started shooting back immediately, and we sustained several injuries and one casualty. However, in their haste to escape us, they dropped some supplies to lighten their wagon.")
          time.sleep(1)
          Food = Food + 50
          Ammo = Ammo + 40
        elif DiceRoll ==1:
          Die()
          print("\nThey shot back immediately and killed one of us before dissapearing in the mountains. We must push on without supplies, and minus a party member.")
        elif DiceRoll >2:
          if Karma >=-5:
            print("\nWe got the supplies, but we feel terrible. Let's never talk about it again.")
            FoodGained = 50 * Difficulty
            AmmoGained = 30 * Difficulty
            MoneyGained = 50 * Difficulty
            Food = Food + FoodGained
            Ammo = Ammo + AmmoGained
            Money = Money + MoneyGained
            print("\nLooted $",MoneyGained,", X",AmmoGained,"Ammo, and",FoodGained,"food.")
            Karma = Karma - 1
          else:
            print("\nWe obtained their supplies and continued on our adventure.")
            FoodGained = 50 * Difficulty
            AmmoGained = 50 * Difficulty
            MoneyGained = 100 * Difficulty
            print("\nLooted $",MoneyGained,", X",AmmoGained,"Ammo, and",FoodGained,"food.")
            Food = Food + FoodGained
            Ammo = Ammo + AmmoGained
            Money = Money + MoneyGained
            Karma = Karma -1

def LocationFunc():
  global Location
  global Town
  if Town == 0:
    Location = "Hanover"
  if Town == 1:
    Location = "Sawk Trail Trading Post"
  if Town == 2:
    Location = "Nashville"
  if Town == 3:
    Location = "Nebraska State Trading Post"
  if Town == 4:
    Location = "Denver Trading Post"
  if Town == 5:
    Location = "Wyoming Remote Trader"
  if Town == 6:
    Location = "Idaho State Trading Post"
  if Town == 7:
    Location = "Oregon State Traders"
  if Town == 8:
    Location = "Home Stretch"
  Town = Town + 1

def SickCheck():
  global Difficulty
  Default_Probability = 100/Difficulty
  Probability = random.randint(1,Default_Probability)
  if Probability == 1:
    Sick()

def Story():
    global Location
    global Miles
    print("\nYou embark from",Location,"for your next waypoint about",Miles,"miles west...")
    print("X")
    for i in range(Miles):
        time.sleep(.8)
        print("|")
        StoryEvents()
        TroubleCheck()
        FoodCheck()
        DoWeNeedFood()
        TokenCheck()
        AreWeTHATDesperate()
        SickCheck()
        MedFunc()
    sys.stdout.write("X")
    LocationFunc()
    print("\nYou have arrived at",Location,"and elect to stop by the store for supplies.")
    time.sleep(3)
    Shop()

def Sick():
  global Char1Health
  global Char2Health
  global Char3Health
  global Char4Health
  global Character_1
  global Character_2
  global Character_3
  global Character_4
  CharacterHurt = random.randint(1,4)
  if CharacterHurt == 1:
    CharacterHurt = Character_1
    if Char1Health != 'Dead':
      if Char1Health == 'Gravely Injured':
        print("\n|",CharacterHurt,"has fallen ill on top of their previous injuries, causing complications.\n",Character_1,"has died.")
        Char1Health = 'Dead'
      elif Char1Health == 'Healthy':
        print("\n|",CharacterHurt,"has contracted a nasty sickness and needs medicine.")
        Char1Health = 'Sick'
        MedFunc()
      elif Char1Health == 'Injured':
        print("\n|",CharacterHurt,"has contracted an illness, furthering the damage of their previous injuries.\nThey will need medicine fast.")
        Char1Health = 'Gravely Injured'
        MedFunc()
      elif Char1Health == 'Sick':
        print("\n|",Character_1,"contracted a second illness, causing severe complications.\n",Character_1,"has died.")
        Char1Health = 'Dead'
  if CharacterHurt == 2:
    CharacterHurt = Character_2
    if Char2Health != 'Dead':
      if Char2Health == 'Gravely Injured':
        print("\n|",CharacterHurt,"has fallen ill on top of their previous injuries, causing complications.\n",Character_2,"has died.")
        Char2Health = 'Dead'
      elif Char2Health == 'Healthy':
        print("\n|",CharacterHurt,"has contracted a nasty sickness and needs medicine.")
        Char2Health = 'Sick'
        MedFunc()
      elif Char2Health == 'Injured':
        print("\n|",CharacterHurt,"has contracted an illness, furthering the damage of their previous injuries.\nThey will need medicine fast.")
        Char2Health = 'Gravely Injured'
        MedFunc()
      elif Char2Health == 'Sick':
        print("\n|",Character_3,"contracted a second illness, causing severe complications.\n",Character_3,"has died.")
        Char2Health = 'Dead'
    if CharacterHurt == 3:
      CharacterHurt = Character_3
      if Char3Health != 'Dead':
        if Char3Health == 'Gravely Injured':
          print("\n|",CharacterHurt,"has fallen ill on top of their previous injuries, causing complications.\n",Character_3,"has died.")
          Char3Health = 'Dead'
        elif Char3Health == 'Healthy':
          print("\n|",CharacterHurt,"has contracted a nasty sickness and needs medicine.")
          Char3Health = 'Sick'
          MedFunc()
        elif Char3Health == 'Injured':
          print("\n|",CharacterHurt,"has contracted an illness, furthering the damage of their previous injuries.\nThey will need medicine fast.")
          Char3Health = 'Gravely Injured'
          MedFunc()
        elif Char3Health == 'Sick':
          print("\n|",Character_3,"contracted a second illness, causing severe complications.\n",Character_3,"has died.")
          Char3Health = 'Dead'
    if CharacterHurt == 4:
      CharacterHurt = Character_4
      if Char4Health != 'Dead':
        if Char4Health == 'Gravely Injured':
          print("\n|",CharacterHurt,"has fallen ill on top of their previous injuries, causing complications.\n",Character_4,"has died.")
          Char4Health = 'Dead'
        elif Char4Health == 'Healthy':
          print("\n|",CharacterHurt,"has contracted a nasty sickness and needs medicine.")
          Char4Health = 'Sick'
          MedFunc()
        elif Char4Health == 'Injured':
          print("\n|",CharacterHurt,"has contracted an illness, furthering the damage of their previous injuries.\nThey will need medicine fast.")
          Char4Health = 'Gravely Injured'
          MedFunc()
        elif Char4Health == 'Sick':
          print("\n|",Character_4,"contracted a second illness, causing severe complications.\n",Character_4,"has died.")
          Char4Health = 'Dead'

def StoryEvents():
  global Difficulty
  global Food
  global Ammo
  global Money
  global Karma
  global Water_Tablets
  Default_Probability = 100 / Difficulty
  round(Default_Probability)
  EventProbability = random.randint(1,Default_Probability)
  Event = random.randint(1,4)
  if EventProbability <5:
    if Event == 1:
      print("| You come to a river, will you attempt to ford (Risky) or go around the river? (+ Several Days Travel)")
      FordRiver = input("\n(Ford/Around): ")
      if FordRiver == "Ford" or FordRiver == "ford":
        DiceRoll = random.randint(1,6)
        if DiceRoll >=3:
          CharacterEvents()
          print("\nSuccessfully forded the river and continued on our journey.")
        if DiceRoll <3:
          for i in range(5):
            CharacterEvents()
          print("\nThe ford was rough, but we got by with a lot of scrapes and bruises.")
      if FordRiver == "Around" or FordRiver == "around":
        print("\nWe added a few days to our journey, but we made it around.")
        Food = Food - 30
    elif Event == 2:
      if Karma > -5:
        print("\n| We're under attack by bandits! Will we fight back (Risky) or try to lose them? (+ Several Days Travel) ")
        Attack = input("\n(Fight/Run): ")
        if Attack == "Fight" or Attack == "fight":
          DiceRoll = random.randint(1,6)
          if DiceRoll >=3:
            CharacterEvents()
            Ammo = Ammo - 10
            print("\nSuccessfully fought off the bandits.. but..")
            print("\n",Ammo,"X Ammo\n",Food,"X Food\n")
            Looty = input("\nShould we loot the bodies..?\n\n(Y/N): ")
            if Looty == "y" or Looty == "Y":
              InfectionRoll = random.randint(1,6)
              if Food <=60:
                print("\nWe really needed the supplies, so we don't feel too bad about it.")
                FoodLoot = 10*DiceRoll 
                MoneyLoot = 100*DiceRoll
                Food = Food + FoodLoot
                Money = Money + MoneyLoot
                print("\nLooted $",MoneyLoot,"and",FoodLoot,"food.")
              else:
                print("\nWe didn't really need them, but extra supplies are always welcome.")
                FoodLoot = 10*DiceRoll 
                MoneyLoot = 100*DiceRoll
                Food = Food + FoodLoot
                Money = Money + MoneyLoot
                print("\nLooted $",MoneyLoot,"and",FoodLoot,"food.")
                Karma = Karma - 1
              if InfectionRoll == 1:
                print("\nWe think one of those bandits had a nasty skin disease\nIt's starting to cover our skin..")
                Sick()
          if DiceRoll <3:
            for i in range(5):
              CharacterEvents()
            print("\nWe lost one of our party members to a stray bullet and suffered several injuries.")
            Die()
        if Attack == "Run" or Attack == "run":
          for i in range(5):
            CharacterEvents()
          print("\nThey hit a couple of us, but nothing life threatening. We lost some food though.")
          Food = Food - 20
      if Karma < -5:
        print("\n| Some bandits spotted us, recognized our wagon, and turned around instantly.")
        time.sleep(1)
        if Karma < -7:
          print("\nShould we chase after them?")
          choice = input("\nY/N: ")
          if choice == "Y" or choice == "y":
            FoodGained = 200 * Difficulty
            AmmoGained = 150 * Difficulty
            MoneyGained = 300 * Difficulty
            print("\nWe followed them back to their camp, which ended up being ripe pickings.")
            print("\nLooted $",MoneyGained,", X",AmmoGained,"Ammo, and",FoodGained,"food.")
            Food = Food + FoodGained
            Ammo = Ammo + AmmoGained
            Money = Money + MoneyGained
    elif Event == 3:
      if Water_Tablets == "Yes":
        print("| The water looks suspicious, it's a good thing we picked up water tablets.")
      elif Water_Tablets == "No":
        print("| You have died of Dysentary.")
        Die()
    elif Event == 4:
      print("| A wagon stuck on the side of the road flags you down as you pass,\n begging for food and any supplies you can spare.\n What would we be willing to part with?")
      time.sleep(2)
      print("\n",Ammo,"X Ammo\n",Food,"X Food\n")
      Charity = int(input("\n1. 20 Ammo\n2. 30 Food\n3. Rob Them\n4. Nothing\n: "))
      if Charity == 1:
        if Ammo > 50:
          print("\nWe had a surplus of ammo anyways, and they were instantly overjoyed\n to be able to hunt food. We walked away feeling good about ourselves.")
          Karma = Karma + 1
        if Ammo <=50:
          print("\nWe don't have much ammo left, but we handed them a few handfuls.\n We'd never seen anybody so grateful in our lives.")
          Karma = Karma + 2
        Ammo = Ammo - 50
      elif Charity == 2:
        if Food > 60:
          print("\nWe had a lot of food to spare anyways, so we didn't mind sharing.\n They must have been starving, because they started eating immediately.\nThey gave us some money for our troubles.\n+$200")
          Money = Money + 200
          Karma = Karma + 1
        if Food <= 60:
          print("\nDespite having little food ourselves, we opted to share. \nWe'd never seen a bunch more grateful.\nThey gave us some money for our troubles.\n+$300")
          Money = Money + 300
        Food = Food - 30
      elif Charity == 3:
        print("\nThey didn't have much food or ammo, but they had medicine.")
        Food = Food + 20
        Ammo = Ammo + 10
        if Karma >=0:
          print("\nWe feel terrible about what we did. \nDid we really need the supplies that bad?")
          Karma = Karma - 2
        else:
          print("\nThey were doomed to begin with, we could use those supplies more.")
          Karma = Karma - 3
      elif Charity == 4:
        if Ammo >=50:
          print("\nWe're not a charity, so we drove right past them. \nOur supplies are ours.")
          Karma = Karma - 3
        if Ammo <50:
          print("\nWe barely have any supplies left as is. \nWe want to help, but we would die before we make it to the next town.")
    elif Event == 5:
      test = 5
    

def DifficultySelect():
  global Difficulty
  global Money
  global Food
  global Miles
  DifficultySelect = int(input("\nSelect difficulty\n1. Easy\n2. Normal\n3. Hard\n4. Nightmare\n\n\n: "))
  if DifficultySelect == 1:
    Money = 1000
    Difficulty = DifficultySelect
    Food = 200
  elif DifficultySelect == 2:
    Money = 700
    Difficulty = DifficultySelect
    Food = 90
  elif DifficultySelect == 3:
    Money = 500
    Difficulty = 4
    Food = 50
  elif DifficultySelect == 4:
    Money = 100
    Difficulty = 10
    Food = 10

def mainmenu():
  global PlayerName
  txt = open("highscores").readlines()
  print("Welcome to the Oregon Trail\n\nHigh Scores:\n",txt)
  Menu = int(input("\n\n1. New Game\n\n2. Load Game\n\n3. User Manual\n\n: "))
  if Menu == 1:
    print("\nBeginning new game..")
    PlayerName = input("\nEnter name for save file\nName: ")
  elif Menu == 2:
    load()
  elif Menu == 3:
    clear()
    a_file = open("usermanual.txt")
    lines = a_file.readlines()
    for line in lines:
      print(line)
    entertocontinue = input("\n\n\nEnter to continue\n")
    clear()
    mainmenu()
  else:
    print("Beginning new game...")
    PlayerName = input("\nEnter name for save file\nName: ")


def save():
  global Money
  global Difficulty
  global Food
  global Ammo
  global Town
  global PlayerName
  global Character_1
  global Character_2
  global Character_3
  global Character_4
  global Char1Health
  global Char2Health
  global Char3Health
  global Char4Health
  global Karma
  global Location
  global Water_Tablets
  global Medicine
  Save = input("\n\nDo you want to save your progress? \nY/N:")
  if Save == 'Y' or Save == 'y':
    file = open(PlayerName + "save.txt", "w")
    MoneySTR = Money
    FoodSTR = Food
    AmmoSTR = Ammo
    TownSTR = Town
    DifficultySTR = Difficulty
    KarmaSTR = Karma
    MedSTR = Medicine
    MoneySTR = repr(MoneySTR)
    FoodSTR = repr(FoodSTR)
    AmmoSTR = repr(AmmoSTR)
    TownSTR = repr(TownSTR)
    DifficultySTR = repr(DifficultySTR)
    KarmaSTR = repr(KarmaSTR)
    MedSTR = repr(MedSTR)
    file.write(MoneySTR+"/"+FoodSTR+"/" +AmmoSTR+"/"+TownSTR+"/"+DifficultySTR+"/"+Character_1+"/"+Character_2+"/"+Character_3+"/"+Character_4+"/"+Char1Health+"/"+Char2Health+"/"+Char3Health+"/"+Char4Health+"/"+KarmaSTR+"/"+PlayerName+"/"+Location+"/"+Water_Tablets+"/"+MedSTR)
    file.close
    clear()
    print("\nGame saved.")

def load():
  global Money
  global Food
  global Ammo
  global Town
  global Difficulty
  global Character_1
  global Character_2
  global Character_3
  global Character_4
  global Char1Health
  global Char2Health
  global Char3Health
  global Char4Health
  global Karma
  global PlayerName
  global Location
  global Water_Tablets
  global Medicine
  PlayerName = input("\nEnter name on save file\nName: ")
  txt = open(PlayerName + "save.txt","r").readlines()
  MoneySTR = (txt[0].split("/")[0])
  FoodSTR = (txt[0].split("/")[1])
  AmmoSTR = (txt[0].split("/")[2])
  TownSTR = (txt[0].split("/")[3])
  DifficultySTR = (txt[0].split("/")[4])
  Character_1 = (txt[0].split("/")[5])
  Character_2 = (txt[0].split("/")[6])
  Character_3 = (txt[0].split("/")[7])
  Character_4 = (txt[0].split("/")[8])
  Char1Health = (txt[0].split("/")[9])
  Char2Health = (txt[0].split("/")[10])
  Char3Health = (txt[0].split("/")[11])
  Char4Health = (txt[0].split("/")[12])
  KarmaSTR = (txt[0].split("/")[13])
  PlayerName = (txt[0].split("/")[14])
  Location = (txt[0].split("/")[15])
  Water_Tablets = (txt[0].split("/")[16])
  MedSTR = (txt[0].split("/")[17])
  Money = Money + int(MoneySTR)
  Food = Food + int(FoodSTR)
  Ammo = Ammo + int(AmmoSTR)
  Town = Town + int(TownSTR)
  Difficulty = Difficulty + int(DifficultySTR)
  Karma = Karma + int(KarmaSTR)
  Medicine = Medicine + int(MedSTR)
  Character_1 = str(Character_1)
  Character_2 = str(Character_2)
  print("\nLoaded Successfully")
  print("-----------------\nDEBUG MODE\n\n")
  print(globals())
  cont = input("\n\nEnter to continue")
  Shop()
  StoryLoop()

def Ending():
  global Money
  global Karma
  global Food
  global Ammo
  global Char1Health
  global Char2Health
  global Char3Health
  global Char4Health
  CharsAlive = 0
  if Char1Health != 'Dead':
    CharsAlive = CharsAlive + 1
  if Char2Health != 'Dead':
    CharsAlive = CharsAlive + 1
  if Char3Health != 'Dead':
    CharsAlive = CharsAlive + 1
  if Char4Health != 'Dead':
    CharsAlive = CharsAlive + 1
  print("\nYou reach your destination, ready to start your new life.")
  time.sleep(2)
  if Karma >= 10:
    print("\nThe several people you helped along the way wait for you at the gate, expressing their gratitude and showering you with gifts. \nYou are beloved by the community and are offered the best the town has to offer. \nYou can rest easy in your new life of luxury.")
  if Karma >= -3 and Karma < 10:
    print("\nYou enter the gate and find a small home using whatever money you had left. \nYou can rest easy knowing you've made it.")
  if Karma <= -4 and Karma >= -7:
    print("\nBut word of the terrible things you did on the trail spread fast, and you were shunned by the community. \nYou decide to live as a hermit in the mountains instead.")
  if Karma < -7 and Karma >= -10:
    print("\nBut the atrocities you committed to get here would haunt you, \nas the community meets you with torches and pitchforks, calling you a 'murderer' and a 'monster'. \nYou flee to the mountains to begin a new life away from society.")
  if Karma < -10:
    print("\nBut you are met at the gate with rifles cocked and loaded. \nYou have become an infamous outlaw wanted for the murder of dozens. \nYou are forced to reside to a life as a bandit, as you are shunned by all communities except the criminal world.")
  HighScore = Money + Food + Ammo *CharsAlive
  print("\nYour score is",HighScore)
  Scoreboard = input("Enter name for scoreboard: ")
  HighScoreSTR = repr(HighScore)
  Writing = (Scoreboard+"   "+HighScoreSTR)
  file = open("highscores", "w")
  file.write(Writing)
  file.close
  time.sleep(3)
  print("\nTry again?")
  choice = input("Y/N: ")
  if choice == 'N' or choice == 'n':
    time.sleep(300)


def StoryLoop():
  global Miles
  global Town
  while Town <= 8:
    RandomMiles = random.randint(10,15)
    Miles = Miles + RandomMiles
    Story()
    clear()
  Ending()

def main():
  mainmenu()
  CharacterSelect()
  DifficultySelect()
  clear()
  LocationFunc()
  Shop()
  clear()
  StoryLoop()

main()
