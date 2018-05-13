from db import DatabaseController as dbc
import config
import unittest

dbc.DB_FILE_PATH = config.TEST_DB_FILE_PATH


class SpecializationTest(unittest.TestCase):

    def test_save_new_specialization(self):
        with open(dbc.DB_FILE_PATH, "r+") as f:
            f.truncate()

        to_save = dbc.Specialization()
        to_save.capacity = 92
        to_save.name = "new specialization"
        to_save.identifier = 1

        result = dbc.save_specialization(to_save)
        saved = dbc.get_specialization_by_id(1)

        self.assertEqual(to_save.to_xml(), saved.to_xml())
        self.assertEqual('OK', result)

    def test_save_duplicate_specialization(self):
        with open(dbc.DB_FILE_PATH, "r+") as f:
            f.truncate()

        to_save = dbc.Specialization()
        to_save.capacity = 92
        to_save.name = "new specialization"
        to_save.identifier = 1

        dbc.save_specialization(to_save)

        result = dbc.save_specialization(to_save)
        saved = dbc.get_all_specializations()

        self.assertEqual(1, len(saved))
        self.assertEqual('ALREADY_EXISTING', result)

    def test_get_specialization_by_id(self):
        with open(dbc.DB_FILE_PATH, "r+") as f:
            f.truncate()

        to_save1 = dbc.Specialization()
        to_save1.capacity = 11
        to_save1.name = "new specialization 1"
        to_save1.identifier = 1

        to_save2 = dbc.Specialization()
        to_save2.capacity = 22
        to_save2.name = "new specialization 2"
        to_save2.identifier = 2

        dbc.save_specialization(to_save1)
        dbc.save_specialization(to_save2)

        found = dbc.get_specialization_by_id(2)

        self.assertEqual(to_save2.to_xml(), found.to_xml())

    def test_get_all_specializations(self):
        with open(dbc.DB_FILE_PATH, "r+") as f:
            f.truncate()

        to_save1 = dbc.Specialization()
        to_save1.capacity = 11
        to_save1.name = "new specialization 1"
        to_save1.identifier = 1

        to_save2 = dbc.Specialization()
        to_save2.capacity = 22
        to_save2.name = "new specialization 2"
        to_save2.identifier = 2

        dbc.save_specialization(to_save1)
        dbc.save_specialization(to_save2)

        found = dbc.get_all_specializations()

        self.assertEqual(2, len(found))

    def test_delete_specialization_by_id(self):
        with open(dbc.DB_FILE_PATH, "r+") as f:
            f.truncate()

        to_save1 = dbc.Specialization()
        to_save1.capacity = 11
        to_save1.name = "new specialization 1"
        to_save1.identifier = 1

        to_save2 = dbc.Specialization()
        to_save2.capacity = 22
        to_save2.name = "new specialization 2"
        to_save2.identifier = 2

        dbc.save_specialization(to_save1)
        dbc.save_specialization(to_save2)

        dbc.delete_specialization_by_id(2)

        found1 = dbc.get_specialization_by_id(1)
        found2 = dbc.get_specialization_by_id(2)

        self.assertEqual(to_save1.to_xml(), found1.to_xml())
        self.assertEqual(None, found2)

    def test_update_specialization_found(self):
        with open(dbc.DB_FILE_PATH, "r+") as f:
            f.truncate()

        original = dbc.Specialization()
        original.capacity = 11
        original.name = "new specialization 1"
        original.identifier = 1

        dbc.save_specialization(original)

        updated = dbc.Specialization()
        updated.capacity = 21
        updated.name = "updated specialization 1"
        updated.identifier = 1

        result = dbc.update_specialization(updated)

        found = dbc.get_specialization_by_id(1)

        self.assertEqual(updated.to_xml(), found.to_xml())
        self.assertEqual('OK', result)

    def test_update_specialization_not_found(self):
        with open(dbc.DB_FILE_PATH, "r+") as f:
            f.truncate()

        original = dbc.Specialization()
        original.capacity = 11
        original.name = "new specialization 1"
        original.identifier = 1

        dbc.save_specialization(original)

        updated = dbc.Specialization()
        updated.capacity = 21
        updated.name = "updated specialization 1"
        updated.identifier = 2

        result = dbc.update_specialization(updated)

        found = dbc.get_specialization_by_id(1)

        self.assertEqual(original.to_xml(), found.to_xml())
        self.assertEqual('Entry not found', result)


    def test_save_specialization_no_name(self):
        with open(dbc.DB_FILE_PATH, "r+") as f:
            f.truncate()

        to_save = dbc.Specialization()
        to_save.capacity = 92
        to_save.identifier = 1

        result = dbc.save_specialization(to_save)
        found = dbc.get_specialization_by_id(1)

        self.assertEqual('OK', result)
        self.assertEqual(to_save.to_xml(), found.to_xml())
        found.print()

    def test_save_specialization_no_capacity(self):
        with open(dbc.DB_FILE_PATH, "r+") as f:
            f.truncate()

        to_save = dbc.Specialization()
        to_save.identifier = 1
        to_save.name = 'No capacity'

        result = dbc.save_specialization(to_save)
        found = dbc.get_specialization_by_id(1)

        self.assertEqual('OK', result)
        self.assertEqual(to_save.to_xml(), found.to_xml())
        found.print()

    def test_save_specialization_no_id(self):
        with open(dbc.DB_FILE_PATH, "r+") as f:
            f.truncate()

        to_save = dbc.Specialization()
        to_save.name = 'No id'
        to_save.capacity = 92

        result = dbc.save_specialization(to_save)
        found = dbc.get_specialization_by_id(-1)

        self.assertEqual('OK', result)
        self.assertEqual(to_save.to_xml(), found.to_xml())
        found.print()

    def test_save_specialization_incorrect_data(self):
        with open(dbc.DB_FILE_PATH, "r+") as f:
            f.truncate()

        to_save = dbc.Specialization()
        to_save.identifier = 1
        to_save.name = 4567
        to_save.capacity = 'Incorrect capacity'

        result = dbc.save_specialization(to_save)
        found = dbc.get_specialization_by_id(1)

        self.assertEqual('OK', result)
        self.assertEqual(to_save.to_xml(), found.to_xml())
        found.print()


class CandidateTest(unittest.TestCase):

    def test_save_new_candidate(self):
        with open(dbc.DB_FILE_PATH, "r+") as f:
            f.truncate()

        to_save = dbc.Candidate()
        to_save.cnp = 987654321
        to_save.first_name = "new student in town"
        to_save.surname = " mhm "
        to_save.email = "new@email.com"
        to_save.info_grade = 6.7
        to_save.math_grade = 8.9
        to_save.high_school_avg_grade = 9.5
        to_save.admission_grade = 7.8
        to_save.first_option = 2
        to_save.second_option = 1

        result = dbc.save_candidate(to_save)
        saved = dbc.get_candidate_by_id(987654321)

        self.assertEqual(to_save.to_xml(), saved.to_xml())
        self.assertEqual('OK', result)

    def test_save_duplicate_candidate(self):
        with open(dbc.DB_FILE_PATH, "r+") as f:
            f.truncate()

        to_save = dbc.Candidate()
        to_save.cnp = 987654321
        to_save.first_name = "new student in town"
        to_save.surname = " mhm "
        to_save.email = "new@email.com"
        to_save.info_grade = 6.7
        to_save.math_grade = 8.9
        to_save.high_school_avg_grade = 9.5
        to_save.admission_grade = 7.8
        to_save.first_option = 2
        to_save.second_option = 1

        dbc.save_candidate(to_save)

        result = dbc.save_candidate(to_save)
        saved = dbc.get_all_candidates()

        self.assertEqual(1, len(saved))
        self.assertEqual('ALREADY_EXISTING', result)

    def test_get_candidate_by_id(self):
        with open(dbc.DB_FILE_PATH, "r+") as f:
            f.truncate()

        to_save1 = dbc.Candidate()
        to_save1.cnp = 123456789
        to_save1.first_name = "student1 in town"
        to_save1.surname = " name1 "
        to_save1.email = "new1@email.com"
        to_save1.info_grade = 6.7
        to_save1.math_grade = 8.9
        to_save1.high_school_avg_grade = 9.5
        to_save1.admission_grade = 7.8
        to_save1.first_option = 2
        to_save1.second_option = 1

        to_save2 = dbc.Candidate()
        to_save2.cnp = 987654321
        to_save2.first_name = " student2 in town"
        to_save2.surname = " name2"
        to_save2.email = "student2@email.com"
        to_save2.info_grade = 6.7
        to_save2.math_grade = 8.9
        to_save2.high_school_avg_grade = 9.5
        to_save2.admission_grade = 7.8
        to_save2.first_option = 2
        to_save2.second_option = 1

        dbc.save_candidate(to_save1)
        dbc.save_candidate(to_save2)

        found = dbc.get_candidate_by_id(123456789)

        self.assertEqual(to_save1.to_xml(), found.to_xml())

    def test_get_all_candidates(self):
        with open(dbc.DB_FILE_PATH, "r+") as f:
            f.truncate()

        sp1 = dbc.Specialization()
        sp1.capacity = 92
        sp1.name = "specialization 1"
        sp1.identifier = 1

        sp2 = dbc.Specialization()
        sp2.capacity = 92
        sp2.name = "specialization 2"
        sp2.identifier = 2

        dbc.save_specialization(sp1)
        dbc.save_specialization(sp2)

        to_save1 = dbc.Candidate()
        to_save1.cnp = 123456789
        to_save1.first_name = "student1 in town"
        to_save1.surname = " name1 "
        to_save1.email = "new1@email.com"
        to_save1.info_grade = 6.7
        to_save1.math_grade = 8.9
        to_save1.high_school_avg_grade = 9.5
        to_save1.admission_grade = 7.8
        to_save1.first_option = 2
        to_save1.second_option = 1

        to_save2 = dbc.Candidate()
        to_save2.cnp = 987654321
        to_save2.first_name = " student2 in town"
        to_save2.surname = " name2"
        to_save2.email = "student2@email.com"
        to_save2.info_grade = 6.7
        to_save2.math_grade = 8.9
        to_save2.high_school_avg_grade = 9.5
        to_save2.admission_grade = 7.8
        to_save2.first_option = 2
        to_save2.second_option = 1

        dbc.save_candidate(to_save1)
        dbc.save_candidate(to_save2)

        found = dbc.get_all_candidates()
        self.assertEqual(2, len(found))

        found = dbc.get_all_candidates(1)
        self.assertEqual(2, len(found))

    def test_delete_candidate_by_id(self):
        with open(dbc.DB_FILE_PATH, "r+") as f:
            f.truncate()

        to_save1 = dbc.Candidate()
        to_save1.cnp = 123456789
        to_save1.first_name = "student1 in town"
        to_save1.surname = " name1 "
        to_save1.email = "new1@email.com"
        to_save1.info_grade = 6.7
        to_save1.math_grade = 8.9
        to_save1.high_school_avg_grade = 9.5
        to_save1.admission_grade = 7.8
        to_save1.first_option = 2
        to_save1.second_option = 1

        to_save2 = dbc.Candidate()
        to_save2.cnp = 987654321
        to_save2.first_name = " student2 in town"
        to_save2.surname = " name2"
        to_save2.email = "student2@email.com"
        to_save2.info_grade = 6.7
        to_save2.math_grade = 8.9
        to_save2.high_school_avg_grade = 9.5
        to_save2.admission_grade = 7.8
        to_save2.first_option = 2
        to_save2.second_option = 1

        dbc.save_candidate(to_save1)
        dbc.save_candidate(to_save2)

        dbc.delete_candidate_by_id(123456789)

        found1 = dbc.get_candidate_by_id(123456789)
        found2 = dbc.get_candidate_by_id(987654321)

        self.assertEqual(to_save2.to_xml(), found2.to_xml())
        self.assertEqual(None, found1)

    def test_update_candidate_found(self):
        with open(dbc.DB_FILE_PATH, "r+") as f:
            f.truncate()

        original = dbc.Candidate()
        original.cnp = 123456789
        original.first_name = "student1 in town"
        original.surname = " name1 "
        original.email = "new1@email.com"
        original.info_grade = 6.7
        original.math_grade = 8.9
        original.high_school_avg_grade = 9.5
        original.admission_grade = 7.8
        original.first_option = 2
        original.second_option = 1

        dbc.save_candidate(original)

        updated = dbc.Candidate()
        updated.cnp = 123456789
        updated.first_name = "this is my name"
        updated.surname = " my surname "
        updated.email = " i got a new mail"
        updated.info_grade = 6.7
        updated.math_grade = 8.9
        updated.high_school_avg_grade = 9.5
        updated.admission_grade = 7.8
        updated.first_option = 2
        updated.second_option = 1

        result = dbc.update_candidate(updated)

        found = dbc.get_candidate_by_id(123456789)

        self.assertEqual(updated.to_xml(), found.to_xml())
        self.assertEqual('OK', result)

    def test_update_specialization_not_found(self):
        with open(dbc.DB_FILE_PATH, "r+") as f:
            f.truncate()

        original = dbc.Candidate()
        original.cnp = 123456789
        original.first_name = "student1 in town"
        original.surname = " name1 "
        original.email = "new1@email.com"
        original.info_grade = 6.7
        original.math_grade = 8.9
        original.high_school_avg_grade = 9.5
        original.admission_grade = 7.8
        original.first_option = 2
        original.second_option = 1

        dbc.save_candidate(original)

        updated = dbc.Candidate()
        updated.cnp = 987654321
        updated.first_name = "this is my name"
        updated.surname = " my surname "
        updated.email = " i got a new mail"
        updated.info_grade = 6.7
        updated.math_grade = 8.9
        updated.high_school_avg_grade = 9.5
        updated.admission_grade = 7.8
        updated.first_option = 2
        updated.second_option = 1

        result = dbc.update_candidate(updated)

        found = dbc.get_candidate_by_id(123456789)

        self.assertEqual(original.to_xml(), found.to_xml())
        self.assertEqual('Entry not found', result)


    def test_save_candidate_misiing_data(self):
        with open(dbc.DB_FILE_PATH, "r+") as f:
            f.truncate()

        to_save = dbc.Candidate()

        result = dbc.save_candidate(to_save)
        found = dbc.get_candidate_by_id(0)

        self.assertEqual('OK', result)
        self.assertEqual(to_save.to_xml(), found.to_xml())
        found.print()

    def test_save_candidate_incorrect_data(self):
        with open(dbc.DB_FILE_PATH, "r+") as f:
            f.truncate()

        to_save = dbc.Candidate()
        to_save.surname = 1234

        result = dbc.save_candidate(to_save)

        self.assertEqual('OK', result)


class AdmissionResultTest(unittest.TestCase):

    def test_save_new_admission(self):
        with open(dbc.DB_FILE_PATH, "r+") as f:
            f.truncate()

        to_save = dbc.AdmissionResult()
        to_save.candidate_cnp = 987654321
        to_save.allocation = dbc.AdmissionStatus.FEE
        to_save.specialization_id = 0
        to_save.final_score = 8.6

        to_save.print()

        result = dbc.save_admission_result_for_candidate(to_save)
        saved = dbc.get_admission_result_for_candidate(987654321)

        self.assertEqual(to_save.to_xml(), saved.to_xml())
        self.assertEqual('OK', result)

    def test_save_duplicate_admission(self):
        with open(dbc.DB_FILE_PATH, "r+") as f:
            f.truncate()

        to_save = dbc.AdmissionResult()
        to_save.candidate_cnp = 987654321
        to_save.allocation = dbc.AdmissionStatus.FEE
        to_save.specialization_id = 0
        to_save.final_score = 8.6

        dbc.save_admission_result_for_candidate(to_save)

        result = dbc.save_admission_result_for_candidate(to_save)
        saved = dbc.get_admission_results()

        self.assertEqual(1, len(saved))
        self.assertEqual('OK', result)

    def test_get_admission_result_for_candidate(self):
        with open(dbc.DB_FILE_PATH, "r+") as f:
            f.truncate()

        to_save1 = dbc.AdmissionResult()
        to_save1.candidate_cnp = 987654321
        to_save1.allocation = dbc.AdmissionStatus.FEE
        to_save1.specialization_id = 0
        to_save1.final_score = 8.6

        to_save2 = dbc.AdmissionResult()
        to_save2.candidate_cnp = 1234567
        to_save2.allocation = dbc.AdmissionStatus.FREE
        to_save2.specialization_id = 0
        to_save2.final_score = 9.0

        dbc.save_admission_result_for_candidate(to_save1)
        dbc.save_admission_result_for_candidate(to_save2)

        found = dbc.get_admission_result_for_candidate(1234567)

        self.assertEqual(to_save2.to_xml(), found.to_xml())

    def test_get_all_results(self):
        with open(dbc.DB_FILE_PATH, "r+") as f:
            f.truncate()

        to_save = dbc.Specialization()
        to_save.capacity = 92
        to_save.name = "new specialization"
        to_save.identifier = 0

        result = dbc.save_specialization(to_save)

        to_save1 = dbc.AdmissionResult()
        to_save1.candidate_cnp = 987654321
        to_save1.allocation = dbc.AdmissionStatus.FEE
        to_save1.specialization_id = 0
        to_save1.final_score = 8.6

        to_save2 = dbc.AdmissionResult()
        to_save2.candidate_cnp = 1234567
        to_save2.allocation = dbc.AdmissionStatus.FREE
        to_save2.specialization_id = 0
        to_save2.final_score = 9.0

        dbc.save_admission_result_for_candidate(to_save1)
        dbc.save_admission_result_for_candidate(to_save2)

        found = dbc.get_admission_results()

        self.assertEqual(2, len(found))

        found = dbc.get_admission_results(1)

        self.assertEqual(2, len(found))

    def test_delete_admission_by_id(self):
        with open(dbc.DB_FILE_PATH, "r+") as f:
            f.truncate()

        to_save1 = dbc.AdmissionResult()
        to_save1.candidate_cnp = 987654321
        to_save1.allocation = dbc.AdmissionStatus.FEE
        to_save1.specialization_id = 0
        to_save1.final_score = 8.6

        to_save2 = dbc.AdmissionResult()
        to_save2.candidate_cnp = 1234567
        to_save2.allocation = dbc.AdmissionStatus.FREE
        to_save2.specialization_id = 0
        to_save2.final_score = 9.0

        dbc.save_admission_result_for_candidate(to_save1)
        dbc.save_admission_result_for_candidate(to_save2)

        dbc.delete_admission_result_for_candidate(987654321)

        found1 = dbc.get_admission_result_for_candidate(987654321)
        found2 = dbc.get_admission_result_for_candidate(1234567)

        self.assertEqual(to_save2.to_xml(), found2.to_xml())
        self.assertEqual(None, found1)

    def test_update_specialization_found(self):
        with open(dbc.DB_FILE_PATH, "r+") as f:
            f.truncate()

        original = dbc.AdmissionResult()
        original.candidate_cnp = 987654321
        original.allocation = dbc.AdmissionStatus.FEE
        original.specialization_id = 0
        original.final_score = 8.6

        dbc.save_admission_result_for_candidate(original)

        updated = dbc.AdmissionResult()
        updated.candidate_cnp = 987654321
        updated.allocation = dbc.AdmissionStatus.UNPROCESSED
        updated.specialization_id = 0
        updated.final_score = 0.0

        result = dbc.update_admission_result_for_candidate(updated)

        found = dbc.get_admission_result_for_candidate(987654321)

        self.assertEqual(updated.to_xml(), found.to_xml())
        self.assertEqual('OK', result)

    def test_update_specialization_not_found(self):
        with open(dbc.DB_FILE_PATH, "r+") as f:
            f.truncate()

        original = dbc.AdmissionResult()
        original.candidate_cnp = 987654321
        original.allocation = dbc.AdmissionStatus.FEE
        original.specialization_id = 0
        original.final_score = 8.6

        dbc.save_admission_result_for_candidate(original)

        updated = dbc.AdmissionResult()
        updated.candidate_cnp = 12345
        updated.allocation = dbc.AdmissionStatus.UNPROCESSED
        updated.specialization_id = 0
        updated.final_score = 0.0

        result = dbc.update_admission_result_for_candidate(updated)

        found = dbc.get_admission_result_for_candidate(987654321)

        self.assertEqual(original.to_xml(), found.to_xml())
        self.assertEqual('Entry not found', result)

    def test_save_admission_no_data(self):
        with open(dbc.DB_FILE_PATH, "r+") as f:
            f.truncate()

        to_save = dbc.AdmissionResult()

        result = dbc.save_admission_result_for_candidate(to_save)
        found = dbc.get_admission_result_for_candidate(0)

        self.assertEqual('OK', result)
        self.assertEqual(to_save.to_xml(), found.to_xml())
        found.print()

    def test_save_admission_incorrect_data(self):
        with open(dbc.DB_FILE_PATH, "r+") as f:
            f.truncate()

        to_save = dbc.AdmissionResult()
        to_save.allocation = 'allocation'

        result = dbc.save_admission_result_for_candidate(to_save)
        found = dbc.get_admission_result_for_candidate(0)

        self.assertEqual('OK', result)
        self.assertEqual(to_save.to_xml(), found.to_xml())
        found.print()


if __name__ == '__main__':
    unittest.main()
