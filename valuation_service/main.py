"""
Handle main events for program
"""
from planety.valuation_service.aggregate import get_key, compare_products_to_matches, get_top_low_for_match
from planety.valuation_service.file_handler import get_all_values_for_column, \
    parse_csv, save_csv_to_file, fill_product_object, fill_matches_object, fill_currency_object
from planety.valuation_service.calculations import get_parsed_column, convert_currency

# from planety.definitions import run_py_lint

__author__ = "Przemek"


def main():
    """Main function to handle everything"""
    # run_py_lint()

    data_file = parse_csv('data.csv')
    matches_file = parse_csv('matchings.csv')
    currencies_file = parse_csv('currencies.csv')

    products = fill_product_object(data_file)
    matches = fill_matches_object(matches_file)
    currencies = fill_currency_object(currencies_file)

    convert_currency(currencies, products)

    # sorting original copy of list
    products.sort(key=get_key)

    matching_id_lists = get_parsed_column(get_all_values_for_column(matches_file, 'matching_id'))
    get_matched_lists = compare_products_to_matches(products, matches, matching_id_lists)

    get_top_low_for_match(get_matched_lists, matches)
    # print(a)
    save_csv_to_file()


if __name__ == "__main__":
    main()
