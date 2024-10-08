
# 화재 위험성 평가 프로그램 (Fire Risk Assessment Program)

### 불 가능? 불가능!
4조. 
 - 조장: 김민준 
 - 조원: 강혜나, 정세림, 이승연(보건)
### 화재 위험성 평가 프로그램 (Fire Risk Assessment Program)

이 프로그램은 산업현장에서 가장 많이 사용되는 가연성 물질 10종에 대해 화재 위험을 평가하는 도구입니다. 사용자는 특정 화학 물질의 이름을 입력하고, 점화원 수, 화재 하중, 온도, 습도와 같은 환경 조건을 지정하여 해당 화학 물질의 화재 위험을 확인할 수 있습니다.

### 진행 과정

1. **인화점에 따른 가연성 분류**
   - 프로그램은 휘발유, 아세톤, 이황화탄소 등 10가지 가연성 물질에 대한 인화점을 기반으로 가연성을 분류합니다.
   - 분류된 가연성은 낮은 수준(1)에서 높은 수준(5)까지 점수로 나타냅니다.

2. **화재 위험 점수 계산**
   - 사용자가 입력한 환경 조건 (점화원 수, 화재 하중, 온도, 습도)에 따라 화재 위험 점수를 계산합니다.
   - 온도가 높고 습도가 낮을수록 화재 위험 점수는 증가하며, 점화원 수와 화재 하중도 점수에 영향을 줍니다.

3. **화재 위험 등급 출력**
   - 계산된 화재 위험 점수를 기반으로 매우 낮음, 낮음, 보통, 높음, 매우 높음 등 다섯 가지 등급으로 분류하여 출력합니다.

### 사용 방법

1. **프로그램 실행**
   - 프로그램을 실행하면 화면에 화재 위험 평가 프로그램이라는 메시지가 표시됩니다.

2. **물질 입력**
   - 사용자는 [물질 보기]에서 제공되는 가연성 물질 중 하나의 이름을 입력합니다.
   - "종료"를 입력하면 프로그램이 종료됩니다.

3. **환경 조건 입력**
   - 입력된 물질의 가연성이 분류된 후, 사용자는 점화원 수, 화재 하중, 온도, 습도를 순서대로 입력합니다.
   - 각 입력 값은 범위나 형식에 맞지 않으면 프로그램에서 오류 메시지가 표시됩니다.

4. **결과 출력**
   - 입력된 데이터를 바탕으로 계산된 가연성 점수, 화재 위험 점수, 그리고 해당 점수에 따른 화재 위험 등급이 화면에 출력됩니다.

### 예시

사용자가 "휘발유"라는 물질을 선택하고, 점화원 수 3, 화재 하중 4, 온도 25°C, 습도 50%로 입력했을 때 계산된 결과는 다음과 같습니다:
- 가연성 점수: 1점 (낮은 가연성)
- 화재 위험 점수: 12.00
- 화재 위험 등급: 보통 (Moderate)

### 개발 환경

- Python 3.8
- 필요한 외부 라이브러리 없음


