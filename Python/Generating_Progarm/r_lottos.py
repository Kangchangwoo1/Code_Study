import random
counters = [0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0
            ,0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0,0, 0, 0,0]

#in_val1 = 46
#in_val2 = 46

print("간단하게 수행되는 LOTTO 프로그램 ")
print()
in_val = []


def no(r_in):
    for i in range(r_in):
        value = random.randint(0, 44)
        counters[value] = counters[value] + 1

    for i in range(45):
        print("숫자가 ", i+1, "인 경우는 ", counters[i], "번")

    new_list = sorted(counters, reverse=True)

    for i in range(7):
        print("선택된 숫자가",counters.index(new_list[i])+1,"인 경우는",new_list[i],"번")
        counters[counters.index(new_list[i])]=0


def one(r_in, in_val0):
    for i in range(r_in):
        value = random.randint(0, 44)
        if value == in_val0:  #in_val1
            counters[value] = 0
        else:
            counters[value] = counters[value] + 1

    for i in range(45) :
        print("숫자가 ", i+1, "인 경우는 ", counters[i], "번")

    new_list = sorted(counters, reverse=True)

    for i in range(7) :
        print("선택된 숫자가",counters.index(new_list[i])+1,"인 경우는",new_list[i],"번")
        counters[counters.index(new_list[i])]=0


def two(r_in, in_v0, in_v1):
    for i in range(r_in):
        value = random.randint(0, 44)

        if value == in_v0:  #in_val1
            counters[value] = 0
        elif value == in_v1:   #in_val2
            counters[value] = 0
        else:
            counters[value] = counters[value] + 1
        #counters[value] = counters[value] + 1

    for i in range(45):
        print("숫자가 ", i+1, "인 경우는 ", counters[i], "번")

    new_list = sorted(counters, reverse=True)

    for i in range(7):
        print("선택된 숫자가",counters.index(new_list[i])+1,"인 경우는",new_list[i],"번")
        counters[counters.index(new_list[i])]=0


def three(r_in, in_v, in_w, in_x):
    for i in range(r_in): # 몇번을 돌릴것인지 결정
        value = random.randint(0, 44)

        if value == in_v:  #in_val1
            counters[value] = 0
        elif value == in_w:   #in_val2
            counters[value] = 0
        elif value == in_x:    #in_val3
            counters[value] = 0
        else:
            counters[value] = counters[value] + 1

    for i in range(45) :
        print("숫자가 ", i+1, "인 경우는 ", counters[i], "번")

    new_list = sorted(counters, reverse=True)

    for i in range(7) :
        print("선택된 숫자가",counters.index(new_list[i])+1,"인 경우는",new_list[i],"번")
        counters[counters.index(new_list[i])]=0



def four(r_in, in_v, in_w, in_x, in_y):
    for i in range(r_in): # 몇번을 돌릴것인지 결정
        value = random.randint(0, 44)

        if value == in_v:  #in_val1
            counters[value] = 0
        elif value == in_w:   #in_val2
            counters[value] = 0
        elif value == in_x:    #in_val3
            counters[value] = 0
        elif value == in_y:    #in_val4
            counters[value] = 0
        else:
            counters[value] = counters[value] + 1

    for i in range(45) :
        print("숫자가 ", i+1, "인 경우는 ", counters[i], "번")

    new_list = sorted(counters, reverse=True)

    for i in range(7) :
        print("선택된 숫자가",counters.index(new_list[i])+1,"인 경우는",new_list[i],"번")
        counters[counters.index(new_list[i])]=0


def in_call():
    rot = int(input("몇번 수행할까요? : "))
    return rot


c_y = int(input("미리 확정한 숫자가 몇개 있습니까? (0 ~ 4개) "))


for i in range(5):


    if (c_y == 4):
        for i in range(c_y):
            in_v = int(input(" 숫자 입력 : ")) -1
            in_w = int(input(" 숫자 입력 : ")) -1
            in_x = int(input(" 숫자 입력 : ")) -1
            in_y = int(input(" 숫자 입력 : ")) -1
            in_val.append(in_v)
            r_in = in_call()
            four(r_in, in_v, in_w, in_x, in_y)
    elif (c_y == 3):
        for i in range(c_y):
            in_v = int(input(" 숫자 입력 : ")) -1
            in_w = int(input(" 숫자 입력 : ")) -1
            in_x = int(input(" 숫자 입력 : ")) -1
            in_val.append(in_v)
            r_in = in_call()
            three(r_in, in_v, in_w, in_x)
    elif (c_y == 2):
        for i in range(c_y):
            in_v = int(input(" 숫자 입력 : " )) -1
            in_w = int(input(" 숫자 입력 : ")) -1
            in_val.append(in_v)
            r_in = in_call()
            two(r_in, in_v, in_w)
    elif (c_y == 1):
        for i in range(c_y):
            in_v = int(input(" 숫자 입력 : ")) -1
   #         in_val.append(in_v)
            r_in = in_call()
            print(in_val)
            one(r_in, in_v )
    elif (c_y == 0):
        rst = in_call()
        no(rst)
    else:
        print("다시 선택해 주세요!")
