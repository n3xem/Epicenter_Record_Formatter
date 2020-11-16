from datetime import date
import json
import sys
import datetime as dt


def dic2simple(dic):
    dic.pop('record_class_header')
    dic.pop('latitude')
    dic.pop('longitude')
    dic.pop('depth')
    dic.pop('magnitude')
    dic.pop('travel_time_table')
    dic.pop('epicenter_auxiliary_info')
    dic.pop('damage_scale')
    dic.pop('tsunami_scale')
    dic.pop('observ_point_num')
    dic.pop('focus_decision_flag')
    dic.pop('epicenter_eval')

    time_dic = dic["time"]
    year = int(time_dic["year"])
    month = int(time_dic["month"])
    day = int(time_dic["day"])
    hour = int(time_dic["hour"])
    minute = int(time_dic["minute"])
    second = int(time_dic["second"][0:2])

    date_time = dt.datetime(
        year, month, day, hour=hour, minute=minute, second=second)

    dic.pop('time')
    dic["time"] = str(date_time)


if __name__ == '__main__':
    if len(sys.argv) <= 2:
        print('引数を正しく入力してください')
        print('ex: $ python src/epicenter_json2simple.py src.json dest.json')
        sys.exit()
    with open(sys.argv[1]) as f:
        df = json.load(f)

    for dic in df["data"]:
        dic2simple(dic)

    with open('data/' + sys.argv[2], 'w') as f:
        json.dump(df, f, indent=4)
