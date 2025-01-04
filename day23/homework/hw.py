firstname="tato"
lastname="tevzadze"
age=15
country="Georgia"
city="samtredia"
hobby="Gym"



def myinfo(firstname, lastname, age, country, city, hobby):
    allinfo= f"hello my name is {firstname},{lastname},i am {age} years old, I am living in{country},{city},my favorite hobby is{hobby}"
    return allinfo



getall= myinfo(firstname, lastname, age, country, city, hobby)
print(getall)

    
    