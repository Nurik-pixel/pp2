import re

# 1
a = "abbb"
b = re.search(r'a*b*', a)
print(bool(b))

# 2
a = "abbb"
b = re.fullmatch(r'a(bb|bbb)', a)
print(bool(b))

# 3
a = "abc_def"
b = re.findall(r'[a-z]+_[a-z]+', a)
print(b)

# 4
a = "Abc"
b = re.findall(r'[A-Z][a-z]+', a)
print(b)

# 5
a = "axb"
b = re.fullmatch(r'a.*b', a)
print(bool(b))

# 6
a = "hello, world. test"
b = re.sub(r'[ ,.]', ":", a)
print(b)

# 7
a = "hello_world"
b = ''.join(x.capitalize() for x in a.split('_'))
print(b)

# 8
a = "HelloWorld"
b = re.split(r'(?=[A-Z])', a)
print(b)

# 9
a = "HelloWorld"
b = re.sub(r'(?=[A-Z])', " ", a).strip()
print(b)

# 10
a = "HelloWorld"
b = re.sub(r'([a-z])([A-Z])', r'\1_\2', a).lower()
print(b)