import random

def is_sorted(to_be_sorted):
    i = 0
    sorted = True
    while i < len(to_be_sorted):
        if to_be_sorted[i] > to_be_sorted[ i + 1]:
            sorted = False
            continue
        i += 1
    return sorted

# def random_sort(to_be_sorted):
#     sorted = False
#     while !sorted:
if __name__ == '__main__':

    sorted = False
    print("Why am I so bad\n")
    while sorted == False:
        to_be_sorted = random.sample(range(2), 2)
        print(to_be_sorted)
        sorted = is_sorted(to_be_sorted)

    print("Why am I so bad\n")