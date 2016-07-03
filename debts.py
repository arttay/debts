from Calcs import calc

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
			"interest":20.24,
			"payoff": 3579.48
		}
	}

constants 	= define_constants()
calc 		= calc()
payment 	= input("Payment amount: ")


calc.calcDebt(constants["CREDIT_CARD"]["total"], constants["CREDIT_CARD"]["interest"], payment, constants["CREDIT_CARD"]["payoff"])
