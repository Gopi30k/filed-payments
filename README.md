# Filed Payments

#### Coding Problem to built a web API in flask on simple payment processing

## Problem Statement

[Click Here](https://github.com/Gopi30k/filed-payments/blob/develop/ProblemStatement/PythonCodingTest.pdf) to View the problem statement

## Steps to run the Project

### Dependencies

```
Python 3.6+ is needed
```

### Installation

1.) Clone the Git repository in your local machine

```
git clone https://github.com/Gopi30k/filed-payments.git
```

2.) Move/Navigate to the Project Directory

```
cd filed-payments
```

3.) Use Python venv to create a virtual environment

```
python -m venv env
```

4.) Activate Virtual Environment

#### Windows
```
./env/Scripts/Activate
```

#### Linux/MacOS
```
source env/bin/activate
```

5.) Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

```bash
pip install -r requirements.txt
```

6.) Run the Flask server

```bash
python run.py
```

7.) API endpoint

```bash
http://127.0.0.1:5000/process-payment
```

## Testing - Unit Test

1.) Move/Navigate to tests folder from root folder in a new Terminal

```bash
cd tests
```

2.) Run the Unit Test

```bash
python -m unittest test_payment.py
```
