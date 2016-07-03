class calc(object):
	def calcDebt(self, total, interestRate, payments, payoff=0):
		key = 1
		total = total - payoff
		while (total >= 0):
			total = total - payments;
			formatDic = {
				"monthKey": key,
				"amountLeft": total
			}
			print 'Month: {0[monthKey]} | Amount Left: {0[amountLeft]}'.format(formatDic)
			key = key + 1;