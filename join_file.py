def count_lines(file):
  with open(file, "r", encoding="utf-8") as f:
    count = 0
    for line in f:
      count += 1
    return count
doc_1 = count_lines("1.txt")
doc_2 = count_lines("2.txt")
doc_3 = count_lines("3.txt")

res_dic = {}
data ={}
with open ("1.txt", "r", encoding="utf-8") as f:
  res_dic[doc_1] = ("1.txt", f.read())
# print(res_dic)

with open ("2.txt", "r", encoding="utf-8") as f:
  res_dic[doc_2] = ("2.txt", f.read())
# print(res_dic)

with open ("3.txt", "r", encoding="utf-8") as f:
  res_dic[doc_3] = ("3.txt", f.read())
# print(res_dic)

data = dict(sorted(res_dic.items()))
# print(data)

with open ("result.txt" , "w", encoding="utf-8") as f:
  for key, value in data.items():
    f.write(value[0] +"\n")
    f.write(str(key) +"\n")
    f.write(str(value[1]) +"\n")