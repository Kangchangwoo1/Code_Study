#모듈호출
#============================================================#
import random
#============================================================#


#함수선언
#============================================================#

# (1)반복횟수와 (2)'미리 고른 숫자로 구성된' 리스트를 인자로 받아서 룰렛을 돌려서 반환하는 함수
def turn_that_roulette(routine_number,selected_number_case=None):
    #'counters'에 빈 리스트를 할당한다.
    counters = []
    # 45번 반복한다.
    for i in range(45):
        # 0을 45번 'counters'라는 빈 리스트에 추가해준다.
        counters.append(int(0))

    #만약에 '미리 고른 숫자로 구성된' 리스트가 있다면,
    if selected_number_case != None:
        #함수에 입력된 반복횟수만큼 반복한다.
        for i in range(routine_number):
            # 0~44번 중에 한 가지를 뽑는다. (index로 활용하기 위해서 0부터함.)
            value = random.randint(0, 44)
            # 만약에 '미리 고른 숫자로 구성된' 리스트에 들어있지 않다면,
            if (value+1) not in selected_number_case:
                #'counters'에 'value'번째 자리에 있는 값에 1을 더해준다.
                counters[value] = counters[value] + 1

    #그게 아니고 '미리 고른 숫자로 구성된' 리스트가 없다면,
    else:
        #함수에 입력된 반복횟수만큼 반복한다.
        for i in range(routine_number):
            # 0~44번 중에 한 가지를 뽑는다. (index로 활용하기 위해서 0부터함.)
            value = random.randint(0, 44)
            #'counters'에 'value'번째 자리에 있는 값에 1을 더해준다.
            counters[value] = counters[value] + 1

    # 'counters'라고 하는 리스트를 반환해준다.
    return counters

# (1)숫자 별 카운팅 횟수 리스트와 (2)'미리 고른 숫자로 구성된' 리스트를 인자로 받아서 각 값을 출력해주는 함수
def show_that_counters(counters,selected_number_case=None):
    # 보기 편하게 띄어쓰기 해준다.
    print("\n")
    # 만약 '미리 고른 숫자로 구성된' 리스트가 없다면,
    if selected_number_case ==None:
        # 45번 반복한다.
        for i in range(45):
            # 각 숫자와 몇 번 카운팅되었는 지 출력해준다.
            print("숫자가 ", i+1, "인 경우는 ", counters[i], "번")

    # 그게 아니고 '미리 고른 숫자로 구성된' 리스트가 없다면,
    else:
        # 45번 반복한다.
        for i in range(45):
            # range(45)에서 뽑히는 숫자에 1을 더한 값이 '미리 고른 숫자로 구성된' 리스트에 있다면,
            if i+1 in selected_number_case:
                # 각 숫자와, 제외된다는 문구를 출력해준다.
                print("숫자가 ", i+1, "인 경우는 ", "미리 선택된 값이므로, 제외됩니다.")
            #아니라면,
            else:
                # 각 숫자와 몇 번 카운팅되었는 지 출력해준다.
                print("숫자가 ", i+1, "인 경우는 ", counters[i], "번")

# 마지막으로 7가지 순번을 출력해주는 함수
def final_statement(counters):
    # 'counters'라고 하는 리스트를 숫자 크기에 따라서 재정렬해서 'new_list'에 할당한다.
    new_list = sorted(counters, reverse=True)
    # 보기 편하게 띄어쓰기 해준다.
    print("\n")
    # 7번 반복한다.
    for i in range(7):
        # 순서대로 인 'new_list'에서 값을 받고 해당 값을 기준으로 'counters'에서 위치값을 찾은 뒤 출력해준다.
        print("선택된 숫자가",counters.index(new_list[i])+1,"인 경우는",new_list[i],"번")
        # 출력해준 뒤 해당 위치에 있던 값에 -1을 할당해준다. (0으로 하면 중복호출 가능성이 있다.)
        counters[counters.index(new_list[i])]=-1
    # 정렬된 new_list를 반환한다. (특별히 필요없음)
    return new_list

#============================================================#


#메인함수
#============================================================#

#프로그램 시작
#시작과 관련된 프린트문 출력
print ("\nLotto 프로그램을 실행합니다.")
print ("학번/학년/산업경영공학과/금지윤\n")

#반복횟수를 입력받아서 int로 변환하여 'routine_number'에 할당
routine_number = int(input("\n반복횟수를 입력해주십시오.(1에서 10000사이 값):"))
#미리 정해진 숫자 개수를 입력받아서 int로 변환하여 'fixed_idx'에 할당
fixed_idx = int(input("\n이미 정해진 숫자 개수를 입력해주십시오.(0에서 5사이 값):"))

# 미리 정해진 숫자를 저장하기 위해서 'fixed_idx_case'에 빈 리스트를 할당해준다.
fixed_idx_case = []

# 만약 미리 정해진 숫자가 없다면,
if fixed_idx == 0:
    # (1)반복횟수를 넣고 룰렛을 돌린다.
    roulette_output = turn_that_roulette(routine_number)
    # (1)돌려서 나온 룰렛함수 결과물을 넣고 결과를 출력해준다.
    show_that_counters(roulette_output)
    # (1)돌려서 나온 룰렛함수 결과물을 넣고 상위 7개의 숫자를 출력해준다.
    final_statement(roulette_output)

# 그게 아니고 미리 정해진 숫자가 있다면,
else:
    # 정해진 숫자의 개수만큼 반복한다.
    for i in range(fixed_idx):
        # 1에서 45 사이 값을 받아서 'input_value'에 할당한다.
        input_value = input("\n %d번째 숫자를 선택해주세요.(1에서 45사이 값):" %(i+1))
        # 미리 정해진 숫자 리스트에 해당 값을 저장한다.
        fixed_idx_case.append(int(input_value))

    # (1)반복횟수와 (2)미리 정해진 숫자 리스트를 넣고 룰렛을 돌린다.
    roulette_output = turn_that_roulette(routine_number,fixed_idx_case)
    # (1)돌려서 나온 룰렛함수 결과물과 (2)미리 정해진 숫자리스트를 넣고 결과를 출력해준다.
    show_that_counters(roulette_output,fixed_idx_case)
    # (1)돌려서 나온 룰렛함수 결과물을 넣고 상위 7개의 숫자를 출력해준다.
    final_statement(roulette_output)

#종료와 관련된 프린트문 출력
print("\n\n프로그램을 종료합니다.")
