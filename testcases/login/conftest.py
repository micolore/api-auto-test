import pytest
from testcases.conftest import login_data


@pytest.fixture(scope="function")
def testcase_data(request):
    testcase_name = request.function.__name__
    return login_data.get(testcase_name)