
# Tuples;
    # -> Just like a list but it's immutable, you can't modify it in any way
    # -> Faster & Efficient than list in terms of immutability
tuple

my_tuple = (1, 3, 6, 9, 'CaptainMS')
print(my_tuple)
print(my_tuple[2])
print(my_tuple[4])


user1 = {
    (1, 2): 1234,                 # tuple in dictonary
    ('user'): "murlidhar1319",
    'ok': 'alright'
}

print(user1[('user')])




# Tuples 2;
tuple

new_tuple = (123456789, 13579, 2468)    # 0 is not permitted to be at first
print(new_tuple)
print(new_tuple[0])

# Other list functionalities could be used, except the functions which tends to modifiy it
a, b, c, d, *other = (3, 6, 9, 369, 336699, 996633)
print(a)
print(a, b, c, d)
print(other)




# Sets;
    # -> Set is an unordered collection of unique objects.
    # -> Set doesn't supports index
set

my_set = {1, 3, 5, 7, 9}
print(my_set)

my_set0 = {1, 3, 3, 5, 7, 9, 9}
print(my_set)

my_set.add(333)
print(my_set)

my_set0.add(999)
print(my_set0)



# Problem-1
my_list = [1, 2, 3, 4, 5, 5]
print(my_list)

# print uniques only
# Typecasting
a = set(my_list)
print(a)
# or,
print(set(my_list))


print(9 in my_set)
print(963 in my_set)

print(len(my_set))

# .copy()
new_set = my_set.copy()
my_set.clear()
print(my_set)
print(new_set)


# Sets 2;
set
my_set2 = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8, 9}
print("\nSets 2; ")

# .difference()
print(my_set2.difference(your_set))

# .discard()
print(your_set)
your_set.discard(8)
print(your_set)

# .intersection()
print(my_set2.intersection(your_set))
print(my_set2 & (your_set))

# .isdisjoint()
print(my_set2.isdisjoint(your_set))

# .difference_update()
print(my_set2)
print(my_set2.difference_update(your_set))
print(my_set2)

# .isdisjoint()
print(my_set2.isdisjoint(your_set))

# .union()
print(my_set2.union(your_set))
print(my_set2 | (your_set))


my_set2 = {4, 5}
your_set = {4, 5, 6, 7, 8, 9}

# .issubset()
print(my_set2.issubset(your_set))
print(your_set.issubset(my_set2))

# .issuperset()
print(my_set2.issuperset(your_set))
print(your_set.issuperset(my_set2))



