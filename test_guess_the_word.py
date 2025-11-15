import guess_the_word

def test_choose_word_from_list():
    """Ensure choose_word always returns a word from the list."""
    words = ["orange", "yellow", "purple"]
    for _ in range(20):
        assert guess_the_word.choose_word(words) in words


def test_reveal_letters_correct_guess():
    """Test that correct letters are revealed in the word."""
    word = "orange"
    hidden = "******"
    updated = guess_the_word.reveal_letters(word, hidden, "a")
    assert updated == "**a***"


def test_reveal_letters_incorrect_guess():
    """Test that incorrect letter guesses do not change the hidden word."""
    word = "orange"
    hidden = "******"
    updated = guess_the_word.reveal_letters(word, hidden, "z")
    assert updated == hidden


def test_is_correct_guess_true():
    """Full-word guess is correct."""
    assert guess_the_word.is_correct_guess("purple", "purple") is True


def test_is_correct_guess_false():
    """Full-word guess is incorrect."""
    assert guess_the_word.is_correct_guess("purple", "orange") is False
