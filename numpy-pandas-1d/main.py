import os
import pandas as pd
import numpy as np

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


countries = np.array([
    'Algeria', 'Argentina', 'Armenia', 'Aruba', 'Austria', 'Azerbaijan',
    'Bahamas', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Bolivia',
    'Botswana', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi',
    'Cambodia', 'Cameroon', 'Cape Verde'
])

# Female school completion rate in 2007 for those 20 countries
female_completion = np.array([
    97.35583,  104.62379,  103.02998,   95.14321,  103.69019,
    98.49185,  100.88828,   95.43974,   92.11484,   91.54804,
    95.98029,   98.22902,   96.12179,  119.28105,   97.84627,
    29.07386,   38.41644,   90.70509,   51.7478,   95.45072
])

# Male school completion rate in 2007 for those 20 countries
male_completion = np.array([
    95.47622,  100.66476,   99.7926,   91.48936,  103.22096,
    97.80458,  103.81398,   88.11736,   93.55611,   87.76347,
    102.45714,   98.73953,   92.22388,  115.3892,   98.70502,
    37.00692,   45.39401,   91.22084,   62.42028,   90.66958
])

def overall_completion_rate(female_completion, male_completion):
    return ((male_completion + female_completion) / 2.)

overall_rate = overall_completion_rate(female_completion, male_completion)
print overall_rate

def standardize(values):
    return (values - values.mean()) / values.std() 

standardized_values = standardize(female_completion)
print standardized_values


# = creates new reference
a = np.array([1, 2, 3, 4, 5])
b = a
a = a + np.array([1, 1, 1, 1, 1])
print(b)

# += modifies inplace
a = np.array([1, 2, 3, 4, 5])
b = a
a += np.array([1, 1, 1, 1, 1])
print(b)

# Slicing array makes view into array
a = np.array([1, 2, 3, 4, 5])
s = a[:3]
s[0] = 100
print a
