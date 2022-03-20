#!/usr/bin/env python
# coding: utf-8

# 조건문 if

# In[1]:


a=3 


# In[2]:


if a>1:
    print("a is greather than 1")


# 반복문 for

# In[3]:


for a in [1,2,3]:
    print(a)


# 반복문 while

# In[4]:


i=0
while i<3:
    i=i+1
    print(i)


# 함수

# In[5]:


def add(a,b):
    return a+b


# In[6]:


add(3,4)


# 정수형

# In[8]:


#int
a= 123
b= -178
c= 0


# 실수형

# In[10]:


#float
a=1.2
a=-3.45


# 사칙연산

# In[13]:


a=3
b=5
a+b

7%3


# 문자열 자료형

# In[14]:


#str
"Hello world"


# In[15]:


food="banana" 


# In[16]:


food


# 이스케이프 코드 
# 
# \n: 문자열 안에서 줄을 바꿀 때 사용
# 
# 
# \t: 문자열 사이 탭 간격 줄 때 사용 

# 문자열 길이 구하기

# In[25]:


a= "afadsfotkkasdjfolasdfusariowe"


# In[26]:


print(len(a))


# 문자열 인덱싱 

# In[27]:


a= "happy i like happy"


# In[29]:


a[2] #0부터 시작합니다


# In[32]:


a[-4] # 거꾸로의 방법


# 슬라이싱 기법

# In[34]:


a[0:5]


# In[37]:


a[8:]


# In[38]:


a[:]


# In[39]:


a[5:-3]


# 문자열 포맷팅

# 1. 숫자 바로 대입 

# In[43]:


'i eat %d apples' % 3


# 2. 문자열 바로 대입

# In[44]:


"i eat %s apples" %"five"


# 3. 숫자 값을 나타내는 변수로 대입

# In[52]:


number=3

'i eat %d apples' % number


# 문자열 포맷 코드

# %s 문자열 
# 
# 
# %d 정수 
# 
# 
# %f  부동 소수

#  1. 정렬과 공백

# In[54]:


"%10s" % "hi"


# 문자열 관련 함수

# In[57]:


A = "hobby"
A.count('b') #b 몇개 인지 세기 


# In[60]:


A = 'hello my name is'
A.find('e') #위치 알려주기


# In[63]:


A = "Life is too short"
A.index('t') #위치알려주기2


# In[86]:


ff=",".join('abcd')
#문자열 삽입


# In[68]:


a="hi"
a.upper()
b="HI"
b.lower()


# In[70]:


a =" hi"
a.lstrip() # 왼쪽 공백 지우기


# In[72]:


a = " hi "
a.rstrip() #오른쪽 공백 지우기 


# In[75]:


a = " hi "
a.strip() #양쪽 공백 지우기


# replace(바뀌게 될 문자열, 바꿀 문자열)

# In[81]:


a = "LIFE IS TO SHORT"


# In[82]:


a.replace("LIFE","YOUR LEG")


# split(문자열 나누기)

# In[83]:


a.split()


# In[85]:


ff.split(',')


# 리스트 

# In[1]:


odd=[1,2,3,4,5]


# 리스트 관련 함수

# In[5]:


a = [1,2,3]
a.append(4) # 리스트의 맨 마지막 추가


# In[8]:


a=[1,5,6,3,4]
a.sort() # 리스트 정렬
print(a)


# In[11]:


a=['a','c','b']
a.reverse() #리스트 뒤집기
a


# In[15]:


a.index('a') #위치반환 


# In[18]:


a.insert(0,4) # 0자리에 4집어넣어라 


# In[17]:


a


# In[1]:


a=[1,2,3]


# In[3]:


a.extend([4,5])
a


# 튜플

#  튜플은 그 값을 바꿀 수 없다

# ()로 진행 된 형태이다 그 외는 리스트로 동일

# 딕셔너리 

# In[4]:


dic= {'name':'pey','phone':'010~'}


# In[5]:


dic


# In[14]:


a={1:'a'}
a[3]='b'


# In[15]:


a


# In[16]:


dic.keys()


# In[17]:


for k in a.keys():
    print(k)


# In[18]:


list(a.keys())


# In[20]:


a.values()


# In[21]:


a.items()


# In[23]:


a.clear()


# In[24]:


a


# In[25]:


dic= {'name':'pey','phone':'010~'}


# In[26]:


dic.get('name')


# In[27]:


'name' in dic


# In[100]:


s1=set([1,2,3])
l1= list(s1)


# In[101]:


s2 = set({3,4,5,6,7,8})


# In[102]:


s1 & s2


# In[103]:


s1.union(s2)


# In[104]:


#값 추가하기 


# In[105]:


s1.update([4,5,6])


# In[106]:


s1


# 불 자료형

# In[118]:


a = True


# In[21]:


b= False


# while 조건문:
#     수행할 문장

# In[119]:


a =[1,2,3,4]


# In[120]:


while a:
    a.pop()


# In[123]:


if []:
    print("참")
else:
     print("거짓")


# 변수를 만드는 여러가지 방법

# In[126]:


a, b =('python','life')
(a, b) ='python','life' #튜플
[a, b] =('python','life') # 리스트


# In[152]:


a=13
b=a%2

if a%2==0 :
    print('짝수')
else:
    print('홀수')
    


# In[137]:


a=13
b=a%2
b


# In[143]:


a='a:b:c:d'


# In[149]:


a


# In[150]:


money= True
if money:
    print("택시를 타고 가라")
else:
    print("걸어가라")


# In[154]:


#X==Y #==X와Y가 같다 


# In[155]:


1 in [1,2,3]


# In[156]:


1 not in [1,2,3]


# 주머니에 돈이 있으면 택시를 타고, 주머니에 돈은 없지만 카드가 있으면 택시를 타고, 돈도 없고 카드도 없으면 걸어가라.

# while 반복문 

# In[32]:


treeHit= 0 


# In[39]:


while treeHit <0:
    treeHit = treeHit+1
    print("나무를%d만큼 찍었습니다."% treeHit)
    if treeHit == 10:
        print("나무넘어갑니다.")


# for 문

# In[41]:


for i in range(10):
    print(i, end='')


# 파일 생성하기

# In[44]:


#f = open('','w')
#f.close() #파일 객체 닫아주는 역할을 함 해도 되고 안해도 되고 근데 해야 오류 안난대

#r 읽기 
#w 쓰기
#a 추가모드


# 정규표현식

# '''
# \ - 다른 문자와 함께 사용되어 특수한 의미로 사용
# 
# - \d : 숫자를 [0-9]와 동일 (digit)
# - \D : 숫자가 아닌 문자 [^0-9]와 동일
# - \s : 공백 문자(띄어쓰기, 탭, 엔터 등) (script)
# - \S : 공백이 아닌 문자
# - \w : 알파벳대소문자, 숫자 [0-9a-zA-Z]와 동일 (word)
# - \W : non alpha-numeric 문자 [^0-9a-zA-Z]와 동일
# - \t, \n, \r - tab, newline, return
# '''

# In[ ]:




