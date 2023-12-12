# duplicate elements are not acceptable on setType
setType = {10, "data", "data1", 50}
listType = [10, 20, 30, 40, 50]
dictionaryType1 = {101: "Shabib", 102:"Abu", 103:"Said", 104:"MD"}
dictionaryType2 = {"MD": 101, "Abu":102, "Said":103, "Shabib":104}
tupleType = ('Xbox', 500.99)
num3 = 1+2j
int_ger = 123
float_er = 1.23
new_number = int_ger + float_er





print(type(num3))
print(type(setType))
print(type(listType))
print(type(dictionaryType1))
print(type(tupleType))
print(type(new_number))
print(dictionaryType1[101])
print(dictionaryType2['MD'])