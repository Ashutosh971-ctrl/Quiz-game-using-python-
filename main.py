yourAnswer = 'Enter your answer :- '
correctAnswer = 'CONGRATS! YOUR ANSWER IS CORRECT '
incorrectAnswer = 'OPPS! YOUR ANSWER IS INCORRECT '
invalidAnswer = 'SORRY! YOU ENTER A INVALID OPTION. PLEASE ENTER A VALID ONE '

print("                                          Welcome to the Battle Of Brains the Quiz Game ")
us = "BATTLE_OF_BRAINS"
for f in range(3):
    u1 = input("Enter user name:-")
    d = 2
    if us == u1:
        print("NOW YOU CAN PROCEED TOWARDS ENTERING THE PASSWORD")
        pa = 'bobs@123'
        for g in range(3):
            p = input("Enter the password:-")
            h = 2
            if pa == p:
                print("CONGRATS!! :)")
                print("NOW YOU CAN PLAY THE GAME")
                print("General Instructions:-\n1. There are 3 different groups of questions.\n  A. Bollywood Quiz\n  B. General Knowledge Quiz\n  C. Sports Quiz\n2. Every group contains 10 questions of M.C.Q type\n3. Attempting all questions of any group is necessary\n4. Filling your bio-data is necessary")
                print("---------------------------------------------------------------------------------------------------------------------")
                n = input(yourAnswer)
                c = int(input(
                    "CHOOSE BETWEEN CATEGORIES 1, 2, 3 \n1. BOLLYWOOD QUIZ \n2. GENRAL KNOWLEDGE QUIZ \n3. SPORTS QUIZ \nEnter your choice=> "))
                a = 0
                s = int(a)
                if c == 1:
                    print(
                            "                                             YOU HAVE CHOSEN BOLLYWOOD QUIZ")
                    print("..........................................................................................................................................................................................................................................")
                    print("""Q1. In the movie Piku, what does Amitabh Bachchan's character (Bhashkor Banerjee) suffer from?
                          1 CANCER
                          2 ERECTILE DYSFUNCTIONse
                          3 ARTHRITIS
                          4 CHRONIC CONSTIPATION """)
                    ans = int(input(yourAnswer))
                    if ans == 4:
                        print(correctAnswer)
                        s += 1
                    elif (ans == 1 or ans == 2 or ans == 3):
                        print(incorrectAnswer)
                        s += 0
                    elif ans > 4:
                        print(invalidAnswer)
                    print("""Q2. The story of Kabhi Khushi Kabhie Gham revolves around the trials and tribulations of which family?
                          1 THE MALHOTRAS
                          2 THE RAICHANDS
                          3 THE SINGHANIAS
                          4 THE OBEROIS""")
                    ans = int(input(yourAnswer))
                    if ans == 2:
                        print(correctAnswer)
                        s += 1
                    elif (ans == 1 or ans == 4 or ans == 3):
                        print(incorrectAnswer)
                        s += 0
                    else:
                        print(invalidAnswer)

                    print("""Q3. In Hera Pheri, what was Paresh Rawal's character called?
                          1 RAJU
                          2 DEVI PRASAD
                          3 SHYAM
                          4 BABURAO GANPATRAO APTE """)
                    ans = int(input(yourAnswer))
                    if ans == 4:
                        print(correctAnswer)
                        s += 1
                    elif (ans == 1 or ans == 2 or ans == 3):
                        print(incorrectAnswer)
                        s += 0
                    else:
                        print(invalidAnswer)

                    print("""Q4. In Dear Zindagi, what does Shah Rukh Khan's character, Dr Jehangir Khan, do?
                          1 HE IS A THERAPIST
                          2 HE IS AN ARCHITECT
                          3 HE IS AN ACTOR
                          4 HE IS A JOURNALIST """)
                    ans = int(input(yourAnswer))
                    if ans == 1:
                        print(correctAnswer)
                        s += 1
                    elif (ans == 4 or ans == 2 or ans == 3):
                        print(incorrectAnswer)
                        s += 0
                    else:
                        print(invalidAnswer)

                    print("""Q5. According to song'pappu can not dance', what brand of shirt does Pappu wear?
                          1 PRADA
                          2 GUCCI
                          3 ARMANI
                          4 CHANEL """)
                    ans = int(input(yourAnswer))
                    if ans == 2:
                        print(correctAnswer)
                        s += 1
                    elif (ans == 1 or ans == 4 or ans == 3):
                        print(incorrectAnswer)
                        s += 0
                    else:
                        print(invalidAnswer)

                    print("""Q6. Which movie is this popular line from:"Dosti ka ek usool hai madam - no sorry, no thank you.'
                          1 KUCH KUCH HOTA HAI
                          2 DILWALE DULHANIA LE JAYEGE
                          3 MAINE PYAR KIYA
                          4 ANDAZ APNA APNA """)
                    ans = int(input(yourAnswer))
                    if ans == 3:
                        print(correctAnswer)
                        s += 1
                    elif (ans == 1 or ans == 2 or ans == 4):
                        print(incorrectAnswer)
                        s += 0
                    else:
                        print(
                                invalidAnswer)

                    print("""Q7. In the movie Kahaani, which Indian city does Vidya Bagchi visit in order to search for her missing husband?
                          1 AGRA
                          2 MUMBAI
                          3 KOLKATA
                          4 CHENNAI """)
                    ans = int(input(yourAnswer))
                    if ans == 3:
                        print(correctAnswer)
                        s += 1
                    elif (ans == 1 or ans == 2 or ans == 4):
                        print(incorrectAnswer)
                        s += 0
                    else:
                        print(
                                invalidAnswer)

                    print("""Q8. Finish the quote from Om Shanti Om: 'Ek chutki sindoor ki keemat, tum kya jaano ___?
                          1 OM BABU
                          2 MAHESH BABU
                          3 RAMESH BABU
                          4 NAALAYAK""")
                    ans = int(input(yourAnswer))
                    if ans == 3:
                        print(correctAnswer)
                        s += 1
                    elif (ans == 1 or ans == 2 or ans == 4):
                        print(incorrectAnswer)
                        s += 0
                    else:
                        print(
                                invalidAnswer)

                    print("""Q9. What is the name of Saif Ali Khan from the movie Omkara?
                          1 RANCHHODDAS SHAMALDAS CHANCHAD
                          2 GABBAR SINGH
                          3 SARDAR KHAN
                          4 LANGDA TYAGI """)
                    ans = int(input(yourAnswer))
                    if ans == 4:
                        print(correctAnswer)
                        s += 1
                    elif (ans == 1 or ans == 2 or ans == 3):
                        print(incorrectAnswer)
                        s += 0
                    else:
                        print(invalidAnswer)

                    print("""Q10. In Jab We Met, what is the name of Geet's cousin?
                          1 ROOP
                          2 SIMRAN
                          3 PREET
                          4 PRIYA """)
                    ans = int(input(yourAnswer))
                    if ans == 1:
                        print(correctAnswer)
                        s += 1
                    elif (ans == 4 or ans == 2 or ans == 3):
                        print(incorrectAnswer)
                        s += 0
                    else:
                        print(invalidAnswer)

                if c == 2:
                    print(
                            "                                             YOU HAVE CHOSEN GENERAL KNOWLEDGE QUIZ")
                    print("..........................................................................................................................................................................................................................................")
                    print("""Q1 WHO IS THE FIRST WOMAN PRESIDENT OF UN GENERAL ASSEMBLY?
                          1.VIJAYA LAKSHMI PANDIT
                          2.MARIA ESTELA PERON
                          3.ANEXIAMANDER
                          4.MARCO POLO""")
                    ans = int(input(yourAnswer))
                    if ans == 1:
                        print(correctAnswer)
                        s += 1
                    elif (ans == 4 or ans == 2 or ans == 3):
                        print(incorrectAnswer)
                        s += 0
                    else:
                        print(invalidAnswer)

                    print("""Q2 WHO IS THE FIRST MAN TO REACH NORTH POLE?
                          1.ROBERT PEARY
                          2.ROALD AMUNDSEN
                          3.MARCO POLO
                          4.TRYGVE LIE""")
                    ans = int(input(yourAnswer))
                    if ans == 1:
                        print(correctAnswer)
                        s += 1
                    elif (ans == 4 or ans == 2 or ans == 3):
                        print(incorrectAnswer)
                        s += 0
                    else:
                        print(invalidAnswer)

                    print("""Q3 WHO IS FIRST SPACE TOURIST?
                          1.NIKOLAI BULGANIN
                          2.ALEXEY LEONOV
                          3.DENNIS TITO
                          4.NAWANG GAMBU""")
                    ans = int(input(yourAnswer))
                    if ans == 3:
                        print(correctAnswer)
                        s += 1
                    elif (ans == 4 or ans == 2 or ans == 1):
                        print(incorrectAnswer)
                        s += 0
                    else:
                        print(invalidAnswer)

                    print("""Q4 WHO IS THE FIRST EUROPEAN TO VISIT CHINA?
                          1.REITA FARIA
                          2.MARCO POLO
                          3.JANET YELLEN
                          4.FRANCES PHIPPS""")
                    ans = int(input(yourAnswer))
                    if ans == 2:
                        print(correctAnswer)
                        s += 1
                    elif (ans == 4 or ans == 1 or ans == 3):
                        print(incorrectAnswer)
                        s += 0
                    else:
                        print(invalidAnswer)

                    print("""Q5 WHICH IS THE FIRST CITY IS TO BE ATTACKED WITH ATOM BOMB?
                          1.WUHAN
                          2.JOHANSBERG
                          3.HIROSHIMA
                          4.NAGASAKI""")
                    ans = int(input(yourAnswer))
                    if ans == 3:
                        print(correctAnswer)
                        s += 1
                    elif (ans == 4 or ans == 2 or ans == 1):
                        print(incorrectAnswer)
                        s += 0
                    else:
                        print(invalidAnswer)

                    print("""Q6 WHO IS THE FIRST EDUCATION MINISTER OF INDIA?
                          1.DR. RADHAKRISHNAN
                          2.AMARTYASEN
                          3.DR. ZAKIR HUSSAIN
                          4.ABDUL KALAM AZAD""")
                    ans = int(input(yourAnswer))
                    if ans == 4:
                        print(correctAnswer)
                        s += 1
                    elif (ans == 1 or ans == 2 or ans == 3):
                        print(incorrectAnswer)
                        s += 0
                    else:
                        print(invalidAnswer)

                    print("""Q7 WHICH IS THE FIRST BANK OF INDIA?
                          1.STATE BANK OF INDIA
                          2.BANK OF HINDUSTAN
                          3.DENA BANK
                          4.PUNJAB NATIONAL BANK""")
                    ans = int(input(yourAnswer))
                    if ans == 2:
                        print(correctAnswer)
                        s += 1
                    elif (ans == 4 or ans == 1 or ans == 3):
                        print(incorrectAnswer)
                        s += 0
                    else:
                        print(invalidAnswer)

                    print("""Q8 WHO IS THE FIRST INDIAN WOMAN TO RECIEVE ASHOKA CHAKRA?
                          1.NIRAJ BHANOT
                          2.MOTHER TERESA
                          3.PUNEETA ARORA
                          4.REITA FARIA""")
                    ans = int(input(yourAnswer))
                    if ans == 1:
                        print(correctAnswer)
                        s += 1
                    elif (ans == 4 or ans == 2 or ans == 3):
                        print(incorrectAnswer)
                        s += 0
                    else:
                        print(invalidAnswer)

                    print(
                            "Q9 WHO IS THE FIRST COUNTRY TO ISSUE PAPER CURRENCY?\n1.INDIA\n2.USA\n3.RUSSIA\n4.CHINA")
                    ans = int(input(yourAnswer))
                    if ans == 4:
                        print(correctAnswer)
                        s += 1
                    elif (ans == 1 or ans == 2 or ans == 3):
                        print(incorrectAnswer)
                        s += 0
                    else:
                        print(invalidAnswer)

                    print("""Q10 WHICH IS THE FIRST SPACESHIP LAUNCHED ON MOON?
                          1.VIKING-1
                          2.COLOMBO
                          3.ARAYABHATTA
                          4.AGNI""")
                    ans = int(input(yourAnswer))
                    if ans == 1:
                        print(correctAnswer)
                        s += 1
                    elif (ans == 4 or ans == 2 or ans == 3):
                        print(incorrectAnswer)
                        s += 0
                    else:
                        print(invalidAnswer)

                if c == 3:
                    print("                                             YOU HAVE CHOSEN SPORTS QUIZ")
                    print("..........................................................................................................................................................................................................................................")
                    print("""Q1 WORLD FIRST TEST MATCH IS PLAYED BETWEEN WHICH TEAMS?
                          1.INDIA v/s ENGLAND
                          2.INDIA v/s AUSTRALIA
                          3.AUSTRALIA v/s ENGLAND
                          4.AUSTRALIA v/s NEW ZEALAND""")
                    ans = int(input(yourAnswer))
                    if ans == 3:
                        print(correctAnswer)
                        s += 1
                    elif (ans == 4 or ans == 2 or ans == 1):
                        print(incorrectAnswer)
                        s += 0
                    else:
                        print(invalidAnswer)

                    print("""Q2 HOW MANY MEDALS DOES INDIA HAVE WON IN TOKYO OLYMPICS 2020?
                          1. 7
                          2. 6
                          3. 5
                          4. 4""")
                    ans = int(input(yourAnswer))
                    if ans == 1:
                        print(correctAnswer)
                        s += 1
                    elif (ans == 4 or ans == 2 or ans == 3):
                        print(incorrectAnswer)
                        s += 0
                    else:
                        print(invalidAnswer)

                    print("""Q3 WHO WON THE FIRST MEDAL FOR INDIA IN TOKYO OLYMPICS 2020?
                          1.NEERAJ CHOPRA
                          2.MIRABAI CHANU
                          3.P.V SINDHU
                          4.RAVI KUMAR DHAIYA""")
                    ans = int(input(yourAnswer))
                    if ans == 2:
                        print(correctAnswer)
                        s += 1
                    elif (ans == 4 or ans == 1 or ans == 3):
                        print(incorrectAnswer)
                        s += 0
                    else:
                        print(invalidAnswer)

                    print("""Q4 WHO WON BRONZE MEDAL FOR INDIA IN WRESTLING IN TOKYO 2020?
                          1.RUPINDAR PAL SINGH
                          2.BAJRANG PUNIA
                          3.MANDEEP SINGH
                          4.AMIT ROHIDAS""")
                    ans = int(input(yourAnswer))
                    if ans == 2:
                        print(correctAnswer)
                        s += 1
                    elif (ans == 4 or ans == 1 or ans == 3):
                        print(incorrectAnswer)
                        s += 0
                    else:
                        print(invalidAnswer)

                    print("""Q5 WHO WON FIRST GOLD MEDAL FOR INDIA IN TOKYO 2020?
                          1.MANDEEP SINGH
                          2.NEERAJ CHOPRA
                          3.VARUN KUMAR
                          4.SUMIT""")
                    ans = int(input(yourAnswer))
                    if ans == 2:
                        print(correctAnswer)
                        s += 1
                    elif (ans == 4 or ans == 1 or ans == 3):
                        print(incorrectAnswer)
                        s += 0
                    else:
                        print(invalidAnswer)

                    print("""Q6 IN WHICH FIELD DOES INDIA WON THE GOLD MEDAL?
                          1.JAVELLIN THROW
                          2.HOCKEY
                          3.TENNIS
                          4.WEIGHT LIFTING""")
                    ans = int(input(yourAnswer))
                    if ans == 1:
                        print(correctAnswer)
                        s += 1
                    elif (ans == 4 or ans == 2 or ans == 3):
                        print(incorrectAnswer)
                        s += 0
                    else:
                        print(invalidAnswer)

                    print("""Q7 WHAT IS THE VENUE FOR THE WORLD TEST CHAMPIONSHIP (2019-2021) WHICH IS PLAYED BETWEEN INDIA v/s NEW ZEALAND?
                          1.THE AGEAS BOWL
                          2.THE OVAL
                          3.OLD TARAFFORD
                          4.TRENT BRIDGE""")
                    ans = int(input(yourAnswer))
                    if ans == 1:
                        print(correctAnswer)
                        s += 1
                    elif (ans == 4 or ans == 2 or ans == 3):
                        print(incorrectAnswer)
                        s += 0
                    else:
                        print(invalidAnswer)

                    print("""Q8 WHAT IS THE VENUE FOR CRICKET WORLD CUP FINAL 2019?
                          1.LORD'S
                          2.OLD TARAFFORD
                          3.TRENT BRIDGE
                          4.THE OVAL""")
                    ans = int(input(yourAnswer))
                    if ans == 1:
                        print(correctAnswer)
                        s += 1
                    elif (ans == 4 or ans == 2 or ans == 3):
                        print(incorrectAnswer)
                        s += 0
                    else:
                        print(invalidAnswer)

                    print("""Q9 IN WHICH COUNTRY DOES THE FIRST T20 WORLD CUP PLAYED IN 2007?
                          1.SOUTH AFRICA
                          2.INDIA
                          3.ENGLAND & WALES
                          4.AUSTRALIA""")
                    ans = int(input(yourAnswer))
                    if ans == 1:
                        print(correctAnswer)
                        s += 1
                    elif (ans == 4 or ans == 2 or ans == 3):
                        print(incorrectAnswer)
                        s += 0
                    else:
                        print(invalidAnswer)

                    print("""Q10 WHO IS THE PLAYER OF SERIES IN 2011 WORLD CUP?
                          1.YUVRAJ SINGH
                          2.M.S DHONI
                          3.KUMAR SANGAKARA
                          4.SACHIN TENDULKAR""")
                    ans = int(input(yourAnswer))
                    if ans == 1:
                        print(correctAnswer)
                        s += 1
                    elif (ans == 4 or ans == 2 or ans == 3):
                        print(incorrectAnswer)
                        s += 0
                    else:
                        print(invalidAnswer)

                    if s in range(0, 10):
                        print("Congrats!!!", n,
                              "\nYou have scored", s, "out of 10")
                    else:
                        print("Hurray!! huhu...", n,
                              "you have given all correct answers")
                import mysql.connector as sa
                a_s = sa.connect(host="localhost", user="root",
                                 password=" ", database="asd")
                sad = a_s.cursor()
                name = n
                scr = s
                d = (name, scr)
                sad.execute("insert into asd values (%s,%s)", d)
                a_s.commit()
                sad.execute("select * from asd order by SCORE desc")
                x = sad.fetchall()
                pos = 0
                print("POSITION", "|", "PLAYER_NAME", "|", "SCORE")
                print("-----------------------------")
                for t in x:
                    pos += 1
                    print(pos, t)
            break
        else:
            print("WRONG PASSWORD!! :(")
                  print("NUMBER OF ATTEMPTS LEFT", h-g)
                  break
                  else:
                  print("WRONG USERNAME :(")
                        print("NUMBER OF ATTEMPTS LEFT", d-f)
