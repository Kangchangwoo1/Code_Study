# 'Titanic: Machine Learning from Disaster' 학습일지

    
    
    

## Competition overview
* Competition Name : Titanic: Machine Learning from Disaster
* Purpose of Competition : 타이타닉 호의 생존자를 예측하는 Clasification 문제
* Term : 2018.08.01 ~ 2018.08.05
* Link : https://www.kaggle.com/c/titanic




### Method1. UsingTensorflow&Seaborn
- 설명
> 데이터과학 강의를 수강했을 때, 참고했었던 학우의 소스코드입니다.


- 정확도
> Kaggle 정확도 : 0.76076 %

- 느낀점
> 코드를 적고, 결과를 확인하고 수순대로 진행하는 데 있어서는 어렵지 않고 적잖이 이해할 수 있었다. 하지만 머신러닝
> 개념, 모듈 사용법 등은 확실히 알지 못하다보니 이해하기가 쉽지 않다. 데이터 시각화, Scikit-learn, Tensorflow, 정확도 척도
> Scaler, 각 척도들의 개념들이 부족하다. 
    
    
- 코드
> Variable = DataFrame.nlargest(10, 'Column')['Column'] 
>
> 데이터프레임 중에 특정한 컬럼의 수치대로 나열하고 싶을 떄 활용가능
>
> DataFrame.isnull().count().sort_values(ascending=False) 
>
> 결측치 확인할 때, 활용가능
>
> DataFrame.describe() 
>
> 데이터 프레임의 요약정보 반환
>
> DataFrame.Column.astype(str) 
>
> 컬럼의 형변환 시 활용 가능
    
    
- 추가진행
> 아마, 전처리하는 데 있어서 추가적으로 확인할 수 있는 정보가 있다면 활용할 수 있을 것 같다. 하지만 현재까지는 피쳐 수도 적었고
> 설명 자체가 많지 않아서 아마 다양한 기법을 적용해보고 가장 정확도 높은 모델을 적용하는 식으로 정확도를 높일 수 있을 듯 싶다.
> 아웃라이어 값을 지워주거나 각 모델 간의 파라미터를 수정하다보면 높아질 수 있을 듯 하다. 하지만 그 전에 각 학습 모델의 이해가 선행
> 되어야 할 듯 싶다.
    
    
- 마무리
> 매우 부족함을 많이 느낄 수 있었다. 내 코드는 아니였지만, 공부할 부분이 매우 많은 듯 보인다.


### Method2. A_Data_Science_Framework_To_Achieve_99%Accuracy
- 설명
> Kaggle 홈페이지 Kernel 중에 기본적인 이해를 돕기 위한 튜토리얼 형식으로 적혀있는 외부자료
>
> (https://www.kaggle.com/ldfreeman3/a-data-science-framework-to-achieve-99-accuracy)

- 정확도
> 

- 느낀점
> 
    
    
- 코드
> 
    
- 추가진행
> 
    
    
- 마무리
> 
 
 
 
 
 
 


