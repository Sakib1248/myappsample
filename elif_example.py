name = 'Bob'
age = 3000

if name == 'Alice':
    print('Hi Alice')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 2000:
    print('Unlike you Alice is not an undead, immortal vampire.')
elif age > 100:
    print('You are not Alice, granie.')
    
print('Hello world!')
print('What is your name?')
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is:', len(myName))

