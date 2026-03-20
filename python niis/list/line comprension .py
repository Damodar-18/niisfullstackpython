#[expression for item in iterable if codition]
l=[4,6,7,9,23,12]
#l1=[i for i in l]
#l1=[i+3 for i in l]
l1=[i+3 for i in l if i%2==0]
print(l1)