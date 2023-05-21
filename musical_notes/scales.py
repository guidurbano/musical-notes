"""
Module for musical scales.

Attributes:
    SCALES: Scales implemented using integer notation
    NOTES: Musical notes

# SCALES
The scales are implemented in a constant called `SCALES`.
If you want to see all the implemented scales, you can use:

```python title="Interactive Shell"
>>> from musical_notes.scales import SCALES
>>> SCALES
{'major': (0, 2, 4, 5, 7, 9, 11), 'minor': (0, 2, 3, 5, 7, 8, 10)}

```

The integer notation for the scales was taken from the Wikipedia page.

# Notes
"""

NOTES = 'C C# D D# E F F# G G# A A# B'.split()
SCALES = {
    'major': (0, 2, 4, 5, 7, 9, 11),
    'minor': (0, 2, 3, 5, 7, 8, 10)
}


def scale(tonic: str,
          tonality: str,
          ) -> dict[str, list[str]]:
    """
    Generates a scale based on a tonic and a tonality.

    Parameters:
    tonic: The note that will be the tonic of the scale
    tonality: The tonality of the scale

    Returns:
        A dictionary with the notes of the scale and their degrees

    Raises:
        ValueError: If the tonic is not a valid note
        KeyError: If the scale does not exist or has not been implemented.

    Examples:
        >>> scale('C', 'major')
        {'notes': ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'degrees': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}

        >>> scale('A', 'minor')
        {'notes': ['A', 'B', 'C', 'D', 'E', 'F', 'G'], 'degrees': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
    """
    tonic = tonic.upper()

    try:
        intervals = SCALES[tonality]
        tonic_pos = NOTES.index(tonic)
    except ValueError:
        raise ValueError(
            f'This note does not exist. Please try one of these: {NOTES}')
    except KeyError:
        raise KeyError(
            'This scale does not exist or has not been implemented. '
            f'Try one of these: {list(SCALES.keys())}')

    temp = []
    for interval in intervals:
        note = (tonic_pos + interval) % 12
        temp.append(NOTES[note])

    return {'notes': temp,
            'degrees': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
