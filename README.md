# Med_Demo

A browser-based automated smoke test suite for a healthcare application. This project uses Python, Playwright, and pytest to validate core user flows through page objects and a structured test case.

## Tech stack

- Python 3.x
- pytest
- Playwright for Python
- Page Object Model pattern

## Project structure

- `Pages/` - Page object definitions for UI interactions
- `Tests/` - Test modules using pytest
- `conftest.py` - Pytest fixtures and test setup
- `.gitignore` - Repository ignore rules

## Installation

1. Install Python 3.10 or later.
2. Create and activate a virtual environment.
3. Install dependencies.

Example:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install pytest playwright
python -m playwright install
```

## Environment setup

- Activate the virtual environment before running tests.
- Ensure browser dependencies are installed with `python -m playwright install`.
- If additional environment variables are required, define them in your shell or a secure `.env` file. This repository does not include an environment file by default.

## Running tests

Run the full test suite with pytest from the repository root:

```bash
pytest
```

## Running a specific test

Run a single test file:

```bash
pytest Tests/test_smoke.py
```

Run a specific test function by node id:

```bash
pytest Tests/test_smoke.py::test_smoke
```

## Reporting

No dedicated reporting tool configuration was detected in this repository. If you want structured test reports, add a reporting plugin such as `pytest-html` or `Allure` and update the test command accordingly.

## Continuous integration

No CI/CD configuration files were detected in the current repository. For a production-ready workflow, add a pipeline definition such as GitHub Actions, GitLab CI, or another CI provider.

## Notes

- This repository is designed as a test automation demonstration for a healthcare web application.
- The suite uses Playwright `page` fixtures and page object classes to keep interactions reusable and maintainable.
- Keep sensitive credentials out of version control and use secure environment configuration for production tests.
