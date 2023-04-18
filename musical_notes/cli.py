from rich.console import Console
from rich.table import Table
from typer import Argument, Typer

from musical_notes.escalas import escala as _escala
from musical_notes.campo_harmonico import campo_harmonico as _campo_harmonico
from musical_notes.acordes import acorde as _acorde

console = Console()
app = Typer()


@app.command()
def escala(
    tonica: str = Argument('c', help='Tônica da escala'),
    tonalidade: str = Argument('maior', help='Tonalidade da escala'),
):
    table = Table()
    notas, graus = _escala(tonica, tonalidade).values()

    for grau in graus:
        table.add_column(grau)

    table.add_row(*notas)
    console.print(table)


@app.command()
def acorde(cifra: str = Argument('C', help='Cifra do acorde')):
    table = Table()
    notas, graus = _acorde(cifra).values()

    for grau in graus:
        table.add_column(grau)

    table.add_row(*notas)
    console.print(table)


@app.command()
def campo_harmonico(tonica: str = Argument('c',
                                           help='Tônica do campo harmonico'
                                           ),
                    tonalidade: str = Argument('maior',
                                               help='Tonalidade do campo')):
    table = Table()
    acordes, graus = _campo_harmonico(tonica, tonalidade).values()

    for grau in graus:
        table.add_column(grau)

    table.add_row(*acordes)
    console.print(table)
