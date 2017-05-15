

def get_key(custom):
    """
    Allows to sort by an object property

    :param custom:
    :return:
    """
    return custom.get_key()


def create_dict_matching_products(matches_id: list) -> dict:
    """
    Create empty dictionary for matching ID's
    :param matches_id:
    :return:
    """
    max_id = max(matches_id)
    dictionary = {}
    counter = 1
    while counter <= max_id:
        dictionary[counter] = []
        counter += 1
    return dictionary


def compare_products_to_matches(products: list, matches: list, matches_id: list) -> dict:
    """
    Fill the dictionary, according to matching id
    :param products:
    :param matches:
    :param matches_id:
    :return: Dictionary for each matching id from matches.csv
    """
    dict_valid_products = create_dict_matching_products(matches_id)
    for product in products:
        for match in matches:
            m_id = match.matching_id
            p_id = product.matching_id
            if m_id == p_id:
                dict_valid_products[p_id].append(product)

    return dict_valid_products


def get_top_low_for_match(match_ids: dict) -> list:
    """
    Get top elements from dict for each key
    :param match_ids:
    :return:
    """
    for each_elem in match_ids:
        pass
    return list()
