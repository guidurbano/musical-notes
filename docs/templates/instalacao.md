## Como instalar o projeto

Para instalação do CLI do projeto recomendamos que use o `pipx` para fazer
a instalação:

```bash
pipx install musical-notes
```

Embora isso seja somente uma recomendação! Você pode instalar o projeto
com o gerenciador de sua preferência. Como o `pip`:

```bash
pip install musical-notes
```

## Os comandos

O `musical-notes` distribui cada função em um subcomando e você pode executar
cada um deles para testar agora. O objetivo desse tutorial é explicar o
funcionamento básico da aplicação em linha de comando.

Os subcomandos são dividios em três funcões: `escalas`, `acordes` e
`campo harmônico`.

### Escalas

O subcomando de escalas nos auxilia a ter fácil acesso a formação das
escalas musicais.

Caso seja invocada sem nenhum parâmetro, retornará a escala de Dó maior:

```bash
{{ commands.run }} escala
```

Com isso será fornecida uma tabela no terminal informando essa escala:

| I | II | III | IV | V | VI | VII |
| - | -- | --- | -- | - | -- | --- |
| C | D  | E   | F  | G | A  | B   |

Um exemplo no terminal é:
