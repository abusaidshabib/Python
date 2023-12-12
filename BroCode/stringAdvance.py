# slicing = create a substring by extracting elements from another string
# indexing[] or slice[]
# [start:stop:step]

name = "Md. Abu Said Shabib"

#=================== This is using indexing[]
# [start:stop:step]
first_name = name[0:12]
last_name = name[13:]
step_name = name[0:13:2]
step_name1 = name[0:13:3]
reversed_name = name[::-1]
print(first_name +" "+ last_name)
print(step_name)
print(step_name1)
print(reversed_name)

#=================== This is using slice[]
website = "https://web.whatsapp.com/"
website2= "https://www.google.com/"
# (start,stop,step)
sliced = slice(8,-5)
print(website[sliced])
print(website2[sliced])