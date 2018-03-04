import requests
import time
import threading
from utils import*
import random
import proxymanager

url = 'https://www.habitburger.com/signup/'

emails = []


class Entry(threading.Thread):
	def __init__(self,month,day):
		threading.Thread.__init__(self)
		self.month = str(month)
		if len(self.month) > 1:
			self.month = '0' + self.month
		self.day = str(day)
		self.failedAttempts = 0
	def run(self):
		if gmail:
			self.email = random.choice(emails)
			emails.remove(self.email)
			print(len(emails))
		else:
			self.email = '{}.{}.{}@{}'.format(username,self.month,self.day,domain)
		print(self.email)
		data = {
			"gform_field_values": "",
			"gform_source_page_number_6": "1",
			"gform_submit": "6",
			"gform_target_page_number_6": "0",
			"gform_unique_id": "",
			"input_10": firstName,
			"input_11": lastName,
			"input_12": "",
			"input_13": "",
			"input_14": "",
			"input_15": "",
			"input_16": "",
			"input_2": self.email,
			"input_3": nearestID,
			"input_4": self.month,
			"input_5": self.day,
			"input_6": zipCode,
			"input_7": "6ABC7BEC-536E-462C-ABD3-EE3E2F6E233B",
			"input_8": "2608",
			"input_9": "CharClub Signup Page",
			"is_submit_6": "1",
			"state_6": "WyJbXSIsIjAzN2JjZjRmOTZkOTZjNTZmNzQ1ZGM3ODIzYTgzYzM4Il0="
		}
		r = requests.post(url,data=data,proxies=random.choice(proxies))
		# print(r.text)
		if 'success' in str(r.text):
			cLog('[{}] - {}  - succesful'.format(r.status_code,self.email),'green')
			return True
		else:
			cLog('[{}] - {}  - FAILED'.format(r.status_code,self.email),'red')
			if self.failedAttempts < 5:
				print('retrying..')
				self.run()
				self.failedAttempts +=1
			return False


def generateEmails(username, domain):
	email = ""
	username_length = len(username)
	combinations = pow(2, username_length - 1)
	padding = "{0:0" + str(username_length - 1) + "b}"
	for i in range(0, combinations):
		bin = padding.format(i)
		full_email = ""
		for j in range(0, username_length - 1):
			full_email += (username[j]);
			if bin[j] == "1":
				full_email += "."
		full_email += (username[j + 1])
		email = full_email + '@' + domain
		global emails
		emails.append(email)
		print(emails)



userEmail = input('email: ')
username,domain = userEmail.split('@')
if 'gmail' in userEmail:
	gmail = True
	generateEmails(username,domain)
else:
	gmail = False
nearestID = input('nearest store ID ')
zipCode = input('zip ')
firstName = input('first name ')
lastName = input('last name ')

stamp = '''
▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀
▐░▌          ▐░▌       ▐░▌     ▐░▌     ▐░▌       ▐░▌▐░▌          ▐░▌
▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌     ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌     ▐░▌     ▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀▀▀▀▀▀█░▌ ▀▀▀▀▀▀▀▀▀█░▌
▐░▌          ▐░▌       ▐░▌     ▐░▌     ▐░▌       ▐░▌          ▐░▌          ▐░▌
▐░▌          ▐░▌       ▐░▌     ▐░▌     ▐░▌       ▐░▌ ▄▄▄▄▄▄▄▄▄█░▌ ▄▄▄▄▄▄▄▄▄█░▌ ▄
▐░▌          ▐░▌       ▐░▌     ▐░▌     ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌
 ▀            ▀         ▀       ▀       ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀
 '''
proxies = proxymanager.importProxies('proxies')
# print(proxies)
print('\n\n')
print(stamp)
print('\n\n')
print('               written by anton. @thesolecop')
for bMonth in range(1,13):
	for bDay in range(1,32):
		t = Entry(bMonth,bDay)
		t.start()
		time.sleep(0.5)
