import this

True #앞글자가 반드시 대문자
False

True==1
False==0
#이진법
#명시적인 것이 암시적인 것보다 낫다.

True=='1'
True!='1'

False=='0'
False!='0'

True and True
True and False
True or False

1
"1"
type(1)
type("1")
1 == "1"

"Hello World!"
"경기도 성남시 분당구"

# == 비교연산, = 할당연산

till = "Today I Learned"
print(till)
till= till.lower()
print(till)
till= till.upper()
print(till)

lang=[]
print(lang)

lang.append("python")#추가하기
lang.append("java")
lang.append("c")
print(lang)

print(lang[0])
print(lang[1])
print(lang[-1])
print(lang[2])

for i in lang:
    print(i)

for i in lang:
    if i == "python":
        print("python1")
    else :
        print("기타")

count = len(lang)
for i in range(count):
    print(lang)

#1부터 9까지 나옴
for i in range(1, 10):
    if i % 2 == 0:
        print("python")
    else:
        print("java")

for i, val in enumerate(lang) : 
    print(i, val)

address = " 경기도 성남시 분당구 불정로 "
address = address.strip()#앞뒤공백제거

len(address)
address_list = address.split() #공백으로 문자열 분리
address.split(";") #해당 문자로 나눔

print(address[:2])
print(address_list)
print(address.startswith("경기")) #경기로 address가 시작하냐
"경기" in address #경기가 adress에 있는지

gu = address_list[2]
street = address_list[3]
address_list[-1]
print(gu, street)

"".join(address_list) #공백없이 문자열로 다 붙임
" ".join(address_list) #공백 넣어서 문자열로 다 붙이기


"경기" in address_list #원소를 비교할 때는 텍스트가 전부 일치해야만 true값이 나옴
print ("분당구" in address_list)