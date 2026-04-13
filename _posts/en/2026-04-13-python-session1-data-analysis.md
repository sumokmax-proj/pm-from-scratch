---
layout: post
title: "Python for Biomedical Students — Session 1: Your First Data Analysis"
date: 2026-04-13 09:00:00 +0900
lang: en
ref: python-session-1
categories: [tutorials]
tags: [python, data-analysis, pandas, matplotlib, tutorial]
description: "Learn Python through real data analysis. In 90 minutes, analyze 303 heart disease patients and build 4 charts — starting from zero Python knowledge."
---

> **Instructor:** Max Kang  
> **Duration:** 90 minutes  
> **Tool:** Google Colab (browser only — no installation needed)  
> **Goal:** Analyze real patient data from scratch. You'll pick up Python naturally along the way.

---

## Spoiler Alert — Here's What You'll Build Today

Before we start, let me show you the **end result**. By the end of this 90-minute session, you will have written Python code that produces all of this:

**Finding 1: Age distribution of 303 heart disease patients**

```
A histogram showing most patients are between 50-60 years old,
with a red dashed line marking the average age.
```

**Finding 2: Gender matters**

```
A bar chart revealing that male patients in this dataset have
a significantly higher rate of heart disease than female patients.
```

**Finding 3: Heart rate tells a story**

```
A scatter plot of Age vs. Max Heart Rate, where heart disease
patients (red dots) cluster in the lower-right — older age,
lower max heart rate.
```

**Finding 4: Cholesterol comparison**

```
A box plot comparing cholesterol levels between the two groups,
showing the distribution, median, and outliers side by side.
```

**All of this from a dataset of real patients. All of it written by you. Starting from zero.**

If that sounds impossible in 90 minutes — good. That surprise is the whole point. Let's go.

---

## What We'll Do Today

We're going to analyze a **real heart disease dataset** — 303 patients, 14 medical features, and a diagnosis of whether each patient has heart disease or not.

Along the way, you'll naturally learn the Python you need. No boring grammar drills — we jump straight into data.

| Time | What We Do |
|------|-----------|
| 0:00 | Spoiler alert + set up Google Colab |
| 0:10 | Calculate a patient's BMI (learn variables & math) |
| 0:25 | Load the Heart Disease dataset |
| 0:45 | Ask questions to the data |
| 1:05 | Visualize the answers (build those spoiler charts!) |
| 1:25 | Wrap up + preview of Session 2 |

---

## Part 1 — Setting Up (10 min)

### Why Python?

One sentence: **Python is the #1 language in data science, AI, and biomedical research** — and it reads almost like English:

```python
if blood_pressure > 140:
    print("Hypertension detected")
```

You probably understood that without any programming experience. That's the beauty of Python.

### Opening Google Colab

1. Go to **<https://colab.research.google.com>**
2. Sign in with your Google account
3. Click **"New Notebook"**
4. You'll see a blank **code cell** — type Python here, press `Shift + Enter` to run

That's it. No installation, no setup. Let's code.

### Hello World

Type this and press `Shift + Enter`:

```python
print("Hello, Biomedical World!")
```

Output:

```
Hello, Biomedical World!
```

`print()` displays text on screen. The text inside quotes is called a **string**. Congratulations — you just ran Python!

---

## Part 2 — Your First Calculation: Patient BMI (15 min)

Let's say you have a patient: 70 kg, 175 cm tall. What's their BMI?

### Step 1: Store the data in variables

A **variable** is a name that holds a value — like a labeled container.

```python
weight_kg = 70
height_cm = 175
```

Run this cell. Nothing visible happens — Python just remembered those numbers.

> **Naming tip:** Use lowercase with underscores: `blood_pressure`, `heart_rate`. Lines starting with `#` are **comments** — Python ignores them, they're notes for humans.

### Step 2: Calculate BMI

BMI = weight ÷ height² (in meters)

```python
height_m = height_cm / 100
bmi = weight_kg / (height_m ** 2)
print(bmi)
```

Output: `22.857142857142858` — correct, but messy. Let's clean it up:

```python
print(f"BMI: {bmi:.1f}")
```

Output: `BMI: 22.9`

> **f-string:** Put `f` before the quotes, then `{variable:.1f}` inside to display 1 decimal place. You'll use this a lot.

### Step 3: Classify the BMI

```python
if bmi < 18.5:
    print("Underweight")
elif bmi < 25.0:
    print("Normal weight")
elif bmi < 30.0:
    print("Overweight")
else:
    print("Obese")
```

Output: `Normal weight`

> **How `if/elif/else` works:** Python checks each condition from top to bottom and runs the first one that's true. The indented code (4 spaces) belongs to that condition.

### Quick Math Reference

| Operator | Meaning | Example |
|----------|---------|---------|
| `+` | Addition | `10 + 3` → `13` |
| `-` | Subtraction | `10 - 3` → `7` |
| `*` | Multiplication | `10 * 3` → `30` |
| `/` | Division | `10 / 3` → `3.33` |
| `**` | Power | `10 ** 2` → `100` |

### Try it yourself

Change the weight and height values and run again. What's *your* BMI?

```python
# Replace these with your own values
weight_kg = ___
height_cm = ___

height_m = height_cm / 100
bmi = weight_kg / (height_m ** 2)
print(f"My BMI: {bmi:.1f}")
```

---

## Part 3 — Loading the Heart Disease Dataset (20 min)

Now let's move from one patient to **303 patients**. Doing this by hand would be insane. That's where `pandas` comes in.

### Importing pandas

```python
import pandas as pd
```

> `pandas` is a tool that gives Python the ability to handle data tables — think of it as Excel inside Python. We nickname it `pd` to save typing.

### Loading the data

```python
url = "https://raw.githubusercontent.com/datasets/heart-disease/main/data/heart.csv"
df = pd.read_csv(url)

print(f"Loaded! {df.shape[0]} patients, {df.shape[1]} features")
```

> `df` stands for **DataFrame** — a table where each row is a patient and each column is a feature.

### First look

```python
df.head()
```

This shows the first 5 rows. You'll see something like:

| | age | sex | cp | trestbps | chol | … | target |
|-|-----|-----|----|----------|------|---|--------|
| 0 | 63 | 1 | 3 | 145 | 233 | … | 1 |
| 1 | 37 | 1 | 2 | 130 | 250 | … | 1 |

### What do these columns mean?

| Column | Meaning | Values |
|--------|---------|--------|
| `age` | Patient's age | Years |
| `sex` | Biological sex | 1 = Male, 0 = Female |
| `cp` | Chest pain type | 0–3 |
| `trestbps` | Resting blood pressure | mm Hg |
| `chol` | Cholesterol level | mg/dl |
| `fbs` | Fasting blood sugar > 120? | 1 = Yes, 0 = No |
| `thalach` | Max heart rate (exercise) | bpm |
| `exang` | Chest pain during exercise? | 1 = Yes, 0 = No |
| `target` | **Heart disease diagnosis** | **1 = Yes, 0 = No** |

### Quick overview

```python
df.describe()
```

This gives you count, mean, standard deviation, min, max, and quartiles for **every column at once**. The kind of summary that would take 30 minutes in a spreadsheet.

### Check for missing data

```python
df.isnull().sum()
```

If all zeros → great, the dataset is clean!

---

## Part 4 — Asking Questions to the Data (20 min)

This is where it gets fun. We'll ask questions in English, then answer them in one or two lines of Python.

### Q1. What's the average age of patients?

```python
avg_age = df["age"].mean()
print(f"Average age: {avg_age:.1f} years")
```

> `df["age"]` grabs the "age" column. `.mean()` calculates the average. That's it — one line.

### Q2. How many patients have heart disease?

```python
df["target"].value_counts()
```

Output:

```
1    165
0    138
```

165 patients with heart disease, 138 without. Let's make it clearer:

```python
counts = df["target"].value_counts()
total = len(df)

print(f"Heart disease:    {counts[1]} patients ({counts[1]/total*100:.1f}%)")
print(f"No heart disease: {counts[0]} patients ({counts[0]/total*100:.1f}%)")
```

### Q3. Is cholesterol different between the two groups?

```python
chol_by_group = df.groupby("target")["chol"].mean()

print("Average cholesterol (mg/dl):")
print(f"  No disease: {chol_by_group[0]:.1f}")
print(f"  Disease:    {chol_by_group[1]:.1f}")
```

> `.groupby("target")` splits the data into two groups (disease vs. no disease), then `.mean()` calculates the average for each. This is like a pivot table in Excel.

### Q4. What about blood pressure?

```python
bp_by_group = df.groupby("target")["trestbps"].mean()

print("Average resting blood pressure (mm Hg):")
print(f"  No disease: {bp_by_group[0]:.1f}")
print(f"  Disease:    {bp_by_group[1]:.1f}")
```

### Q5. Who are the high-risk patients?

Let's filter: patients over 60 with cholesterol above 250.

```python
high_risk = df[(df["age"] > 60) & (df["chol"] > 250)]

print(f"High-risk patients (age>60, chol>250): {len(high_risk)} out of {len(df)}")
high_risk[["age", "sex", "chol", "trestbps", "target"]].head(10)
```

> **Filter syntax:** Each condition goes in parentheses, connected with `&` (and) or `|` (or). This is how you search through thousands of records in seconds.

### Q6. Male vs. Female — who has more heart disease?

```python
gender_disease = pd.crosstab(
    df["sex"].map({1: "Male", 0: "Female"}),
    df["target"].map({1: "Disease", 0: "No Disease"})
)
print(gender_disease)
```

> `.map({1: "Male", 0: "Female"})` replaces numbers with readable labels. The `{1: "Male", 0: "Female"}` part is called a **dictionary** — it maps the value on the left to the label on the right.

---

## Part 5 — Visualizing the Answers (20 min)

Numbers tell the truth, but charts tell the **story**. Let's turn our findings into visuals.

```python
import matplotlib.pyplot as plt
```

> `matplotlib` is Python's most popular charting library. We nickname it `plt`.

### Chart 1: Age Distribution (Histogram)

*"What ages are most common in this dataset?"*

```python
plt.figure(figsize=(9, 5))
plt.hist(df["age"], bins=20, color="steelblue", edgecolor="white")
plt.axvline(df["age"].mean(), color="red", linestyle="--",
            label=f'Mean: {df["age"].mean():.1f} years')
plt.title("Age Distribution of Patients", fontsize=15, fontweight="bold")
plt.xlabel("Age (years)")
plt.ylabel("Number of Patients")
plt.legend()
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()
```

> **What's a histogram?** Each bar represents an age range. The taller the bar, the more patients in that range. The red dashed line shows the average.

### Chart 2: Heart Disease by Gender (Bar Chart)

*"Are men or women more affected?"*

```python
gender_disease = pd.crosstab(
    df["sex"].map({1: "Male", 0: "Female"}),
    df["target"].map({1: "Disease", 0: "No Disease"})
)

gender_disease.plot(kind="bar", color=["#4CAF50", "#F44336"], 
                    figsize=(8, 5), edgecolor="white")
plt.title("Heart Disease by Gender", fontsize=15, fontweight="bold")
plt.xlabel("Gender")
plt.ylabel("Number of Patients")
plt.xticks(rotation=0)
plt.legend(title="Diagnosis")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()
```

### Chart 3: Age vs. Max Heart Rate (Scatter Plot)

*"Does max heart rate drop with age? Is the pattern different for heart disease patients?"*

```python
colors = df["target"].map({0: "#4CAF50", 1: "#F44336"})

plt.figure(figsize=(9, 5))
plt.scatter(df["age"], df["thalach"], c=colors, alpha=0.6, edgecolors="white", s=50)
plt.title("Age vs. Maximum Heart Rate", fontsize=15, fontweight="bold")
plt.xlabel("Age (years)")
plt.ylabel("Max Heart Rate (bpm)")

import matplotlib.patches as mpatches
plt.legend(handles=[
    mpatches.Patch(color="#4CAF50", label="No Disease"),
    mpatches.Patch(color="#F44336", label="Heart Disease")
])
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

> **Reading this chart:** Each dot is one patient. Green = healthy, red = heart disease. Notice any pattern? (Hint: look at the bottom-right area.)

### Chart 4: Cholesterol by Diagnosis (Box Plot)

*"Is cholesterol higher in heart disease patients?"*

```python
fig, ax = plt.subplots(figsize=(7, 5))

no_disease = df[df["target"] == 0]["chol"]
disease = df[df["target"] == 1]["chol"]

bp = ax.boxplot(
    [no_disease, disease],
    labels=["No Disease", "Heart Disease"],
    patch_artist=True,
    medianprops=dict(color="red", linewidth=2)
)
bp["boxes"][0].set_facecolor("#C8E6C9")
bp["boxes"][1].set_facecolor("#FFCDD2")

ax.set_title("Cholesterol by Diagnosis", fontsize=15, fontweight="bold")
ax.set_ylabel("Cholesterol (mg/dl)")
ax.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()
```

> **Reading a box plot:** The red line is the median. The box covers the middle 50% of values. Dots outside the "whiskers" are outliers (unusually high or low values).

---

## Wrap Up

### Remember the Spoiler Alert?

Go back to the top. Those 4 charts we showed you before we started? **You just built every single one of them.** From scratch. In 90 minutes. Starting from zero Python knowledge.

That wasn't magic. That was you.

### What You Just Did

| Step | What You Did | Python You Used |
|------|-------------|-----------------|
| Calculated BMI | Math with patient data | Variables, operators, `if/elif/else`, f-strings |
| Loaded 303 patients | Read a CSV from the internet | `pd.read_csv()`, `df.head()`, `df.describe()` |
| Asked 6 questions | Filtered, grouped, counted | `.mean()`, `.value_counts()`, `.groupby()`, filters |
| Made 4 charts | Visualized patterns | `plt.hist()`, `.plot()`, `plt.scatter()`, `boxplot()` |

### The Key Insight

You didn't need to memorize Python syntax to do real data analysis. You needed to:

1. **Know what's possible** (Python can load data, filter it, chart it)
2. **Know the basic pattern** (`df["column"].method()`)
3. **Look up the details** when needed (this document, Google, AI assistants)

That's exactly how professional data scientists work.

### What's Next — Session 2 Preview

In Session 1, you wrote every line by hand. In **Session 2**, we'll use **AI (ChatGPT/Claude) + VS Code** to build an **interactive web dashboard** from this same Heart Disease dataset — in under 30 minutes.

---

## Appendix A: Quick Reference

### Variables & Math

```python
age = 25                       # Integer
temp = 36.5                    # Decimal (float)
name = "Nguyen"                # Text (string)
is_sick = True                 # Boolean (True/False)

bmi = weight / (height ** 2)   # Math works as expected
print(f"Result: {bmi:.1f}")    # f-string: 1 decimal place
print(f"Percent: {0.85:.1%}")  # f-string: percentage → 85.0%
```

### Conditionals

```python
if value < 18.5:
    print("Low")
elif value < 25.0:
    print("Normal")
else:
    print("High")
```

### pandas — Data Analysis

```python
import pandas as pd
df = pd.read_csv("file.csv")          # Load data

df.head()                              # First 5 rows
df.shape                               # (rows, columns)
df.describe()                          # Statistics for all columns
df.isnull().sum()                      # Check missing values

df["col"].mean()                       # Average
df["col"].median()                     # Median
df["col"].value_counts()               # Count each unique value

df.groupby("A")["B"].mean()           # Average of B, grouped by A
df[df["age"] > 50]                     # Filter: age over 50
df[(df["age"] > 50) & (df["sex"] == 1)]  # Multiple conditions

pd.crosstab(df["A"], df["B"])          # Cross-tabulation (pivot)
df["col"].map({0: "No", 1: "Yes"})     # Replace values with labels
```

### matplotlib — Charts

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(9, 5))

plt.hist(data, bins=20)                # Histogram
plt.bar(labels, values)                # Bar chart
plt.scatter(x, y, c=colors)           # Scatter plot
plt.boxplot([group1, group2])          # Box plot

plt.title("Title", fontsize=15, fontweight="bold")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.axvline(x=value, color="red", linestyle="--")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

---

## Appendix B: Common Errors & Fixes

| Error | Likely Cause | Fix |
|-------|-------------|-----|
| `SyntaxError` | Missing `:`, `)`, or `"` | Check the line for typos |
| `NameError: name 'x' is not defined` | Variable not created yet | Run the cell that defines it first |
| `IndentationError` | Wrong spacing after `if`/`else` | Use exactly 4 spaces |
| `KeyError` | Column name wrong | Check with `df.columns` |
| `ModuleNotFoundError` | Library not available | Run `!pip install library_name` in Colab |

**When stuck:** Copy the error message → paste it into ChatGPT or Claude → get an instant explanation.

---

## Appendix C: Mini Challenges

Test yourself! Try these without looking at the answers below.

**Challenge 1:** What is the median cholesterol of all patients?

**Challenge 2:** How many patients are under 40 years old?

**Challenge 3:** What's the average max heart rate (`thalach`) for male vs. female patients?

**Challenge 4 (Bonus):** Create a scatter plot of cholesterol (`chol`) vs. blood pressure (`trestbps`), colored by heart disease diagnosis.

---

### Challenge Solutions

**Challenge 1:**

```python
print(f"Median cholesterol: {df['chol'].median():.1f} mg/dl")
```

**Challenge 2:**

```python
young = df[df["age"] < 40]
print(f"Patients under 40: {len(young)}")
```

**Challenge 3:**

```python
hr_by_sex = df.groupby("sex")["thalach"].mean()
print(f"Female avg max HR: {hr_by_sex[0]:.1f} bpm")
print(f"Male avg max HR:   {hr_by_sex[1]:.1f} bpm")
```

**Challenge 4:**

```python
colors = df["target"].map({0: "#4CAF50", 1: "#F44336"})

plt.figure(figsize=(9, 5))
plt.scatter(df["chol"], df["trestbps"], c=colors, alpha=0.6, edgecolors="white")
plt.title("Cholesterol vs. Blood Pressure", fontsize=15, fontweight="bold")
plt.xlabel("Cholesterol (mg/dl)")
plt.ylabel("Resting Blood Pressure (mm Hg)")

import matplotlib.patches as mpatches
plt.legend(handles=[
    mpatches.Patch(color="#4CAF50", label="No Disease"),
    mpatches.Patch(color="#F44336", label="Heart Disease")
])
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

---

> **See you in Session 2!**  
> Next time: We'll turn this analysis into an interactive web dashboard using VS Code and AI.
