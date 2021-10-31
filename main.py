print('enter a positive number of 4 digits')
number = input()
while int(number) < 1000 or int(number) > 9999:
    print('its not 4 digits try again, enter a positive number of 4 digits')
    number = input()
sum = 0
newNum = ""
for i in number:
    sum += int(i)
print('the digits sum is:', sum)
print('the new reversed number is:', end="")
number1 = number
while int(number) % 10 != 0:
    n1 = int(number) % 10
    print(n1, end="")
    number = int(number)//10
print('')
if int(int(number1) % 10) == int(int(number1)//1000) and int(int(number1)//100 % 10) == int(int(number1)//10 % 10):
    print('the number:', number1, 'is pelindrom')
else:
    print('the number:', number1, 'is not pelindrom')
