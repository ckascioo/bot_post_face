from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.support.select import Select # Para funcionar com seleção de dropdown
from selenium.webdriver.common.keys import Keys # Para usar teclas do teclado

def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=800,1000', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,
    })
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    return driver

driver = iniciar_driver()
# Navegar até o site
driver.get('https://facebook.com/')
sleep(3)

# Digitar email
email = driver.find_element(By.ID, 'email')
sleep(2)
email.send_keys('ckascio0@yahoo.com.br')
sleep(2)

# Digitar senha
senha = driver.find_element(By.ID, 'pass')
sleep(2)
senha.send_keys('ckask8871002')
sleep(2)

# Clicar em login
entrar = driver.find_element(By.XPATH, '//button[@name="login"]')
sleep(3)
entrar.click()
sleep(5)

# Encontrar e clicar no campo de postagem
postagem = driver.find_element(By.XPATH, '//div[@class="xi81zsa x1lkfr7t xkjl1po x1mzt3pk xh8yej3 x13faqbe"]')
sleep(2)
postagem.click()
sleep(3)

# Clicar dentro do campo para escrever
escrever = driver.find_element(By.XPATH, '//p[@class="xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8"]')
sleep(2)
escrever.click()

# Digitar algo
escrever.send_keys('Oi, é apenas um teste')
sleep(2)

# Clicar em publicar
publicar = driver.find_element(By.XPATH, '//div[@class="x1n2onr6 x1ja2u2z x78zum5 x2lah0s xl56j7k x6s0dn4 xozqiw3 x1q0g3np xi112ho x17zwfj4 x585lrc x1403ito x972fbf xcfux6l x1qhh985 xm0m39n x9f619 xn6708d x1ye3gou xtvsq51 x1r1pt67"]')
sleep(2)
publicar.click()


input('')
driver.close()