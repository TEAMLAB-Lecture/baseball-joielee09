# -*- coding: utf-8 -*-

import random


def get_random_number():
    # Helper Function - 지우지 말 것
    # 100부터 999까지 수를 램덤하게 반환함
    return random.randrange(100, 1000)

# .isdecimal()
def is_digit(user_input_number):
    s_len = len(user_input_number)
    for i in range(s_len):
        if not user_input_number[i].isdigit():
            return False
    return True

# return True if int(user_input_number) >= 100 and int(user_input_number) < 1000 else False
def is_between_100_and_999(user_input_number):
    if(len(user_input_number)==3):
        return True
    return False

# .count()
def is_duplicated_number(three_digit):
    s = set()
    for i in range(len(three_digit)):
        if(three_digit[i] in s):
            return True
        s.add(three_digit[i])
    return False

# is False
def is_validated_number(user_input_number):
    if not (is_digit(user_input_number)):
        return False
    if not (is_between_100_and_999(user_input_number)):
        return False
    if (is_duplicated_number(user_input_number)):
        return False
    return True


def get_not_duplicated_three_digit_number():
    while(True):
        x = random.randrange(100, 1000)
        if (is_validated_number(str(x))):
            return x
        continue
    return 0


def get_strikes_or_ball(user_input_number, random_number):
    strike=0
    ball=0
    inputLen = len(user_input_number)
    numberLen = len(random_number)
    inputSet = set(user_input_number[i] for i in range(inputLen))
    numberSet = set(random_number[i] for i in range(numberLen))
    
    
    if(inputLen != numberLen):
        return
    
    for i in range(inputLen):
        if(user_input_number[i]==random_number[i]):
            strike+=1
            inputSet.remove(user_input_number[i])
    inter = inputSet.intersection(numberSet)
    ball = len(inter)

    if(strike==3):
        return [3,0]
    return [strike, ball]


def is_yes(one_more_input):
    s = one_more_input.lower()
    if(s=='y' or s=='yes'):
        return True
    return False


def is_no(one_more_input):
    s = one_more_input.lower()
    if(s=='n' or s=='no'):
        return True
    return False


def main():
    print("Play Baseball")
    user_input = 999
    random_number = str(get_not_duplicated_three_digit_number())
    print("Random Number is : ", random_number)

    noChk= False
    
    while(True):
        if(noChk):
            break
        user_input  = input("Input guess number: ")
        if(user_input=='0'):
            noChk = True
        if (is_validated_number(user_input)) is False:
            print("Wrong input, Input again")
            continue
        s,b = get_strikes_or_ball(user_input, random_number)
        print("Strikes : ", s, "Balls : ", b)
        if(s==3):
            while(True):
                ans = input("You Win, one more(Y/N) ?")
                if(ans =='0'):
                    noChk = True
                    break
                if(is_yes(ans)):
                    random_number = str(get_not_duplicated_three_digit_number())
                    print("Random Number is : ", random_number)
                    break
                elif(is_no(ans)):
                    noChk = True
                    break
                else:
                    print("Wrong input, Input again")
                    continue
    print("Thank you for using this program")
    print("End of the Game")

if __name__ == "__main__":
    main()
