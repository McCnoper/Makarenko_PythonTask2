x = str(0)
while(len(str(x))!=3): #Перевірка чи число трицифрове
        x = int(input("Enter number")); #отримання числа з перетворюванням його в int
if x // 100 == x % 10: #перевірка чи є поліндромом
    print("Is polyndrome") 
else: print("Isn`t polyndrome")
