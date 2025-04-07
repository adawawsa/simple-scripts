def remove_duplicates_ordered(input_list):
    #空のリストとセットを使って順序を保持して重複を削除
    seen = set()
    result = []
    for item in input_list:
        if item not in seen:
            seen.add(item)
            result.append(item)
    
    return result
    
#使用例
original_list = [1, 2, 2, 3, 4, 4, 5]
unique_ordered_list = remove_duplicates_ordered(original_list)

print("元のリスト:", original_list)
print("重複を削除したリスト:", unique_ordered_list)