#can i drink?

age = 18
title = "none"
allowed_to_drink = False

if age >= 18:
    title = "Adult" 
    if age >= 21:
        allowed_to_drink = True
    else:
        allowed_to_drink = False
else:
    title = "Minor"




