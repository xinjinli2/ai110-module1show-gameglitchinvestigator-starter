from logic_utils import check_guess, parse_guess, get_range_for_difficulty, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

def test_parse_guess_valid():
    # Test that parse_guess accepts valid input within range
    ok, guess, err = parse_guess("50", min_value=1, max_value=100)
    assert ok
    assert guess == 50
    assert err is None

def test_parse_guess_invalid_number():
    # Test that parse_guess rejects non-numeric input
    ok, guess, err = parse_guess("abc", min_value=1, max_value=100)
    assert not ok
    assert err == "That is not a number."
    assert guess is None

def test_parse_guess_out_of_range():
    # Test that parse_guess rejects guesses outside the specified range
    ok, guess, err = parse_guess("150", min_value=1, max_value=100)
    assert not ok
    assert err == "Guess must be at most 100."
    assert guess is None

def test_get_range_for_difficulty_easy():
    # Test range for Easy difficulty
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20

def test_get_range_for_difficulty_normal():
    # Test range for Normal difficulty
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 100

def test_get_range_for_difficulty_hard():
    # Test range for Hard difficulty
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 1000

def test_update_score_win():
    # Test that score increases on win
    new_score = update_score(0, "Win", 1)
    assert new_score == 100

def test_update_score_wrong():
    # Test that score does not change on wrong guess
    new_score = update_score(0, "Too Low", 1)
    assert new_score == 0
