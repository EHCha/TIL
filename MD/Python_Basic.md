# Python 기초 문법

## vscode 매뉴얼

- `ctrl + s` 로 저장
- 터미널 열기: ```ctrl + shift + ` ```
- 터미널로 이동: ``` ctrl + ` ```



#### 저장 - 변수(variable)

- 숫자
  - 크기를 가진다
- 글자(string)
  - 숫자에 따옴표를 붙이면 글자가 된다.
  - ex) '58' = 글자
- 참 / 거짓
  - true, false
  - 조건/반복을 위해 사용



#### 저장 - 리스트(list)

- 대괄호로 나타냄 [ ]
  - ex) [68,58,40,70,...]
- 숫자는 0부터 시작



- ' ' : single quotation
- "": double quotation



#### 저장 - 딕셔너리(dictionary

- 이름표를 단 여러 개의 값을 저장할 수 있는 저장공간
- 중괄호로 나타냄 { } 
  - ex) {"영등포구" : 58, "서대문구" : 54, "도봉구" : 70, ...... } 
  - ex) { key1 : value1, key2 : value2 } 
- 이름표(key)는 중복이 되면 안된다.



#### 조건 -if, else

```python
if ***:
    print()
else:
    print()
```



- 들여쓰기 (indentation)를 해야한다.
- flow chart 논리흐름도



#### 조건 - elif

1. 미세먼지 (elif)

``` python
dust = 170

if dust > 150 :
    print('매우 나쁨')
    
elif dust > 80 :
    print('나쁨')

elif dust > 30 :
    print('보통')
    
else:
    print('좋음')
```



2. 반복 (while)

```python
n = 0
while n<3:
    print(n)
    n += 1
```

`while` 횟수의 제한이 없는 반복

탈출코드: while 문을 빠져 나가기 위한 조건



3. 반복 (for)

```python
dusts = [59, 25, 102]
for value in dusts:
    print(value)
```

횟수의 제한이 있는 반복

 

pythontutor.com에서 파이썬의 논리 흐름을 파악 가능



- range(start, end, step)

  - range() 사용시 데이터를 다 만들지 않고 필요할때만 만들어서 메모리에 올림 (메모리를 적게 사용)

  ```python
  a = range (3)
  print(a)
  
  #result
  #range(0,3)
  ```

  ``` 
  a = list(range(3))
  print(a)
  
  #result
  #[0, 1, 2]
  ```

- abs(): 절대값을 보여줌

- len():  글자 수를 나타냄

  

#### 모듈

- 함수나 변수 등을 모아 놓은 파이썬 파일

- import : reserved word(예약어)

- import후 함수나 변수를 불어올 때 파일명. 변수명

  

#### 리스트, 리스트 비교

``` python
a = [1, 3, 4, 6]
b = [4, 6, 3, 1]

if a == b :
    print('same')
    
else:
    print('not same')
```

- sort를 사용하지 않으면 not some 출력

- sort 사용하지 않고 리스트 비교를 하기 위해서는 다음과 같은 코드를 사용하면 된다.



``` python
a = [1, 3, 4, 6]
b = [4, 6, 3, 1]

member = 0
for i in range(4) :
    if b[i] in a:
        member += 1
        
if member == 4 :
    print('same')
    
else:
    print('not same')
```



#### 로또 예제

```  python

```















#### 요청과 응답

- 요청(request) - 주소 (url) : 클라이언트 ==> 서버
- 응답(response) - HTML : 클라이언트 <== 서버
- JSON



API

- pip install requests

  