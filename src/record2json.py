import sys
import json


def record_to_dic(line):
    year = line[1:5]
    month = line[5:7]
    day = line[7:9]
    hour = line[9:11]
    minute = line[11:13]
    second = line[13:17]
    magnitude = line[52:54]
    max_seisemic_intensity = line[61]
    epicenter_name = line[68:92]

    dictionary = {}
    dictionary["magnitude"] = magnitude
    dictionary["max_seisemic_intensity"] = max_seisemic_intensity
    dictionary["epicenter_name"] = epicenter_name

    time = {}
    time["year"] = year
    time["month"] = month
    time["day"] = day
    time["hour"] = hour
    time["minute"] = minute
    time["second"] = second
    dictionary["time"] = time

    return dictionary


if __name__ == '__main__':
    json_dic = {}
    json_dic["data"] = []
    path = sys.argv[1]
    with open(path) as f:
        l_strip = [s.strip() for s in f.readlines()]
        for line in l_strip:
            if line[61] == ' ':
                continue
            json_dic["data"].append(record_to_dic(line))

    with open('./data/quake_list.json', 'w') as fjson:
        json.dump(json_dic, fjson, ensure_ascii=False,
                  indent=4, separators=(',', ': '))
