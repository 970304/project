import yaml

f = open('demo.yaml')

# res = yaml.load(f,Loader=yaml.FullLoader)
res = yaml.load(f, Loader=yaml.FullLoader)
print(res.get('db'))
f.close()
# for i in res:
#     print(i)


# info = {'name':'aa', 'age':18, 'sex':'x'}
# info2 = ["Lily", 19]
#
# ff = open('demo.yaml', 'a')
# print(yaml.dump_all([info,info2],ff))


