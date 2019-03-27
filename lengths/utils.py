import inspect


def get_child_members_list(members, parent_class):
    members_list = []
    for name, obj in inspect.getmembers(members):
        if inspect.isclass(obj) and issubclass(obj, parent_class):
            members_list.append(obj)
    return members_list
