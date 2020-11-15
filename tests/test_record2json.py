import unittest
from src.record2json import record_to_dic


class TestRecord2JsonMethods(unittest.TestCase):

    def test_record_to_dic(self):
        arg = 'J2019020100014045 008 362146 024 1370344 020  69914303v   511   4142TOYAMA GIFU BORDER REG   12A'
        correct_dic = {
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
        self.assertEqual(record_to_dic(arg), correct_dic)


if __name__ == '__main__':
    unittest.main()
