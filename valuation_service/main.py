"""
Handle main events for program
"""
from planety.valuation_service.calculations import *
from planety.valuation_service.file_handler import *
from planety.valuation_service.aggregation import *

__author__ = "Przemek"


def main():
    # currency.csv
    currencies = parse_csv('currencies.csv')
    currency_currencies = get_all_values_for_column(currencies, 'currency')
    currency_ratio = get_all_values_for_column(currencies, 'ratio')

    # data.csv
    data = parse_csv('data.csv')
    # print(data)
    # data_id = get_all_values_for_column(data, 'id')
    data_quantity = get_all_values_for_column(data, 'quantity')
    data_price = get_all_values_for_column(data, 'price')
    data_price = multiply_two_lists(data_quantity, data_price)
    print(data)
    print(data_price)
    # print(data_price * data_quantity)
    # print(data_price)
    # print(data_price)
    data_currency = get_all_values_for_column(data, 'currency')


if __name__ == "__main__":
    main()
    # a = merge_columns(data_currency, data_price)
    # print(a)
    # print(a)
    # print(data_currency)
    # data_matching_id = get_all_values_for_column(data, 'matching_id')
    # print(data_matching_id)
    # matchings.csv
    # matches = parse_csv('matchings.csv')
    # matches_matching_id = get_all_values_for_column(matches, 'matching_id')
    # matches_top_priced_count = get_all_values_for_column(matches, 'top_priced_count')
    # print(matches)
    # save final results

    # grouped_columns = group_columns_by_param(matches, data)

    # save_csv_to_file()
