'''
pandas는 패널데이터의 약자.
엑셀과유사함 = 패널데이터
엑셀 사용시보다 대용량 데이터를 빠르게 처리 가능함.
쥬피터 노트북 기존 소스코드 재사용가능 -> 반복작업에 유용함
10 minutes to pandas 파일 따라해보는 걸 추천
pandas cheat sheet'''

import pandas as pd

#pd.DataFrame?

df = pd.DataFrame(
    {"a" : [4, 5, 6],
     "b": [7, 8, 9],
     "c": [10, 11, 12]},
     index=[1,2,3]
)

print(df)
print(["a"])
#series데이터 벡터 형태
print([["a"]]) #dataframe 행렬 2차원 형태

#행을 기준으로 함 row
print(df["a"] >4) #불리언으로 표시됨
print(df[df["a"]>4]) #df값으로 표시됨

#컬럼형태
df["a"]
print(df["a"]) #컬럼 두 개 이상 가져올 때는 컬럼을 리스트 형태로 감싸줘야함
print(df[["a","b"]])

df["a"].value_counts() #카테고리별로나눌때
len(df)

df["a"].sort_values()
df.drop(["c"], axis=1) #0은 로우, 1은 컬럼 세로


print(df.groupby(["a"])["b"].mean().agg(["mean","sum", "count"])) #a로 그룹바이해서 b로 평균 구할 수 잇다.
print(df.groupby(["a"])["b"].describe())

print(pd.pivot_table(df, index="a"))
print(pd.pivot_table(df, index="a", values="b"))
print(pd.pivot_table(df, index="a", values="b", aggfunc="sum"))

#df.plot.area()
df.plot.bar()
print(df.plot.density())