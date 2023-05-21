from pytest import mark
from musical_notes.chords import chord

"""
{'notes': ['C', 'E', 'G'], 'degrees': ['I', 'III', 'V']}
"""


@mark.parametrize(
        'note, expected',
        [
            ('C', ['C', 'E', 'G']),
            ('Cm', ['C', 'D#', 'G']),
            ('C°', ['C', 'D#', 'F#']),
            ('C+', ['C', 'E', 'G#']),
            ('Cm+', ['C', 'D#', 'G#']),
            ('F#', ['F#', 'A#', 'C#']),
        ],
)
def test_chord_should_return_corresponding_notes(note, expected):
    notes, _ = chord(note).values()

    assert expected == notes


@mark.parametrize(
        'chord_symbol, expected',
        [
            ('C', ['I', 'III', 'V']),
            ('Cm', ['I', 'III-', 'V']),
            ('C°', ['I', 'III-', 'V-']),
            ('C+', ['I', 'III', 'V+']),
            ('Cm+', ['I', 'III-', 'V+']),
        ],
)
def test_chord_should_return_corresponding_degrees(chord_symbol, expected):
    _, degrees = chord(chord_symbol).values()

    assert expected == degrees
