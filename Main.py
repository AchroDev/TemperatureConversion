#Temperature conversion function will accept temps list and tempScale letter value
def convertTemp(temps, tempScale):
    if tempScale == "F":                   #If temperature scale is Fahrenheit, calculate Celsius equivalent
        #FahrenheitToCelsius(temp):
        temps[0] = ((temps[1]-32) * 5/9)
    elif tempScale == "C":                 #If temperature scale is Celsius, calculate Fahrenheit equivalent
        #CelsiusToFahrenheit(temp):
        temps[1] = ((temps[0] * 9/5) + 32)
    #Returns temps list
    return(temps)

#Prompt the use to enter a temperature value and scale
tempEntered = float(input("Enter a temperature value: "))
tempScale = input("Enter a single letter to indicate the temperature scale (C or F): ")

tempScale = (tempScale.upper())  #Store upper case value of temperature scale entered

#Initialize a list to hold temperature values to pass to function
temps = [0,0]

#Evaluate temperature scale entered
if tempScale == "C":
    temps[0] = tempEntered #Populate Celsius list portion zero with temperature value entered
elif tempScale == "F":
    temps[1] = tempEntered #Populate Fahrenheit list portion one with temperature value entered

#Call function to conver temperatures passing in temperature values in list and letter code for temperature scale
convertTemp(temps, tempScale)

#Print results from temperature conversion function
print ("You entered", tempEntered, " degrees ", tempScale, ">>>")
print ("The temperature in Celsius is ", temps[0])
print ("The temperature in Fahrenheit is ", temps[1])