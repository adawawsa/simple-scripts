import unittest
def remove_duplicates_ordered(input_list):
    # 空のリストとセットを使って順序を保持して重複を削除
    seen = set()
    result = []
    for item in input_list:
        if item not in seen:
            seen.add(item)
            result.append(item)
    
    return result
    
class TestRemoveDuplicatesOrdered(unittest.TestCase):
    def test_remove_duplicates_ordered(self):
        self.assertEqual(remove_duplicates_ordered([1, 2, 2, 3, 4, 4, 5]), [1, 2, 3, 4, 5])
        #重複削除
    def test_empty_list(self):
        self.assertEqual(remove_duplicates_ordered([]), [])
        #空のリスト
    def test_ordere_list(self):
        self.assertEqual(remove_duplicates_ordered(["a", "b", "c", "d", "e"]), ["a", "b", "c", "d", "e"])
        #順序を保持

if __name__ == '__main__':
    unittest.main()