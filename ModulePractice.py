import requests, sys

x = requests.get('https://grayphite.com/')
# print(x.text) => It will show huge text from website

file = sys.argv[0]
a = int(sys.argv[1])
b = int(sys.argv[2])
print(f'File name: {file}', int(sys.argv[1]), int(sys.argv[2]),a+b)