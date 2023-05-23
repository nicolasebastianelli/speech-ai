# Contributing

When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method with the owners of this repository before making a change.
Please note we have a [code of conduct](CODE_OF_CONDUCT.md), please follow it in all your interactions with the project.

## Development environment setup

To set up a development environment, please follow these steps:

1. Clone the repo

   ```sh
   git clone https://github.com/nicolasebastianelli/speech-ai.git
   ```

2. Setup ```venv``` & ```poetry```:
* Create venv:```python3 -m venv venv```
* Activate venv:```source venv/bin/activate```
* Install poetry ```pip install poetry```

3. Install dependencies and pre-commit:
* Install dependencies:```poetry install```
* Pre-commit install: ```pre-commit install```

4. Testing, Linting, Formatting:
* Test: ```pytest```
* Linter: ```pylint speechai examples tests```
* Linter ```flake8 speechai examples tests -v```
* Style: ```black . -v```
* Imports ```isort . -v --atomic --diff```

## Issues and feature requests

You've found a bug in the source code, a mistake in the documentation or maybe you'd like a new feature? Take a look at [GitHub Discussions](https://github.com/nicolasebastianelli/speech-ai/discussions) to see if it's already being discussed. You can help us by [submitting an issue on GitHub](https://github.com/nicolasebastianelli/speech-ai/issues). Before you create an issue, make sure to search the issue archive -- your issue may have already been addressed!

Please try to create bug reports that are:

- _Reproducible._ Include steps to reproduce the problem.
- _Specific._ Include as much detail as possible: which version, what environment, etc.
- _Unique._ Do not duplicate existing opened issues.
- _Scoped to a Single Bug._ One bug per report.

**Even better: Submit a pull request with a fix or new feature!**

### How to submit a Pull Request

1. Search our repository for open or closed
   [Pull Requests](https://github.com/nicolasebastianelli/speech-ai/pulls)
   that relate to your submission. You don't want to duplicate effort.
2. Fork the project
3. Create your feature branch (`git checkout -b feat/amazing_feature`)
4. Commit your changes (`git commit -m 'feat: add amazing_feature'`) [SpeechAI](https://github.com/nicolasebastianelli/speech-ai) uses [conventional commits](https://www.conventionalcommits.org), so please follow the specification in your commit messages.
5. Push to the branch (`git push origin feat/amazing_feature`)
6. [Open a Pull Request](https://github.com/nicolasebastianelli/speech-ai/compare?expand=1)
