import unittest
from src.json2simple import dic2simple


class TestJson2SimpleMethods(unittest.TestCase):
    def test_dic2simple(self):
        src_dic = {
            "record_class_header": "J",
            "time": {
                "year": "2019",
                "month": "02",
                "day": "01",
                "hour": "00",
                "minute": "01",
                "second": "4045",
                "time_standard_error_sec": " 008"
            },
            "latitude": {
                "latitude_degree": " 36",
                "latitude_minute": "2146",
                "latitude_standard_error_minute": " 024"
            },
            "longitude": {
                "longitude_degree": " 137",
                "longitude_minute": "0344",
                "longitude_standard_error_minute": " 020"
            },
            "depth": {
                "depth_km": "  699",
                "depth_standard_error": "143"
            },
            "magnitude": {
                "magnitude_1": "03",
                "magnitude_1_type": "v",
                "magnitude_2": "  ",
                "magnitude_2_type": " "
            },
            "travel_time_table": "5",
            "epicenter_eval": "1",
            "epicenter_auxiliary_info": "1",
            "max_seisemic_intensity": " ",
            "damage_scale": " ",
            "tsunami_scale": " ",
            "large_area_class_num": "4",
            "small_area_class_num": "142",
            "epicenter_name": "TOYAMA GIFU BORDER REG  ",
            "observ_point_num": " 12",
            "focus_decision_flag": "A"
        }

        correct_dic = {
            "max_seisemic_intensity": " ",
            "large_area_class_num": "4",
            "small_area_class_num": "142",
            "epicenter_name": "TOYAMA GIFU BORDER REG  ",
            "time": "2019-02-01 00:01:40"
        }

        dic2simple(src_dic)

        self.assertEqual(src_dic, correct_dic)


if __name__ == '__main__':
    unittest.main()
