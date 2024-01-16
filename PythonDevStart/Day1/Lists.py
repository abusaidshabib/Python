mylist = [1,2,3]
mylist = ['string value', 1, 2,3,23.2, True, 'asdf', [1,2,3]]
print(len(mylist))
print(mylist[0])
print(mylist[:6])
mylist[0] = "changed value"
mylist.append('New Item')
mylist.append(['New Item'])
mylist.extend('new Item')
mylist.pop()
print(mylist)