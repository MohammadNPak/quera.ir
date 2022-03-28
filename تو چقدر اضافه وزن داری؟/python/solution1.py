# https://quera.org/problemset/3404/

n = int(input())
m = float(input())

bmi = n/(m**2)
print(f"{bmi:.2f}")

if bmi<18.5:
  print("Underweight")
elif 18.5 <= bmi < 25:
  print("Normal")
elif 25 <= bmi < 30:
  print("Overweight")
elif bmi >= 30:
  print("Obese")
