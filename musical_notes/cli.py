from rich.console import Console
from rich.table import Table
from typer import Argument, Typer

from musical_notes.scales import scale as _scale
from musical_notes.harmonic_field import harmonic_field as _harmonic_field
from musical_notes.chords import chord as _chord

console = Console()
app = Typer()


@app.command()
def scale(
    tonic: str = Argument('c', help='Tonic of the scale'),
    tonality: str = Argument('major', help='Tonality of the scale'),
):
    table = Table()
    notes, degrees = _scale(tonic, tonality).values()

    for degree in degrees:
        table.add_column(degree)

    table.add_row(*notes)
    console.print(table)


@app.command()
def chord(chord_symbol: str = Argument('C', help='Chord symbol')):
    table = Table()
    notes, degrees = _chord(chord_symbol).values()

    for degree in degrees:
        table.add_column(degree)

    table.add_row(*notes)
    console.print(table)


@app.command()
def harmonic_field(tonic: str = Argument('c',
                                         help='Tonic of the harmonic field'),
                   tonality: str = Argument('major',
                                            help='Tonality of the field')):
    table = Table()
    chords, degrees = _harmonic_field(tonic, tonality).values()

    for degree in degrees:
        table.add_column(degree)

    table.add_row(*chords)
    console.print(table)
