def sandwich_ingredients(*ingredients):
    """打印顾客点的所有配料"""
    print("\nHere are the ingredients for your sandwich: ")
    for ingredient in ingredients:
        print("-"+ingredient)
