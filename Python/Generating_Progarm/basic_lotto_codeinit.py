import random

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

# def show_that_counters(counters,selected_number_case=None):
#     print("\n"),
#     if selected_number_case ==None:
#         for i in range(45):
#             print("숫자가 ", i+1, "인 경우는 ", counters[i], "번")
#
#     else:
#         for i in range(45):
#             if i+1 in selected_number_case:
#                 print("숫자가 ", i+1, "인 경우는 ", "미리 선택된 값이므로, 제외됩니다.")
#             else:
#                 print("숫자가 ", i+1, "인 경우는 ", counters[i], "번")

def final_statement(counters,fixed_idx_case):
    new_list = sorted(counters, reverse=True)
    print("\n")
    for i in fixed_idx_case:
        print("먼저 선택된 숫자는",i,"입니다.")
    for i in range(7-len(fixed_idx_case)):
        print("선택된 숫자가",counters.index(new_list[i])+1,"인 경우는",new_list[i],"번")
        counters[counters.index(new_list[i])]=-1
    return new_list

print ("\nLotto 프로그램을 실행합니다.")
print ("학번/학년/산업경영공학과/금지윤\n")

routine_number = int(input("\n반복횟수를 입력해주십시오.(1에서 10000사이 값):"))
fixed_idx = int(input("\n이미 정해진 숫자 개수를 입력해주십시오.(0에서 5사이 값):"))

fixed_idx_case = []

if fixed_idx == 0:
    roulette_output = turn_that_roulette(routine_number)
    # show_that_counters(roulette_output)
    final_statement(roulette_output,fixed_idx_case)

else:
    for i in range(fixed_idx):
        input_value = input("\n %d번째 숫자를 선택해주세요.(1에서 45사이 값):" %(i+1))
        fixed_idx_case.append(int(input_value))

    roulette_output = turn_that_roulette(routine_number, selected_number_case=fixed_idx_case)
    # show_that_counters(roulette_output,fixed_idx_case)
    final_statement(roulette_output,fixed_idx_case)

print("\n\n프로그램을 종료합니다.")
