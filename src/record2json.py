import sys
import json


def record_to_dic(line: str):
    year = line[1:5]
    month = line[5:7]
    day = line[7:9]
    hour = line[9:11]
    minute = line[11:13]
    second = line[13:17]
    time_standard_error_sec = line[17:21]

    latitude_degree = line[21:24]
    latitude_minute = line[24:28]
    latitude_standard_error_minute = line[28:32]

    longitude_degree = line[32:36]
    longitude_minute = line[36:40]
    longitude_standard_error_minute = line[40:44]

    depth_km = line[44:49]
    depth_standard_error = line[49:52]

    magnitude_1 = line[52:54]
    magnitude_1_type = line[54]
    magnitude_2 = line[55:57]
    magnitude_2_type = line[57]

    travel_time_table = line[58]
    epicenter_eval = line[59]
    epicenter_auxiliary_info = line[60]
    max_seisemic_intensity = line[61]
    damage_scale = line[62]
    tsunami_scale = line[63]
    large_area_class_num = line[64]
    small_area_class_num = line[65:68]
    epicenter_name = line[68:92]
    observ_point_num = line[92:95]
    focus_decision_flag = line[95]

    dic = {}

    time = {}
    time["year"] = year
    time["month"] = month
    time["day"] = day
    time["hour"] = hour
    time["minute"] = minute
    time["second"] = second
    time["time_standard_error_sec"] = time_standard_error_sec
    dic["time"] = time

    latitude = {}
    latitude["latitude_degree"] = latitude_degree
    latitude["latitude_minute"] = latitude_minute
    latitude["latitude_standard_error_minute"] = latitude_standard_error_minute
    dic["latitude"] = latitude

    longitude = {}
    longitude["longitude_degree"] = longitude_degree
    longitude["longitude_minute"] = longitude_minute
    longitude["longitude_standard_error_minute"] = longitude_standard_error_minute
    dic["longitude"] = longitude

    depth = {}
    depth["depth"] = depth_km
    depth["depth_standard_error"] = depth_standard_error
    dic["depth"] = depth

    magnitude = {}
    magnitude["magnitude_1"] = magnitude_1
    magnitude["magnitude_1_type"] = magnitude_1_type
    magnitude["magnitude_2"] = magnitude_2
    magnitude["magnitude_2_type"] = magnitude_2_type
    dic["magnitude"] = magnitude

    dic["travel_time_table"] = travel_time_table
    dic["epicenter_eval"] = epicenter_eval
    dic["epicenter_auxiliary_info"] = epicenter_auxiliary_info
    dic["max_seisemic_intensity"] = max_seisemic_intensity
    dic["damage_scale"] = damage_scale
    dic["tsunami_scale"] = tsunami_scale
    dic["large_area_class_num"] = large_area_class_num
    dic["small_area_class_num"] = small_area_class_num
    dic["epicenter_name"] = epicenter_name
    dic["observ_point_num"] = observ_point_num
    dic["focus_decision_flag"] = focus_decision_flag

    return dic


if __name__ == '__main__':
    if(len(sys.argv) <= 2):
        print("引数を指定してください")
        print("ex: $ python src/record2json.py src dest.json")
        sys.exit()
    json_dic = {}
    json_dic["data"] = []
    path = sys.argv[1]
    with open(path) as f:
        l_strip = [s.replace('\n', '') for s in f.readlines()]
        for line in l_strip:
            # if line[61] == ' ':
            #    continue
            json_dic["data"].append(record_to_dic(line))

    with open('./data/' + sys.argv[2], 'w') as fjson:
        json.dump(json_dic, fjson, ensure_ascii=False,
                  indent=4, separators=(',', ': '))
