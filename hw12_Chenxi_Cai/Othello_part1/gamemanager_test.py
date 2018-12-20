from gamemanager import GameManager


def test_constructor():
    game = GameManager(6, 6, 80)
    assert game.TC == 6
    assert game.TR == 6
    assert game.CW == 80
    assert game.turn == 0
    assert game.end is False


def test_player_make_move():
    game = GameManager(6, 6, 80)
    # test case that has legal move
    game.player_make_move(200, 100)
    assert game.tiles_list[2][1].color == game.BLACK
    assert game.tiles_list[2][2].color == game.BLACK
    assert game.turn == 1
    # test case that no legal move
    game = GameManager(2, 2, 80)
    game.player_make_move(70, 70)
    assert game.turn == 1


def test_computer_make_move():
    # test case that no legal move
    game = GameManager(2, 2, 80)
    game.turn = 1
    game.computer_make_move()
    assert game.turn == 0
    # test case that has legal move
    game = GameManager(6, 6, 80)
    game.turn = 1
    game.computer_make_move()
    assert game.tiles_list[1][3].color == game.WHITE
    assert game.tiles_list[2][3].color == game.WHITE
    assert game.turn == 0
