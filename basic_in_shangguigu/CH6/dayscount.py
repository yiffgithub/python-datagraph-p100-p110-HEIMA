date = input("Enter the date in the format yyyy-mm-dd: ")
date = date.split('-')
print(date)
year = int(date[0])
month = int(date[1])
day = int(date[2])

days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if year % 4 == 0:
    days[2] = 29
else:
    days[2] = 28

result = 0
calculation_formula = "Calculating total days from the start of the year:\n"
for i in range(month):
    result += days[i]
    if i == 0:
        continue;
    else:
        calculation_formula += f"  {days[i+1]}+ ";

result += day
calculation_formula += f"  {day} "
calculation_formula += f"= {result}"

print(calculation_formula)
