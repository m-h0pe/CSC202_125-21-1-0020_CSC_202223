#PYTHON LOOPS
#  STUDENT AVERAGE HEIGHT
studheight= input("input a list of students height").split()
for n in range(0, len(studheight)) :
     studheight[n] = int(studheight[n])
print(studheight)
total_heit= 0
for height in studheight :
        total_heit += height
print(total_heit)
num_stud= 0
for students in studheight :
    num_stud +=1
print(num_stud)
avG_height = round(total_heit/num_stud)
print(avG_height)

# STUDENT HIGH SCORE CHALLENGE
studscores= input("input a list of students scores").split()
for n in range(0, len(studscores)):
      studscores[n] = int(studscores[n])
      print(studscores)
higscore =0
for score in studscores :
    #   print(score)
     if score > higscore :
      higscore = score
print(f"the high score is {higscore}")

# ADDING EVEN  NUMBERS CHALLENGE
total = 0
for number in range(1,101) :
    #tieven = number % 2
    # if tieven ==0 :
    if number%2 ==0 :
     total +=number
    print(total)

# FIZZBUZZ CHALLENGE
for number in range(1,101) :
    if number%3 == 0 and number%5 == 0:
        print("FizzBuzz")
    elif number%3 == 0:
        print("Fizz")
    elif number%5 == 0:
        print("Buzz")
    else :
        print(number)
        

