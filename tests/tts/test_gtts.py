from unittest.mock import Mock

import pytest
from gtts.tokenizer.pre_processors import abbreviations, end_of_line

from speechai.tts.gtts import GTTS


@pytest.fixture(name="mock_gtts")
def fixture_mock_gtts(mocker):
    return mocker.patch("speechai.tts.gtts.gTTS", autospec=True)


def test_gtts_initialization():
    gtts = GTTS()
    assert gtts.get_language() == "en"


def test_gtts_text_to_speech(mock_gtts):
    gtts = GTTS()

    text = "Hello"
    save_to = "/path/to/save"
    mock_tts_instance = Mock()
    mock_gtts.return_value = mock_tts_instance

    assert gtts.text_to_speech(text, save_to) == save_to
    mock_gtts.assert_called_once_with(text, lang=gtts.get_language(), pre_processor_funcs=[abbreviations, end_of_line])
    mock_tts_instance.save.assert_called_once_with(save_to)


def test_gtts_set_language():
    gtts = GTTS()
    language_code = "es"
    gtts.set_language(language_code)
    assert gtts.get_language() == language_code
