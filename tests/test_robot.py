from mars_rover.robot import Robot


def test_output():
    walle = Robot(x=1, y=1, orientation="N", xmax=20, ymax=20)
    result = walle.output()
    assert result == "(1, 1, N)"


def test_tick_basic_forward():
    walle = Robot(x=1, y=1, orientation="N", xmax=20, ymax=20)

    walle.tick("F")
    result = walle.output()
    assert result == "(1, 2, N)"

    walle.tick("F")
    walle.tick("F")
    walle.tick("F")
    walle.tick("F")
    result = walle.output()
    assert result == "(1, 6, N)"


def test_tick_basic_turn():
    walle = Robot(x=1, y=1, orientation="N", xmax=20, ymax=20)

    walle.tick("R")
    result = walle.output()
    assert result == "(1, 1, E)"

    walle.tick("R")
    result = walle.output()
    assert result == "(1, 1, S)"

    walle.tick("R")
    result = walle.output()
    assert result == "(1, 1, W)"

    walle.tick("R")
    result = walle.output()
    assert result == "(1, 1, N)"

    walle.tick("R")
    result = walle.output()
    assert result == "(1, 1, E)"

    walle.tick("L")
    result = walle.output()
    assert result == "(1, 1, N)"

    walle.tick("L")
    result = walle.output()
    assert result == "(1, 1, W)"

    walle.tick("L")
    result = walle.output()
    assert result == "(1, 1, S)"

    walle.tick("L")
    result = walle.output()
    assert result == "(1, 1, E)"

    walle.tick("L")
    result = walle.output()
    assert result == "(1, 1, N)"


def test_tick_invalid_character():
    walle = Robot(x=1, y=1, orientation="N", xmax=20, ymax=20)

    walle.tick("Q")
    walle.tick("r")
    walle.tick("l")
    walle.tick("4")
    walle.tick("#")
    result = walle.output()
    assert result == "(1, 1, N)"


def test_tick_turn_andtick():
    walle = Robot(x=1, y=1, orientation="N", xmax=20, ymax=20)

    walle.tick("R")
    walle.tick("F")

    result = walle.output()
    assert result == "(2, 1, E)"


def test_records_lost():
    walle = Robot(x=1, y=1, orientation="N", xmax=2, ymax=2)

    walle.tick("F")
    walle.tick("F")
    walle.tick("F")
    walle.tick("F")  # keep going way off grid

    result = walle.output()
    assert result == "(1, 2, N) LOST"
