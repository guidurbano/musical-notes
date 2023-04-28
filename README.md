<img src="https://musical-notes-docs.readthedocs.io/en/latest/assets/logo.png" width="200">

# Musical Notes
[![Documentation Status](https://readthedocs.org/projects/musical-notes-docs/badge/?version=latest)](https://musical-notes-docs.readthedocs.io/en/latest/?badge=latest)
[![codecov](https://codecov.io/gh/guidurbano/musical-notes/branch/main/graph/badge.svg?token=VC19SV2A1M)](https://codecov.io/gh/guidurbano/musical-notes)
![CI](https://github.com/guidurbano/musical-notes/actions/workflows/pipeline.yml/badge.svg)


Notas musicais é um CLI para ajudar na formação de escalas, acordes e campos
harmônicos.

Toda aplicação é baseada em um comando `musical-notes`. Esse comando
tem um subcomando relacionado a cada ação que a aplicação pode realizar.
Como `escalas`, `acordes` e `campo-harmonico`.

## Instalação

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

## Como usar?

### Escalas

Você pode chamar as escalas via linha de comando. Por exemplo:

```bash
musical_notes escala
```

Retornando os graus e as notas correspondentes a essa escala:
```
┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━┓
┃ I ┃ II ┃ III ┃ IV ┃ V ┃ VI ┃ VII ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━┩
│ C │ D  │ E   │ F  │ G │ A  │ B   │
└───┴────┴─────┴────┴───┴────┴─────┘
```

#### Alteração na tônica da escala

O primeiro parâmetro do CLI é a tônica da escala que deseja exibir. Desta forma,
você pode alterar a escala retornada. Por exemplo, a escala de `F#`:

```bash
musical_notes escalas F#
```

```
┏━━━━┳━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ I  ┃ II ┃ III ┃ IV ┃ V  ┃ VI ┃ VII ┃
┡━━━━╇━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ F# │ G# │ A#  │ B  │ C# │ D# │ F   │
└────┴────┴─────┴────┴────┴────┴─────┘
```

#### Alteração na tonalidade da escala

O segundo parâmetro do CLI é a tonalidade da escala.
Por exemplo, a escala de `D#` maior:

```bash
musical_notes escalas D# maior
```

```
┏━━━━┳━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ I  ┃ II ┃ III ┃ IV ┃ V  ┃ VI ┃ VII ┃
┡━━━━╇━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ D# │ F  │ G   │ G# │ A# │ C  │ D   │
└────┴────┴─────┴────┴────┴────┴─────┘
```

### Acordes

Uso básica

```bash
musical_notes acorde
┏━━━┳━━━━━┳━━━┓
┃ I ┃ III ┃ V ┃
┡━━━╇━━━━━╇━━━┩
│ C │ E   │ G │
└───┴─────┴───┘
```

### Variações na cifra

```bash
musical_notes acorde C+
┏━━━┳━━━━━┳━━━━┓
┃ I ┃ III ┃ V+ ┃
┡━━━╇━━━━━╇━━━━┩
│ C │ E   │ G# │
└───┴─────┴────┘
```

Até o momento você pode usar acordes maiores, menores, diminuto e aumentados.

!!! info "Sobre os acordes"
    Pode ser que os acordes que você busque ainda não tenham sido implementados.
    No momento, somente acordes com tríades foram implementados

### Campo harmônico

Você pode chamr os campos harmônicos via o subcomando `campo-harmonico`. Por
exemplo,

```bash
musical_notes campo-harmonico
┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━━┓
┃ I ┃ ii ┃ iii ┃ IV ┃ V ┃ vi ┃ vii° ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━━┩
│ C │ Dm │ Em  │ F  │ G │ Am │ B°   │
└───┴────┴─────┴────┴───┴────┴──────┘
```

Por padrão os parâmetros utilizados são a tônica de `C` e o campo harmônico `maior`

### Alteração nos campos harmônicos

Você pode alterar os parâmetros da tônica e da tonalidade.

```bash
musical_notes campo-harmonico [TONICA] [TONALIDADE]
```

#### Alteração na tônica do campo harmônico

Um exemplo com o campo harmônico de E:

```bash
musical_notes campo-harmonico E
┏━━━┳━━━━━┳━━━━━┳━━━━┳━━━┳━━━━━┳━━━━━━┓
┃ I ┃ ii  ┃ iii ┃ IV ┃ V ┃ vi  ┃ vii° ┃
┡━━━╇━━━━━╇━━━━━╇━━━━╇━━━╇━━━━━╇━━━━━━┩
│ E │ F#m │ G#m │ A  │ B │ C#m │ D#°  │
└───┴─────┴─────┴────┴───┴─────┴──────┘
```

#### Alteração da tonalidade do campo harmônico

Um exemplo mudando o campo harmônico para menor de E:

```bash
musical_notes campo-harmonico E menor
┏━━━━┳━━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ i  ┃ ii° ┃ III ┃ iv ┃ v  ┃ VI ┃ VII ┃
┡━━━━╇━━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ Em │ F#° │ G   │ Am │ Bm │ C  │ D   │
└────┴─────┴─────┴────┴────┴────┴─────┘
```

## Mais informações sobre o CLI

Para descobrir outras opções, você pode usar a flag `--help`

```bash
musical_notes --help

Usage: musical-notes [OPTIONS] COMMAND [ARGS]...
Commands  acorde campo-harmonico escala
```


```

 Usage: musical-notes escalas [OPTIONS] [TONICA] [TONALIDADE]

  Arguments
   tonica          [TONICA]      Tônica da escala [default:c]
   tonalidade      [TONALIDADE]  Tonalidade da escala [default: maior]
```

```

 Usage: musical-notes campo-harmonico [OPTIONS] [TONICA] [TONALIDADE]

  Arguments
   tonica          [TONICA]      Tônica do campo harmonico [default:c]
   tonalidade      [TONALIDADE]  Tonalidade do campo [default: maior]
```
