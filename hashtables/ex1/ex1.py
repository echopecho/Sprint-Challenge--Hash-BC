#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (
    HashTable,
    hash_table_insert,
    hash_table_remove,
    hash_table_retrieve,
    hash_table_resize,
)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    # result = None

    for i, weight in enumerate(weights):
        compliment_weight = hash_table_retrieve(ht, limit - weight)
        hash_table_insert(ht, weight, i)
        if compliment_weight is not None:
            result = (
                (i, compliment_weight)
                if i >= compliment_weight
                else (compliment_weight, i)
            )
            print(result)
            return result

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
