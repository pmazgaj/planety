"""
Handle main events for program
"""
import logging
from planety.valuation_service.aggregate import get_key, compare_products_to_matches, get_top_low_for_match, \
    get_sum_avg_for_match
from planety.valuation_service.file_handler import get_all_values_for_column, \
    parse_csv, save_csv_to_file, fill_product_object, fill_matches_object, fill_currency_object
from planety.valuation_service.calculations import get_parsed_column, convert_currency

__author__ = "Przemek"

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s:%(levelname)s:%(message)s")


def log_object_info(obj_name: str = "default", object_to_log: list = ()) -> None:
    """
    Log information into console
    :param obj_name: Object name to put into logger 
    :param object_to_log: Values to be shown into logger
    :return: 
    """
    logging.debug('%s: %s', obj_name.capitalize(), object_to_log)


def main():
    """Main function to handle everything"""
    data_file = parse_csv('data.csv')
    matches_file = parse_csv('matchings.csv')
    currencies_file = parse_csv('currencies.csv')

    products = fill_product_object(data_file)
    matches = fill_matches_object(matches_file)
    currencies = fill_currency_object(currencies_file)
    log_object_info('products', products)
    log_object_info('matches', matches)
    log_object_info('currencies', currencies)

    convert_currency(currencies, products)

    # sorting original copy of list by custom key
    products.sort(key=get_key)

    matching_id_lists = get_parsed_column(get_all_values_for_column(matches_file, 'matching_id'))
    get_matched_dict = compare_products_to_matches(products, matches, matching_id_lists)

    top_and_low = get_top_low_for_match(get_matched_dict, matches)
    sum_and_avg = get_sum_avg_for_match(get_matched_dict)

    # products under limit of top priced count
    under_limit = top_and_low['under_limit']

    save_csv_to_file(sum_avg_dict=sum_and_avg, under_limit=under_limit)


if __name__ == "__main__":
    main()
