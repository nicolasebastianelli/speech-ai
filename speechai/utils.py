import os


def create_directory_from_path(filepath):
    directory = os.path.dirname(filepath)
    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
            print(f"Directory {directory} created.")
        except OSError as error:
            print(f"An error occurred while creating directory. Error details: {error}")
