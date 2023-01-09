"""Functions which helps the locomotive engineer to keep track of the train."""


# TODO: define the 'get_list_of_wagons' function
def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    (*tmp,) = args
    return tmp


# TODO: define the 'fixListOfWagons()' function
def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :parm each_wagons_id: list - the list of wagons.
    :parm missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    a1, b1, c1, *d1 = each_wagons_id
    (*combined,) = c1, *missing_wagons, *d1, a1, b1
    return combined


# TODO: define the 'add_missing_stops()' function
def add_missing_stops(route: dict, **kwargs):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    return {**route, **{"stops": [*kwargs.values()]}}


# TODO: define the 'extend_route_information()' function
def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    return {**route, **more_route_information}


# TODO: define the 'fix_wagon_depot()' function
def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    [[a1, a2, a3], [b1, b2, b3], [c1, c2, c3]] = wagons_rows
    return [[a1, b1, c1], [a2, b2, c2], [a3, b3, c3]]
