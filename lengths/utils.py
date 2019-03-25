import sys
import inspect


def get_all_lengths():
    from lengths import units
    length_list = []
    for name, obj in inspect.getmembers(units):
        if inspect.isclass(obj):
            length_list.append(obj)
    return length_list


def get_unit_class(unit):
    unit_class = None
    length_list = get_all_lengths()
    for length in length_list:
        if not length.has_alias(unit):
            continue
        unit_class = length
    return  unit_class

