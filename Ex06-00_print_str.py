print("start String")
str1 = "Python OOT"
str2 = 'Python OOT'
str3 = "'Python OOT'"
str4 = '"Python OOT"'
print(str1, str2, str3, str4)

str1 = "python programing"
# str1 = "รติวัฒน์ information Technology"
print("ตัวอักษร ลำดับที่ :1",str1[0])
print("ตัวอักษร ลำดับที่ :1-7",str1[0:6])
print("ตัวอักษร ลำดับที่ :1-7 ตัดครั้งละ2 ตัว ตั้งแต่ลำดับที่ 3-7 ทิ้ง >>",str1[0:6:2])
print("ตัวอักษร ลำดับที่ :8-19" ,str1[7:18])
print("ตัวอักษร ลำดับที่ :8-19 ตัดตั้งแต่ลำดับที่ 9-19 ทิ้ง" ,str1[7:18:2])

str1 = 'ohio'
for data in str1:
    if 'a' in data or 'e' in data or 'i' in data or 'o' in data or 'u' in data:
        print(data, end='')
print("  แสดงข้อมูลว่า มี a,e,i,o,u อยู่ในข้อความหรือไม่ \n")
#str1 = "abc"
#str2 = "xyz"
str1 = "information"
str2 = ":"
str3 = "technology"
print(str1+str2+str3)
print(str1, str2, str3)
print(str1*1)
print((str1+str3)*2)

print("a" == "A")
print("a" != "A")
print("a" < "A")
print("aa" <= "aA")
print("abc" < "ab" + "C")
print("aaa" <= "a" + "aa")

str1 = "a) My Python Program"
str2 = "-"
str3 = ("01","01","19")
str4 = "x12"
print(str1.count("P"))
print(str1.count("P", 7))
print(str1.count("P", 7, 10))
print(len(str1))
print(str1.capitalize())
print(str1.lower())
print(str1.upper())
print(str1.swapcase())
print(str1.strip())
print(str1.find("P"))
print(str1.find("P", 7))
print(str1.find("P", 7, 10))
print(str1.find("Programs"))
print(str1.replace("My", ""))
print(str2.join(str3))
print(str4.isdigit())
print(str4.ljust(6, "*"))
print(str4.rjust(6, "*"))
print("end String")
print("start List&Tuple")
list1 = ["Tiger", "20", "Smile", "bangkok",  "Snail", "081-8188216"]
print("list1[0] = " , list1[0])
print("list1[0:2] = ", list1[0:2])
print("list1[1:6:4] = ", list1[1:6:4])
tuple1 = ("Tiger", "20", "Smile", "bangkok",  "Snail", "081-8188216")
print("tuple1[0] = " , tuple1[0])
print("tuple1[0:2] = ", tuple1[0:2])
print("tuple1[1:6:4] = ", tuple1[1:6:4])

list1 = ['o', 'h', 'i', 'o']
for data in list1:
    if 'a' in data or data == 'e' or data == 'i' or data == 'o' or data == 'u':
        print(data, end='')
print("\n")
tuple1 = ('o', 'h', 'i', 'o')
for data in tuple1:
    if 'a' in data or data == 'e' or data == 'i' or data == 'o' or data == 'u':
        print(data, end='')
print("\n")

list1 = ["Tiger", 20, "Smile", 20, "Snail", 30]
tuple1 = ("Tiger", 20, "Smile", 20, "Snail", 30)
print(list1.count(20))
print(tuple1.count(30))
print(len(list1))
print(len(tuple1))
print(list1.index(20))
print(tuple1.index(30))
list1.append("Coconut")
list1.append(22)
print(list1)
list1.remove(30)
print(list1)
list1.pop(2)
print(list1)
list1.clear()
print(list1)
print("end List&Tuple")

print("start Set")
set1 = {'o', 'h', 'i', 'o'}
for data in set1:
    if 'a' in data or data == 'e' or data == 'i' or data == 'o' or data == 'u':
        print(data, end='')
print("\nend Set")

set1 = {"pig", "dog", "bird", "chicken"}
set2 = {"pig", "mushroom", "duck", "chicken"}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
set1.add("lion")
print(set1)
set2.remove("duck")
print(set2)
set1.clear()
print(set1)

data  = {"name": "Anna", "age": 22, "height": 165}
print(data["name"])
print(data[ "age"])
print(data["height"])

dict1  = {"name": "Anna", "age": 22, "height": 165}
print(len(dict1))
d = dict1.keys()
print(d)
d = dict1.values()
print(d)
d = dict1.items()
print(d)
d = dict1.get("name")
print(d)
dict1.update({"weight": 45})
print(dict1)
dict1.pop("name")
print(dict1)
print(dict1)
dict1.clear()
