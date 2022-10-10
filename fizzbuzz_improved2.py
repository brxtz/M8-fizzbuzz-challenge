#Author: Rafael Bratfich de Oliveira
#IT 4320

#Module 8
#Challenge: FizzBuzz on GitHub

for i in range(1, 101): #variable 'i' will loop between 1-100
    if(i % 3 == 0 and i % 5 == 0): #if 'i' is multiple of 3 and 5 then 'FizzBuzz' is printed
        print("FizzBuzz")
    elif(i % 3 == 0): #if 'i' is only multiple of 3 then 'Fizz' is printed
        print("Fizz")
    elif(i % 5 == 0): #if 'i' is only multiple of 5 then 'Buzz' is printed
        print("Buzz")
    else:  #if 'i' is not multiple of neither 3 or 5 than 'i' itself is printed
        print(i) 