from enum import Enum
import config

DB_FILE_PATH = config.DB_FILE_PATH


def build_begin_tag(tag_name):
    return "<" + tag_name + ">"


def build_end_tag(tag_name):
    return "</" + tag_name + ">"


def get_begin_tag(current_line):
    line = str.strip(current_line)
    elements = str.split(line, "<")
    elements = str.split(elements[1], ">")
    if elements[0].startswith("/"):
        return None
    else:
        return elements[0]


def get_tag_value(current_line):
    line = str.strip(current_line)
    elements = str.split(line, "<")
    elements = str.split(elements[1], ">")
    return elements[1]


# Specialization


class Specialization:
    identifier = -1
    name = ' '
    capacity = 0

    table_tag = "specialization"
    id_tag = "id"
    name_tag = "name"
    capacity_tag = "capacity"

    def print(self):
        print(
            repr(
                self.identifier) +
            ' - ' +
            self.name +
            ' - ' +
            repr(
                self.capacity))

    def to_xml(self):
        result = build_begin_tag(Specialization.table_tag) + "\n"
        result += "\t" + build_begin_tag(Specialization.id_tag) + repr(
            self.identifier) + build_end_tag(Specialization.id_tag) + "\n"
        result += "\t" + build_begin_tag(Specialization.name_tag) + \
            self.name + build_end_tag(Specialization.name_tag) + "\n"
        result += "\t" + build_begin_tag(Specialization.capacity_tag) + repr(
            self.capacity) + build_end_tag(Specialization.capacity_tag) + "\n"
        result += build_end_tag(Specialization.table_tag) + "\n"
        return result


def get_all_specializations():
    with open(DB_FILE_PATH, "r+") as f:
        new_f = f.readlines()
        result = []
        for line in new_f:
            tag = get_begin_tag(line)
            if tag == Specialization.table_tag:
                found = Specialization()
            if tag == Specialization.id_tag:
                value = get_tag_value(line)
                found.identifier = int(value)
            if tag == Specialization.name_tag:
                value = get_tag_value(line)
                found.name = value
            if tag == Specialization.capacity_tag:
                value = get_tag_value(line)
                found.capacity = int(value)
                result.append(found)
        return result


#print("get all specializations")
#all_specializations = get_all_specializations()
#for x in all_specializations:
#    x.print()


def get_specialization_by_id(id):
    with open(DB_FILE_PATH, "r+") as f:
        new_f = f.readlines()
        for line in new_f:
            tag = get_begin_tag(line)
            if tag == Specialization.table_tag:
                found = Specialization()
            if tag == Specialization.id_tag:
                value = get_tag_value(line)
                found.identifier = int(value)
            if tag == Specialization.name_tag:
                value = get_tag_value(line)
                found.name = value
            if tag == Specialization.capacity_tag:
                value = get_tag_value(line)
                found.capacity = int(value)
                if found.identifier == id:
                    return found
        return None


#print("\nget spec by id")
#found_by_id = get_specialization_by_id(6)
#found_by_id.print()
#print(found_by_id.to_xml())


def delete_specialization_by_id(categ_id):
    with open(DB_FILE_PATH, "r+") as f:
        new_f = f.readlines()
        f.seek(0)
        count = 0
        while count < (len(new_f)):
            line = new_f[count]
            tag = get_begin_tag(line)
            if tag == Specialization.table_tag:
                new_line = new_f[count + 1]
                id_line = get_tag_value(new_line)
                if int(id_line) == categ_id:
                    count += 5
                    continue
            f.write(new_f[count])
            count += 1
        f.truncate()


#print("\ndelete specialization by id")
#delete_specialization_by_id(5)


def save_specialization(category):
    existing = get_specialization_by_id(category.identifier)
    if existing is None:
        with open(DB_FILE_PATH, "a") as f:
            f.write(category.to_xml())
        return 'OK'
    else:
        return 'ALREADY_EXISTING'


#print("\nsave new specialization")
#toSave = Specialization()
#toSave.capacity = 92
#toSave.name = "new specialization"
#toSave.identifier = 8

#save_specialization(toSave)


def update_specialization(category):
    existing = get_specialization_by_id(category.identifier)
    if existing is None:
        return "Entry not found"
    else:
        delete_specialization_by_id(category.identifier)
        save_specialization(category)
        return "OK"


#print("\nupdate specialization")
#toUpdate = Specialization()
#toUpdate.capacity = 1000
#toUpdate.name = "new specialization name"
#toUpdate.identifier = 8
#update_specialization(toUpdate)


# student


class Candidate:
    cnp = 0
    first_name = ' '
    surname = ' '
    email = ' '
    info_grade = 0.0  # set to 0 if value is not known
    math_grade = 0.0
    high_school_avg_grade = 0.0
    admission_grade = 0.0
    first_option = 0
    second_option = 0

    table_tag = "candidate"
    cnp_tag = "cnp"
    first_name_tag = "first_name"
    surname_tag = "surname"
    email_tag = "email"
    info_grade_tag = "info_grade"
    math_grade_tag = "math_grade"
    high_school_avg_grade_tag = "high_school_avg_grade"
    admission_grade_tag = "admission_grade"
    first_option_tag = "first_option"
    second_option_tag = "second_option"

    def print(self):
        print(
            repr(
                self.cnp) +
            ' - ' +
            self.first_name +
            ' - ' +
            self.surname +
            ' - ' +
            self.email +
            ' - ' +
            repr(
                self.info_grade) +
            ' - ' +
            repr(
                self.math_grade) +
            ' - ' +
            repr(
                self.high_school_avg_grade) +
            ' - ' +
            repr(
                self.admission_grade) +
            ' - ' +
            repr(
                self.first_option) +
            ' - ' +
            repr(
                self.second_option))

    def to_xml(self):
        result = build_begin_tag(Candidate.table_tag) + "\n"
        result += "\t" + build_begin_tag(Candidate.cnp_tag) + repr(
            self.cnp) + build_end_tag(Candidate.cnp_tag) + "\n"
        result += "\t" + build_begin_tag(Candidate.first_name_tag) + \
            self.first_name + build_end_tag(Candidate.first_name_tag) + "\n"
        result += "\t" + build_begin_tag(Candidate.surname_tag) + \
            self.surname + build_end_tag(Candidate.surname_tag) + "\n"
        result += "\t" + build_begin_tag(Candidate.email_tag) + \
            self.email + build_end_tag(Candidate.email_tag) + "\n"
        result += "\t" + build_begin_tag(Candidate.info_grade_tag) + repr(
            self.info_grade) + build_end_tag(Candidate.info_grade_tag) + "\n"
        result += "\t" + build_begin_tag(Candidate.math_grade_tag) + repr(
            self.math_grade) + build_end_tag(Candidate.math_grade_tag) + "\n"
        result += "\t" + build_begin_tag(Candidate.high_school_avg_grade_tag) + repr(
            self.high_school_avg_grade) + build_end_tag(Candidate.high_school_avg_grade_tag) + "\n"
        result += "\t" + build_begin_tag(Candidate.admission_grade_tag) + repr(
            self.admission_grade) + build_end_tag(Candidate.admission_grade_tag) + "\n"
        result += "\t" + build_begin_tag(Candidate.first_option_tag) + repr(
            self.first_option) + build_end_tag(Candidate.first_option_tag) + "\n"
        result += "\t" + build_begin_tag(Candidate.second_option_tag) + repr(
            self.second_option) + build_end_tag(Candidate.second_option_tag) + "\n"
        result += build_end_tag(Candidate.table_tag) + "\n"
        return result


def get_all_candidates(type=0):
    with open(DB_FILE_PATH, "r+") as f:
        new_f = f.readlines()
        result = []
        for line in new_f:
            tag = get_begin_tag(line)
            if tag == Candidate.table_tag:
                found = Candidate()
            if tag == Candidate.cnp_tag:
                value = get_tag_value(line)
                found.cnp = int(value)
            if tag == Candidate.first_name_tag:
                value = get_tag_value(line)
                found.first_name = value
            if tag == Candidate.surname_tag:
                value = get_tag_value(line)
                found.surname = value
            if tag == Candidate.email_tag:
                value = get_tag_value(line)
                found.email = value
            if tag == Candidate.info_grade_tag:
                value = get_tag_value(line)
                found.info_grade = float(value)
            if tag == Candidate.math_grade_tag:
                value = get_tag_value(line)
                found.math_grade = float(value)
            if tag == Candidate.high_school_avg_grade_tag:
                value = get_tag_value(line)
                found.high_school_avg_grade = float(value)
            if tag == Candidate.admission_grade_tag:
                value = get_tag_value(line)
                found.admission_grade = float(value)
            if tag == Candidate.first_option_tag:
                if type == 1:
                    value = get_tag_value(line)
                    found.first_option = get_specialization_by_id(int(value)).name
                else:
                    value = get_tag_value(line)
                    found.first_option = int(value)
            if tag == Candidate.second_option_tag:
                if type == 1:
                    value = get_tag_value(line)
                    found.second_option = get_specialization_by_id(int(value)).name
                else:
                    value = get_tag_value(line)
                    found.second_option = int(value)
                result.append(found)
        return result


#print("\nget_all_candidates")
#all_candidates = get_all_candidates()
#for x in all_candidates:
#    x.print()


def get_candidate_by_id(cnp_identifier):
    with open(DB_FILE_PATH, "r+") as f:
        new_f = f.readlines()
        for line in new_f:
            tag = get_begin_tag(line)
            if tag == Candidate.table_tag:
                found = Candidate()
            if tag == Candidate.cnp_tag:
                value = get_tag_value(line)
                found.cnp = int(value)
            if tag == Candidate.first_name_tag:
                value = get_tag_value(line)
                found.first_name = value
            if tag == Candidate.surname_tag:
                value = get_tag_value(line)
                found.surname = value
            if tag == Candidate.email_tag:
                value = get_tag_value(line)
                found.email = value
            if tag == Candidate.info_grade_tag:
                value = get_tag_value(line)
                found.info_grade = float(value)
            if tag == Candidate.math_grade_tag:
                value = get_tag_value(line)
                found.math_grade = float(value)
            if tag == Candidate.high_school_avg_grade_tag:
                value = get_tag_value(line)
                found.high_school_avg_grade = float(value)
            if tag == Candidate.admission_grade_tag:
                value = get_tag_value(line)
                found.admission_grade = float(value)
            if tag == Candidate.first_option_tag:
                value = get_tag_value(line)
                found.first_option = int(value)
            if tag == Candidate.second_option_tag:
                value = get_tag_value(line)
                found.second_option = int(value)
                if found.cnp == cnp_identifier:
                    return found
        return None


#print("\nget candidate by cnp")
#found_by_id = get_candidate_by_id(12345)
#found_by_id.print()
#print(found_by_id.to_xml())


def delete_candidate_by_id(cnp_identifier):
    with open(DB_FILE_PATH, "r+") as f:
        new_f = f.readlines()
        f.seek(0)
        count = 0
        while count < (len(new_f)):
            line = new_f[count]
            tag = get_begin_tag(line)
            if tag == Candidate.table_tag:
                new_line = new_f[count + 1]
                id_line = get_tag_value(new_line)
                print(id_line)
                if int(id_line) == cnp_identifier:
                    count += 12
                    continue
            f.write(new_f[count])
            count += 1
        f.truncate()


#print("\ndelete candidate by cnp")
#delete_candidate_by_id(123456)


def save_candidate(new_candidate):
    existing = get_candidate_by_id(new_candidate.cnp)
    if existing is None:
        with open(DB_FILE_PATH, "a") as f:
            f.write(new_candidate.to_xml())
        return 'OK'
    else:
        return 'ALREADY_EXISTING'



#print("\nsave new_candidate")
#new_candidate = Candidate()
#new_candidate.cnp = 987654321
#new_candidate.first_name = "new student in town"
#new_candidate.surname = " mhm "
#new_candidate.email = "new@email.com"
#new_candidate.info_grade = 6.7
#new_candidate.math_grade = 8.9
#new_candidate.high_school_avg_grade = 9.5
#new_candidate.admission_grade = 7.8
#new_candidate.first_option = 2
#new_candidate.second_option = 1


#save_candidate(new_candidate)


def update_candidate(candidate_to_update):
    existing = get_candidate_by_id(candidate_to_update.cnp)
    if existing is None:
        return "Entry not found"
    else:
        delete_candidate_by_id(candidate_to_update.cnp)
        save_candidate(candidate_to_update)
        return "OK"


#print("\nupdate candidate")
#new_candidate.surname = "updated name"
#update_candidate(new_candidate)


# Repartition


class AdmissionStatus(Enum):
    FEE = "With fee"
    FREE = "Budget"
    REJECTED = "Rejected"
    UNPROCESSED = "None"


class AdmissionResult:
    candidate_cnp = 0
    final_score = 0.0
    specialization_id = 0  # add -1 with Rejected for no repartition
    allocation = AdmissionStatus.UNPROCESSED

    table_tag = "repartition"
    candidate_cnp_tag = "candidate_cnp"
    final_score_tag = "final_score"
    specialization_id_tag = "specialization_id"
    allocation_tag = "allocation"

    def print(self):
        print(
            repr(
                self.candidate_cnp) +
            ' - ' +
            repr(
                self.specialization_id) +
			' - ' +
            repr(
                self.final_score) +
            ' - ' +
            self.allocation.name)

    def to_xml(self):
        result = build_begin_tag(AdmissionResult.table_tag) + "\n"
        result += "\t" + build_begin_tag(AdmissionResult.candidate_cnp_tag) + repr(
            self.candidate_cnp) + build_end_tag(AdmissionResult.candidate_cnp_tag) + "\n"
        result += "\t" + build_begin_tag(AdmissionResult.final_score_tag) + repr(
            self.final_score) + build_end_tag(AdmissionResult.final_score_tag) + "\n"
        result += "\t" + build_begin_tag(AdmissionResult.allocation_tag) + \
            self.allocation.name + build_end_tag(AdmissionResult.allocation_tag) + "\n"
        result += "\t" + build_begin_tag(AdmissionResult.specialization_id_tag) + repr(
            self.specialization_id) + build_end_tag(AdmissionResult.specialization_id_tag) + "\n"
        result += build_end_tag(AdmissionResult.table_tag) + "\n"
        return result


def get_admission_results(type=0):
    with open(DB_FILE_PATH, "r+") as f:
        new_f = f.readlines()
        result = []
        for line in new_f:
            tag = get_begin_tag(line)
            if tag == AdmissionResult.table_tag:
                found = AdmissionResult()
            if tag == AdmissionResult.candidate_cnp_tag:
                value = get_tag_value(line)
                found.candidate_cnp = int(value)
            if tag == AdmissionResult.specialization_id_tag:
                if type == 1:
                    value = get_tag_value(line)
                    found.specialization_id = get_specialization_by_id(int(value)).name
                else:
                    value = get_tag_value(line)
                    found.specialization_id = int(value)
            if tag == AdmissionResult.final_score_tag:
                value = get_tag_value(line)
                found.final_score = float(value)
            if tag == AdmissionResult.allocation_tag:
                value = get_tag_value(line)
                found.allocation = getattr(AdmissionStatus, value)
                result.append(found)
        return result


#print("\nget_admission_results")
#all_results = get_admission_results()
#for x in all_results:
#    x.print()


def get_admission_result_for_candidate(candidate_cnp):
    with open(DB_FILE_PATH, "r+") as f:
        new_f = f.readlines()
        for line in new_f:
            tag = get_begin_tag(line)
            if tag == AdmissionResult.table_tag:
                found = AdmissionResult()
            if tag == AdmissionResult.candidate_cnp_tag:
                value = get_tag_value(line)
                found.candidate_cnp = int(value)
            if tag == AdmissionResult.final_score_tag:
                value = get_tag_value(line)
                found.final_score = float(value)
            if tag == AdmissionResult.specialization_id_tag:
                value = get_tag_value(line)
                found.specialization_id = int(value)
            if tag == AdmissionResult.allocation_tag:
                value = get_tag_value(line)
                found.allocation = getattr(AdmissionStatus, value)
                if candidate_cnp == found.candidate_cnp:
                    return found
        return None

"""
printprint("\nget_admission_result_for_candidate")
found_by_id = get_admission_result_for_candidate(12345)
found_by_id.print()
print(found_by_id.to_xml())
"""

def delete_admission_result_for_candidate(candidate_cnp):
    with open(DB_FILE_PATH, "r+") as f:
        new_f = f.readlines()
        f.seek(0)
        count = 0
        while count < (len(new_f)):
            line = new_f[count]
            tag = get_begin_tag(line)
            if tag == AdmissionResult.table_tag:
                new_line = new_f[count + 1]
                id_line = get_tag_value(new_line)
                if int(id_line) == candidate_cnp:
                    count += 6 # 5
                    continue
            f.write(new_f[count])
            count += 1
        f.truncate()


#print("\ndelete admission result for candidate by cnp")
#delete_admission_result_for_candidate(987654321)


def save_admission_result_for_candidate(adm_result):
    existing = get_admission_result_for_candidate(adm_result.candidate_cnp)
    if existing is None:
        with open(DB_FILE_PATH, "a") as f:
            f.write(adm_result.to_xml())		
        return "OK"
    else:
        return update_admission_result_for_candidate(adm_result)


#print("\nsave admission_result")
#admiss_result = AdmissionResult()
#admiss_result.candidate_cnp = 987654321
#admiss_result.allocation = AdmissionStatus.FEE
#admiss_result.specialization_id = 4

#save_admission_result_for_candidate(admiss_result)


def update_admission_result_for_candidate(adm_result):
    existing = get_admission_result_for_candidate(adm_result.candidate_cnp)
    if existing is None:
        return "Entry not found"
    else:
        delete_admission_result_for_candidate(adm_result.candidate_cnp)
        with open(DB_FILE_PATH, "a") as f:
            f.write(adm_result.to_xml())
        return "OK"


#print("\nupdate admission_result")
#admiss_result.allocation = AdmissionStatus.REJECTED
#admiss_result.specialization_id = -1


#update_admission_result_for_candidate(admiss_result)
