def is_fruit(input_food):  # must be lowercase, no space or symbols...
    fruit_list = ["banana", "apple", "pear"]
    return input_food in fruit_list


if __name__ == "__main__":
    food = "Apple"
    print(is_fruit(food))
