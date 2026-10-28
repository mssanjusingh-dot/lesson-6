height=float( input ( " please enter  ur height in cm") )
weight=float( input ( " please enter  ur weight in kg") )
BMI=weight/(height/100)**2

print(" ur BMI is ",BMI)
if BMI <= 18.4:
    print("u r underweight " )

elif BMI<= 24.9 :
    print(" u r healthy ")

elif BMI<= 29.9 :
    print(" u r overweight ")

elif BMI<= 34.9 :
    print(" u r severly overweight ")

elif BMI<= 39.9 :
    print(" u r obese ")

else :
    print(" u r severly obese ")