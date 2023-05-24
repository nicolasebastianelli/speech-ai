from unittest.mock import Mock, PropertyMock

import pytest

from speechai.llm import Cohere


@pytest.fixture(name="cohere_api_key")
def fixture_cohere_api_key():
    return "mock-api-key"


@pytest.fixture(name="mock_cohere")
def fixture_mock_cohere(mocker):
    mock_cohere = mocker.patch("speechai.llm.cohere.cohere.Client", autospec=True)
    return mock_cohere


def test_cohere_llm_initialization(cohere_api_key, mock_cohere):
    Cohere(cohere_api_key)
    mock_cohere.assert_called_once_with(cohere_api_key)


def test_cohere_llm_generate_text(cohere_api_key, mock_cohere):
    cohere_llm = Cohere(cohere_api_key)

    prompt = "Hello"
    mock_generation = Mock()
    type(mock_generation).text = PropertyMock(return_value=" Hello, World! ")
    mock_response = Mock()
    type(mock_response).generations = PropertyMock(return_value=[mock_generation])

    mock_cohere.return_value.generate.return_value = mock_response

    assert cohere_llm.generate_text(prompt) == "Hello, World!"
    mock_cohere.return_value.generate.assert_called_once_with(
        model="command", prompt=prompt, max_tokens=200, temperature=0.750
    )
