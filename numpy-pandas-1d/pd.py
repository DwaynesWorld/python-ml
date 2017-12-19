import pandas as pd

countries = ['Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda',
             'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan',
             'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus',
             'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia']

life_expectancy_values = [74.7,  75.,  83.4,  57.6,  74.6,  75.4,  72.3,  81.5,  80.2,
                          70.3,  72.1,  76.4,  68.1,  75.2,  69.8,  79.4,  70.8,  62.7,
                          67.3,  70.6]

gdp_values = [1681.61390973,   2155.48523109,  21495.80508273,    562.98768478,
              13495.1274663,   9388.68852258,   1424.19056199,  24765.54890176,
              27036.48733192,   1945.63754911,  21721.61840978,  13373.21993972,
              483.97086804,   9783.98417323,   2253.46411147,  25034.66692293,
              3680.91642923,    366.04496652,   1175.92638695,   1132.21387981]

le = pd.Series(life_expectancy_values)
gdp = pd.Series(gdp_values)

def variable_correlation(x1, x2):
    above = (x1 > x1.mean()) & (x2 > x2.mean())
    below = (x1 < x1.mean()) & (x2 < x2.mean())
    same = (above | below).sum()
    diff = len(x1) - same
    return same, diff


print variable_correlation(le, gdp)


import pandas as pd

countries = [
    'Afghanistan', 'Albania', 'Algeria', 'Angola',
    'Argentina', 'Armenia', 'Australia', 'Austria',
    'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh',
    'Barbados', 'Belarus', 'Belgium', 'Belize',
    'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina',
]


employment_values = [
    55.70000076,  51.40000153,  50.5,  75.69999695,
    58.40000153,  40.09999847,  61.5,  57.09999847,
    60.90000153,  66.59999847,  60.40000153,  68.09999847,
    66.90000153,  53.40000153,  48.59999847,  56.79999924,
    71.59999847,  58.40000153,  70.40000153,  41.20000076,
]

# Employment data in 2007 for 20 countries
employment = pd.Series(employment_values, index=countries)


def max_employment(employment):
    max_country = employment.idxmax()
    max_value = employment[max_country]

    return (max_country, max_value)

print(max_employment(employment))

names = pd.Series([
    'Andre Agassi',
    'Barry Bonds',
    'Christopher Columbus',
    'Daniel Defoe',
    'Emilio Estevez',
    'Fred Flintstone',
    'Greta Garbo',
    'Humbert Humbert',
    'Ivan Ilych',
    'James Joyce',
    'Keira Knightley',
    'Lois Lane',
    'Mike Myers',
    'Nick Nolte',
    'Ozzy Osbourne',
    'Pablo Picasso',
    'Quirinus Quirrell',
    'Rachael Ray',
    'Susan Sarandon',
    'Tina Turner',
    'Ugueth Urbina',
    'Vince Vaughn',
    'Woodrow Wilson',
    'Yoji Yamada',
    'Zinedine Zidane'
])



def reverse_names(names):
    def split_flip(name):
        s = name.split()
        return "{}, {}".format(s[1], s[0])

    return names.apply(split_flip)

print(reverse_names(names))
