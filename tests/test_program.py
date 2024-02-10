from mars_rover.program import run_program


def test_example_1():

    input = iter(["4 8", "(2, 3, E) LFRFF", "(0, 2, N) FFLFRFF"])

    result = run_program(input)
    assert result == [
        "(4, 4, E)",
        "(0, 4, W) LOST",
    ]


def test_example_2():

    input = iter(["4 8", "(2, 3, N) FLLFR", "(1, 0, S) FFRLF"])

    result = run_program(input)
    assert result == ["(2, 3, W)", "(1, 0, S) LOST"]


def test_example_big_grid():

    input = iter(
        [
            "100 100",
            "(50, 50, N) FLLFRFFRLFFFRLFFFRLFFFRLF",
            "(2, 50, N) FLLFRFFRLFFFRLFFFRLFFFRLF",
            "(99, 99, S) FFFFFFFFFFFFFFFFFRFFFFFFFFFFRFFFLFFFFFFFFFFFFFFFFFFF",
        ]
    )

    result = run_program(input)
    assert result == ["(38, 50, W)", "(0, 50, W) LOST", "(70, 85, W)"]


def test_no_input_spacing():

    input = iter(["4 8", "(2,3,E)LFRFF", "(0,2,N)FFLFRFF"])

    result = run_program(input)
    assert result == [
        "(4, 4, E)",
        "(0, 4, W) LOST",
    ]
