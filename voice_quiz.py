import pyttsx3
speech = pyttsx3.init()
cricket_key ={1:"b",2:"b",3:"d",4:"b",5:"b"}
politics_key = {1:"a",2:"c",3:"d",4:"b",5:"a"}
computer_key = {1:"c",2:"b",3:"c",4:"c",5:"d"}
print("Welcome to the game please select the field in which you want give a quiz for example cricket, politics, computer.")
speech.say("Welcome to the game please select the field in which you want give a quiz for example cricket, politics, computer.")
speech.runAndWait()
score = 0

field = input("Enter your field here :")

if(field=="cricket"):
    que1=("Which country is going to host the world cup 2023 this year.?")
    print(que1)
    speech.say(que1)
    speech.runAndWait()
    print("A) Australia     B) India")
    print("C) England       D) Pakistan")
    cans1 = input("Enter your option here :")
    if(cans1==cricket_key.get(1)):
     score+=2
     speech.say("Corrent answer lets go for the next question")
     speech.runAndWait()
     que2=("Who is the current captain of team India.?")
     print(que2)
     speech.say(que2)
     speech.runAndWait()
     print("A) Virat kohli   B) Rohit Sharma")
     print("C) Kl Rahul      D) MS Dhoni")
     cans2 = input("Enter your option here :")
     if (cans2 == cricket_key.get(2)):
         score+=2
         speech.say("Corrent answer lets go for the next question")
         speech.runAndWait()
         que3 =("Who is known as the god of cricket.?")
         print(que3)
         speech.say(que3)
         speech.runAndWait()

         print("A) Virat kohli   B) Rohit Sharma")
         print("C) Kl Rahul      D) Sachin Tendulkar")
         cans3 =input("Enter your option here :")
         if(cans3 == cricket_key.get(3)):
             score+=2
             speech.say("Corrent answer lets go for the next question")
             speech.runAndWait()
             que4 = ("Can RCB win the IPL trophy.?")
             speech.say(que4)
             speech.runAndWait()
             print(que4)
             print("A) NO            B) Never")
             print("C) Yes           D) May be")
             cans4 = input("Enter your option here :")
             if(cans4==cricket_key.get(4)):
                 score+=2
                 speech.say("Corrent answer lets go for the next question")
                 speech.runAndWait()
                 que5 = ("How many times India won the ODI workd cup.?")
                 speech.say(que5)
                 speech.runAndWait()
                 print(que5)
                 print("A) 4             B) 2")
                 print("C) 1             D) Never")
                 cans5 = input("Enter your option here :")
                 if (cans5 == cricket_key.get(5)):
                     speech.say("Corrent answer lets go for the next question")
                     speech.runAndWait()
                     score += 2
                     print("Congratulation..! You have reached to the end Your score out of 10 is :",score)
                 else:
                     print("Sorry your answer is wrong you cant move further.")
                     print("Your score is ", score)
                     speech.say("Sorry you have given wrong answer, you cant move futher your score is ", score)
                     speech.runAndWait()


         else:
             print("Sorry your answer is wrong you cant move further.")
             print("Your score is ", score)
             speech.say("Sorry you have given wrong answer, you cant move futher your score is ",score)
             speech.runAndWait()

     else:
         print("Sorry your answer is wrong you cant move further.")
         print("Your score is ", score)
         speech.say("Sorry you have given wrong answer, you cant move futher your score is ", score)
         speech.runAndWait()

    else:
        print("Sorry your answer is wrong you cant move further.")
        print("Your score is ",score)
        speech.say("Sorry you have given wrong answer, you cant move futher your score is ", score)
        speech.runAndWait()




elif(field=="politics"):
    que1 = ("What is the term for a government ruled by a single individual with absolute power?")
    print(que1)
    speech.say(que1)
    speech.runAndWait()
    print("A) Democracy     B) Dictatorsip")
    print("C) Monarchy      D) None")
    cans1 = input("Enter your option here :")
    if (cans1 == politics_key.get(1)):
        score += 2
        speech.say("Corrent answer lets go for the next question")
        speech.runAndWait()
        que2 = ("Which party is rulling in India currently?")
        print(que2)
        speech.say(que2)
        speech.runAndWait()
        print("A) Congress   B) AAP")
        print("C) BJP        D) Shiv Sena")
        cans2 = input("Enter your option here :")
        if (cans2 == politics_key.get(2)):
            score += 2
            speech.say("Correct answer lets go for the next question")
            speech.runAndWait()
            que3 = ("Who is known as the god of cricket.?")
            print(que3)
            speech.say(que3)
            speech.runAndWait()

            print("A) Virat kohli   B) Rohit Sharma")
            print("C) Kl Rahul      D) Sachin Tendulkar")
            cans3 = input("Enter your option here :")
            if (cans3 == politics_key.get(3)):
                score += 2
                speech.say("Correct answer lets go for the next question")
                speech.runAndWait()
                que4 = ("Can RCB win the IPL trophy.?")
                speech.say(que4)
                speech.runAndWait()
                print(que4)
                print("A) NO            B) Never")
                print("C) Yes           D) May be")
                cans4 = input("Enter your option here :")
                if (cans4 == politics_key.get(4)):
                    score += 2
                    speech.say("Corrent answer lets go for the next question")
                    speech.runAndWait()
                    que5 = ("How many times India won the ODI workd cup.?")
                    speech.say(que5)
                    speech.runAndWait()
                    print(que5)
                    print("A) 4             B) 2")
                    print("C) 1             D) Never")
                    cans5 = input("Enter your option here :")
                    if (cans5 == politics_key.get(5)):
                        speech.say("Correct answer")
                        speech.runAndWait()
                        score += 2
                        print("Congratulation..! You have reached to the end Your score out of 10 is :", score)
                    else:
                        print("Sorry your answer is wrong you cant move further.")
                        print("Your score is ", score)
                        speech.say("Sorry you have given wrong answer, you cant move futher your score is ", score)
                        speech.runAndWait()


            else:
                print("Sorry your answer is wrong you cant move further.")
                print("Your score is ", score)
                speech.say("Sorry you have given wrong answer, you cant move futher your score is ", score)
                speech.runAndWait()

        else:
            print("Sorry your answer is wrong you cant move further.")
            print("Your score is ", score)
            speech.say("Sorry you have given wrong answer, you cant move futher your score is ", score)
            speech.runAndWait()

    else:
        print("Sorry your answer is wrong you cant move further.")
        print("Your score is ", score)
        speech.say("Sorry you have given wrong answer, you cant move futher your score is ", score)
        speech.runAndWait()

elif(field=="computer"):
    que1 = ("Who is the father of computer?")
    print(que1)
    speech.say(que1)
    speech.runAndWait()
    print("A) Tim cook          B) Issac newton")
    print("C) charles Babbage   D) None")
    cans1 = input("Enter your option here :")
    if (cans1 == computer_key.get(1)):
        score += 2
        speech.say("Correct answer lets go for the next questeion")
        speech.runAndWait()
        que2 = ("Which of the following is a computer programming language?")
        print(que2)
        speech.say(que2)
        speech.runAndWait()
        print("A) Cobra      B) Python")
        print("C) Mamba      D) None")
        cans2 = input("Enter your option here :")
        if (cans2 == computer_key.get(2)):
            score += 2
            speech.say("Correct answer lets go for the next question")
            speech.runAndWait()
            que3 = ("Which language is known as the mother of all programming languages ?")
            print(que3)
            speech.say(que3)
            speech.runAndWait()

            print("A) Java          B) Java Script")
            print("C) C             D) Python")
            cans3 = input("Enter your option here :")
            if (cans3 == computer_key.get(3)):
                score += 2
                speech.say("Correct answer lets go for the next question")
                speech.runAndWait()
                que4 = ("In computer most processing takes place in ________?")
                speech.say(que4)
                speech.runAndWait()
                print(que4)
                print("A) Hard disk     B) Moniter")
                print("C) CPU           D) None")
                cans4 = input("Enter your option here :")
                if (cans4 == computer_key.get(4)):
                    score += 2
                    speech.say("Correct answer lets go for the next question")
                    speech.runAndWait()
                    que5 = ("Which one of the follwing is the operating system of the computer?")
                    speech.say(que5)
                    speech.runAndWait()
                    print(que5)
                    print("A) Windowss             B) Linus")
                    print("C) Mac OS               D) All of the above")
                    cans5 = input("Enter your option here :")
                    if (cans5 == computer_key.get(5)):
                        speech.say("Correct answer")
                        speech.runAndWait()
                        score += 2
                        print("Congratulation..! You have reached to the end Your score out of 10 is :", score)
                    else:
                        print("Sorry your answer is wrong you cant move further.")
                        print("Your score is ", score)
                        speech.say("Sorry you have given wrong answer, you cant move futher your score is ", score)
                        speech.runAndWait()


            else:
                print("Sorry your answer is wrong you cant move further.")
                print("Your score is ", score)
                speech.say("Sorry you have given wrong answer, you cant move futher your score is ", score)
                speech.runAndWait()

        else:
            print("Sorry your answer is wrong you cant move further.")
            print("Your score is ", score)
            speech.say("Sorry you have given wrong answer, you cant move futher your score is ", score)
            speech.runAndWait()

    else:
        print("Sorry your answer is wrong you cant move further.")
        print("Your score is ", score)
        speech.say("Sorry you have given wrong answer, you cant move futher your score is ", score)
        speech.runAndWait()




