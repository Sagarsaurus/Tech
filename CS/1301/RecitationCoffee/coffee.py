def coffee():
    cups_of_coffee = raw_input("How many cups of coffee did you have today? ")
    hours_of_sleep = raw_input("How many hours of sleep did you get last night? ")
    cups_of_coffee = int(cups_of_coffee)
    hours_of_sleep = int(hours_of_sleep)
    score = 3 * cups_of_coffee + hours_of_sleep
    if score >= 12:
        RESULT_OF_COFFEE =  "super hyper"
    elif score >= 6 and score < 12:
        RESULT_OF_COFFEE = "mellow"
    else:
        RESULT_OF_COFFEE = "sluggish"
    return RESULT_OF_COFFEE


def typeOfDay():
    x = raw_input("The weather was favorable today (enter YES for true, NO for false):")
    y = raw_input("I had a good time with my friends today (enter YES for true, NO for false):")
    if x == "YES" and y =="YES":
        RESULT_OF_TYPE_OF_DAY =  "spectacular"
    elif x == "YES" or y =="YES":
        RESULT_OF_TYPE_OF_DAY = "decent"
    else:
        RESULT_OF_TYPE_OF_DAY = "crummy"
    return RESULT_OF_TYPE_OF_DAY

    
def main():
    print "You completed a %s day in a %s manner!!" %(typeOfDay(), coffee())
