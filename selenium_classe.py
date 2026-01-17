from selenium.webdriver import Chrome, ChromeOptions


class Selenium:
    def configurar_selenium(self):
        print("Configurando o Selenium...")
        options = ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--window-size=1920,1080')
        options.add_argument('--disable-gpu')
        options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')

        return Chrome(options=options)