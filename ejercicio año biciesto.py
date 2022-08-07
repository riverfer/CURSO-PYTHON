def isYearLeap(year):
    if  year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("Es año biciesto")
    else:    
        print ("No es año biciesto")

isYearLeap(1900)
isYearLeap(2000)
isYearLeap(2016)
isYearLeap(1987)