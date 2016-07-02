import Calcs

def define_constants():
	return {
		"GREAT_LAKES": {

		},
		"BND": {
			"total": 19371.60,
			"interest": 5.710
		},
		"CREDIT_CARD":{
			"total": 8438.23,
			"interest":20.24
		}
	}

constants = define_constants()
calc = Calcs;
calc.printInput("art")