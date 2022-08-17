import json
import os
from matplotlib import pyplot as plt


class File:
    def __init__(self, year, month, day, messages):
        self.year = year
        self.month = month
        self.day = day
        self.messages = messages
        self.date = year + "-" + month + "-" + day

    def __repr__(self):
        return self.date + " " + str(self.messages)


files = []

files2022_draft = []

year_2022 = []
messages_2022 = []

folder_path = "/Users/jackie.moonshot/Desktop/anticonti/Conti Jabber Chat Logs 2021 - 2022"
for filename in os.listdir(folder_path):
    with open(os.path.join(folder_path, filename), 'r') as f:
        content = f.read()
    parsed_values = []
    decoder = json.JSONDecoder()
    counter = 0
    while content:
        value, new_start = decoder.raw_decode(content)
        content = content[new_start:].strip()
        counter += 1
        parsed_values.append(value)
    date = filename[14:22]
    file_info = File(date[:4], date[4:6], date[-2:], len(parsed_values))
    files.append(file_info)
    # print(date, len(parsed_values))

files.sort(key=lambda r: r.date)

for file in files:
    if file.year == "2022":
        messages_2022.append(file.messages)
        year_2022.append(file.month + "." + file.day)

plt.bar(year_2022, messages_2022)
plt.title('FREQUENCY 2022')
plt.xlabel('dates', fontsize=15)
plt.ylabel('number of messages', fontsize=15)
plt.show()

for file in files:
    print(repr(file))
