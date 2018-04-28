from db.DatabaseController import get_admission_results

def get_results():
	all_results = get_admission_results()
	return all_results

class CalculateResults():
    test = "Should add logic here"
   