from record2json import record_to_dic
from json2simple import dic2simple
import sys
import json


if __name__ == '__main__':
    if(len(sys.argv) <= 2):
        print("引数を指定してください")
        print("ex: $ python src/record2simplejson.py src dest.json")
        sys.exit()

    json_dic = {"data": []}
    record_path = sys.argv[1]
    save_filename = sys.argv[2]

    with open(record_path) as f:
        record_lines = [s.replace('\n', '') for s in f.readlines()]
        for line in record_lines:
            json_dic["data"].append(record_to_dic(line))

        for dic in json_dic["data"]:
            dic2simple(dic)

    with open('./data/' + save_filename, 'w') as f:
        json.dump(json_dic, f, ensure_ascii=False,
                  indent=4, separators=(',', ': '))
