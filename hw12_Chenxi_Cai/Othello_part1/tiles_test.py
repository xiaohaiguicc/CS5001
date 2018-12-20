from tiles import Tiles


def test_constructor():
    tiles = Tiles(6, 6, 80)
    assert tiles.TC == 6
    assert tiles.TR == 6
    assert tiles.CW == 80
    for col in range(tiles.TC):
        for row in range(tiles.TR):
            if col == tiles.TC // 2 - 1 and row == tiles.TR // 2 - 1:
                tiles.tiles_list[col][row].color == tiles.WHITE
            elif col == tiles.TC // 2 and row == tiles.TR // 2:
                tiles.tiles_list[col][row].color == tiles.WHITE
            elif col == tiles.TC // 2 and row == tiles.TR // 2 - 1:
                tiles.tiles_list[col][row].color == tiles.BLACK
            elif col == tiles.TC // 2 - 1 and row == tiles.TR // 2:
                tiles.tiles_list[col][row].color == tiles.BLACK
            else:
                tiles.tiles_list[col][row] == 0


def test_islgeal():
    tiles = Tiles(6, 6, 80)
    # 1. black tile with count
    legal = tiles.islegal(2, 2, "BLACK", "count")
    assert legal is False and tiles.flip_count == 0
    legal = tiles.islegal(3, 2, "BLACK", "count")
    assert legal is False and tiles.flip_count == 0
    legal = tiles.islegal(2, 3, "BLACK", "count")
    assert legal is False and tiles.flip_count == 0
    legal = tiles.islegal(3, 3, "BLACK", "count")
    assert legal is False and tiles.flip_count == 0
    # case 1
    legal = tiles.islegal(2, 4, "BLACK", "count")
    assert legal is False and tiles.flip_count == 0
    legal = tiles.islegal(3, 4, "BLACK", "count")
    assert legal is True and tiles.flip_count == 1
    # case 2
    tiles.flip_count = 0
    legal = tiles.islegal(3, 1, "BLACK", "count")
    assert legal is False and tiles.flip_count == 0
    legal = tiles.islegal(2, 1, "BLACK", "count")
    assert legal is True and tiles.flip_count == 1
    # case 3
    tiles.flip_count = 0
    legal = tiles.islegal(1, 3, "BLACK", "count")
    assert legal is False and tiles.flip_count == 0
    legal = tiles.islegal(1, 2, "BLACK", "count")
    assert legal is True and tiles.flip_count == 1
    # case 4
    tiles.flip_count = 0
    legal = tiles.islegal(4, 2, "BLACK", "count")
    assert legal is False and tiles.flip_count == 0
    legal = tiles.islegal(4, 3, "BLACK", "count")
    assert legal is True and tiles.flip_count == 1
    # case 5
    tiles.flip_count = 0
    legal = tiles.islegal(1, 1, "BLACK", "count")
    assert legal is False and tiles.flip_count == 0
    # case 6
    legal = tiles.islegal(4, 4, "BLACK", "count")
    assert legal is False and tiles.flip_count == 0
    # case 7
    legal = tiles.islegal(4, 1, "BLACK", "count")
    assert legal is False and tiles.flip_count == 0
    # case 8
    legal = tiles.islegal(1, 4, "BLACK", "count")
    assert legal is False and tiles.flip_count == 0
    # 2. black tile with flip
    # case 1
    tiles = Tiles(6, 6, 80)
    legal = tiles.islegal(3, 4, "BLACK", "flip")
    assert legal is True and tiles.tiles_list[3][3].color == tiles.BLACK
    # case 5
    legal = tiles.islegal(1, 1, "BLACK", "flip")
    assert legal is True and tiles.tiles_list[2][2].color == tiles.BLACK
    # case 2
    tiles = Tiles(6, 6, 80)
    legal = tiles.islegal(2, 1, "BLACK", "flip")
    assert legal is True and tiles.tiles_list[2][2].color == tiles.BLACK
    # case 7
    legal = tiles.islegal(1, 3, "WHITE", "flip")
    legal = tiles.islegal(1, 4, "BLACK", "flip")
    assert legal is True and tiles.tiles_list[2][3].color == tiles.BLACK
    # case 3
    tiles = Tiles(6, 6, 80)
    legal = tiles.islegal(1, 2, "BLACK", "flip")
    assert legal is True and tiles.tiles_list[2][2].color == tiles.BLACK
    # case 8
    legal = tiles.islegal(1, 3, "WHITE", "flip")
    legal = tiles.islegal(4, 1, "WHITE", "flip")
    assert legal is True and tiles.tiles_list[3][2].color == tiles.WHITE
    # case 4
    tiles = Tiles(6, 6, 80)
    legal = tiles.islegal(4, 3, "BLACK", "flip")
    assert legal is True and tiles.tiles_list[3][3].color == tiles.BLACK
    # case 6
    legal = tiles.islegal(4, 4, "WHITE", "flip")
    assert legal is True and tiles.tiles_list[3][3].color == tiles.WHITE


def test_flipping():
    tiles = Tiles(6, 6, 80)
    # "col"
    tiles.flipping(2, 3, "col", tiles.BLACK, 2)
    assert tiles.tiles_list[2][2].color == tiles.BLACK
    # "row"
    tiles.flipping(3, 4, "row", tiles.BLACK, 3)
    assert tiles.tiles_list[3][3].color == tiles.BLACK
    # "leftdiag"
    tiles.flipping(1, 3, "leftdiag", tiles.WHITE, 1, 1)
    assert tiles.tiles_list[2][2].color == tiles.WHITE
    assert tiles.tiles_list[3][3].color == tiles.WHITE
    # "rightdiag"
    tiles.flipping(1, 3, "rightdiag", tiles.WHITE, 1, 4)
    assert tiles.tiles_list[2][3].color == tiles.WHITE
    assert tiles.tiles_list[3][2].color == tiles.WHITE


def test_nolegal():
    tiles = Tiles(2, 2, 80)
    assert tiles.nolegal("BLACK") is True
    assert tiles.nolegal("WHITE") is True
    tiles = Tiles(6, 6, 80)
    assert tiles.nolegal("BLACK") is False
    assert tiles.nolegal("WHITE") is False


def test_computer_flip():
    tiles = Tiles(6, 6, 80)
    tiles.computer_flip()
    assert tiles.flip_count == 0
