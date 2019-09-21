import random
import time
def main(start,end,ip):
	#inputed_text = input("Hi, input your random range")

	print (start,end,ip)
	if(ip=="127.0.0.1"):
		return(admin(start,end))
	else:
		return(smertnuy(start,end))


def smertnuy(start,end):
	numbers=list()
	for a in range(int(end)):
		numbers.insert(a,random.randrange(int(start),int(end)))
	return(numbers)
def admin(start,end):
	#return("16")
	numbers=list()
	a=0
	for a in range(15):
		numbers.insert(a,random.randrange(int(start),int(end)))
	numbers.insert(a+1,16)
	return(numbers)

def onemore():
	zapros = main(0,10000,"127.0.0.1")
	for a in range(len(zapros)):
		time.sleep(0.3)
		print(zapros[a])
#main("1","500","192.168.1.1")
#main(1,500,"")
if __name__ == '__main__':
	#main(1,500,"192.168.1.1")
	onemore()