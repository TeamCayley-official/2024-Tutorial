2주차

1번
# 30에서 1씩 빼다가 결과가 5의 배수가 되면 멈추는 식을 작성해보세요.
# n = 30

# while n <= 30:
#   n = n - 1
#   print(n)
#   if n % 5 ==0:
#     break

2번
# 1에서 100사이의 모든 짝수의 합을 구해보세요.
# sum_list=[]

# for i in range(1,101):
#   if i%2 == 0:
#    sum_list.append(i)

# print(sum(sum_list))

3번
# 다음 과일 이름 리스트 중, 과일 이름의 길이가 가장 긴 과일을 찾아보세요
# fruits = ['사과', '오렌지', '파인애플', '귤', '천도복숭아', '리치', '코코넛', '샤인머스켓', '드래곤후르츠', '한라봉', '감']

# name_len=[]
# for i in fruits:
#   a = len(i)
#   name_len.append(a)

# index_num = name_len.index(max(name_len))
# print('{0}: {1}글자'.format(fruits[index_num], max(name_len)))
:드래곤후르츠

4번
# while문을 활용하여 구구단 1단 부터 9단까지 출력해보세요.
# num = 0
# while num <= 8:
#   num += 1
#   num2 = 1
#   while num2 <=9:
#     print('%d * %d = %d'%(num, num2, num * num2))
#     num2 += 1
#   print('===%d단 끝!==='%(num))
# print('구구단 1단 부터 9단까지 끝!')

# i = 1
# while i < 3:
#     i = i + 1
#     j = 1
#     while j < 10:
#         print(i, 'X', j, '=', i*j)
#         j = j + 1

5번
# 369게임 결과를 출력해보세요. (단, 33은 박수 두 번치고, 50번째에 게임은 끝남)
# clap = ['3', '6', '9']

# for i in range(1, 51):
#   count = 0
#   for j in str(i):
#       if j in clap:
#           count += 1
#   if count > 0:
#       i = '짝!' * count
#   print(i)

6번
# beyonce의 등수는 1등, 임영웅의 등수는 3등, 장원영의 등수는 2등입니다. 이 정보들을 변수에 넣어, 아래 예시와 같이 이름을 입력받고 점수를 출력하는 프로그램을 만드세요. 만약 존재하지 않는 학생의 이름을 입력 받을 경우, 입력값은 없어요. 라는 문장을 출력하도록 하세요.
# rank = {'beyonce' : '1', '임영웅':'3', '장원영' : '2'}
# name_list = list(rank.keys())
# name = input("이름은?")

# while name :
# ​    if  name in name_list:
# ​        print(name,"의 등수는 ",rank[name],sep='' )

# ​    elif name not in name_list:
# ​        print(name,"는(은) 없어요",sep='')

# ​    break


1번
# 구구단을 외자! 숫자를 입력받으면, 해당 숫자의 구구단(해당 숫자에 1~9를 곱한 값들)을 출력하는 함수를 만드세요.
# def print_dan(x):
# 	for i in list(range(1,10)):
# 		print (x * i)

# dan = int(input("숫자를 입력하세요"))
# while dan != 0:
# 	print_dan(dan)
# 	dan = int(input())

2번
죄송합니다.. 잘 모르겠습니다 ㅠㅠ
