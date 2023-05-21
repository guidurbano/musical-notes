from musical_notes.scales import NOTES, scale


def _minor(chord):
    note, _ = chord.split('m')
    if '+' in chord:
        tonic, third, fifth = triad(note, 'minor')
        notes = [tonic, third, semitone(fifth, interval=1)]
        degrees = ['I', 'III-', 'V+']
    else:
        notes = triad(note, 'minor')
        degrees = ['I', 'III-', 'V']
    return notes, degrees


def semitone(note, interval):
    pos = NOTES.index(note) + interval
    return NOTES[pos % 12]


def triad(note, tonality):
    degrees = (0, 2, 4)
    scale_notes, _ = scale(note, tonality).values()
    return [scale_notes[degree] for degree in degrees]


def chord(chord: str) -> dict[str, list[str]]:
    """
    Generates the notes of a chord based on a chord symbol.

    Parameters:
        chord: A chord symbol.

    Returns:
        A dictionary with the corresponding notes and degrees in the major scale.

    Examples:
        >>> chord('C')
        {'notes': ['C', 'E', 'G'], 'degrees': ['I', 'III', 'V']}

        >>> chord('Cm')
        {'notes': ['C', 'D#', 'G'], 'degrees': ['I', 'III-', 'V']}

        >>> chord('C°')
        {'notes': ['C', 'D#', 'F#'], 'degrees': ['I', 'III-', 'V-']}

        >>> chord('C+')
        {'notes': ['C', 'E', 'G#'], 'degrees': ['I', 'III', 'V+']}

        >>> chord('Cm+')
        {'notes': ['C', 'D#', 'G#'], 'degrees': ['I', 'III-', 'V+']}
    """

    if 'm' in chord:
        notes, degrees = _minor(chord)
    elif '°' in chord:
        note, _ = chord.split('°')
        tonic, third, fifth = triad(note, 'minor')
        notes = [tonic, third, semitone(fifth, interval=-1)]
        degrees = ['I', 'III-', 'V-']
    elif '+' in chord:
        note, _ = chord.split('+')
        tonic, third, fifth = triad(note, 'major')
        notes = [tonic, third, semitone(fifth, interval=+1)]
        degrees = ['I', 'III', 'V+']
    else:
        notes = triad(chord, 'major')
        degrees = ['I', 'III', 'V']

    chord_data = {'notes': notes, 'degrees': degrees}

    return chord_data
