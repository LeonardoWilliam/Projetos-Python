import pandas as pd

nota1 = float(input("Digite a nota do aluno: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))


dados = {
    "Notas" : [nota1, nota2, nota3]
}

df= pd.DataFrame(dados)

media = df["Notas"].mean()

print(df)

print("Sua media foi {:.2f}".format(media))
if media >=7:
    print("APROVADO")
elif media >=5:
    print("RECUPERAÇÃO")
else:
    print("REPROVADO")

#