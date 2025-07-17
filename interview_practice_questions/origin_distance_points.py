import math

# input: [[0,1],[-2,0],[2,1]]
# input: k - want the first k closest to origin points

def find_k_closest_origin_distance(coordinates, k):
    if not coordinates or k <= 0:
        return []
    if len(coordinates) <= k:
        return coordinates

    k_dict = {}
    curr_max = -1

    coordinates.sort()

    for coord in coordinates:
        x = coord[0]
        y = coord[1]
        # dist = sqrt( (x2 - x1)^2 + (y2 - y1)^2 )
        distance = round(math.sqrt(math.pow(x,2) + math.pow(y,2)), 2)

        # print('current coord ', coord)
        # print('current max ', curr_max)


        # we want to add this point to our k_dict
        if distance < curr_max or curr_max == -1:
            # scenario: if our k_dict full, kick out largest val
            k_dict_vals = list(x for v in k_dict.values() for x in v)
            if len(k_dict_vals) == k:
                current_max_values = k_dict[curr_max]
                if len(current_max_values) > 1:
                    del k_dict[curr_max]

                else:
                    current_max_values.pop()
                    k_dict[curr_max] = current_max_values

                    # reassign a new current max
                    curr_max = max(k_dict.keys())


        # scenario: we don't have enough k points yet, fill it up
        k_dict_vals = list(x for v in k_dict.values() for x in v)
        if len(k_dict_vals) < k:
            # keep track of an updated current max
            if distance > curr_max or curr_max == -1:
                curr_max = distance

            if distance in k_dict:
                current_values = k_dict[distance]
                current_values.append(coord)
                k_dict[distance] = current_values
            else:
                k_dict[distance] = [coord]

        # print('current k_dict ', k_dict)
        # print()

    k_dict_vals = list(x for v in k_dict.values() for x in v)
    return k_dict_vals


if __name__ == "__main__":
    print(find_k_closest_origin_distance([[0,1],[-2,0],[2,1]], 2))
    # print(find_k_closest_origin_distance([[3,4], [1,2], [-1,0], [-1,-1], [2,2], [5,5], [0,1]], 3))
    # print(find_k_closest_origin_distance([[1, 1], [-1, -1], [1, -1], [-1, 1], [3, 4], [0, 2]], 4))


# python specific stuff I could do to memorize
"""
    math.sqrt(num)           (import math)
    math.pow(num, power)     (import math)
    sort() vs. sorted()
        list.sort() is a method that sorts the list in-place, meaning
          it modifies the original list directly and returns None.
        sorted() is a built-in function that returns a new sorted list,
          leaving the original iterable unchanged.
    round(num, decimal_places)

"""