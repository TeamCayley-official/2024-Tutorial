#6장 실습
#1.
num = 30
while num <= 30 :
   num -= 1
   print(num)
   if num % 5 == 0:
      break

#2.
list=[]

for i in range(1,101):
  if i % 2 == 0:
    list.append(i)

print(sum(list))

#3.
fruits = ['사과', '오렌지', '파인애플', '귤', '천도복숭아', '리치', '코코넛', '샤인머스켓', '드래곤후르츠', '한라봉', '감']

name_len=[]
for i in fruits:
  a = len(i)
  name_len.append(a)

index_num = name_len.index(max(name_len))
print('{0}: {1}글자'.format(fruits[index_num], max(name_len)))

#4.
num = 0
while num <= 8:
  num += 1
  num2 = 1
  while num2 <= 9:
    print('%d * %d = %d' %(num, num2, num*num2))
    num2 += 1

#5. 
clap = ['3','6','9']

for i in range(1,51):
  count = 0
  for j in str(i):
    if j in clap:
      count += 1
  if count > 0:
    i = '짝!'* count
  print(i)
  
#7장 실습
#1.
def print_dan(x):
	for i in list(range(1,10)):
		print (x * i)

dan = int(input("숫자를 입력하세요"))
while dan != 0:
	print_dan(dan)
	dan = int(input())
    

#2.
def lotto_generator(x):
	import random
	valist = list(range(1,46))
	lottery_nums = []
	for i in range(6):
		random.shuffle(valist)
		val  = random.choice(valist)
		lottery_nums.append(val)
	print("\n%s회 :" % x , end = " ")
	for i in lottery_nums:
		print(i,end = " ")
	return lottery_num
def lotto_stat(x):
    results = {}
    for i in range(1,46):
        results[i] = 0
    for i in range(1,x+1):
        lottery_nums = lotto_generator(i)
        for i in lottery_nums:
            results[i] = results[i] + 1
    print("\n")
    for i in results.keys():
        print("%s : %d회" % (i,results[i]))
    return results


results = lotto_stat(30)

this_nums = sorted(results, key= lambda c :results[c], reverse=True)[:6]

print("이 주의 로또 번호 :",end = " ")
for i in this_nums:
    print(i, end = " ")