# Main script...


def do_stuff(num):
    try: 
        return int(num) + 5
    except ValueError as err:
        return err
    except TypeError:
        print("You must enter a number!")


if __name__ == "__main__":
    do_stuff(None)
