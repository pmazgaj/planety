"""
Handle main events for program
"""
import logging
from planety.valuation_service.aggregate import get_key, compare_products_to_matches, get_top_low_for_match, \
    get_sum_avg_for_match
from planety.valuation_service.file_handler import get_all_values_for_column, \
    parse_csv, save_csv_to_file, fill_product_object, fill_matches_object, fill_currency_object
from planety.valuation_service.calculations import get_parsed_column, convert_currency, get_average_value_for_column, \
    get_sum_for_column

# from planety.definitions import run_py_lint

__author__ = "Przemek"

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s:%(levelname)s:%(message)s")


def log_object_info(obj_name: str="default", object_to_log: list=()) -> None:
    """
    Log information into console
    :param obj_name: Object name to put into logger 
    :param object_to_log: Values to be shown into logger
    :return: 
    """
    print(len(object_to_log))
    logging.debug('%s: %s', obj_name.capitalize(), object_to_log)


def main():
    """Main function to handle everything"""
    # run_py_lint()

    data_file = parse_csv('data.csv')
    matches_file = parse_csv('matchings.csv')
    currencies_file = parse_csv('currencies.csv')

    products = fill_product_object(data_file)
    matches = fill_matches_object(matches_file)
    currencies = fill_currency_object(currencies_file)
    # log_object_info('products', products)
    # log_object_info('matches', matches)
    # log_object_info('currencies', currencies)

    a = convert_currency(currencies, products)
    print(a)
    # sorting original copy of list
    products.sort(key=get_key)

    matching_id_lists = get_parsed_column(get_all_values_for_column(matches_file, 'matching_id'))
    get_matched_dict = compare_products_to_matches(products, matches, matching_id_lists)

    top_and_low = get_top_low_for_match(get_matched_dict, matches)
    sum_and_avg = get_sum_avg_for_match(get_matched_dict)
    # average_price = get_average_value_for_column(top_and_low['over_limit'])
    # total_price = get_sum_for_column(top_and_low['under_limit'])

    # print(average_price)
    # print(total_price)
    save_csv_to_file(top_low_dict=top_and_low, sum_avg_dict=sum_and_avg)


if __name__ == "__main__":
    main()
