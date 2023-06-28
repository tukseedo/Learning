catNames = []
while True:
    print('Enter name of Cat ' + str(len(catNames) + 1) + ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name] # LIST CONCATENATION
print('The cat names are:')
for name in catNames:
    print(name)