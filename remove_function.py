def remove(list_of_items, item_to_remove):
    """
    Remove all occurrences of an item from a list.
    
    Args:
        list_of_items (list): The list to remove items from
        item_to_remove: The item to remove from the list
        
    Returns:
        list: A new list with all occurrences of item_to_remove removed
    """
    return [item for item in list_of_items if item != item_to_remove]


# Example usage
if __name__ == "__main__":
    my_list = [1, 2, 3, 2, 4, 2, 5]
    item = 2
    result = remove(my_list, item)
    print(f"Original list: {my_list}")
    print(f"After removing {item}: {result}")