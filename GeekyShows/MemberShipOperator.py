# The membership operators are useful to test for membership in a sequence such as string, lists, tuples and dictionaries.
# There are two type of Membership operator: -
# ---- in
# This operators is used to find an element in the specified sequence.
# It returns True if element is found in the specified sequence else it return False.
# ---- not in

target = "Shabib"
print("Sh" in target)
print("sh" in target)
print("s" in target)

# it works with list, tuples, dictionary, set, 

listed = ['10', 10, 'yu', 'test']
print('test' in listed)

seted = {'10', 10, 'yu', 'test'}
print('test' in seted)

tupled = ('11', 12, '13', '16')
print(12 in tupled)

# ============= not in ====================
print("subs" not in target)

value1 = 10
value2 = 10

print(value1 is value2)
print(value1 is not value2)