# autor: YaRkyungmin
# 2021-12-30
# Python DataType Tuple

# tuple datatype(sequence, immutable)
'''
sequence
중복
수정 X
삭제 X
'''
a = ()
b = (1) 
c = (1,) #원소가 하나일때는 ,를 찍어줘야 Tuple로 인식함 
print(type(a),type(b),type(c))
d = (1,2,3,'4')
tuple_new = 1,2,3 #괄호없이도 tuple 선언 가능하다.
tuple_new1 = 1,
print(type(tuple_new),tuple_new)
print(type(tuple_new1),tuple_new1)

## tuple indexing
tuple_index = (1,2,3,4,5,(6,7,8))
print(tuple_index[1])
print(tuple_index[5][2])

## tuple -> list type cating
tuple_li = (1,2,3)
tuple_li = list(tuple_li)
print(type(tuple_li))

## tuple edit
tuple_edit = (1,2)
### tuple_edit[0] = 2 #error

## tuple slicing
tuple_sli = (1,2,3,4)
print(tuple_sli[:1]) # tuple형태로 하나의 원소를 출력할때는 ,를 붙인상태로 출력됨
print(tuple_sli[:2])

## tuple operator
tuple_op = (1,2,3)
tuple_op2 = (4,5,6)

print(tuple_op+tuple_op2)
print(tuple_op*3)

## tuple function
'''
index
count
'''
tuple_fu = (1,3,46,7,1,1)
print(tuple_fu.index(1)) #찾는 원소가 튜블안에 여러개 포함 되어 있을때는 제일 첫번째 원소 index만 찾아준다.
print(tuple_fu.count(1))

## tuple packing & unpacking
### packing
tuple_pack = ('p','a','c','k','i','n','g')
print(tuple_pack[1])
print(tuple_pack[0])

### unpacking
(x1,x2,x3,x4,x5,x6,x7) = tuple_pack
print(type(x1),type(x2),type(x3))
print(x1,x2,x3,x4,x5,x6,x7)

tuple_unpacking = 1, 2, 3
z1,z2,z3 = tuple_unpacking
print(type(z1),type(z2),type(z3))
print(z1,z2,z3)

list_test = [1,2,3] #list도 unpacking 가능하다
zz,zz1,zz2 = list_test
print(zz,zz1,zz2)