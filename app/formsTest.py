import unittest
import app.utils
import db.DatabaseController
import app.forms
import flask
from unittest.mock import MagicMock

class TestUtils(unittest.TestCase):

    def test_not_null_get_results(self):
        results = app.utils.get_results()
        self.assertIsNotNone(results)

    def test_get_results(self):
        results = app.utils.get_results()
        self.assertTrue(len(results) > 0)
        
    def test_not_null_admision_status (self):
        candidate = db.DatabaseController.Candidate()
        candidate.cnp = 555555555
        candidate.first_name = 'John'
        candidate.surname = 'Johnson'
        candidate.email = ' '
        candidate.info_grade = 5.0  # set to 0 if value is not known
        candidate.math_grade = 5.0
        candidate.high_school_avg_grade = 5.0
        candidate.admission_grade = 3.0
        candidate.first_option = 3
        candidate.second_option = 4
        candidate.candidate_cnp = candidate.cnp
        candidate.final_score = 4
        candidate.specialization_id = 3
        candidate.allocation = ""

        specializations = db.DatabaseController.get_all_specializations()
        specs = {}
        opt_arr = {}

        for item in specializations:
            specs[item.identifier] = {}
            specs[item.identifier]["name"] = item.name 
            specs[item.identifier]["capacity"] = item.capacity 
            specs[item.identifier]["free_spots"] = item.capacity
        
        opt_arr[str(candidate.cnp)] = {}
        opt_arr[str(candidate.cnp)]["first_option"] = candidate.first_option
        opt_arr[str(candidate.cnp)]["second_option"] = candidate.second_option

        st = app.utils.set_admision_status (candidate,specs,opt_arr)

        self.assertIsNotNone(st)

    def test_admision_status (self):
        candidate = db.DatabaseController.Candidate()
        candidate.cnp = 555555555
        candidate.first_name = 'John'
        candidate.surname = 'Johnson'
        candidate.email = ' '
        candidate.info_grade = 5.0  # set to 0 if value is not known
        candidate.math_grade = 5.0
        candidate.high_school_avg_grade = 5.0
        candidate.admission_grade = 3.0
        candidate.first_option = 3
        candidate.second_option = 4
        candidate.candidate_cnp = candidate.cnp
        candidate.final_score = 4
        candidate.specialization_id = 3
        candidate.allocation = ""

        specializations = db.DatabaseController.get_all_specializations()
        specs = {}
        opt_arr = {}

        for item in specializations:
            specs[item.identifier] = {}
            specs[item.identifier]["name"] = item.name 
            specs[item.identifier]["capacity"] = item.capacity 
            specs[item.identifier]["free_spots"] = item.capacity
        
        opt_arr[str(candidate.cnp)] = {}
        opt_arr[str(candidate.cnp)]["first_option"] = candidate.first_option
        opt_arr[str(candidate.cnp)]["second_option"] = candidate.second_option

        st = app.utils.set_admision_status (candidate,specs,opt_arr)

        self.assertTrue(st == db.DatabaseController.AdmissionStatus.REJECTED)

    def test_not_null_calculate_scor(self):
        results = app.utils.calculate_results()
        for item in results:
            self.assertIsNotNone(item)

    def test_calculate_scor(self):
        results = app.utils.calculate_results()
        for item in results:
            self.assertTrue(0 <= item.final_score <= 10)

    def test_not_null_calculate_final_score_for_candidate(self):
        candidate = db.DatabaseController.Candidate ()
        candidate.info_grade = 10.0  # set to 0 if value is not known
        candidate.math_grade = 10.0
        candidate.high_school_avg_grade = 10.0
        candidate.admission_grade = 10.0
        final_sc = app.utils.calculate_final_score_for_candidate(candidate)
        self.assertIsNotNone(final_sc)

    def test_calculate_final_score_for_candidate_right_value(self):
        candidate = db.DatabaseController.Candidate ()
        candidate.info_grade = 10.0  # set to 0 if value is not known
        candidate.math_grade = 10.0
        candidate.high_school_avg_grade = 10.0
        candidate.admission_grade = 10.0
        final_sc = app.utils.calculate_final_score_for_candidate(candidate)
        self.assertTrue(final_sc == 10)
        
    def test_calculate_final_score_for_candidate_fine_interval(self):
        candidate = db.DatabaseController.Candidate ()
        candidate.info_grade = 10.0  # set to 0 if value is not known
        candidate.math_grade = 10.0
        candidate.high_school_avg_grade = 10.0
        candidate.admission_grade = 10.0
        final_sc = app.utils.calculate_final_score_for_candidate(candidate)
        self.assertTrue(0 <= final_sc <= 10)
        

if __name__ == '__main__':
    unittest.main()