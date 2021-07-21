#program

cash = int(input("depo: "))
percent = int(input("percent: "))
add = int(input("add cash in month: "))
year = int(input("years: "))

def p(num, percent):
  return (num / 100) * percent

def p_add(add, percent):
  result = 0
  count = 12
    while count > 0:
      count -= 1
      per = ((result / 100) * percent)
      result = result + per + add
  return result

def calc(cash , per, a, y):
  c = cash
  p_a = p_add(a, per)
  count = 0
  result = 0
  while count < y:
    per = p(c, percent)
    c = c + per + p_a
    count += 1
  print("Year", count, ":", round(c, 2), " Add:", a * 12, " Your percent:", round(per + (p_a - (a * 12))))
  print("Add all time:", (a * 12) * y + cash, "\n", "Your profit:", round(c - (cash +((a * 12) * y)), 2))

calc(cash, percent, add, year)
