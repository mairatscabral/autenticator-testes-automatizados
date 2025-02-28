import unittest
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):

    def setUp(self):
    
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://127.0.0.1:8000/accounts/login/") 

    def test_login_sucesso(self):
        driver = self.driver

        username_input = driver.find_element(By.NAME, "username") 
        password_input = driver.find_element(By.NAME, "password") 
        
        username_input.send_keys("mairateste")
        password_input.send_keys("123456")

        password_input.send_keys(Keys.RETURN)

        self.assertEqual(driver.title, "Autenticator - Dashboard")  
        

    def tearDown(self):
        
        self.driver.quit()

class TestCadastroUsuario(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://127.0.0.1:8000/accounts/register/")  # Substitua pela URL de cadastro do seu sistema

    def test_cadastro_sucesso(self):
        driver = self.driver

        nome_input = driver.find_element(By.NAME, "username") 
        email_input = driver.find_element(By.NAME, "email") 
        senha_input = driver.find_element(By.NAME, "password1")  
        confirmacao_senha_input = driver.find_element(By.NAME, "password2")  
        
        nome_input.send_keys("Novo Usuario")
        email_input.send_keys("usuario@exemplo.com")
        senha_input.send_keys("senha_segura")
        confirmacao_senha_input.send_keys("senha_segura")

        confirmacao_senha_input.send_keys(Keys.RETURN)
        
        self.assertEqual(driver.title, "Autenticator - Login") 

    def test_cadastro_invalido_email(self):
        driver = self.driver

        nome_input = driver.find_element(By.NAME, "username") 
        email_input = driver.find_element(By.NAME, "email") 
        senha_input = driver.find_element(By.NAME, "password1")  
        confirmacao_senha_input = driver.find_element(By.NAME, "password2")  
        
        nome_input.send_keys("mateste3")
        email_input.send_keys("mairateste@exemplo.com")
        senha_input.send_keys("senha_segura")
        confirmacao_senha_input.send_keys("senha_segura")

        confirmacao_senha_input.send_keys(Keys.RETURN)
        
        self.assertEqual(driver.title, "Autenticator - Login")

        erro_email = driver.find_element(By.XPATH, "//div[contains(@class, 'alert') and contains(text(), 'Email já cadastrado')]")
        self.assertTrue(erro_email.is_displayed(), "A mensagem de erro para email já cadastrado não foi exibida.")

    def test_senhas_nao_correspondem(self):
        driver = self.driver

        nome_input = driver.find_element(By.NAME, "username") 
        email_input = driver.find_element(By.NAME, "email") 
        senha_input = driver.find_element(By.NAME, "password1")  
        confirmacao_senha_input = driver.find_element(By.NAME, "password2")  
        
        nome_input.send_keys("Novo Usuario")
        email_input.send_keys("usuario@exemplo.com")
        senha_input.send_keys("senha_segura")
        confirmacao_senha_input.send_keys("senha_errada")

        confirmacao_senha_input.send_keys(Keys.RETURN)  
        
        self.assertEqual(driver.title, "Autenticator - Login") 

        erro_senha = driver.find_element(By.XPATH, "//div[contains(@class, 'alert') and contains(text(), 'As senhas não coincidem')]")
        self.assertTrue(erro_senha.is_displayed(), "A mensagem de erro para senhas não coincidentes não foi exibida.")

    def tearDown(self):

        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
