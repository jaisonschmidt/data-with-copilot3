# CLI de Manipulação de DataFrame

Este projeto fornece uma interface de linha de comando (CLI) para manipular um DataFrame a partir de um arquivo CSV, utilizando apenas a biblioteca padrão do Python. O objetivo é facilitar transformações comuns em dados, especialmente para uso em pipelines de dados e ambientes CI/CD.

## Sumário

- [Objetivos](#objetivos)
- [Instalação](#instalação)
- [Uso](#uso)
- [Comandos Disponíveis](#comandos-disponíveis)
- [Exemplos](#exemplos)
- [Sobre os Dados](#sobre-os-dados)
- [Contribuindo](#contribuindo)
- [Licença](#licença)

## Objetivos

- Demonstrar como criar uma CLI robusta para manipulação de dados com Python.
- Automatizar transformações em arquivos CSV.
- Servir como base para integração em pipelines de dados.

## Instalação

1. Clone o repositório:
    ```sh
    git clone https://github.com/seu-usuario/seu-repo.git
    cd seu-repo
    ```

2. (Opcional) Crie e ative um ambiente virtual:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Instale as dependências:
    ```sh
    pip install -r workshop/requirements.txt
    ```

## Uso

Navegue até o diretório `workshop` e execute o script `main.py` com o comando desejado:

```sh
cd workshop
python main.py <comando>
```

### Comandos Disponíveis

- `drop_notes`: Remove a coluna `notes` do DataFrame.
- `select_high_ratings`: Seleciona linhas onde a coluna `rating` é 90 ou superior.
- `drop_and_one_hot_encode_red_wine`: Codifica a categoria 'Red Wine' como one-hot e remove a coluna `variety`.
- `remove_newlines_carriage_returns`: Remove quebras de linha e retornos de carro das colunas de texto.
- `convert_ratings_to_int`: Converte a coluna `rating` de float para inteiro.

## Exemplos

Remover a coluna 'notes':
```sh
python main.py drop_notes
```

Selecionar linhas com classificações altas:
```sh
python main.py select_high_ratings
```

Codificação one-hot para 'Red Wine' e remoção da coluna 'variety':
```sh
python main.py drop_and_one_hot_encode_red_wine
```

Remover quebras de linha e retornos de carro:
```sh
python main.py remove_newlines_carriage_returns
```

Converter coluna 'rating' para inteiro:
```sh
python main.py convert_ratings_to_int
```

## Sobre os Dados

Os dados estão localizados em `workshop/train.csv` e possuem as seguintes colunas principais:

- `notes`: Notas de texto sobre os dados.
- `rating`: Classificações numéricas para os dados.
- `variety`: Tipo ou variedade (exemplo: 'Red Wine').

Após as transformações, os dados são salvos em `workshop/transformed_train.csv`.

## Contribuindo

Contribuições são bem-vindas! Siga os passos:

1. Faça um fork do repositório.
2. Crie uma branch (`git checkout -b feature-nome`).
3. Faça suas alterações.
4. Commit (`git commit -m 'Descrição da alteração'`).
5. Push (`git push origin feature-nome`).
6. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](../LICENSE)