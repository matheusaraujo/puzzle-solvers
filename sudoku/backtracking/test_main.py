from main import solve, Matrix


def test_sample_easy():
    input: Matrix = [
        [0, 3, 2, 0, 5, 6, 8, 9, 1],
        [6, 4, 8, 1, 0, 2, 3, 0, 7],
        [5, 9, 1, 7, 3, 8, 0, 4, 0],
        [9, 8, 0, 6, 2, 3, 7, 1, 4],
        [3, 6, 4, 9, 7, 1, 5, 2, 8],
        [1, 2, 0, 8, 0, 5, 0, 6, 3],
        [2, 7, 0, 0, 6, 4, 1, 8, 5],
        [4, 1, 3, 5, 8, 9, 0, 7, 0],
        [0, 0, 0, 0, 0, 7, 4, 3, 9]
    ]

    output = solve(input)

    expected_output: Matrix = [[
        7, 3, 2, 4, 5, 6, 8, 9, 1],
        [6, 4, 8, 1, 9, 2, 3, 5, 7],
        [5, 9, 1, 7, 3, 8, 2, 4, 6],
        [9, 8, 5, 6, 2, 3, 7, 1, 4],
        [3, 6, 4, 9, 7, 1, 5, 2, 8],
        [1, 2, 7, 8, 4, 5, 9, 6, 3],
        [2, 7, 9, 3, 6, 4, 1, 8, 5],
        [4, 1, 3, 5, 8, 9, 6, 7, 2],
        [8, 5, 6, 2, 1, 7, 4, 3, 9]
    ]

    assert output == expected_output


def test_sample_medium():
    input: Matrix = [
        [7, 5, 2, 8, 4, 3, 9, 1, 6],
        [6, 3, 8, 1, 5, 9, 7, 4, 2],
        [1, 9, 4, 7, 6, 2, 3, 5, 8],
        [0, 0, 0, 0, 2, 1, 4, 7, 0],
        [2, 7, 0, 0, 0, 4, 8, 0, 1],
        [4, 0, 0, 0, 8, 7, 2, 3, 0],
        [0, 2, 0, 4, 0, 8, 6, 9, 0],
        [0, 0, 0, 0, 0, 6, 5, 2, 0],
        [0, 0, 0, 2, 0, 5, 1, 8, 0],
    ]

    output = solve(input)

    expected_output: Matrix = [
        [7, 5, 2, 8, 4, 3, 9, 1, 6],
        [6, 3, 8, 1, 5, 9, 7, 4, 2],
        [1, 9, 4, 7, 6, 2, 3, 5, 8],
        [3, 8, 5, 6, 2, 1, 4, 7, 9],
        [2, 7, 9, 5, 3, 4, 8, 6, 1],
        [4, 1, 6, 9, 8, 7, 2, 3, 5],
        [5, 2, 7, 4, 1, 8, 6, 9, 3],
        [8, 4, 1, 3, 9, 6, 5, 2, 7],
        [9, 6, 3, 2, 7, 5, 1, 8, 4]
    ]

    assert output == expected_output


def test_sample_hard():
    input: Matrix = [
        [3, 7, 9, 0, 5, 0, 0, 0, 0],
        [4, 8, 6, 2, 0, 0, 3, 7, 5],
        [1, 5, 2, 3, 6, 7, 0, 0, 0],
        [5, 2, 4, 0, 0, 0, 0, 9, 3],
        [7, 6, 8, 0, 3, 0, 5, 0, 0],
        [9, 1, 3, 0, 2, 0, 7, 0, 0],
        [6, 4, 0, 0, 0, 0, 0, 3, 0],
        [2, 9, 1, 0, 8, 3, 0, 5, 0],
        [8, 3, 0, 0, 4, 0, 0, 0, 0],
    ]

    output = solve(input)

    expected_output: Matrix = [
        [3, 7, 9, 4, 5, 8, 1, 2, 6],
        [4, 8, 6, 2, 1, 9, 3, 7, 5],
        [1, 5, 2, 3, 6, 7, 8, 4, 9],
        [5, 2, 4, 8, 7, 1, 6, 9, 3],
        [7, 6, 8, 9, 3, 4, 5, 1, 2],
        [9, 1, 3, 5, 2, 6, 7, 8, 4],
        [6, 4, 7, 1, 9, 5, 2, 3, 8],
        [2, 9, 1, 6, 8, 3, 4, 5, 7],
        [8, 3, 5, 7, 4, 2, 9, 6, 1]
    ]

    assert output == expected_output
