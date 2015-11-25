import datetime

#creation of todays date in 1-366 for calculations of 30 day periods
strtoday = datetime.datetime.now()
today = int(strtoday.strftime('%j')) # remove all modifications of todays code for launch


# Create Object by defining (credit limit, interest)
	# note interest is input as a percent number (ie. 20% input as 20, not .2)

class Credit:
	def __init__(self, init_limit, init_interest, day):
		self.limit = init_limit
		self.interest = init_interest

		self.action_log = [] # [action, amount, pass/fail]
		
		self.owed = 0
		self.balance = self.limit - self.owed
		 
	def update_log(self, action, amount, result):
		
		if result == True:
			pass_fail = "a success!"
		elif result == False:
			pass_fail = "failed"
	
		self.action_log.append("{} occured. Amount: {}. Action was {}. Owe: ${}. Limit: ${}".format(action, str(amount), pass_fail, str(self.owed), str(self.limit)))

	


	# Pay with card
	def pay(self, price):
		action_name = "Payment with card"
		# validate balance to limit
		if price < self.balance:
			# make the payment
			
			self.owed = self.owed + price
			self.update_log(action_name, price, True)
		else:
			# throw error
			self.update_log(action_name, price, False)

		
	# Deposit Money
	def pay_debt(self, deposit_amount):
		action_name = "Paid debt"

		# make a check for correct values

		if deposit_amount < self.owed:
			# Modify Owed Amount
			self.owed -= deposit_amount 

			success = True
		else:
			print("Sorry that is more than you owe on the account, go spend some money!!")
			success = False

		self.update_log(action_name, deposit_amount, success)
	
	# Withdrawl money from card (Cash Withdrawl)
	# Available Credit
	# Increase Limit
	# Increase Interest
	# Calculate interest on day 30

today = 1
new_card = Credit(10000, 10, today)

day_of_pay_period = 3
new_card.pay(200)

new_card.pay_debt(100)


for action in new_card.action_log:
	print(action)