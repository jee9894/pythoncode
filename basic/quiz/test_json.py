import json

customer = {
    'id':152352,
    'name':'홍길동',
    'history':[
        {'date':'2015-03-11', 'item':'IPhone'},
        {'date':'2016-02-23', 'item':'Monitor'},
    ]
}

with open('./basic/quiz/data.json', 'wt') as f:
    json.dump(customer, f, indent=4)

with open('./basic/quiz/data.json', 'rt') as f:
    a = json.load(f)
    print(a)