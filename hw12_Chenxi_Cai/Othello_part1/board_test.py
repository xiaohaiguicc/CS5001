from board import Board


def test_constructor():
    board = Board(6, 6, 80)
    assert board.TC == 6
    assert board.TR == 6
    assert board.CW == 80
