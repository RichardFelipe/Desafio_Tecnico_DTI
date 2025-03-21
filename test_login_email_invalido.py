import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLoginEmailInvalido(unittest.TestCase):

    def setUp(self):
        # Configuração do driver do navegador
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://automationpractice.pl/index.php?controller=authentication&back=my-account")
        print("Navegador iniciado e página carregada.")

    def tearDown(self):
        # Finaliza o driver do navegador
        self.driver.quit()
        print("Navegador fechado.")

    def test_login_email_invalido(self):
        driver = self.driver

        try:
            # Cenário 2: Login com email inválido
            driver.find_element(By.ID, "email").send_keys("usuario@invalido.com")
            driver.find_element(By.ID, "passwd").send_keys("123456789")
            driver.find_element(By.ID, "SubmitLogin").click()
            
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//div[@class='alert alert-danger']"))
            )
            
            self.assertTrue(driver.find_element(By.XPATH, "//div[@class='alert alert-danger']/ol/li").is_displayed())
            print("Teste de login com email inválido: PASSOU")
        
        except Exception as e:
            driver.save_screenshot('login_email_invalido.png')
            print(f"Teste de login com email inválido: FALHOU - {str(e)}")
            self.fail("Teste de login com email inválido falhou")

if __name__ == "__main__":
    unittest.main()