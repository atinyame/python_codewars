import codewars_test as test


def find_multiples(integer: int, limit: int) -> list[int]:
    return list(range(integer, limit+1, integer))


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(find_multiples(5, 25), [5, 10, 15, 20, 25])
        test.assert_equals(find_multiples(1, 2), [1, 2])
