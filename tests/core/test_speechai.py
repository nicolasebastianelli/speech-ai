from unittest.mock import Mock

import pytest

from speechai import SpeechAI
from speechai.llm import AbstractLLM
from speechai.tts import AbstractTTS


@pytest.fixture(name="mock_llm")
def fixture_mock_llm():
    return Mock(spec=AbstractLLM)


@pytest.fixture(name="mock_tts")
def fixture_mock_tts():
    return Mock(spec=AbstractTTS)


@pytest.fixture(name="mock_create_directory_from_path")
def fixture_mock_create_directory_from_path(mocker):
    return mocker.patch("speechai.core.speechai.create_directory_from_path", autospec=True)


@pytest.fixture(name="speech_ai")
def fixture_speech_ai(mock_llm, mock_tts):
    return SpeechAI(mock_llm, mock_tts)


def test_speech_ai_initialization(speech_ai, mock_llm, mock_tts):
    assert speech_ai.get_llm() == mock_llm
    assert speech_ai.get_tts() == mock_tts


def test_speech_ai_synthesize_dialog(speech_ai, mock_create_directory_from_path):
    prompt = "Hello"
    save_to = "/path/to/save"
    text = "Generated Text"
    audio = b"Audio Bytes"

    speech_ai.get_llm().generate_text.return_value = text
    speech_ai.get_tts().text_to_speech.return_value = audio

    assert speech_ai.synthesize_dialog(prompt, save_to) == [text, audio]
    mock_create_directory_from_path.assert_called_once_with(save_to)
    speech_ai.get_llm().generate_text.assert_called_once_with(prompt)
    speech_ai.get_tts().text_to_speech.assert_called_once_with(text, save_to)


def test_speech_ai_set_llm(speech_ai):
    new_llm = Mock(spec=AbstractLLM)
    speech_ai.set_llm(new_llm)
    assert speech_ai.get_llm() == new_llm


def test_speech_ai_set_tts(speech_ai):
    new_tts = Mock(spec=AbstractTTS)
    speech_ai.set_tts(new_tts)
    assert speech_ai.get_tts() == new_tts


def test_speech_ai_set_language(speech_ai, mock_tts):
    language_code = "en"
    speech_ai.set_language(language_code)
    mock_tts.set_language.assert_called_once_with(language_code)
