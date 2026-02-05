A = 9 > 5
B = 9 - 5 > 9 + 5
C = True
D = False
print(A, B, C, D)
print("*******************")
print("                 ")
ans = None
x = 0
y = 3
if y != 0:
    ans = x/y
print(ans)
print(y)
print(x)

print("*******************")

strA = "6712345678"
strB = 'วันอังคาร'
strC = '"มิถุนายน"'
strD = "'2568'"
strE = "A & " \
       "B"
strF = "H"
noF = ord(strF)
print(strA, strB, strC, strD, strE, strF, noF)


print("**********************")
listA = ["อ.รติวัฒน์",59, "จ.ตาก", "ผศ.ดร.ธงรบ", 40, "จ.พิษณุโลก"]
print("list A =", listA)
listA.append("ผศ.ไพทูรย์")
listA.append(42)
print ("*************************")
print("list A =", listA)
print(listA[0])
print(listA[1])
print(listA[2])
print(listA[3])
print(listA[4])
print(listA[5])
print(listA[6])

print("*************************")
tupleA = ("อ.รติวัฒน์",59, "จ.ตาก", "ผศ.ดร.ธงรบ", 40, "จ.พิษณุโลก")
tupleB = "ผศ.ไพทูรย์",42, "จ.สุโขทัย", "ผศ.ภาวินี", 41, "จ.เพชรบูรณ์"
print("tuple A =", tupleA)
print("tuple B =", tupleB)
print(tupleA[0])
print(tupleA[1])
print(tupleA[2])
print(tupleB[3])
print(tupleB[4])
print(tupleB[5])
print("*************************")
setA = {"อ.รติวัฒน์",59, "จ.ตาก", "ผศ.ดร.ธงรบ", 40, "จ.พิษณุโลก", 41}
print("set A =", setA)
setA.add("ผศ.ไพทรูย์")
print("set A =", setA)
print('*************************')

scores = {'แอนนา': 20.6, 'มีนา': 22.1, 'วันนา': 23.0}
scores['วันนา'] = 21.7
print("คะแนนของ วันนา :=> ", scores['วันนา'])
print("คะแนนของ มีนา :=> ",scores['มีนา'])
print("คะแนนของ วันนา :=> ",scores['วันนา'])
print("คะแนนของ แอนนา :=> ",scores['แอนนา'])

print("*******************")
a = 5
print(type(a))
b = 6.0
print(type(b))
print("a*b = " , a*b)
c = [1, 2, 3]
print(type(c))
d = (1, 2, 3)
print(type(d))
e = {1, 2, 3}
print(type(e))
f = {1: "one", 2: "two", 3: "three"}
print(type(f))
g = float
print(type(g))
h = len ("อ.รติวัฒน์")
print(type(h))
print ("ความยาวของ ตัวแปร h := " ,h)

print("*******************")
print("A"+"&"+"B")
print("A","&","B")

print(3 + 2)
print(3 - 2)
print(3 * 2)
print(130 / 60)
print("จำนวน ช.ม :  ",130 // 60)
print("จำนวน นาที :  ",130 % 60)
print(3 ** 2)
print("เปรียบเทียบมากกว่าน้อยกว่า")
print(9 == 2)
print(9 != 2)
print(9 > 2)
print(9 >= 2)
print(9 < 2)
print(9 <= 2)

print((9>=2) and (9!=2))
print((9>=2) or (9!=2))
print(not  (9!=2))
print('****************')
A = 65
print("a=" ,  bin(A))
B = 33
print("b=" ,  bin(B))

print("A=" , bin(A & B))
print("A=" , bin(A | B))
print("A=" , bin(A ^ B))
print("B=" , bin(B << 2))





strA = ("Bangkok", 200, "Chiangmai", 200)
print(strA)
strA = ["Bangkok", 200, "Chiangmai", 200]
print(strA)
strA = []
print(strA)
strA = {"Bangkok", 200, "Chiangmai", 200}
print(strA)
str1 = "A"+"&"+"B"
str2 = "A","&","B"
print(str1)
print(str2)

print("ขอดูผลลัพธ์ จากจุดนี้")
print("A"+"&"+"B")
print("A","&","B")
str1 = "A"
print(str1)
Asc1 = (ord(str1))
print(Asc1)
print(chr(Asc1))
a = hex(10)
print(a)
a = oct(10)
print(a)
a = bin(10)
print(a)
A = 7.5
A //= 3
print(A)
A -= 2
print(A)
A *= 8
print(A)
A /= 4
print(A)
A //= 5
print(A)
A %= 3
print(A)
A = 'A'
B = 't'
C = -5.5
D = -2.5
X = 256
Y = 8
print("A :" , A)
print("B :" , B)
print((B <= A) or ((D-C) > 0))
print((X >> 2) | (Y << 1))
