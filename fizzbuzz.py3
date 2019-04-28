num=range(0,100)
for number in num:

 if number%5==0 and number%3==0:
  print(number," <<FizzBuzz>>")

 elif number%3==0:
  print(number," <<Fizz>>")
 
 elif number%5==0:
  print(number," <<Buzz>>")

 else:
  print(number)
 