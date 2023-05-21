"""
AAA - Arrange - Act - Assert!
"""

from pytest import raises, mark
from musical_notes.scales import SCALES, NOTES, scale


def test_should_work_with_lowercase_notes():
    # Arrange
    tonic = 'c'
    tonality = 'major'

    # Act
    result = scale(tonic, tonality)

    # Assert
    assert result


def test_should_return_error_for_nonexistent_note():
    tonic = 'X'
    tonality = 'major'

    error_msg = f'This note does not exist, try one of these: {NOTES}'
    with raises(ValueError) as error:
        scale(tonic, tonality)
        assert error_msg == error.value.args[0]


def test_should_return_error_for_nonexistent_scale():
    tonic = 'C'
    tonality = 'tonality'

    error_msg = ('This scale does not exist or has not been implemented. '
                 f'Try one of these: {list(SCALES.keys())}')
    with raises(KeyError) as error:
        scale(tonic, tonality)

        assert error_msg == error.value.args[0]


@mark.parametrize(
        'tonic, tonality, expected',
        [
            ('C', 'major', ['C', 'D', 'E', 'F', 'G', 'A', 'B']),
            ('C#', 'major', ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C']),
            ('F', 'major', ['F', 'G', 'A', 'A#', 'C', 'D', 'E']),
            ('C', 'minor', ['C', 'D', 'D#', 'F', 'G', 'G#', 'A#']),
            ('C#', 'minor', ['C#', 'D#', 'E', 'F#', 'G#', 'A', 'B']),
            ('F', 'minor', ['F', 'G', 'G#', 'A#', 'C', 'C#', 'D#']),
        ]
)
def test_should_return_correct_notes(tonic, tonality, expected):
    result = scale(tonic, tonality)
    assert result['notes'] == expected


def test_should_return_seven_degrees():
    expected = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']
    tonic = 'c'
    tonality = 'major'
    result = scale(tonic, tonality)
    assert result['degrees'] == expected
