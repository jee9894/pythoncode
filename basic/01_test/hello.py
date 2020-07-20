temp = {'name':'jee', 'test':100}

def func(temp):
    temp['name'] = 'kee'

print(temp)
func(temp)
print(temp)

