# Python Testing with pytest by Brian Okken

## Part I - Primary Power

### 1. Getting Started with pytest
### 2. Writing Test Functions
### 3. pytest Fixtures
### 4. Builtin Fixtures
### 5. Parametrization
### 6. Markers

## Part II - Working with Projects

### 7. Strategy
### 8. Configuration Files
### 9. Coverage
### 10. Mocking
### 11. tox and Continuous Integration
### 12. Testing Scripts and Applications
### 13. Debugging Test Failures

## Part III - Booster Rockets

### 14. Third-Party Plugins
### 15. Building Plugins
### 16. Advanced Parametrization

---
---

# Part I - Primary Power

---

# 1. Getting Started with pytest

## Getting Started with pytest

This is a test:

```python
def test_passing():
    assert (1, 2, 3) == (1, 2, 3)
```

This looks very simple. It is. But there’s still a lot going on. The function test_passing() will be discovered by pytest as a test function because it starts with test_ and is in a file that starts with test_. And when the test is run, the assert statement will determine if the test passes or fails. assert is a keyword built into Python and has the behavior of raising a AssertionError exception if the expression after assert is false. Any uncaught exception raised within a test will cause the test to fail. Although any type of uncaught exception can cause a test to fail, traditionally we stick with AssertionError from assert to determine pass/fail for tests.

We’ll get into the nitty-gritty of all of that later. First, I’d like to show you what it looks like to run a test on the command line. And in order to run this test, we’ll need to install pytest. So let’s do that now.

## Installing pytest

The headquarters for pytest is https://pytest.org. That’s the official documentation. But it’s distributed through PyPI (the Python Package Index) at https://pypi.org/ project/pytest.

Like other Python packages distributed through PyPI, use pip to install pytest into the virtual environment you’re using for testing:

```bash
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ pip install pytest
```

The (venv) added before the command prompt lets you know that you are using a virtual environment. For the examples in the rest of the book, we’ll always use a virtual environment. However, in order to save a little clutter on the page, (venv) has been removed. We’ll also always be using python3, but will shorten it to python.

![Figure](ScreenshotsForNotes/Chapter1/Venv.PNG)

## Test Discovery

The part of pytest execution where pytest goes off and finds which tests to run is called test discovery. pytest was able to find all the tests we wanted it to run because we named them according to the pytest naming conventions.

Given no arguments, pytest looks at your current directory and all subdirectories for test files and runs the test code it finds. If you give pytest a filename, a directory name, or a list of those, it looks there instead of the current directory. Each directory listed on the command line is examined for test code, as well as any subdirectories.

Here’s a brief overview of the naming conventions to keep your test code discoverable by pytest:

* Test files should be named test_<something>.py or <something>_test.py.
* Test methods and functions should be named test_<something>.
* Test classes should be named Test<Something>.

Because our test files and functions start with test_, we’re good. There are ways to alter these discovery rules if you have a bunch of tests named differently. I’ll cover how to do that in Chapter 8, Configuration Files, on page 113.

## Test Outcomes

So far we’ve seen one passing test and one failing test. However, pass and fail are not the only outcomes possible. Here are the possible outcomes of a test:

* PASSED (.)—The test ran successfully.
* FAILED (F)—The test did not run successfully.
* SKIPPED (s)—The test was skipped. You can tell pytest to skip a test by using either the @pytest.mark.skip() or @pytest.mark.skipif() decorators, which are discussed in Skipping Tests with pytest.mark.skip, on page 74.
* XFAIL (x)—The test was not supposed to pass, and it ran and failed. You can tell pytest that a test is expected to fail by using the @pytest.mark.xfail() decorator, which is discussed in Expecting Tests to Fail with pytest.mark.xfail, on page 77.
* XPASS (X)—The test was marked with xfail, but it ran and passed.
* ERROR (E)—An exception happened either during the execution of a fixture or hook function, and not during the execution of a test function. Fixtures are discussed in Chapter 3, pytest Fixtures, on page 31, and hook functions are discussed in Chapter 15, Building Plugins, on page 205.

# 2. Writing Test Functions

