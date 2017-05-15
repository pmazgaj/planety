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
    valid_products = create_dict_matching_products(matches_id)

    for match in matches:
        m_id = match.matching_id
        for product in products:
            p_id = product.matching_id
            if m_id == p_id:
                valid_products[p_id].append(product)

    return valid_products


def get_top_low_for_match(valid_products: dict, matches: list) -> dict:
    """
    Get top and low products (by limit from matchings.csv)
    :param valid_products:
    :param matches:
    :return: dict of over and under limits
    """

    m_dict = {}
    over_limit = []
    all_objects = []
    for match in matches:
        m_id = match.matching_id
        m_top_priced_count = match.top_priced_count
        m_dict[m_id] = m_top_priced_count

    for key in valid_products.keys():
        if key in m_dict.keys():
            all_objects.append(valid_products[key])
            over_limit.append(valid_products[key][-1:-(m_dict[key] + 1):-1])

    # lists of elements filtered by matching id
    over_limit = [item for sublist in over_limit for item in sublist]
    all_objects = [item for sublist in all_objects for item in sublist]
    under_limit = [item for item in all_objects if item not in over_limit]

    return {'over_limit': over_limit, 'under_limit': under_limit}


def get_sum_avg_for_match(get_matched_dict: dict):
    """
    Return dictionary with avg sum and value for given matched id.
    :param get_matched_dict: 
    :return: 
    """
    dictionary = {}
    value = 0
    for x in get_matched_dict:
        for y in get_matched_dict[x]:
            value += y.converted_total_price
            dictionary[x] = {'avg_price': value/len(get_matched_dict[x]), 'total_price': value}
    return dictionary
