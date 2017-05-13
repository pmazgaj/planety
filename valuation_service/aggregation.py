"""
Aggregate values from files.
"""

__author__ = "Przemek"


def group_columns_by_param(matches: list, data: list, param='matching_id') -> dict:
    """Group columns by comparing an id"""
    value_1 = []
    value_2 = []
    value_3 = []
    for match in matches:
        match_id = match.get(param, param)
        for product in data:
            product_id = product.get(param, param)

            if match_id == '1' and match_id == product_id:
                value_1.append(match['top_priced_count'])
                value_1.append(product)
            elif match_id == '2' and match_id == product_id:
                value_2.append(match['top_priced_count'])
                value_2.append(product)
            elif match_id == '3' and match_id == product_id:
                value_3.append(match['top_priced_count'])
                value_3.append(product)

    # return
    print(value_1)
    print(value_2)
    print(value_3)
    # print(value)
    # print(product + match.get('top_priced_count'))
