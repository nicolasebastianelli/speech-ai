from unittest.mock import Mock, PropertyMock

import pytest

from speechai.llm import OpenAI


@pytest.fixture(name="openai_api_key")
def fixture_openai_api_key():
    return "mock-api-key"


@pytest.fixture(name="mock_openai")
def fixture_mock_openai(mocker):
    mock_openai = mocker.patch("speechai.llm.openai.openai", autospec=True)
    return mock_openai


def test_openai_llm_initialization(openai_api_key, mock_openai):
    OpenAI(openai_api_key)
    assert mock_openai.api_key == openai_api_key


def test_openai_llm_generate_text(openai_api_key, mock_openai):
    openai_llm = OpenAI(openai_api_key)

    prompt = "Hello"
    mock_choice = Mock()
    type(mock_choice).text = PropertyMock(return_value=" Hello, World! ")
    mock_response = Mock()
    type(mock_response).choices = PropertyMock(return_value=[mock_choice])

    mock_openai.Completion.create.return_value = mock_response

    assert openai_llm.generate_text(prompt) == "Hello, World!"
    mock_openai.Completion.create.assert_called_once_with(engine="text-davinci-003", prompt=prompt, max_tokens=100)
