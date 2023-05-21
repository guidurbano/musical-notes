from musical_notes.scales import scale
from musical_notes.chords import triad


def _triad_in_scale(note, scale_notes):
    """
    Checks if the notes of a chord are in the scale.

    Examples:
        >>> _triad_in_scale('C', ['C', 'D', 'E', 'F', 'G', 'A', 'B'])
        'C'
        >>> _triad_in_scale('D', ['C', 'D', 'E', 'F', 'G', 'A', 'B'])
        'Dm'
        >>> _triad_in_scale('B', ['C', 'D', 'E', 'F', 'G', 'A', 'B'])
        'B°'
    """
    tonic, third, fifth = triad(note, 'major')

    third_in = third in scale_notes
    fifth_in = fifth in scale_notes

    if third_in and fifth_in:
        return tonic
    elif (not third_in) and fifth_in:
        return f'{tonic}m'
    elif (not third_in) and (not third_in):
        return f'{tonic}°'


def _convert_degrees(chord, degree):
    """
    Converts the degree relative to the chord.

    Parameters:
        chord: A chord symbol.
        degree: Degree in uppercase form.

    Examples:
        >>> _convert_degrees('C', 'I')
        'I'
        >>> _convert_degrees('Cm', 'I')
        'i'
        >>> _convert_degrees('C°', 'I')
        'i°'
    """

    if 'm' in chord:
        return degree.lower()
    if '°' in chord:
        return f'{degree.lower()}°'

    return degree


def harmonic_field(tonic: str, tonality: str) -> dict[str, list[str]]:
    """
    Generates a harmonic field based on a tonic and tonality.

    Parameters:
        tonic: The tonic of the harmonic field.
        tonality: The tonality for the field, e.g., major, minor, diminished...

    Returns:
        A harmonic field.

    Examples:
        >>> harmonic_field('C', 'major')
        {'chords': ['C', 'Dm', 'Em', 'F', 'G', 'Am', 'B°'], 'degrees': ['I', 'ii', 'iii', 'IV', 'V', 'vi', 'vii°']}

        >>> harmonic_field('c', 'minor')
        {'chords': ['Cm', 'D°', 'D#', 'Fm', 'Gm', 'G#', 'A#'], 'degrees': ['i', 'ii°', 'III', 'iv', 'v', 'VI', 'VII']}
    """

    notes, _degrees = scale(tonic, tonality).values()
    chords = [_triad_in_scale(note, notes) for note in notes]
    degrees = [
        _convert_degrees(chord, degree) for chord, degree in zip(chords, _degrees)
    ]

    return {'chords': chords, 'degrees': degrees}
