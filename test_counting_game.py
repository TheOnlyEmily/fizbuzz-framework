import pytest

from general_counting_game import GeneralCountingGame


def test_generator_up_to_15():


    class ModCountingGame(GeneralCountingGame):

        def add_phrase(self, n, num):
            return n % num == 0


    fiz_buzz = ModCountingGame((("fiz", 3), ("buzz", 5)))

    fb_list = [r for r in fiz_buzz.game_sequence(16)]

    assert fb_list[0] == 1
    assert fb_list[1] == 2
    assert fb_list[2] == "fiz"
    assert fb_list[3] == 4
    assert fb_list[4] == "buzz"
    assert fb_list[5] == "fiz"
    assert fb_list[6] == 7
    assert fb_list[7] == 8
    assert fb_list[8] == "fiz"
    assert fb_list[9] == "buzz"
    assert fb_list[10] == 11
    assert fb_list[11] == "fiz"
    assert fb_list[12] == 13
    assert fb_list[13] == 14
    assert fb_list[14] == "fizbuzz"
