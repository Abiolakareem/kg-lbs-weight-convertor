import time


def kg():
	num=input('Whats your weight (in lbs) or "x" to switch mode or "c" to close app ' )
	if num =='x':
		lbs()
	elif num =='c':
		closeapp()
	else:
		weight_pound=float(num)
		convert=weight_pound*0.45
		print(f'{weight_pound} lbs is {round(convert, 2)}kg')
				#except:
				#	print ('Enter the appropriate input')
def lbs():
#				try:
	num=input('Whats your weight (in kg) or "x" to switch mode or "c" to close app ')
	if num =='x':
		kg()
	elif num =='c':
		closeapp()
	else:
		weight=float(num)
		convert=weight/0.45
		print(f'{weight} kg is {round(convert, 2)}lbs')
	#	except:
	#				print ('Enter the appropriate input')

def closeapp():
	print ('Thank you for using Convapp')
	#a-=1
	time.sleep(3)
	quit()

mode=input('Conversion mode: Enter "lbs" to convert from kg to lbs or enter "kg" to convert from lbs to kg otherwise enter anything to exit ').lower()
b=1

while b==1:
	if mode=='lbs':
		lbs()
	elif mode=='kg':
		kg()
	else:
		closeapp()
