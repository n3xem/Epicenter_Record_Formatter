import sys
import json


def record_to_dic(line: str):
    # 震源レコードのフォーマットは https://www.data.jma.go.jp/svd/eqev/data/bulletin/data/format/hypfmt_j.html を参照

    record_class_header = line[0]  # レコード種別ヘッダ
    year = line[1:5]  # 西暦
    month = line[5:7]  # 月
    day = line[7:9]  # 日
    hour = line[9:11]  # 時
    minute = line[11:13]  # 分
    second = line[13:17]  # 秒
    time_standard_error_sec = line[17:21]  # 標準誤差(秒)

    latitude_degree = line[21:24]  # 緯度(度)
    latitude_minute = line[24:28]  # 緯度(分)
    latitude_standard_error_minute = line[28:32]  # 標準誤差(分)

    longitude_degree = line[32:36]  # 経度(度)
    longitude_minute = line[36:40]  # 経度(分)
    longitude_standard_error_minute = line[40:44]  # 標準誤差(分)

    depth_km = line[44:49]  # 深さ(km)
    depth_standard_error = line[49:52]  # 標準誤差(km)

    magnitude_1 = line[52:54]  # マグニチュード1
    magnitude_1_type = line[54]  # マグニチュード1種別
    magnitude_2 = line[55:57]  # マグニチュード2
    magnitude_2_type = line[57]  # マグニチュード2種別

    travel_time_table = line[58]  # 使用走時表
    epicenter_eval = line[59]  # 震源評価
    epicenter_auxiliary_info = line[60]  # 震源補助情報
    max_seisemic_intensity = line[61]  # 最大震度
    damage_scale = line[62]  # 被害規模
    tsunami_scale = line[63]  # 津波規模
    large_area_class_num = line[64]  # 大地域区分番号
    small_area_class_num = line[65:68]  # 小地域区分番号
    epicenter_name = line[68:92]  # 震央地名
    observ_point_num = line[92:95]  # 観測点数
    focus_decision_flag = line[95]  # 震源決定フラグ

    time = {
        "year": year,
        "month": month,
        "day": day,
        "hour": hour,
        "minute": minute,
        "second": second,
        "time_standard_error_sec": time_standard_error_sec
    }

    latitude = {
        "latitude_degree": latitude_degree,
        "latitude_minute": latitude_minute,
        "latitude_standard_error_minute": latitude_standard_error_minute
    }

    longitude = {
        "longitude_degree": longitude_degree,
        "longitude_minute": longitude_minute,
        "longitude_standard_error_minute": longitude_standard_error_minute
    }

    depth = {
        "depth_km": depth_km,
        "depth_standard_error": depth_standard_error
    }

    magnitude = {
        "magnitude_1": magnitude_1,
        "magnitude_1_type": magnitude_1_type,
        "magnitude_2": magnitude_2,
        "magnitude_2_type": magnitude_2_type
    }

    dic = {
        "record_class_header": record_class_header,
        "time": time,
        "latitude": latitude,
        "longitude": longitude,
        "depth": depth,
        "magnitude": magnitude,
        "travel_time_table": travel_time_table,
        "epicenter_eval": epicenter_eval,
        "epicenter_auxiliary_info": epicenter_auxiliary_info,
        "max_seisemic_intensity": max_seisemic_intensity,
        "damage_scale": damage_scale,
        "tsunami_scale": tsunami_scale,
        "large_area_class_num": large_area_class_num,
        "small_area_class_num": small_area_class_num,
        "epicenter_name": epicenter_name,
        "observ_point_num": observ_point_num,
        "focus_decision_flag": focus_decision_flag
    }

    return dic


if __name__ == '__main__':
    if(len(sys.argv) <= 2):
        print("引数を指定してください")
        print("ex: $ python src/record2json.py src dest.json")
        sys.exit()

    json_dic = {"data": []}
    record_path = sys.argv[1]
    save_filename = sys.argv[2]

    with open(record_path) as f:
        record_lines = [s.replace('\n', '') for s in f.readlines()]
        for line in record_lines:
            json_dic["data"].append(record_to_dic(line))

    with open('./data/' + save_filename, 'w') as f:
        json.dump(json_dic, f, ensure_ascii=False,
                  indent=4, separators=(',', ': '))
