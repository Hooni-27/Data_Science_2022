# Data_Science_2022

## 01. Data Science란

### Data Science : 데이터를 다루는 일
  - 데이터 마이닝과 유사하게 정형, 비정형 형태를 포함한 다양한 데이터로부터 지식과 인사이트를 추출하는데 과학적 방법론, 프로세스, 아록리즘, 시스템을 동원하는 융합분야(위키피디아)
  - 데이터와 연관된 모든 것을 의미(Journal of Data Science)
  - 데이터 사이언티스트 : 가치를 더할 수 있는 일을 찾고, 데이터를 이용해서 문제를 해결하는 것
  - ![image](https://user-images.githubusercontent.com/79882248/172274158-b5312224-1f71-4791-b8ed-87270d86a3c0.png)

### Data Science 사용 언어(R, Python)
  - R
    - 통계를 위해 만들어진 언어
    - 데이터 분석의 도구가 잘 갖춰짐
    - 통계와 시각화만을 위한 툴
  - Python
    - 다양한 용도로 만들어진 언어(데이터 사이언스 이외의 다른 분야로 넘어갈 수 있음)
    - 데이터 분석의 도구가 평범
    - R에 비해 통계와 시각화를 위한 tool이 부족
    - numpy, pandas, tensorflow 등으로 사용 비중 증가

### Data Science의 Process
  1. 문제 정의하기
    - 해결하고자 하는 문제 정의
    - 목표 설정, 기간 설정, 평가 방법 설정, 필요한 데이터 설정
  2. 데이터 모으기
    - 필요한 데이터를 모을 수 있는 방법 탐색
    - 웹 크롤링(웹 상에 존재하는 contents를 수집하는 작업), 자료 모으기, 파일 읽고 쓰기
  3. 데이터 다듬기
    - 데이터의 퀄리티를 높여서 의미 있는 분석이 가능하게끔 함
    - 데이터 관찰하기, 데이터 오류 제거, 데이터 정리하기
  4. 데이터 분석하기
    - 준비된 데이터로부터 의미 찾기
    - 데이터 파악, 데이터 변형, 통계 분석, 인사이트 발견, 의미 도출
  5. 커뮤니케이션
    - 분석 결과를 다른 사람들에게 전달
    - 다양한 시각화, 커뮤니케이션, 리포트 등

---

## 02. Jupyter Notebook

### jupyter 사용
  - notebook 내의 모든 cell들은 같은 session을 공유
  - jupyter 사용, csv데이터 나타내기(print 사용, print 사용x)
  - ![image](https://user-images.githubusercontent.com/79882248/172289216-689a5d39-3520-4d16-a957-3ff4430f5bd3.png)

---

## 03. numpy

### numpy(numerical python)
  - 계산 작업을 편하게 해줄 도구(library)
  - numpy array(numpy 배열) : python list와 비슷  
    -> 2차원 이상의 행렬 계산 사용시 유용
  - numpy 관련 함수
    - arange() : 인자로 받는 값 만큼 1씩 증가하는 1차원 array 생성
      -> 인자 1개 입력 시 : 0부터 입력한 인자, 값만큼의 크기를 가짐
    - astype(type) : 기존 데이터 형태에서 원하는 data type으로 변경
    - where(boolean 형태 list) : numpy array 중에서 True인 element만 출력
    - 최대값, 최솟값, 평균값, 중앙값 : array.max()-최댓값, array.min()-최솟값, array.mean()-평균값, np.median(array)-중앙값
    - 표준편차, 분산 : array.std()-표준 편차, array.var()-분산
  - 인덱싱, 슬라이싱, numpy 기본 연산, boolean 연산
  - python list vs numpy list
    - numpy array 사용 이유
      - 문법적인 차이 : 덧셈(numpy : 같은 위치의 element가 더해짐 / python : 기존 list 뒤에 element들이 추가됨), 뺄셈, 곱셈, 나눗셈(numpy : 정상 작동 / python : error)
      - 성능 차이
        - numpy : 문법이 간단 + 뛰어난 성능 => 효율적인 데이터 관리
        - 성능 차이의 이유 : 값들이 저장되는 방식의 차이
          - python : 다양한 자료형태의 데이터를 한 list에 저장 가능
          - numpy : 같은 자료형의 data만 들어갈 수 있음 => 속도 개선
    - python : 단순히 값을 추가하고 제거하는 작업을 하는 경우
    - numpy : 수치 계산이 많고 복잡한 작업을 진행하는 경우, 행렬과 같은 다차원 배열의 경우

---

## 04. Pandas

### pandas(data frame)
  - 데이터 보관, 정리, 분석 라이브러리
  - numpy와의 차이점 : pandas -> numpy를 이용하여 만들어짐 => pandas에서 numpy의 기능 사용 가능
