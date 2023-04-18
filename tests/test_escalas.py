"""
AAA - Arrange - Act - Assert!
"""

from pytest import raises, mark
from musical_notes.escalas import ESCALAS, NOTAS, escala


def test_deve_funcionar_com_notas_minusculas():
    # Arrange
    tonica = 'c'
    tonalidade = 'maior'

    # Act
    result = escala(tonica, tonalidade)

    # Assert
    assert result


def test_deve_retornar_erro_dizendo_que_a_nota_nao_existe():
    tonica = 'X'
    tonalidade = 'maior'

    error_msg = f'Essa nota não existe, tente uma dessas {NOTAS}'
    with raises(ValueError) as error:
        escala(tonica, tonalidade)
        assert error_msg == error.value.args[0]


def test_deve_retornar_erro_dizendo_que_a_escala_nao_existe():
    tonica = 'C'
    tonalidade = 'tonalidade'

    error_msg = ('Essa escala não existe ou não foi implementada. '
                 f'Tenta uma dessas: {list(ESCALAS.keys())}')
    with raises(KeyError) as error:
        escala(tonica, tonalidade)

        assert error_msg == error.value.args[0]


@mark.parametrize(
        'tonica,tonalidade, esperado',
        [
            ('C', 'maior', ['C', 'D', 'E', 'F', 'G', 'A', 'B']),
            ('C#', 'maior', ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C']),
            ('F', 'maior', ['F', 'G', 'A', 'A#', 'C', 'D', 'E']),
            ('C', 'menor', ['C', 'D', 'D#', 'F', 'G', 'G#', 'A#']),
            ('C#', 'menor', ['C#', 'D#', 'E', 'F#', 'G#', 'A', 'B']),
            ('F', 'menor', ['F', 'G', 'G#', 'A#', 'C', 'C#', 'D#']),
            ]
)
def test_deve_retornar_as_notas_corretas(tonica, tonalidade, esperado):
    resultado = escala(tonica, tonalidade)
    assert resultado['notas'] == esperado


def test_deve_retornar_os_sete_graus():
    esperado = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']
    tonica = 'c'
    tonalidade = 'maior'
    resultado = escala(tonica, tonalidade)
    assert resultado['graus'] == esperado
