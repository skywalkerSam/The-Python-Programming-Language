# zip function() ...

list_one = [1, 2, 3]
list_two = [10, 20, 30]
list_three = [100, 200, 300]
list_four = [1000, 2000, 3000]

final_list_one = list(zip(list_one, list_two))
print(final_list_one)

final_list_two = list(zip(list_one, list_two, list_three, list_four))
print(final_list_two)


def zip_up(item, item_two):
    zipped_up = list(zip(item, item_two))
    return zipped_up


print("10^3: ", zip_up(list_one, list_four))
