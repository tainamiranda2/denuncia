# Sistema para Armazenar Denúncias

## Tecnologias Utilizadas
- Django
- Python
- SQLite
- Bootstrap

## Ambiente Virtual
Para criar e ativar o ambiente virtual, execute os comandos a seguir:

```bash
python -m venv denv
.\denv\Scripts\activate  # No Windows
source denv/bin/activate  # No Linux/Mac
```

## Instalação e Configuração
Instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

Rode as migrações do banco de dados:

```bash
python manage.py migrate
```

Crie um superusuário para acessar o painel administrativo:

```bash
python manage.py createsuperuser
```

## Execução do Projeto
Para iniciar o servidor de desenvolvimento, utilize o comando:

```bash
python manage.py runserver
```

Acesse o projeto em:
```
http://127.0.0.1:8000/
```

## Páginas
- **Lista de Denúncias**: Exibe todas as denúncias cadastradas.
- **Cadastro de Denúncias**: Formulário para cadastrar novas denúncias.
- **Detalhes de uma Denúncia**: Visualiza as informações completas de uma denúncia.
- **Edição de Denúncia**: Permite atualizar as informações de uma denúncia.

## Funcionalidades
- **Cadastrar**: Adiciona uma nova denúncia ao sistema.
- **Atualizar**: Edita uma denúncia existente.
- **Deletar**: Remove uma denúncia do banco de dados.
- **Listar**: Mostra todas as denúncias cadastradas.
- **Logar**: Autentica o usuário no sistema.
- **Deslogar**: Faz o logout do usuário autenticado.

## Models
- **Denúncia**: Representa uma denúncia cadastrada no sistema.
- **User**: Representa os usuários que acessam o sistema.

## Imagens das Telas


<img src="/denuncia/static/img/logar.png">
<img src="/denuncia/static/img/lista.png">
<img src="/denuncia/static/img/cadastrar.png">