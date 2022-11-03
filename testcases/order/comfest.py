import pytest
from testcases.conftest import order_data


@pytest.fixture(scope="function")
def testcase_data(request):
    testcase_name = request.function.__name__
    return order_data.get(testcase_name)