export PYTHONPATH=${PWD}

# Criar e ativar o ambiente virtual
python -m venv venv
source venv/bin/activate

# Instalar as dependências
pip install -r requirements.txt

# Executar os testes com unittest
python -m unittest discover -s tests

# ou executar os testes com pytest
pytest
