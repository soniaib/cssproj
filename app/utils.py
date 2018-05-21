from db import DatabaseController as DbC

def get_results():
	all_results = DbC.get_admission_results(1)
	assert all_results is not None, "Empty list of candidates"
	return all_results

def calculate_final_score_for_candidate (item):
	final_score = max(item.info_grade, item.math_grade)*0.3 + item.high_school_avg_grade*0.2 + 0.5*item.admission_grade
	assert 4 <= final_score <= 10, "Value out of range [4,10] for admision grade"
	return final_score

def set_admision_status (item,specs,opt_arr):
	if item.final_score < 5:
		allocation = DbC.AdmissionStatus.REJECTED
		assert allocation.index(list(DbC.AdmissionStatus.REJECTED,DbC.AdmissionStatus.FREE,DbC.AdmissionStatus.FEE)), "Wrong status for candidate"
		return allocation
	if specs[item.specialization_id]["free_spots"] > 2:
		allocation = DbC.AdmissionStatus.FREE
		specs[item.specialization_id]["free_spots"] -= 1
	elif specs[item.specialization_id]["free_spots"] > 0:
		allocation = DbC.AdmissionStatus.FEE
		specs[item.specialization_id]["free_spots"] -= 1
	else:
		item.specialization_id = opt_arr[str(item.candidate_cnp)]["second_option"]
		if specs[item.specialization_id]["free_spots"] > 2:
			allocation = DbC.AdmissionStatus.FREE
			specs[item.specialization_id]["free_spots"] -= 1
		elif specs[item.specialization_id]["free_spots"] > 0:
			allocation = DbC.AdmissionStatus.FEE
			specs[item.specialization_id]["free_spots"] -= 1
		else:
			allocation = DbC.AdmissionStatus.REJECTED
	assert allocation.index(list(DbC.AdmissionStatus.REJECTED,DbC.AdmissionStatus.FREE,DbC.AdmissionStatus.FEE)), "Wrong status for candidate"
	return allocation

def calculate_results():
	specializations = DbC.get_all_specializations()
	candidates = DbC.get_all_candidates()
	repartition = []
	specs = {}
	opt_arr = {}
	
	for item in specializations:
		specs[item.identifier] = {}
		specs[item.identifier]["name"] = item.name 
		specs[item.identifier]["capacity"] = item.capacity 
		specs[item.identifier]["free_spots"] = item.capacity
	
	
	for item in candidates:
		r = DbC.AdmissionResult()
		r.candidate_cnp = item.cnp
		r.final_score = calculate_final_score_for_candidate(item)
		r.specialization_id = item.first_option
		r.allocation = DbC.AdmissionStatus.UNPROCESSED
		repartition.append(r)
		opt_arr[str(item.cnp)] = {}
		opt_arr[str(item.cnp)]["first_option"] = item.first_option
		opt_arr[str(item.cnp)]["second_option"] = item.second_option

	repartition = sorted(repartition, key = lambda x: (x.specialization_id, (-1)*x.final_score, ))
	
	for item in repartition:
		item.allocation=set_admision_status(item,specs,opt_arr)
		# print("Candidate CNP: ", item.candidate_cnp)
		# print("Admission Grade: ", item.final_score)
		# print("AdmissionResult: ", item.allocation)
		# print("Specialization: ", specs[item.specialization_id]["name"])
		# print("Specialization ID: ", item.specialization_id)
	assert repartition is not None, "Empty list of candidates for repartition"
	return repartition

def set_results():
	results = calculate_results()
	
	for item in results:
		if DbC.save_admission_result_for_candidate(item) != "OK":
			raise "Error in repartition processing!"
	
	print("Repartition completed successfully.")
	
# set_results()
