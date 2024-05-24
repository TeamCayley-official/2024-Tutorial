#1장 실습
print(1,2,3)

print([1,2,3])

print("Hello World!")

print("Hello", "World", "!")

a=1
b=1
print(a+b)

name="조예은"
print(name)

#2장 실습
print(17%2)   #1이면 홀수, 0이면 짝수

num='168.7'
print(float(num))
print(type(float(num)))

a='코사다마'
print(a[::-1])

phone_num = '010-1234-1234'
print(phone_num.replace('-',''))

studentID = '20221234'
name = '조예은'
print('입학연도: {0} / 이름 : {1} / 학번 : {2}'.format(studentID[:4],name, studentID))

#3장 실습

import math
radius = 3.5
area = math.pi*radius**2
print(area)

print('생년, 월 일을 차례로 입력하세요')
year=int(input('생년?'))
month=int(input('월?'))
day=int(input('일?'))
print('당신은 {0}년 {1}월 {2}일에 태어났습니다'.format(year,month,day))

#4장 실습
beyonce=[0,100,100]
hero = [70,30,0]
won = [100,70,80]
beyonce.append((beyonce[0]+beyonce[1]+beyonce[2])/3)
hero.append((hero[0]+hero[1]+hero[2])/3)
won.append((won[0]+won[1]+won[2])/3)
print((beyonce[3]+hero[3]+won[3])/3)

number=[3,78,2,109,52,11,7,95,25,1003]
number.sort()
print(number[0],number[9])
