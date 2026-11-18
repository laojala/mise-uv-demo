import pytest

from mise_uv_demo import count_characters, count_unique_words, count_words, main


@pytest.mark.parametrize(
    ("text", "words", "unique", "characters"),
    [
        ("", 0, 0, 0),
        (" \t\n", 0, 0, 3),
        ("mise and uv", 3, 3, 11),
        ("Hello hello HELLO", 3, 1, 17),
        ("hello hello!", 2, 2, 12),
        ("café CAFÉ", 2, 1, 9),
    ],
)
def test_counts(text, words, unique, characters):
    assert count_words(text) == words
    assert count_unique_words(text) == unique
    assert count_characters(text) == characters


@pytest.mark.parametrize("greeting", [None, "Hello from the test!"])
def test_main(monkeypatch, capsys, greeting):
    monkeypatch.delenv("APP_GREETING", raising=False)
    if greeting is not None:
        monkeypatch.setenv("APP_GREETING", greeting)
    main()
    assert capsys.readouterr().out == (
        f"{greeting or 'Hello!'}\n"
        'Text: "mise and uv make setup smooth"\n'
        "6 words, 6 unique words, 29 characters\n"
    )
