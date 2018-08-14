
# coding: utf-8

# # 1장. 들어가기
# *** 

# ## 1.1 데이터시대의 도래

# - 수많은 데이터가 일상에 존재하기 때문에 데이터를 가공하여 유의미한 결과를 내는 일이 중요해졌다. 하지만 그 시작은
# - 벽돌을 쌓는일부터 일 것이다. 밑바닥부터 코드를 구현해서 어떻게 우린 데이터를 가공하고 결과를 낼 수 있을 지 익혀보도록 하자.

# ## 1.2 데이터 과학이란?

# - 지저분한 데이터에서 유용한 규칙, Insight를 발견해내는 사람이 데이터 과학자라고 볼 수 있다. 데이팅 서비스 OkCupid의 매칭, Target의 
# - 구매 예측, Facebook의 친구 추천, 오바마의 재선에 도움이 된 당선에 유리한 지역구 찾기 등.. 

# ## 1.3 동기부여를 위한 상상: 데이텀 주식회사
# - 데이터 과학자의 최대 소셜 네트워크, '데이텀(Datum)"의 데이터과학자가 된 것을 가정하고 모든 코드를 밑바닥부터 직접 작성할 것이다.

# ### 1.3.1 핵심인물 찾기

# - 먼저 가입유저들의 아이디와 각 유저 간의 친분관계가 담긴 dict형과 list형의 데이터를 할당한다.

# In[2]:


# 가입유저의 아이디와 이름
users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"}]

# 각 유저 간의 친분관계
friendship = [    (0,1),(0,2),(1,2),(1,3),(2,3),(3,4),
    (4,5),(5,6),(5,7),(6,8),(7,8),(8,9)    ]


# - 다음 각 유저마다 어떤 친구를 가지고 있는 지 넣을 list를 dict의 value로 하고 dict의 key는 friends로 하는 정보를 추가로 넣는다.

# In[3]:


# 유저를 한명 씩 뽑아서 friends 라는 빈 리스트를 할당한다.
for user in users:
    user["friends"] = []


# - (i,j) 형태로 선언된 '각 유저 간의 친분관계'를 각각 열어서 해당 i유저의 친구목록에 j유저를, j유저의 친구목록에 i유저를 추가한다.

# In[4]:


for i,j in friendship:
    users[i]["friends"].append(users[j])
    users[j]["friends"].append(users[i])


# - 그렇게 진행하면 각 유저 별로 몇명의 친구를 가지고 있는 지도 출력해줄 수 있다.

# In[5]:


def number_of_friends(user):
    return len(user["friends"])

total_connections = sum(number_of_friends(user) for user in users)


# - 기본적으로 정수로 저장되기 때문에 Python 3의 나눈셈을 쓰겠다고 설정한 뒤에 나눠준다.
# - 전체 연결 수에 총 유저 수를 나눠줘서 1인당 평균적으로 몇 명과 연결되어 있는 지 구할 수 있다.

# In[6]:


from __future__ import division

num_users = len(users)
avg_connections = total_connections / num_users


# - 각 유저 별로 뽑아서 몇 명의 친구를 가지고 있는 지 다음과 같이 보여 줄 수도 있다.

# In[7]:


num_friends_by_id = [ (user["id"], number_of_friends(user)) for user in users]

num_friends_by_id


# - 'sorted' 함수를 활용해서 다음과 같이 어떤 유저가 친구가 많고 어떤 유저가 친구가 적은 지 보여줄 수 있다.

# In[8]:


sorted(num_friends_by_id, 
       key = lambda num_friends:num_friends[1], 
       reverse=True)


# ### 1.3.2 데이터 과학자 추천하기

# - 친구 추천기능을 넣어보고자, 직관적으로 친구추가 된 친구의 친구를 보여주고자 한다. 따라서
# - 유저를 입력하면 해당 유저의 친구 리스트를 보여주는 함수를 만들었다.

# In[9]:


def friends_of_friend_ids_bad(user):
    return [foaf["id"]
            for friend in user["friends"]
            for foaf in friend["friends"]]

#0번째 유저에 대한 실행 예시
friends_of_friend_ids_bad(users[0])


# - list comprehension을 통해 다른 유저도 출력해주면 다음과 같다. 하지만 다음을 보면 친분관계가 (1,2) 라면
# - 1번 유저에게도 2번 유저가, 2번 유저에게도 1번 유저가 셈이 되어서 중복 포함이 되버린다.

# In[10]:


print ([friend["id"] for friend in users[0]["friends"]])
print ([friend["id"] for friend in users[1]["friends"]])
print ([friend["id"] for friend in users[2]["friends"]])


# - 그 다음으론 둘다 알고 있는 mutual friends가 몇 명인지 한 번 세어 볼 수 있다.

# In[11]:


from collections import Counter

#만약 두 사용자의 id가 다르면 다른 사용자로 인식하는 함수
# True = 두 유저가 서로 다른 id를 가지고 있다. / False = 두 유저가 서로 같은 id를 가지고 있다.
def not_the_same(user,other_user):
    return user["id"] != other_user["id"]

#만약 other_user가 user["friends"]에 포함되지 않으면 친구가 아닌 것으로 간주하는 함수
# 내 친구들이 other_user와 다 다를경우에 true 값이 된다. 즉,
# True = 내 친구 리스트에 없다. False = 내 친구 리스트에 있다. 가 된다. 
def not_friends(user,other_user):
    return all(not_the_same(friend,other_user)
              for friend in user["friends"])

#파이썬은 할당하기 때문에 해당 친구리스트를 열어보면 다른 친구들을 각각 참조한 값들이 위치한다.
#사용자의 친구 개개인에 대해서 그들의 친구들을 세어보고 사용자 자신과 사용자의 친구를 제외하고 셈한다.
def friends_of_ids(user):
    return Counter(foaf["id"]
                  for friend in user["friends"]
                  for foaf in friend["friends"]
                  if not_the_same(user,foaf)
                  and not_friends(user,foaf))

print (friends_of_ids(users[3]))


# In[12]:


for i in users[3]["friends"]:
    print (i["id"],i["name"])


# - 사용자 고유번호와 그에 따른 관심사의 쌍으로 된 흥미목록을 만든다.

# In[13]:


interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]


# - 특정 관심사를 공유하는 사용자를 찾아주는 함수를 만든다.
# - 흥미목록에서 유저아이디, 흥미를 하나씩 뽑은 뒤 흥미목록이 유사하면 같이 뽑아줍니다.

# In[14]:


def data_scientists_who_like(target_interest):
    return [user_id
           for user_id, user_interest in interests
           if user_interest == target_interest]


# - 하지만 for문이 돌면서 모든 경우의 수를 다 파악하기 때문에 사용자 index를 만드는게 나을 수도 있다.

# In[15]:


from collections import defaultdict

# key가 관심사, value가 사용자 id 

user_ids_by_interest = defaultdict(list)


# In[18]:


for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)


# - 주제 별 관심있는 유저의 리스트를 Defalutdict로 선언한다.

# In[19]:


user_ids_by_interest


# - 반대로 사용자 별 관심있는 리스트를 관리해줄 수 도 있다.

# In[20]:


interests_by_user_id = defaultdict(list)

for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)


# In[22]:


interests_by_user_id


# In[42]:


def most_common_interests_with(user_id):
    return Counter(interested_user_id
                  for interest in interests_by_user_id[user_id]
                  for interested_user_id in user_ids_by_interest[interest]
                  if interested_user_id != user_id)


# - 해당 함수를 통해 유저의 id를 넣으면 어떤 유저와 가장 연관이 있는 지 알수 있다.

# ### 1.3.3 연봉과 경력

# - 연봉과 경력에 대한 정보가 있다. 근속연수에 따라서 연봉이 달라지는 지 한번 살펴보고자 한다.

# In[44]:


salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
                        (48000, 0.7), (76000, 6),
                        (69000, 6.5), (76000, 7.5),
                        (60000, 2.5), (83000, 10),
                        (48000, 1.9), (63000, 4.2)]


# - 우선 Scatter를 통해서 얼마나 데이터가 퍼져있는지 확인하고자 한다.

# In[45]:


from matplotlib import pyplot as plt


# In[54]:


Salaries = [salary for salary, tenure in salaries_and_tenures]
Tenures = [tenure for salary, tenure in salaries_and_tenures]

# x축에 연봉, y축에 연차를 넣는다.
plt.scatter(Salaries, Tenures, color = 'green',marker = 'x',linestyle = 'solid')

# 제목을 더하자
plt.title("salaries_and_tenures")

#Y축에 레이블을 추가하자.
plt.ylabel("Tenure")
plt.show()


# - 그 이후는 구간 별로 연봉이 달라지는 지 확인해보자

# In[62]:


salary_by_tenure = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)

salary_by_tenure


# In[63]:


average_salary_by_tenure = {
    tenure : sum(salaries) / len(salaries)
    for tenure, salaries in salary_by_tenure.items()
}
average_salary_by_tenure


# - 위처럼 진행하면 구간 별로 분할되지 않기 때문에 평균을 구하는 의미가 없다.

# In[72]:


def tenure_bucket(tenure):
    if tenure <2:
        return "less than two"
    elif tenure < 5:
        return "between two and five"
    else:
        return "more than five"
    
salary_by_tenure_bucket =defaultdict(list)
for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)
    
salary_by_tenure_bucket


# - return으로 str 값을 뱉어주게끔 설정한 뒤, 결과물로 dict key를 설정하면 각각으로 구성된다.
# - 그 뒤 각각의 구간 내에 값들을 평균값을 내주면 된다.

# In[75]:


average_salary_by_bucket = {
    tenure_bucket : sum(salaries) / len(salaries)
    for tenure_bucket, salaries in salary_by_tenure_bucket.items()}


# In[76]:


average_salary_by_bucket


# - 결론적으로 2년보다 경력이 적은 사원보다 5년 이상 되는 사원이 65%나 더 번다는 사실을 알 수 있다.

# - iteritems()는 복사한 list를 반환하고 items()는 (key,value)쌍의 iterator를 반환하지만 python 버전이 3.0이 되면서 items만 가능하다.

# # 1.3.4 유료계정
# - 더해서 유료 계정 전환율(근속년수와 유료계정 사용여부)에 대해 알고 싶다.

# In[82]:


tenures_and_paid = [(0.7,"paid"),(1.9,"unpaid"),(2.5,"paid"),(4.2,"unpaid"),(6,"unpaid"),(6.5,"unpaid"),
                    (7.5,"unpaid"),(8.1,"unpaid"),(8.7,"paid"),(10,"paid")]


# In[84]:


tenures = [tenure for tenure, paid in tenures_and_paid]
paids = [paid for tenure, paid in tenures_and_paid]

plt.scatter(tenures,paids, color = 'red', marker='o',linestyle='solid')

plt.title("Tenures_and_paid")

plt.show()


# - 16장에서 지속하도록 한다.

# ### 1.3.5 관심주제
# - 마지막으로 가장 인기있는 관심사 주제를 파악하고자 한다.

# In[87]:


interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]


# - 유저 별로 관심있는 관심군들을 뽑아낸 뒤에 소문자로 바뀐 뒤에 띄어쓰기를 기준으로 나눈 뒤에 할당해주고자 한다.

# In[88]:


words_and_counts = Counter(word
                          for user, interest in interests
                          for word in interest.lower().split())


# - 카운트가 최소한 두 번이라도 세졌던 관심사들을 출력한다.

# In[89]:


for word, count in words_and_counts.most_common():
    if count > 1:
        print(word,count)


# - 이와 같은 경우엔 단어 위주로 뽑아냈기 때문에, 의미없는 machine이란 단어가 두 개나 뽑힌 것을 볼 수 있다.
# - 자세한 내용은 20장 '자연어 처리'에서 진행하게 된다.

# ### 1.3.6 시작해보자.
