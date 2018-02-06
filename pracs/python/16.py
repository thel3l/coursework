import pickle

with open('TEXT1.TEXT', 'w') as file:
    d = {'1': 'I', '2': 'II', '3': 'III', '4': 'IV', '5': 'V', '6': 'VI', '7': 'VII', '8': 'VII', '9': 'IX', '10': 'X'}
    pickle.dump(d, file)

with open('TEXT1.TEXT', 'r') as file:
    d = pickle.load(file)

while True:
    dec = str(int(raw_input('Enter decimal number: ')))
    if dec in d.keys():
        print 'The equivalent roman numeral is', d[dec]
    else:
        print 'The equivalent roman numeral is not stored.' 