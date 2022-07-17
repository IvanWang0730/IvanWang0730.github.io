import json
with open('PQ-2H.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()
# data1 = data[0]
# print(data1.split('\t')[0])
# print(data1.split('\t')[1].split('(')[0])
with open('PQ-2H.txt', 'r', encoding='utf-8') as f:
    data1 = f.readlines()

data.extend(data1)
data = list(set(data))

# with open('PQ-2H.txt', 'r', encoding='utf-8') as f:
#     data1 = f.readlines()

# with open('PQ-2H.txt', 'r', encoding='utf-8') as f:
#     data1 = f.readlines()

dic_list = []
for d in data:
    dic = {}
    dic["q"] = d.split('\t')[0]
    dic["a"] = d.split('\t')[1].split('(')[0]
    dic_list.append(dic)

with open('../path_question.json', 'w', encoding='utf-8') as f:
    json.dump(dic_list, f, ensure_ascii=False)
