
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep
import pandas as pd


def search_and_follow_csv(url, usernames):
    driver_path = 'C:\\chromedriver.exe'
    chrome_options = Options()
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--disable-popup-blocking')  # Desativa o bloqueio de pop-ups
    chrome_options.add_argument('--disable-notifications')  # Desativa o bloqueio de notificações

    driver = webdriver.Chrome(options=chrome_options)
    
    # Abre a página no navegador
    driver.get(url)

    # Espera até que os formulários estejam presentes na página
    username_input = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.NAME, "username")))
    password_input = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.NAME, "password")))

    # Envia username e password
    username_input.send_keys("seu login")
    password_input.send_keys("sua senha")

    # Identifica botão submit e loga
    login_button = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    login_button.click()

    sleep(5)

    # Identifica botão de não guardar informações de login e interage 
    login_recuse = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='button']")))
    login_recuse.click()

    sleep(5)


    # Identifica botão de ativar notificações e ativa
        
        #  Não necessário pelo argumento  chrome_options.add_argument('--disable-popup-blocking')  # Desativa o bloqueio de pop-ups
    
    #login_active_popup = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*/text()[normalize-space(.)='Ativar']/parent::*"))) 
    #login_active_popup.click()

    #sleep(5)

    total_followed = 0  # Inicializa a variável antes do loop

    for username in usernames:
        
        # Espera até que as divs estejam presentes na página
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//span[text()='Página inicial']/following::*[name()='svg'][1]"))).click()
        
        # Espera até que as divs estejam presentes na página

        sleep(30)
       
        search_input = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//input[@value='']")))
        search_input.clear()
        search_input.send_keys(username)

        sleep(30)

        # Espera até que o elemento seja clicável
        select_search = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, f".//*[normalize-space(text()) and normalize-space(.)='{username}']/following::span[2]")))
        select_search.click() 

        sleep(15)
   
        followuser =  WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//button/div")))
        followuser.click()
             
        sleep(3)

        # Voltar à página inicial para o próximo username
        driver.get(url)
       
        total_followed += 1  # Incrementa o contador para cada usuário seguido
    

    driver.quit()
    
    print(f"Total de usuários seguidos: {total_followed}")  # Exibe o total após o loop

    return total_followed

    
# Lê todos os valores do arquivo Excel e ignora cabeçalho 
df = pd.read_excel('C:\\dados_divs.xlsx', header=None)
usernames = df.values.flatten().tolist()

# Chamada da função com a link e lista de usernames
search_and_follow_csv("https://instagram.com.br", usernames)



