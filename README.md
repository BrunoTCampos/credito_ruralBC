# Banco Central do Brasil - Matriz de Crédito Rural (em construção)

-------
Este pacote facilita o acesso aos dados de crédito rural do Banco Central do Brasil, ainda em construção.

Acessar os contratos por municipio e gerar um CSV.

Instalação
-------

```bash
$ pip install -r requirements.txt
```

Como usar
-------
```bash
rom creditoruralBC import get_dados_credito_rural
get_dados_municipio(top=50, select="Municipio,Quantidade,Valor", nome_arquivo="meus_dados.csv") #Contratos por Município
```

Licença
-------

[Licença MIT](LICENSE)
