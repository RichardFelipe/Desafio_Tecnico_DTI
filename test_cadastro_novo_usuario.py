import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class TestCadastroNovoUsuario(unittest.TestCase):

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

    def test_cadastro_novo_usuario(self):
        driver = self.driver

        try:
            # Cenário 1: Cadastro de novo usuário com informações válidas
            driver.find_element(By.ID, "email_create").send_keys("Carloss01@gmail.com")
            driver.find_element(By.ID, "SubmitCreate").click()
            
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, "id_gender1"))
            ).click()
            
            driver.find_element(By.ID, "customer_firstname").send_keys("Joao")
            driver.find_element(By.ID, "customer_lastname").send_keys("Silva")
            driver.find_element(By.ID, "passwd").send_keys("142536")
            
            Select(driver.find_element(By.ID, "days")).select_by_value("20")
            Select(driver.find_element(By.ID, "months")).select_by_value("9")
            Select(driver.find_element(By.ID, "years")).select_by_value("2002")
            
            driver.find_element(By.ID, "submitAccount").click()
            
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//p[@class='info-account']"))
            )
            
            self.assertTrue(driver.find_element(By.XPATH, "//p[@class='info-account']").is_displayed())
            print("Teste de cadastro de novo usuário: PASSOU")
        
        except Exception as e:
            driver.save_screenshot('cadastro_novo_usuario.png')
            print(f"Teste de cadastro de novo usuário: FALHOU - {str(e)}")
            self.fail("Teste de cadastro de novo usuário falhou")

if __name__ == "__main__":
    unittest.main()