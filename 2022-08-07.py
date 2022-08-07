"""
1. 숫자형
1) 정수표현
a=123
a=-178
a=0

2) 실수표현
a=1.2
a=4.24e10
a=4.24e-10

3) 8진수 0o
a=0o177
print=0o177

4) 16진수 0x
a=0x8ff
b=0xABC


2. 사칙연산
a**b
a의 b제곱

a%b
나머지를 출력

a//b
몫을 출


3. 문자열 자료형
큰따옴표가 있다.
"Life is too short, You need Python"
"123"

문자열 표현방식
1) 큰따옴표로 둘러싸기
2) 작은따옴표로 둘러싸기
3) 큰따옴표, 작은따옴표 3개로 둘러싸기

문자열에 ' " 추가하기
1)다른 ' " 로 감싸기
2) \ (백슬레시활용)


여러줄인 문자열
\n 사용
multiline='''


"""

print("="*50)
print("Test")
print('='*50)


#문자열길이 구하기
"""
a="life is too short"
len(a)
"""


#문자열 인덱싱
"""
파이썬은 0부터 숫자를셈
a[0] = l
a[1] = i
a[0:4] = life
a[0:3] = lif
==> 0<= a <3

a="20220827rain"
date=a[:8]
weather=a[8:]

"""


#문자열의 포매팅
"""
%d = 숫자
%s = 문자

"""

print("I eat {0} apples".format(3))


number=4
print("I eat {0} apples.".format(number))
      

number=3
day="three"
print("I ate {0} apples. so I was sick for {1} days.".format(number,day))


print("I ate {0} apples. so I was sick for {day} days.".format(10,day=50))
print("I ate {0} apples. so I was sick for {day} days.".format(10,day="four"))

print("{0:<10}".format("hello"))
print("{0:>10}".format("hello"))
print("{0:^10}".format("hello"))

print("{0:~<10}".format("hello"))
print("{0:=^10}".format("heungsun"))

y=3.141592
print("{0:0.4f}".format(y))
print("{{and}}".format(y))


name="heungsun"
age=29
print(f'I\'m {name}. i\'m {age} years old')
print(f'next year, i\'m {age+1} years old')


print(f'{"hi":<10}')






print(f'{"hi":^30}')



print(f'{"python":!^20}')


a="hobby"
print(a.count('b'))


#find와 index의 차이점은 find는 찾는값이 없으면 -1출력, index는 오류
a='python is the best choice'
print(a.find('b'))
print(a.find('z'))
print(a.index('b'))


#사이에 문자넣기(join)
print(",".join('abcd'))

#대문자로(upper)
a='hello'
print(a.upper())

#소문자로(lower)
a='HELLo'
print(a.lower())

#공백지우기(strip)   
a='        hello        '
print(a.lstrip())
print(a.rstrip())
print(a.strip())

#문자열바꾸기(replace)
a='life is too short'
print(a.replace('life','your leg'))

#문자열나누기(split)  () 안의 것을 기준으로 문자를 나눔
print(a.split())
b="a:b:c:d"
print(b.split(':'))


#리스트의 인덱싱.
a=[1,2,3]
print(a[0]+a[2])

a=[1,2,3,['이걸출력할거임','b','c']]
print(a[-1][0])
print(a[3][0])

print(a[:2])
print(a[2:])


#리스트더하기
a=[1,2,3]
b=[4,5,6]
print(a+b)

print(a*3)
print(len(a))

#숫자를 문자로 변환하기(str)
print(str(a[2])+'hi')

#리스트값 수정하기
a=[1,2,3,'이걸바꿀꺼임']
a[3]=4
print(a[3])
print(a)

#리스트값 삭제(del)
del a[3]
print(a)

a=[1,2,3,4]
del a[:2]
print(a)


#리스트에 요소추가(append)
a.append([5,6])
print(a)

#리스트 정렬과(sort) 뒤집기(reverse)
a=[1,3,5,2,4]
b=['b','c','a']
a.sort()
b.sort()
print(a)
print(b)

a.reverse()
b.reverse()
print(a)
print(b)

#리스트에 위치반환(index)
print(a.index(5))


#리스트에 요소삽입(insert(a,b))  a 위치에 b삽입
a=[2,3,4,5]
a.insert(0,1)
a.insert(5,6)
print(a)

#리스트요소제거(remove(x)) [리스트에서 첫번째 나오는x를 삭제]
a=[1,2,3,1,2,3]
a.remove(3)
print(a)

#리스트요소끄집어내고 삭제하기(pop(x)) [x번째요소를끄집어내고 삭제함]
a=[1,2,3]
a.pop()
print(a)
b=[1,2,3]
b.pop(1)
print(b)

#리스트에 x개수세기(count(x))
a=[1,1,1,1,1,2,3]
print(a.count(1))

#리스트확장하기 (extend(x)) [x는 리스트만 올수있다.]
a.extend(['이거','추가할거임'])
print(a)



# 2022.08.07







