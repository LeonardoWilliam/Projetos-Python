import pandas as pd

dados = {
    'Nome': ['Ana', 'Carlos', 'Maria'],
    'Idade': [25, 30, 28],
    'Cidade': ['Rio de Janeiro', 'São Paulo', 'Curitiba']
}

df = pd.DataFrame(dados)

print(df)