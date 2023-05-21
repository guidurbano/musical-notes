![project_logo](assets/logo.png){ width="400" .center }
# Musical notes

Musical Notes is a CLI tool to help with scales, chords, and harmonic fields.

The entire application is based on a `musical-notes` command. This command
has subcommands related to each action that the application can perform,
such as `scales`, `chords`, and `harmonic-field`.
{% include "templates/cards.html" %}


{% include "templates/instalacao.md" %}

## How to use it?
### Scale

You can call scales through command line. For example:

```bash
{{ commands.run }} scale
```

Retorning degrees and corresponding notes to the scale:
```
┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━┓
┃ I ┃ II ┃ III ┃ IV ┃ V ┃ VI ┃ VII ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━┩
│ C │ D  │ E   │ F  │ G │ A  │ B   │
└───┴────┴─────┴────┴───┴────┴─────┘
```

#### Tonic variation of the scale

The first parameter of the CLI is the scale's tonic. Therefore, you can change the scale returned. For example, the scale of `F#`:

```bash
{{ commands.run }} scale F#
```

```
┏━━━━┳━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ I  ┃ II ┃ III ┃ IV ┃ V  ┃ VI ┃ VII ┃
┡━━━━╇━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ F# │ G# │ A#  │ B  │ C# │ D# │ F   │
└────┴────┴─────┴────┴────┴────┴─────┘
```

#### Tonality variation of the scale

The second parameter of the CLI is tonality of the scale.
For example, the scale of `D#` major:

```bash
{{ commands.run }} scale D# major
```

```
┏━━━━┳━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ I  ┃ II ┃ III ┃ IV ┃ V  ┃ VI ┃ VII ┃
┡━━━━╇━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ D# │ F  │ G   │ G# │ A# │ C  │ D   │
└────┴────┴─────┴────┴────┴────┴─────┘
```

### Chords

```bash
{{ commands.run }} chord
┏━━━┳━━━━━┳━━━┓
┃ I ┃ III ┃ V ┃
┡━━━╇━━━━━╇━━━┩
│ C │ E   │ G │
└───┴─────┴───┘
```

### Variations in the chord

```bash
musical_notes chord C+
┏━━━┳━━━━━┳━━━━┓
┃ I ┃ III ┃ V+ ┃
┡━━━╇━━━━━╇━━━━┩
│ C │ E   │ G# │
└───┴─────┴────┘
```

So far, you can use major, minor, diminished, and augmented chords.

!!! warning "About the chords"
	It is possible that the chords you are looking for have not yet been implemented. At the time I am writing this tutorial, only triad chords have been implemented. Therefore, you can use major, minor, augmented, and diminished chords.

### Campo harmônico

You can call the harmonic field via the subcommand `harmonic-field`
For example,

```bash
musical_notes harmonic-field
┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━━┓
┃ I ┃ ii ┃ iii ┃ IV ┃ V ┃ vi ┃ vii° ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━━┩
│ C │ Dm │ Em  │ F  │ G │ Am │ B°   │
└───┴────┴─────┴────┴───┴────┴──────┘
```

By default, the parameters used are the tonic of `C` and the `major` harmonic field.

### Changes to the harmonic fields

You can change the tonic and tonality parameters.

```bash
musical_notes harmonic-field [TONIC] [TONALITY]
```

#### Variation of tonic

You can send the `tonic` of the harmonic field as the first parameter.
Such as the A major harmonic field:

```bash
musical_notes harmonic-field E
┏━━━┳━━━━━┳━━━━━┳━━━━┳━━━┳━━━━━┳━━━━━━┓
┃ I ┃ ii  ┃ iii ┃ IV ┃ V ┃ vi  ┃ vii° ┃
┡━━━╇━━━━━╇━━━━━╇━━━━╇━━━╇━━━━━╇━━━━━━┩
│ E │ F#m │ G#m │ A  │ B │ C#m │ D#°  │
└───┴─────┴─────┴────┴───┴─────┴──────┘
```

#### Change of tonality of the harmonic field

An example changing the harmonic field to E minor:

```bash
musical_notes harmonic-field E minor
┏━━━━┳━━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ i  ┃ ii° ┃ III ┃ iv ┃ v  ┃ VI ┃ VII ┃
┡━━━━╇━━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ Em │ F#° │ G   │ Am │ Bm │ C  │ D   │
└────┴─────┴─────┴────┴────┴────┴─────┘
```

## More information about the CLI

If you want to discover more utilities for the commands, you can use the
`--help` flag in all subcommands.

```bash
musical_notes --help

Usage: musical-notes [OPTIONS] COMMAND [ARGS]...
Commands  chord harmonic-field scale
```


```

 Usage: musical-notes scale [OPTIONS] [TONIC] [TONALITY]

  Arguments
   tonic          [TONIC]      Tonic of the scale [default:c]
   tonality      [TONALITY]  Tonality of the scale [default: major]
```

```

 Usage: musical-notes harmonic-field [OPTIONS] [TONIC] [TONALITY]

  Arguments
   tonic          [TONIC]      Tonic of the scale [default:c]
   tonality      [TONALITY]  Tonality of the scale [default: major]
```
