from unittest import result


def distance_in_miles(miles):
    kilometers=1.6*miles
    result=("{} miles is equals {:.1f} kilometers".format(miles , kilometers))
    return result
print(distance_in_miles(12))
print(distance_in_miles(14))