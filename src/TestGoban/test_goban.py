from goban import Goban, Status


def test_white_is_taken_when_surrounded_by_black():
    goban = Goban([
        '.#.',
        '#o#',
        '.#.',
    ])
    
    # added extra parameter: which color to check
    assert goban.is_taken(1, 1, Status.WHITE) is True

def test_white_is_not_taken_when_it_has_a_liberty():
    goban = Goban([
        '...',
        '#o#',
        '.#.',
    ])

    assert goban.is_taken(1, 1, Status.WHITE) is False

def test_black_shape_is_taken_when_surrounded():
    goban = Goban([
        'oo.',
        '##o',
        'o#o',
        '.o.',
    ])

    # added extra parameter: which color to check
    assert goban.is_taken(0, 1, Status.BLACK) is True
    assert goban.is_taken(1, 1, Status.BLACK) is True
    assert goban.is_taken(1, 2, Status.BLACK) is True

def test_black_shape_is_not_taken_when_it_has_a_liberty():
    goban = Goban([
        'oo.',
        '##.',
        'o#o',
        '.o.',
    ])

    # added extra parameter: which color to check
    assert goban.is_taken(0, 1, Status.BLACK) is False
    assert goban.is_taken(1, 1, Status.BLACK) is False
    assert goban.is_taken(1, 2, Status.BLACK) is False

def test_square_shape_is_taken():
    goban = Goban([
        'oo.',
        '##o',
        '##o',
        'oo.',
    ])

    # added extra parameter: which color to check
    assert goban.is_taken(0, 1, Status.BLACK) is True
    assert goban.is_taken(0, 2, Status.BLACK) is True
    assert goban.is_taken(1, 1, Status.BLACK) is True
    assert goban.is_taken(1, 2, Status.BLACK) is True

