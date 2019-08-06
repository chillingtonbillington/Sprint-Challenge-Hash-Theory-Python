#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)


    if length < 2:
        answer = None

    for i in range(length)
        hash_table_insert(ht, weights[i], i)

    for i in range(length)
        weight_1 = weights[i]
        weight_2 = limit - weight_1
        retrieve = hash_table_retrieve(ht, weight_2)

        if retrieve is not None:
            if retrieve > i:
                answer = (retrieve, i)
            if retrieve < i:
                answer = (i, retrieve)
    return answer 

def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
