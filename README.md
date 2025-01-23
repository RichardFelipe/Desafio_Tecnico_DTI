# Desafio_Tecnico_DTI

Este repositório contém um conjunto de testes automatizados escritos em Python, utilizando o framework Selenium para validar funcionalidades de um sistema web.

# Cenários de Teste

**Cenário 1: Cadastro de novo usuário com informações válidas**  
Dado que o usuário esteja na página "Automation Practice"  
Quando o usuário insere um email válido na seção "Create an account" e clica em "Create an account"  
Então a página deve redirecionar o usuário para a página "Minha Conta" e exibir uma mensagem de boas-vindas  

**Cenário 2: Login com email inválido**  
Dado que o usuário esteja na página "Automation Practice"  
Quando o usuário insere um email inválido (por exemplo, "usuario@invalido") e uma senha qualquer  
Então a página deve exibir uma mensagem de erro indicando que o email é inválido  

**Cenário 3: Login com campo de senha vazio**  
Dado que o usuário esteja na página "Automation Practice"  
Quando o usuário insere um email válido e deixa o campo de senha vazio  
Então a página deve exibir uma mensagem de erro informando que a senha é obrigatória  

# Executando os Testes

Os testes podem ser executados individualmente ou em conjunto, usando o módulo `unittest`.

### Executando Testes Individuais  

**Cadastro de Novo Usuário**  
python -m unittest test_cadastro_novo_usuario.py

**Login com E-mail Inválido**   
python -m unittest test_login_email_invalido.py

**Login com Campo de Senha Vazio**  
python -m unittest test_login_senha_vazia.py

**Executando Todos os Testes**  
Para executar todos os testes de uma vez, utilize o comando:  
python -m unittest discover
