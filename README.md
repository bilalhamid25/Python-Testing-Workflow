# Python Testing Workflow


Welcome to the Python Testing Workflow Showcase! This repository is a comprehensive guide and demonstration of setting up an effective Python testing workflow using industry-standard tools like PyTest, MyPy, PyLint, and GitHub Actions. Whether you're a beginner looking to understand the fundamentals or an experienced developer seeking best practices, this showcase provides in-depth insights into the intricacies of each tool and their integration.

## Key Features

### PyTest: Efficient Unit Testing

Learn how to leverage PyTest, a robust testing framework for Python, to write and execute efficient unit tests. PyTest simplifies the testing process, allowing you to focus on creating comprehensive test cases and ensuring the reliability of your codebase.

### MyPy: Static Type Checking Mastery

Discover the power of MyPy, a static type checker for Python. Dive into the nuances of static type checking and understand how MyPy enhances code quality by catching type-related errors early in the development process.

### PyLint: Code Quality Enforcement

Explore PyLint, a widely-used Python linter that enforces coding standards and identifies potential bugs and code smells. Gain insights into configuring PyLint for your projects and utilizing it to maintain high-quality, clean, and consistent code.

### GitHub Actions: Seamless CI/CD Integration

Delve into GitHub Actions, an integral part of modern development workflows. Uncover the secrets of configuring workflows to automate testing, ensuring that your codebase remains reliable and error-free with each push and pull request.

#### Cross-Platform Testing

The GitHub Actions workflows now test on **Mac**, **Linux**, and **Windows** using Python versions **3.7 to 3.12** on each operating system to ensure compatibility across all platforms.



## Learning Objectives

- Understand the fundamentals of PyTest for effective unit testing.
- Master the art of static type checking with MyPy.
- Enforce coding standards and improve code quality using PyLint.
- Integrate GitHub Actions seamlessly into your development process.
- Gain hands-on experience in setting up and customizing testing workflows.
- Skills to package and import your Python project.


## Folder Structure

```
Python-Testing-Workflow
├── .github
│   └── workflows
│       ├── mypy.yml
│       ├── pylint.yml
│       └── pytest.yml
├── .vscode
│   └── settings.json
├── calculator
│   ├── __init__.py
│   ├── addition.py
│   ├── division.py
│   ├── multiplication.py
│   └── subtraction.py
├── mypy.ini
├── requirements.txt
├── requirements_dev.txt
├── setup.py
├── tests
│   ├── __init__.py
│   ├── test_addition.py
│   ├── test_division.py
│   ├── test_multiplication.py
│   └── test_subtraction.py
├── LICENSE
└── README.md
```

## GitHub Actions Workflows

### MyPy Workflow (`mypy.yml`)

This GitHub Actions workflow leverages MyPy for static type checking. MyPy helps catch type-related errors early in the development process, ensuring a more robust codebase.

### PyLint Workflow (`pylint.yml`)

The PyLint workflow utilizes PyLint to perform linting on your Python code. PyLint enforces coding standards, checks for potential bugs, and promotes consistent and clean code practices.

### PyTest Workflow (`pytest.yml`)

The PyTest workflow runs your test suite using PyTest, a testing framework for Python. PyTest simplifies the process of writing and executing unit tests, providing a comprehensive testing solution.

## Setting up Your Development Environment

- Install project dependencies using `pip install -r requirements.txt`.
- For development, additional requirements are specified in `requirements_dev.txt`.
- Configure your editor with the provided `.vscode/settings.json` for an enhanced development experience.

## Running Tests Locally

Execute the following commands to run tests locally:

### MyPy

```bash
mypy calculator
```

<span style="color: #00ff00; font-size: 16px; font-weight: bold;">Success: no issues found in 5 source files</span>

```bash
mypy tests
```

<span style="color: #00ff00; font-size: 16px; font-weight: bold;">Success: no issues found in 5 source files</span>

### PyLint

```bash
pylint calculator
```

<span style="color: #00ff00; font-size: 16px; font-weight: bold;">Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)</span>

```bash
pylint tests
```

<span style="color: #00ff00; font-size: 16px; font-weight: bold;">Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)</span>

### PyTest

```bash
pytest tests
```

<span style="color: #00ff00; font-size: 16px; font-weight: bold;">=========== 64 passed in 0.08s ===========</span>

## Building and Importing the Package

To build the package, run the following command:

```bash
python setup.py sdist bdist_wheel
```

This will create a source distribution and a wheel distribution in the `dist` directory.

### Installing the Package

After building, you can create a new Python environment and install the package with:

```bash
conda create -n myenv python=3.10 # Or any other python virtual env of your choice
conda activate myenv
cd dist
pip install calculator-0.1-py3-none-any.whl # change the name of the wheel file which you see in the dist folder
```

Now, you can import and use the `calculator` package in your Python environment.

## Example Usage

Suppose you've created a Python file (`example.py`) with the following code:

```python
from calculator.division import divide

result = divide("342", "54")
print(result)
```

Running this file will raise a `TypeError` since you are trying to divide strings.

## Contributing

Feel free to contribute to this project by opening issues, proposing new features, or submitting pull requests. Your contributions are welcome!

## License

This project is licensed under the [MIT License](LICENSE).