def quiz(question, answer, score):
    i = -1
    while i < 11:
        i += 1
        print(question[i])
        user_input = int(input("Enter your answer :- "))
        if user_input == answer[i]:
            print("\nYOUR ANSWER IS CORRECT \n\n")
            score += 1
        elif user_input != answer[i] and user_input > 0 and user_input < 5:
            print("\nYOUR ANSWER IS INCORRECT \n\n")
        else:
            print("\nINVALID OPTION\n\n")
            i -= 1
    return score


bollywoodQuestion = (
    "Q1. In the movie Piku, what does Amitabh Bachchan's character (Bhashkor Banerjee) suffer from?\n1 CANCER\n2 ERECTILE DYSFUNCTIONse\n3 ARTHRITIS\n4 CHRONIC CONSTIPATION ",
    "Q2. The story of Kabhi Khushi Kabhie Gham revolves around the trials and tribulations of which family?\n1 THE MALHOTRAS\n2 THE RAICHANDS\n3 THE SINGHANIAS\n4 THE OBEROIS",
    "Q3. In Hera Pheri, what was Paresh Rawal's character called?\n1 RAJU\n2 DEVI PRASAD\n3 SHYAM\n4 BABURAO GANPATRAO APTE ",
    "Q4. In Dear Zindagi, what does Shah Rukh Khan's character, Dr Jehangir Khan, do?\n1 HE IS A THERAPIST\n2 HE IS AN ARCHITECT\n3 HE IS AN ACTOR\n4 HE IS A JOURNALIST ",
    "Q5. According to song'pappu can not dance', what brand of shirt does Pappu wear?\n1 PRADA\n2 GUCCI\n3 ARMANI\n4 CHANEL ",
    "Q6. Which movie is this popular line from:'Dosti ka ek usool hai madam - no sorry, no thank you.'\n1 KUCH KUCH HOTA HAI\n2 DILWALE DULHANIA LE JAYEGE\n3 MAINE PYAR KIYA\n4 ANDAZ APNA APNA ",
    "Q7. In the movie Kahaani, which Indian city does Vidya Bagchi visit in order to search for her missing husband?\n1 AGRA\n2 MUMBAI\n3 KOLKATA\n4 CHENNAI ",
    "Q8. Finish the quote from Om Shanti Om: 'Ek chutki sindoor ki keemat, tum kya jaano ___?\n1 OM BABU\n2 MAHESH BABU\n3 RAMESH BABU\n4 NAALAYAK",
    "Q9. What is the name of Saif Ali Khan from the movie Omkara?\n1 RANCHHODDAS SHAMALDAS CHANCHAD\n2 GABBAR SINGH\n3 SARDAR KHAN\n4 LANGDA TYAGI ",
    "Q10. In Jab We Met, what is the name of Geet's cousin?\n1 ROOP\n2 SIMRAN\n3 PREET\n4 PRIYA ",
)

bollywoodAnswer = (4, 2, 4, 1, 2, 3, 3, 3, 4, 1)

generalQuestion = (
    "Q1 WHO IS THE FIRST WOMAN PRESIDENT OF UN GENERAL ASSEMBLY?\n1.VIJAYA LAKSHMI PANDIT\n2.MARIA ESTELA PERON\n3.ANEXIAMANDER\n4.MARCO POLO",
    "Q2 WHO IS THE FIRST MAN TO REACH NORTH POLE?\n1.ROBERT PEARY\n2.ROALD AMUNDSEN\n3.MARCO POLO\n4.TRYGVE LIE",
    "Q3 WHO IS FIRST SPACE TOURIST?\n1.NIKOLAI BULGANIN\n2.ALEXEY LEONOV\n3.DENNIS TITO\n4.NAWANG GAMBU",
    "Q4 WHO IS THE FIRST EUROPEAN TO VISIT CHINA?\n1.REITA FARIA\n2.MARCO POLO\n3.JANET YELLEN\n4.FRANCES PHIPPS",
    "Q5 WHICH IS THE FIRST CITY IS TO BE ATTACKED WITH ATOM BOMB?\n1.WUHAN\n2.JOHANSBERG\n3.HIROSHIMA\n4.NAGASAKI",
    "Q6 WHO IS THE FIRST EDUCATION MINISTER OF INDIA?\n1.DR. RADHAKRISHNAN\n2.AMARTYASEN\n3.DR. ZAKIR HUSSAIN\n4.ABDUL KALAM AZAD",
    "Q7 WHICH IS THE FIRST BANK OF INDIA?\n1.STATE BANK OF INDIA\n2.BANK OF HINDUSTAN\n3.DENA BANK\n4.PUNJAB NATIONAL BANK",
    "Q8 WHO IS THE FIRST INDIAN WOMAN TO RECIEVE ASHOKA CHAKRA?\n1.NIRAJ BHANOT\n2.MOTHER TERESA\n3.PUNEETA ARORA\n4.REITA FARIA",
    "Q9 WHO IS THE FIRST COUNTRY TO ISSUE PAPER CURRENCY?\n1.INDIA\n2.USA\n3.RUSSIA\n4.CHINA",
    "Q10 WHICH IS THE FIRST SPACESHIP LAUNCHED ON MOON?\n1.VIKING-1\n2.COLOMBO\n3.ARAYABHATTA\n4.AGNI"
)

generalAnswer = (1, 1, 3, 2, 3, 4, 2, 1, 4, 1)


sportsQuestion = (
    "Q1 WORLD FIRST TEST MATCH IS PLAYED BETWEEN WHICH TEAMS?\n1.INDIA v/s ENGLAND\n2.INDIA v/s AUSTRALIA\n3.AUSTRALIA v/s ENGLAND\n4.AUSTRALIA v/s NEW ZEALAND",
    "Q2 HOW MANY MEDALS DOES INDIA HAVE WON IN TOKYO OLYMPICS 2020?\n1. 7\n2. 6\n3. 5\n4. 4",
    "Q3 WHO WON THE FIRST MEDAL FOR INDIA IN TOKYO OLYMPICS 2020?\n1.NEERAJ CHOPRA\n2.MIRABAI CHANU\n3.P.V SINDHU\n4.RAVI KUMAR DHAIYA",
    "Q4 WHO WON BRONZE MEDAL FOR INDIA IN WRESTLING IN TOKYO 2020?\n1.RUPINDAR PAL SINGH\n2.BAJRANG PUNIA\n3.MANDEEP SINGH\n4.AMIT ROHIDAS",
    "Q5 WHO WON FIRST GOLD MEDAL FOR INDIA IN TOKYO 2020?\n1.MANDEEP SINGH\n2.NEERAJ CHOPRA\n3.VARUN KUMAR\n4.SUMIT",
    "Q6 IN WHICH FIELD DOES INDIA WON THE GOLD MEDAL?\n1.JAVELLIN THROW\n2.HOCKEY\n3.TENNIS\n4.WEIGHT LIFTING",
    "Q7 WHAT IS THE VENUE FOR THE WORLD TEST CHAMPIONSHIP (2019-2021) WHICH IS PLAYED BETWEEN INDIA v/s NEW ZEALAND?\n1.THE AGEAS BOWL\n2.THE OVAL\n3.OLD TARAFFORD\n4.TRENT BRIDGE",
    "Q8 WHAT IS THE VENUE FOR CRICKET WORLD CUP FINAL 2019?\n1.LORD'S\n2.OLD TARAFFORD\n3.TRENT BRIDGE\n4.THE OVAL",
    "Q9 IN WHICH COUNTRY DOES THE FIRST T20 WORLD CUP PLAYED IN 2007?\n1.SOUTH AFRICA\n2.INDIA\n3.ENGLAND & WALES\n4.AUSTRALIA",
    "Q10 WHO IS THE PLAYER OF SERIES IN 2011 WORLD CUP?\n1.YUVRAJ SINGH\n2.M.S DHONI\n3.KUMAR SANGAKARA\n4.SACHIN TENDULKAR"
)

sportsAnswer = (3, 1, 2, 2, 2, 1, 1, 1, 1, 1)

print("---------------------------------------------")
print("Welcome to the Battle Of Brains the Quiz Game")
print("---------------------------------------------")
print("General Instructions:-\n1. There are 3 different groups of questions.\n  A. Bollywood Quiz\n  B. General Knowledge Quiz\n  C. Sports Quiz\n2. Every group contains 10 questions of M.C.Q type\n")
c = int(input("CHOOSE BETWEEN CATEGORIES 1, 2, 3\n1. BOLLYWOOD QUIZ\n2. GENRAL KNOWLEDGE QUIZ\n3. SPORTS QUIZ\nEnter your choice=> "))
yourAnswer = "Enter your answer :- "
yourScore = "Your score = "
if c == 1:
    print(yourScore + str(quiz(bollywoodQuestion, bollywoodAnswer, 0)))
elif c == 2:
    print(yourScore + str(quiz(generalQuestion, generalAnswer, 0)))
else:
    print(yourScore + str(quiz(sportsQuestion, sportsAnswer, 0)))