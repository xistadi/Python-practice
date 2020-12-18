import json

nums = [23, 33, 12, 39, 60, 6, 10]

filename = "nums.json"
with open(filename, "w") as f:
    json.dump(nums, f) #запись в файл f

file = "nums.json"
with open(file) as f:
    nums_new = json.load(f) #выгружаем из файла f

print(nums_new)