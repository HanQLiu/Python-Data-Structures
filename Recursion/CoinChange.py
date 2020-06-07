### Give a target amount n and a list of distinct coin values, return a list of the least amount of coins needed ###
import unittest


def change_coin(target_amount, coins):
    """input a target amount 11 and coin_list [1, 5], return [5, 5, 1]"""
    coin_list = []
    if target_amount == 0:
        return coin_list
    else:
        coins.sort(reverse=True)
        if target_amount >= coins[0]:
            target_amount -= coins[0]
            coin_list.append(coins[0])
            coin_list.extend(change_coin(target_amount, coins))
        elif target_amount < coins[0]:
            coin_list.extend(change_coin(target_amount, coins[1:]))
    return coin_list


class Test(unittest.TestCase):
    """Test cases"""

    '''test change coin'''
    def test_change_coin(self):
        self.assertEqual(change_coin(15, [1, 2, 5]), [5, 5, 5])
        self.assertEqual(change_coin(19, [1, 3, 5]), [5, 5, 5, 3, 1])
        self.assertEqual(change_coin(5, [1, 2]), [2, 2, 1])


'''run the script'''
if __name__ == '__main__':
    unittest.main()

