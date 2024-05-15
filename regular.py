
import csv
import re




with open('phonebook_raw.csv', 'r', encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)


def format_all_in_last_name(contact):
  s_occur = contact[0].count(" ")
  # print(s_occur)
  if s_occur == 2:
    contact[0], contact[1], contact[2] = contact[0].split()
  elif s_occur == 1:
    contact[0], contact[1] = contact[0].split()
  return


def format_all_in_first_name(contact):
  s_occur = contact[1].count(" ")
  # print(s_occur)
  if s_occur == 1:
    contact[1], contact[2] = contact[1].split()
  return


def format_ph(ph):

  def print_ph(ph):
    return f'+7({ph[:3]}){ph[3:6]}-{ph[6:8]}-{ph[8:10]}'

  if len(ph) < 10:
    return
  ph = re.sub(r'[^0-9]', '', ph)[1:]
  if len(ph) > 10:
    additional = ph[10:]
    ph = ph[:10]
    return f'{print_ph(ph)} доб. {additional}'
  elif len(ph) == 10:
    return print_ph(ph)


def merge(contact_list, contact, n):
  list_len = len(contact)
  for i in range(3, list_len):
    if contact[i]: contact_list[n][i] = contact[i]


def delete_contact(contacts_list, n):
  del contacts_list[n]


fio_list = []
contacts_to_delete = []

for contact in contacts_list:
  if not contact[1]:
    format_all_in_last_name(contact)
  elif not contact[2]:
    format_all_in_first_name(contact)
  if contact[5]:
    contact[5] = format_ph(contact[5])
  fio = ' '.join(contact[:3])
  fi = ' '.join(contact[:2])
  for n, fio2 in enumerate(fio_list):
    if fi in fio2:

      merge(contacts_list, contact, n)
      contacts_to_delete.append(len(fio_list))
      fio_list.append('')
      break
  else:
    fio_list.append(fio)

for n in sorted(contacts_to_delete, reverse=True):
  # print(n)
  delete_contact(contacts_list, n)


with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(contacts_list)