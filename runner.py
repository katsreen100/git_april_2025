import pytest

def run_pytest_tests():
    # You can specify test folder, markers, or config file here
    # Example: Run all tests in the "tests" folder and generate a report
    pytest_args = [               # path to your test directory or specific file
        "-m=sanity ",                   # verbose output
        "--tb=short",           # shorter traceback format
        "--maxfail=3",          # stop after 3 failures
        "--disable-warnings",   # suppress warnings
        "--html=reports/report.html",  # generate HTML report (requires pytest-html)
        "--self-contained-html"        # for standalone HTML report
    ]

    exit_code = pytest.main(pytest_args)
    return exit_code

if __name__ == "__main__":
    result = run_pytest_tests()
    print(f"Tests finished with exit code {result}")
