def is_adult(age):
    if age >= 20:
        print('성인입니다')
    else:
        print('청소년입니다')


is_adult(25)  # 성인입니다

fruits = ['사과', '배', '배', '감', '수박', '귤', '딸기', '사과', '배', '수박']

for fruit in fruits:
    print(fruit)
# 사과
# 배
# 배
# 감
# 수박
# 귤
# 딸기
# 사과
# 배
# 수박