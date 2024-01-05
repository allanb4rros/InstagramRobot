from selenium import webdriver
from selenium.webdriver.common.by import By
from openpyxl import Workbook

def extract_data_and_save_to_excel(url, file):
    
    # Config Selenium com o caminho para o driver do navegador
    
    driver_path = 'C:\\chromedriver.exe'

    driver = webdriver.Chrome()

    # Abre a página no navegador
    driver.get(url)

    # Espera até que tabela esteja presentes na página
    divs_lines = driver.find_elements(By.CLASS_NAME, "contributor")

    # Cria um novo arquivo Excel
    workbook = Workbook()
    sheet = workbook.active

    # Loop para extrair os dados e escrever no Excel
    for div_line in divs_lines:
        # Lê o atributo da página onde contém a tag do Instagram
        cells = div_line.find_elements(By.XPATH, "./div[@class='contributor__name']/div[@class='contributor__name-content']")

        # Verifica se há dados antes de adicionar uma nova linha
        if cells:
            data_line = [cell.text for cell in cells]
            #print(data_line)
            sheet.append(data_line)

    # Salva o arquivo Excel
    workbook.save(file)

    # Fecha o navegador após a conclusão do script
    driver.quit()

# Chama a função com os parâmetros desejados
extract_data_and_save_to_excel('https://hypeauditor.com/top-instagram/', 'C:\\dados_divs.xlsx')
