# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Michael Hurtado
# Section: 569
# Assignment: 11.13 LAB: Weather Data
# Date: 13 11 2022
# setting variables
list = []
max_temp = 0
min_temp = 1000000000000000000000000000000000000000000000000000000000000000
total_preciptation = 0
# creating a list of lists with the data
with open("WeatherDataCLL.csv", "r") as File:
    for current_line in File:
        list.append(current_line.split(','))
del list[0]
# finding max temp, min temp, and avg preciptation
for i in range(len(list)):
    if int(list[i][4]) > max_temp:
        max_temp = int(list[i][4])
    if int(list[i][5][:-1]) < min_temp:
        min_temp = int(list[i][5][:-1])
    total_preciptation += float(list[i][2])
avg_preciptation = total_preciptation / len(list)
# printing results
print(f'3-year maximum temperature: {max_temp} F')
print(f'3-year minimum temperature: {min_temp} F')
print(f'3-year average precipitation: {avg_preciptation:.3f} inches')
# getting user inputs
month = input("Please enter a month: ")
month_original = month
year = input("Please enter a year: ")
# changing user input into number that goes with month
if month == "January":
    month = "1"
elif month == "February":
    month = "2"
elif month == "March":
    month = "3"
elif month == "April":
    month = "4"
elif month == "May":
    month = "5"
elif month == "June":
    month = "6"
elif month == "July":
    month = "7"
elif month == "August":
    month = "8"
elif month == "September":
    month = "9"
elif month == "October":
    month = "10"
elif month == "November":
    month = "11"
elif month == "December":
    month = "12"
# setting variables
total_maxtemp = 0
days = 0
days_rain = 0
total_wind = 0
# if date matches user input it will add to variables
for i in range(len(list)):
    if (list[i][0][0:2].strip("/") == month) and (list[i][0][-4:] == year):
        total_maxtemp += int(list[i][4])
        total_wind += float(list[i][1])
        if float(list[i][2]) > 0:
            days_rain += 1
        days += 1
# calculates the average
avg_maxtemp = total_maxtemp / days
avg_wind = total_wind /days
avg_rain = (days_rain / days) * 100
# prints results
print(f'For {month_original} {year}:')
print(f'Mean maximum daily temperature: {avg_maxtemp:.1f} F')
print(f'Mean daily wind speed: {avg_wind:.2f} mph')
print(f'Percentage of days with precipitation: {avg_rain:.1f}%')