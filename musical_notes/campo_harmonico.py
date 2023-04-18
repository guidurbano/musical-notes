from musical_notes.escalas import escala
from musical_notes.acordes import triade


def _triade_na_escala(nota, notas_da_escala):
    """
    Saber se as notas de um acorde estão na escala.

    Examples:
        >>> _triade_na_escala('C', ['C', 'D', 'E', 'F', 'G', 'A', 'B'])
        'C'
        >>> _triade_na_escala('D', ['C', 'D', 'E', 'F', 'G', 'A', 'B'])
        'Dm'
        >>> _triade_na_escala('B', ['C', 'D', 'E', 'F', 'G', 'A', 'B'])
        'B°'
    """
    tonica, terca, quinta = triade(nota, 'maior')

    terca_in = terca in notas_da_escala
    quinta_in = quinta in notas_da_escala
    if terca_in & quinta_in:
        return tonica
    elif (not terca_in) & quinta_in:
        return f'{tonica}m'
    elif (not terca_in) & (not terca_in):
        return f'{tonica}°'


def _converte_graus(cifra, grau):
    """
    Converte o grau relativo a cifra.

    Parameters:
        cifra: Uma cifra de um acorde
        grau: Grau em forma maior

    Examples:
        >>> _converte_graus('C', 'I')
        'I'
        >>> _converte_graus('Cm', 'I')
        'i'
        >>> _converte_graus('C°', 'I')
        'i°'
    """

    if 'm' in cifra:
        return grau.lower()
    if '°' in cifra:
        return f'{grau.lower()}°'

    return grau


def campo_harmonico(tonica: str, tonalidade: str) -> dict[str, list[str]]:
    """
    Gera um campo harmônico com base em uma tônica e uma tonalidade

    Parameters:
        tonica: Primeiro grau do campo harmônico
        tonalidade: tonalidade para o campo. Ex: maior, menor, diminuto...

    Returns:
        Um campo harmônico

    Examples:
        >>> campo_harmonico('C', 'maior')
        {'acordes': ['C', 'Dm', 'Em', 'F', 'G', 'Am', 'B°'], 'graus': ['I', 'ii', 'iii', 'IV', 'V', 'vi', 'vii°']}

        >>> campo_harmonico('c', 'menor')
        {'acordes': ['Cm', 'D°', 'D#', 'Fm', 'Gm', 'G#', 'A#'], 'graus': ['i', 'ii°', 'III', 'iv', 'v', 'VI', 'VII']}
    """

    notas, _graus = escala(tonica, tonalidade).values()
    acordes = [_triade_na_escala(nota, notas) for nota in notas]
    graus = [
        _converte_graus(acorde, grau) for acorde, grau in zip(acordes, _graus)
        ]

    return {'acordes': acordes, 'graus': graus}