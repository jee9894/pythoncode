from mod.sound.etc import mod1 as m
import sys

a = m.add(2,4)
print(a)

b = m.sub(3,4)
print(b)

sys.path.append('c:\\pythoncode\\pythoncode\\mtest')
import mod2

c = mod2.div(3,4)
print(c)