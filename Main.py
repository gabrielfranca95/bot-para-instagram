    
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random


class InstagramBot:
    def __init__(self, username, password): 
        self.username = username
        self.password = password
        # the executable below must be indicated a path, if the path indicates nonexistent, add geckodriver.exe to the webdriver folder and indicate the path to find it!#
        self.driver = webdriver.Firefox(executable_path=r'C:\Users\pc\Downloads\geckodriver\geckodriver.exe')


    def login(self):
        driver = self.driver
        driver.get('https:www.instagram.com')
        time.sleep(10)
        login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        login_button.click()
        time.sleep(10)
        user_element = driver.find_element_by_xpath("//input[@name='username']")
        user_element.click()
        user_element.clear()
        user_element.send_keys(self.username)
        password_element = driver.find_element_by_xpath("//input[@name='password']")
        password_element.click()
        password_element.clear()
        password_element.send_keys(self.password)
        password_element.send_keys(Keys.RETURN)
        time.sleep(10)
        self.curtir_fotos('sua_hashtag')

    @staticmethod
    def digite_como_uma_pessoa(frase, onde_digitar):
        for letra in frase:
            onde_digitar.send_keys(letra)
            time.sleep(random.randint(1,5)/30)


        
    def curtir_fotos(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(8)

        for i in range(1, 3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(8)
        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        [href for href in pic_hrefs if hashtag in href]
        print(hashtag + ' fotos: ' + str(len(pic_hrefs)))

        for pic_href in pic_hrefs:
            driver.get(pic_href)
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            try:
                comentarios = ["Ótimo trabalho!"," Absolutamente fantástico!"," parabens","Que incrível!"," Adoreii issoo!"]
                driver.find_element_by_class_name('Ypffh').click()
                campo_comentario = driver.find_element_by_class_name('Ypffh')
                time.sleep(random.randint(4,8))
                self.digite_como_uma_pessoa(random.choice(comentarios),campo_comentario)
                time.sleep(random.randint(120,300))
                driver.find_element_by_xpath("//button[contains(text(),'Publicar')]").click()
                time.sleep(random.randint(5,8))
               
                Botao_curtir = driver.find_element_by_xpath('//button[@class="dCJp8 afkep"]')
                Botao_curtir.click()
                time.sleep(random.randint(6,8))
                
                Botao_pessoas = driver.find_element_by_xpath('//button[@class="sqdOP yWX7d     _8A5w5    "]')
                Botao_pessoas.click()
                time.sleep(random.randint(5,8))
                for b in range(1, 3):
                    Botao_segue = driver.find_element_by_xpath('//button[@class="sqdOP  L3NKy   y3zKF     "]')
                    Botao_segue.click()
                    time.sleep(3)
            except Exception as e:
                print(e)
                time.sleep(random.randint(1,8))
            


seuBot = InstagramBot('usuario','senha')
seuBot.login()

    
