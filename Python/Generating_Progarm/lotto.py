#모듈호출
#============================================================#
import random
#============================================================#

#함수선언
#============================================================#
def isit_right_number(input_value,case_of_number = None):
    if case_of_number == None:
        case_of_number = [0,1,2,3,4,5]

    try:
        if int(input_value) in case_of_number:
            print ("타당한 값이 입력되었습니다.")
            return True
        else:
            print ("다시 입력해주시기 바랍니다.")
            return False
    except Exception as E:
        print ("다시 입력해주시기 바랍니다.")
        return False

def turn_that_roulette(routine_number,selected_number_case=None):
    counters = []
    for i in range(45):
        counters.append(int(0))
    if selected_number_case != None:
        for i in range(routine_number):
            value = random.randint(0, 44)
            if (value+1) not in selected_number_case:
                counters[value] = counters[value] + 1
    else:
        for i in range(routine_number):
            value = random.randint(0, 44)
            counters[value] = counters[value] + 1


    return counters

def show_that_counters(counters,selected_number_case=None):
    print("\n")
    if selected_number_case ==None:
        for i in range(45):
            print("숫자가 ", i+1, "인 경우는 ", counters[i], "번")
    else:
        for i in range(45):
            if i+1 in selected_number_case:
                print("숫자가 ", i+1, "인 경우는 ", "미리 선택된 값이므로, 제외됩니다.")
            else:
                print("숫자가 ", i+1, "인 경우는 ", counters[i], "번")
def final_statement(counters):
    new_list = sorted(counters, reverse=True)
    print("\n")
    last_call = None
    for i in range(7):
        # if counters.index(new_list[i])+1 == last_call:
        #     print ("반복 횟수가 부족하여 이 이상 순서를 메길 수 없습니다.")
        #     break
        print("선택된 숫자가",counters.index(new_list[i])+1,"인 경우는",new_list[i],"번")
        counters[counters.index(new_list[i])]=-1
        # last_call = counters.index(new_list[i])+1
    return new_list


#============================================================#


#메인함수
#============================================================#

#프로그램 시작
print ("\nLotto 프로그램을 실행합니다.")
print ("학번/학년/산업경영공학과/금지윤\n")

# 반복횟수가 1~5사이의 타당한 숫자가 들어올 때까지 입력반복
while True:
    routine_number = input("\n반복횟수를 입력해주십시오.(1에서 10000사이 값):")
    if isit_right_number(routine_number,[i+1 for i in range(10000)]) == True:
        break

# 정해진 숫자 수가 1~45의 타당한 숫자가 들어올 때까지 입력반복
while True:
    fixed_idx = input("\n이미 정해진 숫자 개수를 입력해주십시오.(0에서 5사이 값):")
    if isit_right_number(fixed_idx) == True:
        break

fixed_idx_case = []

# 정해진 숫자에 따라 다른 프로세스 진행
if fixed_idx == '0':
    roulette_output = turn_that_roulette(int(routine_number))
    show_that_counters(roulette_output)
    final_statement(roulette_output)

else:
    for i in range(int(fixed_idx)):
        while True:
            input_value = input("\n %d번째 숫자를 선택해주세요.(1에서 45사이 값):" %(i+1))
            if isit_right_number(fixed_idx,[i+1 for i in range(45)]) == True:
                if int(input_value) not in fixed_idx_case:
                    break
                else:
                    print("타당하지만 중복된 숫자입니다.")

        fixed_idx_case.append(int(input_value))

    roulette_output = turn_that_roulette(int(routine_number),fixed_idx_case)
    show_that_counters(roulette_output,fixed_idx_case)
    final_statement(roulette_output)

print("\n\n프로그램을 종료합니다.")

#============================================================#
