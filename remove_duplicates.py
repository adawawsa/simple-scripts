def remove_duplicates(input_list):
    #重複を削除したリストを返す
    return list(set(input_list))

original_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = remove_duplicates(original_list)

print("元のリスト:", original_list)
print("重複を削除したリスト:", unique_list)