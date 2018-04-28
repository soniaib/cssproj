from db import DatabaseController as DbC

def get_results():
	all_results = DbC.get_admission_results()
	return all_results

class CalculateResults():
    test = "Should add logic here"
   