import random


def random_guess():
    rand = random.randint(0000, 10000)
    str1 = str(rand)

    if (len(str1))==4:
        print("system generated 4 digit number: \n", rand)
    else:
        zeros ='{:0>4}' .format(rand)
        print("system generated 4 digit number:\n ", zeros)

    def cont():
        d = input("do you want to play again?:[y/n]\n ")
        if d == 'y' or d == 'Y':
            print("")
        elif d == 'n' or d == 'N':
            exit()
        else:
            print("invalid choice")

    def user_input():

        d='y'
        while d=='y' or d=='Y':
            if d=='y':
                enter = input("enter a guess(input):\n ")
                str_input= str(enter)

                count_rabbit = count_tortoise = 0

                if enter.isdigit():
                    if len(str_input) == 4:
                        if str_input == str1:
                            print("winner")
                            d='y'
                            while d=='y' and d=='Y':
                                cont()
                                random_guess()

                        else:
                            for i in range(0, 4):
                                if str_input[i] in str1:
                                    if str1[i]==str_input[i]:
                                        count_rabbit +=1

                                    else:
                                        count_tortoise +=1
                            if count_rabbit<=0 and count_tortoise<=0:
                                print("wrong guess")
                            else:

                                print("You got Rabbit", count_rabbit)
                                print("You got tortoise", count_tortoise)

                    else:
                        print("invalid length")
                else:
                    print("invalid type")

            cont()
        user_input()

    user_input()


random_guess()
