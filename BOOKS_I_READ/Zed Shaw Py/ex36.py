# creating a mapping of cities

states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    "New York":'NY',
    'Michigan':'MI'
}

# create a basic set of states and some cities in them
cities ={
    'CA':"San Francisco",
    'MI':'Detroit',
    'FL':'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities["OR"] = 'Portland'

print('-'*10)

print('NY state has: ',cities['NY'])
print('OR state has: ', cities['OR'])

# print some more states
print('-'*10)
print('Michigan abbreviation is : ',states['Michigan'])
print('Florida abbrevaition is: ',states['Florida'])

print('-'*10)
print('Michigan has: ', cities[states['Michigan']])
print('Florida has: ', cities[states['Florida']])

print('='*10)
for state, abbrev in list(states.items()):
    print(f'{state} is abbrevaited as: {abbrev}')


