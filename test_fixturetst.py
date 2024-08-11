import pytest

pytestmark = pytest.mark.usefixtures('myfixture_module')


def test_one(myfixture_function):
    assert myfixture_function == 100


@pytest.mark.usefixtures('myfixture_class')
class TestFixture:

    def test_two(self, myfixture_function):
        assert myfixture_function == 100

    def test_three(self,myfixture_function):
        pass