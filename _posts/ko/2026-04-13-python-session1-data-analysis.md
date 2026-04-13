---
layout: post
title: "생물의학 전공자를 위한 파이썬 — Session 1: 첫 번째 데이터 분석"
date: 2026-04-13 09:00:00 +0900
lang: ko
ref: python-session-1
categories: [tutorials]
tags: [파이썬, 데이터분석, pandas, matplotlib, 튜토리얼]
description: "실제 데이터 분석으로 파이썬을 배웁니다. 90분 안에 심장질환 환자 303명을 분석하고 차트 4개를 완성합니다 — 파이썬 지식 제로에서 시작."
---

> **강사:** Max Kang  
> **시간:** 90분  
> **도구:** Google Colab (브라우저만 있으면 됨 — 설치 불필요)  
> **목표:** 실제 환자 데이터를 처음부터 분석합니다. 파이썬은 자연스럽게 익혀집니다.

---

## 스포일러 — 오늘 만들 것들

시작 전에 **최종 결과물**을 먼저 보여드릴게요. 90분 후, 여러분은 다음 4가지를 만들어낸 파이썬 코드를 갖게 됩니다.

**발견 1: 심장질환 환자 303명의 연령 분포**

```
환자 대부분이 50~60세 사이임을 보여주는 히스토그램.
평균 나이를 빨간 점선으로 표시.
```

**발견 2: 성별이 중요하다**

```
이 데이터셋에서 남성 환자가 여성보다
심장질환 비율이 훨씬 높음을 보여주는 막대 차트.
```

**발견 3: 심박수가 이야기를 들려준다**

```
나이 vs. 최대 심박수 산점도.
심장질환 환자(빨간 점)는 우하단에 몰림 — 나이 많고, 최대 심박수 낮음.
```

**발견 4: 콜레스테롤 비교**

```
두 그룹의 콜레스테롤 수치를 분포, 중앙값, 이상치까지
나란히 보여주는 박스 플롯.
```

**실제 환자 데이터로. 여러분이 직접 작성한 코드로. 제로에서 시작해서.**

90분 만에 불가능한 것 같다고요? 바로 그 놀라움이 핵심입니다. 시작하죠.

---

## 오늘 할 것들

**실제 심장질환 데이터셋**을 분석합니다 — 환자 303명, 의료 변수 14개, 그리고 심장질환 여부 진단.

파이썬은 필요할 때 자연스럽게 배웁니다. 문법 드릴 없이 — 데이터로 바로 뛰어듭니다.

| 시간 | 내용 |
|------|------|
| 0:00 | 스포일러 공개 + Google Colab 세팅 |
| 0:10 | 환자 BMI 계산 (변수와 연산 학습) |
| 0:25 | 심장질환 데이터셋 불러오기 |
| 0:45 | 데이터에 질문 던지기 |
| 1:05 | 답을 시각화 (스포일러 차트 완성!) |
| 1:25 | 마무리 + Session 2 예고 |

---

## Part 1 — 세팅 (10분)

### 왜 파이썬인가?

한 문장으로: **파이썬은 데이터 과학, AI, 생물의학 연구에서 1위 언어** — 그리고 거의 영어처럼 읽힙니다.

```python
if blood_pressure > 140:
    print("Hypertension detected")
```

프로그래밍 경험 없어도 이해되셨죠? 그게 파이썬의 매력입니다.

### Google Colab 열기

1. **<https://colab.research.google.com>** 접속
2. Google 계정으로 로그인
3. **"새 노트북"** 클릭
4. 빈 **코드 셀** 확인 — 여기에 파이썬 입력, `Shift + Enter`로 실행

끝입니다. 설치도, 세팅도 없어요. 코딩 시작.

### Hello World

이걸 입력하고 `Shift + Enter`:

```python
print("Hello, Biomedical World!")
```

출력:

```
Hello, Biomedical World!
```

`print()`는 텍스트를 화면에 표시합니다. 따옴표 안의 텍스트는 **문자열(string)**이라고 합니다. 축하합니다 — 파이썬을 실행했습니다!

---

## Part 2 — 첫 번째 계산: 환자 BMI (15분)

환자가 있다고 해봅시다: 70kg, 키 175cm. BMI는?

### Step 1: 변수에 데이터 저장

**변수**는 값을 담는 이름 붙은 상자입니다.

```python
weight_kg = 70
height_cm = 175
```

셀을 실행하세요. 아무것도 안 보이는 게 정상 — 파이썬이 숫자를 기억했습니다.

> **이름 짓는 규칙:** 소문자와 밑줄 사용: `blood_pressure`, `heart_rate`. `#`으로 시작하는 줄은 **주석** — 파이썬이 무시하고, 사람을 위한 메모입니다.

### Step 2: BMI 계산

BMI = 체중 ÷ 키² (미터 단위)

```python
height_m = height_cm / 100
bmi = weight_kg / (height_m ** 2)
print(bmi)
```

출력: `22.857142857142858` — 맞는데 지저분합니다. 정리해봅시다:

```python
print(f"BMI: {bmi:.1f}")
```

출력: `BMI: 22.9`

> **f-string:** 따옴표 앞에 `f`를 붙이고, 안에 `{변수:.1f}`를 넣으면 소수점 1자리로 표시합니다. 자주 쓰게 됩니다.

### Step 3: BMI 분류

```python
if bmi < 18.5:
    print("저체중")
elif bmi < 25.0:
    print("정상")
elif bmi < 30.0:
    print("과체중")
else:
    print("비만")
```

출력: `정상`

> **`if/elif/else` 작동 방식:** 파이썬이 위에서부터 조건을 확인하고 처음으로 참인 것을 실행합니다. 들여쓰기된 코드(4칸)가 해당 조건에 속합니다.

### 기본 연산자 정리

| 연산자 | 의미 | 예시 |
|--------|------|------|
| `+` | 더하기 | `10 + 3` → `13` |
| `-` | 빼기 | `10 - 3` → `7` |
| `*` | 곱하기 | `10 * 3` → `30` |
| `/` | 나누기 | `10 / 3` → `3.33` |
| `**` | 거듭제곱 | `10 ** 2` → `100` |

### 직접 해보기

체중과 키 값을 바꿔서 다시 실행해보세요. 내 BMI는?

```python
# 본인 값으로 바꿔서 실행하세요
weight_kg = ___
height_cm = ___

height_m = height_cm / 100
bmi = weight_kg / (height_m ** 2)
print(f"내 BMI: {bmi:.1f}")
```

---

## Part 3 — 심장질환 데이터셋 불러오기 (20분)

이제 환자 1명에서 **303명**으로 넘어갑니다. 손으로 하면 미칠 것 같죠. `pandas`가 여기서 등장합니다.

### pandas 가져오기

```python
import pandas as pd
```

> `pandas`는 파이썬에게 데이터 테이블을 다루는 능력을 줍니다 — 파이썬 안의 엑셀이라고 생각하세요. 타이핑을 줄이려고 `pd`라는 별명을 씁니다.

### 데이터 불러오기

```python
url = "https://raw.githubusercontent.com/datasets/heart-disease/main/data/heart.csv"
df = pd.read_csv(url)

print(f"불러왔습니다! 환자 {df.shape[0]}명, 변수 {df.shape[1]}개")
```

> `df`는 **DataFrame**의 약자 — 각 행이 환자, 각 열이 변수인 테이블입니다.

### 첫 번째 확인

```python
df.head()
```

첫 5행을 보여줍니다:

| | age | sex | cp | trestbps | chol | … | target |
|-|-----|-----|----|----------|------|---|--------|
| 0 | 63 | 1 | 3 | 145 | 233 | … | 1 |
| 1 | 37 | 1 | 2 | 130 | 250 | … | 1 |

### 컬럼의 의미

| 컬럼 | 의미 | 값 |
|------|------|-----|
| `age` | 환자 나이 | 세 |
| `sex` | 생물학적 성별 | 1 = 남성, 0 = 여성 |
| `cp` | 흉통 유형 | 0–3 |
| `trestbps` | 안정 시 혈압 | mm Hg |
| `chol` | 콜레스테롤 | mg/dl |
| `fbs` | 공복 혈당 > 120? | 1 = 예, 0 = 아니오 |
| `thalach` | 운동 시 최대 심박수 | bpm |
| `exang` | 운동 시 흉통? | 1 = 예, 0 = 아니오 |
| `target` | **심장질환 진단** | **1 = 있음, 0 = 없음** |

### 전체 요약

```python
df.describe()
```

**모든 컬럼**의 개수, 평균, 표준편차, 최소, 최대, 사분위수를 한 번에 제공합니다. 스프레드시트에서 30분 걸릴 작업이 한 줄입니다.

### 결측값 확인

```python
df.isnull().sum()
```

모두 0이면 → 데이터가 깨끗합니다!

---

## Part 4 — 데이터에 질문 던지기 (20분)

이제 재미있어집니다. 질문을 한국어로 하고, 파이썬 한두 줄로 답합니다.

### Q1. 환자 평균 나이는?

```python
avg_age = df["age"].mean()
print(f"평균 나이: {avg_age:.1f}세")
```

> `df["age"]`는 "age" 컬럼을 가져옵니다. `.mean()`은 평균을 계산합니다. 끝 — 한 줄입니다.

### Q2. 심장질환 환자는 몇 명?

```python
df["target"].value_counts()
```

출력:

```
1    165
0    138
```

심장질환 있는 환자 165명, 없는 환자 138명. 더 명확하게:

```python
counts = df["target"].value_counts()
total = len(df)

print(f"심장질환 있음: {counts[1]}명 ({counts[1]/total*100:.1f}%)")
print(f"심장질환 없음: {counts[0]}명 ({counts[0]/total*100:.1f}%)")
```

### Q3. 두 그룹의 콜레스테롤이 다를까?

```python
chol_by_group = df.groupby("target")["chol"].mean()

print("평균 콜레스테롤 (mg/dl):")
print(f"  질환 없음: {chol_by_group[0]:.1f}")
print(f"  질환 있음: {chol_by_group[1]:.1f}")
```

> `.groupby("target")`은 데이터를 두 그룹(질환/비질환)으로 나누고, `.mean()`이 각 평균을 계산합니다. 엑셀의 피벗 테이블과 같습니다.

### Q4. 혈압은?

```python
bp_by_group = df.groupby("target")["trestbps"].mean()

print("평균 안정 시 혈압 (mm Hg):")
print(f"  질환 없음: {bp_by_group[0]:.1f}")
print(f"  질환 있음: {bp_by_group[1]:.1f}")
```

### Q5. 고위험 환자는?

60세 이상, 콜레스테롤 250 초과 환자를 필터링합니다.

```python
high_risk = df[(df["age"] > 60) & (df["chol"] > 250)]

print(f"고위험 환자 (60세↑, 콜레스테롤 250↑): 전체 {len(df)}명 중 {len(high_risk)}명")
high_risk[["age", "sex", "chol", "trestbps", "target"]].head(10)
```

> **필터 문법:** 각 조건을 괄호에 넣고 `&` (그리고) 또는 `|` (또는)로 연결합니다. 수천 건의 레코드를 초 단위로 검색하는 방법입니다.

### Q6. 남성 vs. 여성 — 누가 심장질환이 더 많나?

```python
gender_disease = pd.crosstab(
    df["sex"].map({1: "남성", 0: "여성"}),
    df["target"].map({1: "질환 있음", 0: "질환 없음"})
)
print(gender_disease)
```

> `.map({1: "남성", 0: "여성"})`은 숫자를 읽기 좋은 레이블로 바꿉니다. `{1: "남성", 0: "여성"}` 부분은 **딕셔너리** — 왼쪽 값을 오른쪽 레이블로 매핑합니다.

---

## Part 5 — 답을 시각화하기 (20분)

숫자는 진실을 말하지만, 차트는 **이야기**를 합니다.

```python
import matplotlib.pyplot as plt
```

> `matplotlib`은 파이썬의 가장 유명한 차트 라이브러리입니다. `plt`라는 별명을 씁니다.

### 차트 1: 연령 분포 (히스토그램)

*"이 데이터셋에서 어떤 나이가 가장 많은가?"*

```python
plt.figure(figsize=(9, 5))
plt.hist(df["age"], bins=20, color="steelblue", edgecolor="white")
plt.axvline(df["age"].mean(), color="red", linestyle="--",
            label=f'평균: {df["age"].mean():.1f}세')
plt.title("환자 연령 분포", fontsize=15, fontweight="bold")
plt.xlabel("나이 (세)")
plt.ylabel("환자 수")
plt.legend()
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()
```

> **히스토그램이란?** 각 막대가 나이 구간을 나타냅니다. 막대가 높을수록 그 구간의 환자가 많습니다. 빨간 점선이 평균입니다.

### 차트 2: 성별 심장질환 (막대 차트)

*"남성과 여성 중 누가 더 많이 영향받는가?"*

```python
gender_disease = pd.crosstab(
    df["sex"].map({1: "남성", 0: "여성"}),
    df["target"].map({1: "질환 있음", 0: "질환 없음"})
)

gender_disease.plot(kind="bar", color=["#4CAF50", "#F44336"],
                    figsize=(8, 5), edgecolor="white")
plt.title("성별 심장질환 분포", fontsize=15, fontweight="bold")
plt.xlabel("성별")
plt.ylabel("환자 수")
plt.xticks(rotation=0)
plt.legend(title="진단")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()
```

### 차트 3: 나이 vs. 최대 심박수 (산점도)

*"나이가 들면 최대 심박수가 떨어지는가? 심장질환 환자는 패턴이 다른가?"*

```python
colors = df["target"].map({0: "#4CAF50", 1: "#F44336"})

plt.figure(figsize=(9, 5))
plt.scatter(df["age"], df["thalach"], c=colors, alpha=0.6, edgecolors="white", s=50)
plt.title("나이 vs. 최대 심박수", fontsize=15, fontweight="bold")
plt.xlabel("나이 (세)")
plt.ylabel("최대 심박수 (bpm)")

import matplotlib.patches as mpatches
plt.legend(handles=[
    mpatches.Patch(color="#4CAF50", label="질환 없음"),
    mpatches.Patch(color="#F44336", label="심장질환")
])
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

> **차트 읽는 법:** 점 하나가 환자 한 명입니다. 초록 = 건강, 빨강 = 심장질환. 패턴이 보이나요? (힌트: 우하단을 보세요.)

### 차트 4: 진단별 콜레스테롤 (박스 플롯)

*"심장질환 환자의 콜레스테롤이 더 높은가?"*

```python
fig, ax = plt.subplots(figsize=(7, 5))

no_disease = df[df["target"] == 0]["chol"]
disease = df[df["target"] == 1]["chol"]

bp = ax.boxplot(
    [no_disease, disease],
    labels=["질환 없음", "심장질환"],
    patch_artist=True,
    medianprops=dict(color="red", linewidth=2)
)
bp["boxes"][0].set_facecolor("#C8E6C9")
bp["boxes"][1].set_facecolor("#FFCDD2")

ax.set_title("진단별 콜레스테롤", fontsize=15, fontweight="bold")
ax.set_ylabel("콜레스테롤 (mg/dl)")
ax.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()
```

> **박스 플롯 읽는 법:** 빨간 선이 중앙값. 박스가 중간 50% 값을 나타냅니다. "수염" 바깥의 점들은 이상치(비정상적으로 높거나 낮은 값)입니다.

---

## 마무리

### 스포일러를 기억하시나요?

처음으로 돌아가보세요. 시작 전에 보여준 차트 4개? **방금 그것 전부를 직접 만들었습니다.** 처음부터. 90분 만에. 파이썬 지식 제로에서.

마법이 아닙니다. 여러분이 한 겁니다.

### 오늘 한 것들

| 단계 | 한 것 | 사용한 파이썬 |
|------|-------|--------------|
| BMI 계산 | 환자 데이터로 수학 | 변수, 연산자, `if/elif/else`, f-string |
| 환자 303명 불러오기 | 인터넷에서 CSV 읽기 | `pd.read_csv()`, `df.head()`, `df.describe()` |
| 질문 6개 | 필터, 그룹화, 카운트 | `.mean()`, `.value_counts()`, `.groupby()`, 필터 |
| 차트 4개 | 패턴 시각화 | `plt.hist()`, `.plot()`, `plt.scatter()`, `boxplot()` |

### 핵심 인사이트

데이터 분석을 하기 위해 파이썬 문법을 외울 필요가 없습니다. 필요한 것은:

1. **무엇이 가능한지 알기** (파이썬은 데이터를 불러오고, 필터하고, 차트 그릴 수 있다)
2. **기본 패턴 알기** (`df["컬럼"].메서드()`)
3. **세부 내용은 찾아보기** (이 문서, Google, AI 어시스턴트)

프로 데이터 사이언티스트도 정확히 이렇게 일합니다.

### 다음은 — Session 2 예고

Session 1에서는 모든 코드를 직접 작성했습니다. **Session 2**에서는 **AI(ChatGPT/Claude) + VS Code**로 같은 심장질환 데이터셋에서 **인터랙티브 웹 대시보드**를 30분 안에 만듭니다.

나이, 성별, 콜레스테롤을 슬라이더와 드롭다운으로 필터링하면 차트가 실시간으로 업데이트되는 웹앱 — 그게 다음 목표입니다.

---

## 부록 A: 빠른 참조

### 변수 & 수학

```python
age = 25                       # 정수 (Integer)
temp = 36.5                    # 소수 (float)
name = "김민준"                 # 텍스트 (string)
is_sick = True                 # 불리언 (True/False)

bmi = weight / (height ** 2)   # 수학은 그냥 됩니다
print(f"결과: {bmi:.1f}")       # f-string: 소수점 1자리
print(f"비율: {0.85:.1%}")      # f-string: 퍼센트 → 85.0%
```

### 조건문

```python
if value < 18.5:
    print("낮음")
elif value < 25.0:
    print("정상")
else:
    print("높음")
```

### pandas — 데이터 분석

```python
import pandas as pd
df = pd.read_csv("file.csv")          # 데이터 불러오기

df.head()                              # 첫 5행
df.shape                               # (행 수, 열 수)
df.describe()                          # 전체 컬럼 통계
df.isnull().sum()                      # 결측값 확인

df["col"].mean()                       # 평균
df["col"].median()                     # 중앙값
df["col"].value_counts()               # 각 값의 개수

df.groupby("A")["B"].mean()           # A로 그룹화한 B의 평균
df[df["age"] > 50]                     # 필터: 50세 초과
df[(df["age"] > 50) & (df["sex"] == 1)]  # 복수 조건

pd.crosstab(df["A"], df["B"])          # 교차표 (피벗)
df["col"].map({0: "아니오", 1: "예"})   # 값을 레이블로 교체
```

### matplotlib — 차트

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(9, 5))

plt.hist(data, bins=20)                # 히스토그램
plt.bar(labels, values)                # 막대 차트
plt.scatter(x, y, c=colors)           # 산점도
plt.boxplot([group1, group2])          # 박스 플롯

plt.title("제목", fontsize=15, fontweight="bold")
plt.xlabel("X축")
plt.ylabel("Y축")
plt.axvline(x=value, color="red", linestyle="--")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

---

## 부록 B: 자주 나오는 오류 & 해결

| 오류 | 원인 | 해결 |
|------|------|------|
| `SyntaxError` | `:`, `)`, `"` 누락 | 해당 줄 오타 확인 |
| `NameError: name 'x' is not defined` | 변수 미생성 | 변수 정의 셀 먼저 실행 |
| `IndentationError` | `if`/`else` 후 들여쓰기 오류 | 정확히 4칸 사용 |
| `KeyError` | 컬럼명 오류 | `df.columns`로 확인 |
| `ModuleNotFoundError` | 라이브러리 없음 | Colab에서 `!pip install 라이브러리명` 실행 |

**막혔을 때:** 오류 메시지를 복사 → ChatGPT나 Claude에 붙여넣기 → 즉시 설명 받기.

---

## 부록 C: 미니 챌린지

아래 답을 보기 전에 직접 해보세요!

**챌린지 1:** 전체 환자의 콜레스테롤 중앙값은?

**챌린지 2:** 40세 미만 환자는 몇 명?

**챌린지 3:** 남성과 여성의 평균 최대 심박수(`thalach`)는 각각?

**챌린지 4 (보너스):** 콜레스테롤(`chol`) vs. 혈압(`trestbps`) 산점도를 심장질환 여부로 색칠해서 그리세요.

---

### 챌린지 정답

**챌린지 1:**

```python
print(f"콜레스테롤 중앙값: {df['chol'].median():.1f} mg/dl")
```

**챌린지 2:**

```python
young = df[df["age"] < 40]
print(f"40세 미만 환자: {len(young)}명")
```

**챌린지 3:**

```python
hr_by_sex = df.groupby("sex")["thalach"].mean()
print(f"여성 평균 최대 심박수: {hr_by_sex[0]:.1f} bpm")
print(f"남성 평균 최대 심박수: {hr_by_sex[1]:.1f} bpm")
```

**챌린지 4:**

```python
colors = df["target"].map({0: "#4CAF50", 1: "#F44336"})

plt.figure(figsize=(9, 5))
plt.scatter(df["chol"], df["trestbps"], c=colors, alpha=0.6, edgecolors="white")
plt.title("콜레스테롤 vs. 혈압", fontsize=15, fontweight="bold")
plt.xlabel("콜레스테롤 (mg/dl)")
plt.ylabel("안정 시 혈압 (mm Hg)")

import matplotlib.patches as mpatches
plt.legend(handles=[
    mpatches.Patch(color="#4CAF50", label="질환 없음"),
    mpatches.Patch(color="#F44336", label="심장질환")
])
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

---

> **Session 2에서 만납시다!**  
> 다음 시간: VS Code와 AI로 이 분석을 인터랙티브 웹 대시보드로 만듭니다.
