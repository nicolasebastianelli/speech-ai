import pytest

from speechai.utils import create_directory_from_path


@pytest.fixture(name="mock_os")
def fixture_mock_os(mocker):
    mock = mocker.patch("speechai.utils.directory.os", autospec=True)
    return mock


@pytest.fixture(name="mock_logger")
def fixture_mock_logger(mocker):
    return mocker.patch("speechai.utils.directory.logger", autospec=True)


def test_create_directory_from_path_existing_directory(mock_os, mock_logger):
    mock_os.path.dirname.return_value = "/existing/directory"
    mock_os.path.exists.return_value = True

    create_directory_from_path("/existing/directory/file.txt")

    mock_logger.info.assert_not_called()
    mock_os.makedirs.assert_not_called()


def test_create_directory_from_path_new_directory(mock_os, mock_logger):
    mock_os.path.dirname.return_value = "/new/directory"
    mock_os.path.exists.return_value = False

    create_directory_from_path("/new/directory/file.txt")

    mock_logger.info.assert_called_once_with("Directory '%s' created.", "/new/directory")
    mock_os.makedirs.assert_called_once_with("/new/directory")


def test_create_directory_from_path_os_error(mock_os, mock_logger):
    mock_os.path.dirname.return_value = "/new/directory"
    mock_os.path.exists.return_value = False
    mock_os.makedirs.side_effect = OSError("Test error")

    create_directory_from_path("/new/directory/file.txt")

    mock_logger.error.assert_called_once_with(
        "An error occurred while creating directory. Error details: %s", mock_os.makedirs.side_effect
    )
    mock_os.makedirs.assert_called_once_with("/new/directory")
