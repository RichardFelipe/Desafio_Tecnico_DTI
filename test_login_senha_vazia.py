import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLoginSenhaVazia(unittest.TestCase):

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

    def test_login_senha_vazia(self):
        driver = self.driver

        try:
            # Cenário 3: Login com campo de senha vazio
            driver.find_element(By.ID, "email").send_keys("Joao505@gmail.com")
            driver.find_element(By.ID, "SubmitLogin").click()
            
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//div[@class='alert alert-danger']/ol/li"))
            )
            
            error_message = driver.find_element(By.XPATH, "//div[@class='alert alert-danger']/ol/li").text
            self.assertEqual(error_message, "Password is required.")
            print("Teste de login com campo de senha vazio: PASSOU")
        
        except Exception as e:
            driver.save_screenshot('login_senha_vazia.png')
            print(f"Teste de login com campo de senha vazio: FALHOU - {str(e)}")
            self.fail("Teste de login com campo de senha vazio falhou")

if __name__ == "__main__":
    unittest.main()