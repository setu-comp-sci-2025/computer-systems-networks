## Python Overview

- “Has anyone used Python before?”
- “What kinds of things do you think Python is used for?”
- “Why might Python be good for beginners?”

------

## ⚙️ Interpreted vs Compiled

- ## What do you think ‘interpreted’ means?”

  👉 **Answer:**

  - It means the code is **run line-by-line by an interpreter**
  - The program is executed **directly**, without being turned into machine code first

  💡 Simple way to say it:

  > “Python reads and runs your code one line at a time.”

  ------

  ## ❓ “Why might interpreted languages be easier to debug?”

  👉 **Answer:**

  - You see errors **immediately when they happen**
  - You can test code **one line at a time**
  - No need to compile the whole program before running it

  💡 Simple explanation:

  > “If something goes wrong, Python tells you straight away and shows you where.”

  ------

  ## ❓ “Can anyone name a compiled language?”

  👉 **Answer examples:**

  - C
  - C++
  - Java (compiled to bytecode)
  - Rust

  💡 You could say:

  > “Languages like C or C++ are compiled—they’re turned into machine code before running.”

------

## 📦 Variables

- “What is a variable?”
- “What happens if I change a variable after assigning it?”
- “Can a variable in Python change type?”

Is this allowed in Python?”

```
humidity = 66
humidity = "66%"
```

------

## 🧵 f-Strings

- “What does the `f` do in front of a string?”
- “What goes inside the `{}`?”
- “Why are f-strings better than concatenation?”

------

## 🔀 Conditionals

- “What will happen if the temperature is 20?”
- “Which block runs first—`if`, `elif`, or `else`?”
- “Can more than one of these run?”

------

## ⌨️ User Input

- “What type does `input()` return?”
- “Why do we need `float()` here?”
- “What happens if the user enters text instead of a number?”

------

## 🔧 Functions

- “Why do we use functions?”
- “What does `def` do?”
- “What happens if we don’t call the function?”

------

## 📥 Parameters & Arguments

- “What’s the difference between a parameter and an argument?”
- “What does a default value do?”
- “What will this print if `show_humidity=False`?”

------

## 🔁 Loops (For)

- “How many times will this loop run?”

```
for i in range(5):
```

- “What values does `i` take?”
- “Why do we use `i + 1`?”

------

## 🔁 Loops (Lists)

```
for color in colors:
```

- “What is `color` here?”
- “Do we need an index in this loop?”

------

## 🔄 While Loop

- “What would happen if we forgot `count += 1`?”
- “When should we use a `while` instead of a `for` loop?”

------

## 🔤 Strings

- “What is the first character of this string?”
- “What does `len()` return?”
- “What does `[::-1]` do?”

👉 Challenge:

- “How would you remove the first and last character?”

------

## 📂 Files

- “What does `"w"` mean?”
- “What’s the difference between `"w"` and `"a"`?”
- “Why do we use `with open(...)`?”

------

## 📊 Lists

- “What type of data structure is a list?”
- “How do we calculate the average?”
- “What does `_` mean in this loop?”

```
for _ in range(5):
```

------

## 📡 Networking

- “What kind of data do we get back from an API?”
- “Why do we subtract 273.15?”
- “What format is `response.json()`?”

------

## 🔍 Regular Expressions

- “What do you think this pattern is checking?”
- “What does `\d` mean?”
- “Where might regex be useful in real life?”

------

## 📦 Modules

- “Why do we use modules?”
- “What’s the difference between `import math` and `from math import sqrt`?”

------

## 🧠 Nice quick engagement trick

Every few slides, ask:

- “What do you think this code will output?”

This works especially well with:

- slicing
- loops
- conditionals