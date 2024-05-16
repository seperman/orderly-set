def main():
    import timeit
    from functools import partial
    from random import randint

    from ordered_set import OrderedSet as OS1
    from orderly_set import OrderedSet as OS2
    from orderly_set import StableSet as OS3
    from orderly_set import OrderlySet as OS5
    from orderly_set import SortedSet as OS6
    # from sortedcollections import OrderedSet as OS4

    item_count = 10_000
    item_range = item_count * 2
    items = [randint(0, item_range) for _ in range(item_count)]
    items_b = [randint(0, item_range) for _ in range(item_count)]

    oset1a = OS1(items)
    oset2a = OS2(items)
    oset1b = OS1(items_b)
    oset2b = OS2(items_b)
    assert oset1a.difference(oset1b) == oset2a.difference(oset2b)
    assert oset1a.intersection(oset1b) == oset2a.intersection(oset2b)

    oset1c = OS1(items)
    oset2c = OS2(items)
    oset1c.add(item_range + 1)
    oset2c.add(item_range + 1)
    assert oset1c == oset2c

    for i in range(item_range):
        assert (i in oset1a) == (i in oset2a)
        if i in oset1a:
            assert oset1a.index(i) == oset2a.index(i)


    def init_set(T, items) -> set:
        return T(items)


    def init_set_list(T, items) -> list:
        return list(T(items))


    def init_set_d(items) -> dict:
        return dict.fromkeys(items)


    def init_set_d_list(items) -> list:
        return list(dict.fromkeys(items))


    def update(s: set, items) -> set:
        s.update(items)
        return s

    def update_and_get_item(set_type: set, items, items_b) -> set:
        set_ = set_type(items)
        if set_:
            set_[0]
        set_.update(items_b)
        set_[0]
        return set_

    def update_d(s: dict, items) -> dict:
        d2 = dict.fromkeys(items)
        s.update(d2)
        return s


    def symmetric_diff(s: set, s2: set) -> dict:
        return s ^ s2


    def diff(s: set, s2: set) -> dict:
        return s - s2


    orderly_sets_types = [OS1, OS2, OS3, OS5, OS6]  # OS4 is too slow
    orderly_set_type_names = ['ordered_set.OrderedSet', 'orderly_set.OrderedSet', 'StableSet', 'OrderlySet', 'SortedSet']  # 'sortedcollections.OrderedSet' is too slow
    set_types = [set] + orderly_sets_types
    set_type_names = ['set'] + orderly_set_type_names

    oss = [init_set(T, items) for T in set_types]
    oss_b = [init_set(T, items_b) for T in set_types]
    od = init_set_d(items)

    osls = [init_set_list(T, items) for T in set_types[1:-1]] + [init_set_d_list(items)]
    for x in osls:
        assert osls[0] == x

    osls = [update(init_set(T, items), items_b) for T in orderly_sets_types[:-1]] + [
        update_d(init_set_d(items), items_b)
    ]
    osls = [list(x) for x in osls]
    for x in osls:
        assert osls[0] == x

    number = 10000
    repeats = 3
    for i in range(repeats):
        print(f"----- series {i} ------")

        # print("-- initialize a set --")
        # print(f"Using Python dict time: {timeit.timeit(partial(init_set_d, items),number=number)}")
        # for idx, T in zip(set_type_names, set_types):
        #     print(f"{idx} time: {timeit.timeit(partial(init_set, T, items),number=number)}")

        # print("-- update a set --")
        # print(f"Using Python dict: {timeit.timeit(partial(update_d, od, items_b),number=number)}")
        # for idx, os in zip(set_type_names, oss):
        #     print(f"{idx} time: {timeit.timeit(partial(update, os, items_b),number=number)}")

        print("-- update a set and get item --")
        for idx, os in zip(orderly_set_type_names, orderly_sets_types):
            print(f"{idx} time: {timeit.timeit(partial(update_and_get_item, os, items, items_b),number=number)}")

        print("-- set symmetric difference (xor) --")
        for idx, set1, set2 in zip(set_type_names, oss, oss_b):
            print(f"{idx} time: {timeit.timeit(partial(symmetric_diff, set1, set2),number=number)}")

        print("-- set difference (-) --")
        for idx, set1, set2 in zip(set_type_names, oss, oss_b):
            print(f"{idx} time: {timeit.timeit(partial(diff, set1, set2),number=number)}")


if __name__ == '__main__':
    main()
