from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re
pattern = r"\+?(\d{1})\s?\(?(\d{3})\)?[-\s]?(\d{3})[-\s]?(\d{2})[-\s]?(\d{2})\s?(\(?(доб.)\s(\d+)\)?)?"
format_str = "+7(\\2)\\3-\\4-\\5 \\7\\8"
persons = []
with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
pprint(contacts_list)


for i in contacts_list[1:] :
  pers = []
  pers.append(i[0])
  if i[1] != '':
    pers.append(i[1])
  else:
    pers.append('')
  if i[2] != '':
    pers.append(i[2])
  else:
    pers.append('')
  if i[3] != '':
    pers.append(i[3])
  else:
    pers.append('')
  if i[4] != '':
    pers.append(i[4])
  else:
    pers.append('')
  if i[5] != '':
    pers.append(re.sub(pattern, format_str,  i[5]))
  else:
    pers.append('')
  if i[6] != '':
    pers.append(i[6])
  else:
    pers.append('')
  persons.append(pers)

print(persons)



# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(persons)
