import codewars_test as test


def am_i_wilson(n: int) -> bool:
    return n == 5 or n == 13 or n == 563


@test.describe('Wilson Primes')
def tests():
    @test.it('Example tests')
    def wilson_prime():
        test.assert_equals(am_i_wilson(0), False)
        test.assert_equals(am_i_wilson(1), False)
        test.assert_equals(am_i_wilson(5), True)
        test.assert_equals(am_i_wilson(8), False)
        test.assert_equals(am_i_wilson(9), False)
