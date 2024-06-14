A = int(input().strip())
B = int(input().strip())
C = int(input().strip())

number_result = A + B - C

strA = str(A)
strB = str(B)
strC = str(C)

string_concat = strA + strB
string_result = int(string_concat) - int(strC)

print(number_result)
print(string_result)
