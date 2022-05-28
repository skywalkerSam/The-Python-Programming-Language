
# while loops;
# It is very powerful because, it got the Infinity
# -> Work on the conditions, True or False
True
False

i = 0
while i < 21:
    print(i)
    i += 1      # or,  i = i + 1
    break
else:
    print("Done !")

i = 0
while i < 21:
    print(i)
    i += 1      # or,  i = i + 1
else:
    print("Done !")     # It'll run only if the loop says True




# while loops 2;
True  # -1
False  # -0

# We can do the work of for loops in while loops also;
list1 = [369, "Captain", "SpaceX", "NASA", 3, 6, 9]
for items in list1:
    print(items)

    # Same thing in while loop
_ = 0
while _ < len(list1):
    print(list1)
    _ += 1

_ = 0
while _ < len(list1):
    print(list1[_])
    _ += 1
    # Conclusion - for loop is more logical & simple for this solution

    # Infinity;
while True:
    responce = input('Say Something: ')
    if responce == 'ok':
        break




# break, continue, pass ;
        # - works with for & while loops both.

    # break - breaks the loop

    # continue - re-runs the loop

    # pass - simply pass to next line





for item in ('hello'):
    # thinking about it, but i don't wanna error for this
    pass

print('done!')







