1번
# print(1,2,3)
# print([1,2,3])
# print("Hello World!")
# print("Hello", "World", "!")
# a=1
# b=1
# a+b
# name="고다람"
# print(name)


2번
# 17이 홀수 인지 짝수인지 판별해보세요.
#2로 나눴을 때 나머지가 0이면 짝수, 1이면 홀수
# print(17%2)


# 아래 문자열의 자료형을 실수로 바꿔서 출력해보세요.
# num = '168.7'


# 아래 문자열을 거꾸로 출력해보세요.
# a = '코사다마'
# a = '코사다마'
# print(a[::-1])


# 아래 문자열에서 - (hyphen)을 제거하여 출력해보세요.
# phone_num = '010-1234-1234'
# phone_num = '010-1234-1234'
# print(phone_num.replace('-', ''))


# 다음 변수를 활용하여 아래와 같은 결과가 나오게 출력해보세요.
# studentID = '20221234'
# name = '고다람'

# 결과
# 입학연도: 2022 / 이름: 고다람 / 학번: 20221234
# studentID = '20221234'
# name = '고다람'
# print('입학연도: {0} / 이름: {1} / 학번: {2}'.format(studentID[:4], name, studentID))

3번
# 반지름의 값이 3.5인 원이 있습니다. 반지름의 값을 radius라는 변수에 넣으세요. area라는 변수는 원의 면적을 의미합니다. 변수 area의 값을 radius 변수를 이용해 식으로 할당하고, 그 값을 숫자로 출력하세요.
# import math
# radius = 3.5
# area = math.pi*radius**2
# # print(area)

# 사용자로부터 생년월일을 입력받아 다음을 출력하는 프로그램을 작성하세요.

# 생년, 월, 일을 차례로 입력하세요.
# 생년?
# 월?
# 일?
# 당신은 XXXX년 X월 X일에 태어났습니다.

# print("당신의 생년,월,일을 차례로 입print("당신의 생년,월,일을 차례로 입력하세요")
# year=int(input('생년?'))
# month=int(input('월?'))
# day=int(input('일?'))
# print('당신은',year,'년',month,'월',day,'일에 태어났습니다.')
# print('생년월일을 합하면',year+month+day,"입니다.")

4번
# 비욘세의 한국어 점수는 0점, 수학 점수는 100점, 영어 점수는 100점입니다. 임영웅의 한국어 점수는 70점, 수학 점수는 30점, 영어 점수는 0점입니다. 장원영의 한국어 점수는 100점, 수학 점수는 70점, 영어 점수는 80점입니다. 세 학생의 점수들을 담은 리스트를 만들고, 각 학생의 국어, 수학, 영어 점수의 평균을 네번째 데이터로 리스트에 넣으세요. 세 학생의 국어, 수학, 영어 점수의 평균을 print() 함수를 통해 출력하세요.
# beyonce = [0, 100, 100] 
# hero = [70, 30, 0]
# won0 = [100, 70, 80]
# beyonce.append((beyonce[0]+beyonce[1]+beyonce[2])/3)
# hero.append((hero[0]+hero[1]+hero[2])/3)
# won0.append((won0[0]+won0[1]+won0[2])/3)
# print((beyonce[3] + hero[3] + won0[3])/3)

# number라는 변수에 임의의 숫자 10개를 넣으세요. 그 중 가장 큰 수와 가장 작은 수를 print() 함수를 통해 출력하세요.
# number = [10, 2, 3, 4, 5, 7, 6, 8, 9, 100]
# number.sort()
# print(number[0], number[-1])