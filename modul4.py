import os 
os.system('cls')



#if är villkor. tänk på if såhär: om (det här händer) gör (såhär)

lives = 7
import random
run_game = True
secret_number = random.randint(1, 100)

print("secret number", secret_number)
print("ayy gissa nummret")
while True:
    try:
        number = int(input("enter number 0 < x < 101: "))
    except:
        print("nah uh")
    if number > secret_number:
        print("AYYY sänk farten")
        lives -= 1
    if number < secret_number:
        print("nah för långt")
        lives -= 1
        print("lives left " , lives)
    if number == secret_number:
        print('''
        ================
        abow du har rätt
        ================
        ''')
        break
    if lives == 0:
        print('''
             =========== 
              Game Over
             ===========
              ''')
        break
        



#1. Längdcheck för Gröna Lund (gör ett program som kollar längd och godkänner eller nekar besökare)
lgh = float(input("hur lång är du i meter "))
if lgh < 1.40:                                          #mindre än 1.40
        print("nah du för kort")
if lgh >= 1.40 and lgh <= 1.68:                         #allt mellan 1.4 och 1.69
        print("aaaah, du är kort men du får komma in ")
if lgh == 1.69:                                         #bara 1.69
        print("nice")
if lgh >= 1.70:                                         #1.7 och allt över
        print("abow, ahh du får komma in")

#2. Förbättra välkomstprogrammet (nu med koll att man skriver in rätt typ av värden). Använd try


#3. Förbättra BMI-kalkylatorn (se till att stoppa användaren från att skriva in fel)
try:
    längd = float(input("hur lång är du i meter "))
except:
    print("pröva att skriva i decimal tal")
try:
    vikt = int(input("hur mycket väger du i kg "))
except:
    print("skriv i heltal")

print("din BMI är ", vikt//(längd**2))


#4. Skapa ett program som beräknar arean på en cirkel (r*r*pi)
radie = float(input("vad är radien i cm "))
print("arean på den circel är", radie * radie * 3.14, "cm")

#5. Gör en miniräknare som kan räkna med alla fyra räknesätt
print('''
      vilket räknesätt vill du ha?
      1 = addition
      2 = subtration
      3 = multipliation
      4 = division 
      input 
      ''')
raknesatt = int(input(" "))
first = float(input("ditt första tal "))
second = float(input("ditt andra tal "))
if raknesatt == 1: #plus
    print(first + second)
if raknesatt == 2: #minus
    print(first - second)
if raknesatt == 3: #gånger
    print(first * second)
if raknesatt == 4: #dela med
    print(first // second)

#6. Tärning med random.randint()
import random
for i in range(2):
    print(random.randint(1,6))

#7. Gör ett program som kastar så många tärningar som användaren väljer

a3 = int(input("hur många tärningar vill du kasta "))
for rfcd in range(a3):
     print(random.randint(1,6))