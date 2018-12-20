from tile import Tile


def test_constructor():
    tile = Tile(3, 3, 0, 100)
    assert tile.column == 3
    assert tile.row == 3
    assert tile.color == 0
    assert tile.CW == 100
