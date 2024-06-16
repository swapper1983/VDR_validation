# -*- coding: utf-8 -*-
"""
Created on: 03.06.2024
Author: Maxim Filatov

Importing required libraries.
"""

import logging
import os
import warnings
from fnmatch import fnmatch
from glob import glob
from os.path import join
from pprint import pprint
from typing import Tuple

import pandas as pd

from data import equipment_name, material_req_name

# Configuration of logging procedure
warnings.simplefilter(action='ignore', category=UserWarning)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')

logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)


def read_headers_to_list(file_path: str,
                         file_name: str,
                         sheet_name: str,
                         column_name: str) -> list:
    """Read header list from Excel and returns its values as a list.
    """
    try:
        df = pd.read_excel(join(file_path, file_name), sheet_name=sheet_name)
        column_values = df[column_name].tolist()

        return column_values

    except Exception as e:
        logger.error(f"Error reading the config file in: {file_path}. "
                     f"Please, first of all add config file with headers.")
        print(f"Error reading the config file in: {file_path}: {e} \n"
              f"Please, first of all add correct config file with headers.")


def check_files_with_extension(folder_path: str,
                               xlsx_file_exten: str,
                               xls_file: str) -> None:
    """Checking for files with a specific extension exist in folder.
    """
    # Construct the search pattern
    search_pattern_xlsx = os.path.join(folder_path, xlsx_file_exten)
    search_pattern_xls = os.path.join(folder_path, xls_file)
    # Find all files matching the search pattern
    files_xlsx = glob(search_pattern_xlsx)
    files_xls = glob(search_pattern_xls)
    # Check if any files were found
    if not (files_xlsx or files_xls):
        logger.error(f"Error reading the Excel files in: {folder_path}. "
                     f"Please, first of all add files.")
        print(f"Error reading the Excel files in: {folder_path}. "
              f"Please, first of all add files.")


def find_and_validate_columns(file_path: str,
                              sheet_name: str,
                              expected_columns: list) -> Tuple[pd.DataFrame,
                                                               int, None]:
    """Find the row with column names in the specified sheet
        and validate them.
    """
    xlsx_engine: str = 'openpyxl'
    xls_engine: str = 'xlrd'
    file_name: str = file_path.split("\\")[-1]

    if file_name.split('.')[-1] == 'xls':
        engine = xls_engine
    elif file_name.split('.')[-1] == 'xlsx':
        engine = xlsx_engine

    logger.info("End of session.\n-------------------------------------------")
    logger.info(f"Starting with Excel file: {file_name} validation.")
    print(f"\nStarting with Excel file: {file_name} validation.")

    try:
        data = pd.read_excel(file_path,
                             sheet_name=[sheet_name, 'Cover sheet_VD'],
                             header=None,
                             engine=engine)
        df = data[sheet_name]
        df_cover = data['Cover sheet_VD']
        logger.info(f"Read Excel file: {file_path}")
    except Exception as e:
        logger.error(f"Error reading the Excel file: {file_path}. Error: {e}")
        print(f"Error reading the Excel file: {file_path}. Error: {e}")
        return

    equipment_row = df_cover[df_cover.iloc[:, 0] == equipment_name]
    global equipment_value
    equipment_value = equipment_row.iloc[0, 3]

    material_req_row = df_cover[df_cover.iloc[:, 0] == material_req_name]
    global material_req_value
    material_req_value = material_req_row.iloc[0, 3]

    # Iterate over the rows to find the expected column names
    for ind, row in df.iterrows():
        actual_columns = row.dropna().tolist()

        # Checking that all or part of the columns match original template
        if set(expected_columns).issubset(actual_columns):
            # if set(actual_columns).issubset(expected_columns):
            # Validate the columns
            # missing_columns
            # extra_columns = [col for col in expected_columns
            #                  if col not in actual_columns]
            extra_columns = [col for col in actual_columns
                             if col not in expected_columns]
            if not extra_columns:
                logger.info(f"Column validation successful: "
                            f"All expected columns are present "
                            f"in Excel file: {file_path}")
                print(f"Column validation successful: "
                      f"All expected columns are present "
                      f"in Excel file: {file_path}")
                return df, ind

            # missing_columns
            # else:
            #     logger.error(f"Column validation failed: "
            #                  f"Some expected columns are missing. "
            #                  f"In Excel file: {file_path}. ")  # file_name
            #     logger.error(f"Missing columns: {missing_columns}")
            #     logger.info(f"Expected columns: {expected_columns}")
            #     print(f"Column validation failed: "
            #           f"Some expected columns are missing. "
            #           f"In Excel file: {file_path}")
            #     pprint(f"Missing columns: {missing_columns}")
            #     pprint(f"Expected columns: {expected_columns}")
            # return

            else:
                logger.info(f"Column validation successful: "
                            f"Some extra columns were found. "
                            f"In Excel file: {file_path}. ")
                logger.info(f"Extra columns: {extra_columns}")
                # logger.info(f"Expected columns: {expected_columns}")
                print(f"Column validation successful: "
                      f"Some extra columns were found. "
                      f"In Excel file: {file_path}")
                pprint(f"Extra columns: {extra_columns}")
                # pprint(f"Expected columns: {expected_columns}")
            return df, ind

        # Checking that columns match original template, but have mistakes
        # if set(actual_columns).intersection(expected_columns):
        #     # Validate the columns
        #     incorrect_columns = (list(
        #         set(actual_columns).difference(expected_columns)))
        #     logger.error(f"Column validation failed: "
        #                  f"Could not find some expected columns. "
        #                  f"For Excel file: {file_path}. ")  # file_name
        #     logger.error(f"Incorrect columns: {incorrect_columns}")
        #     logger.info(f"Expected columns: {expected_columns}")
        #     print(f"Column validation failed: "
        #           f"Could not find some expected columns. "
        #           f"For Excel file: {file_path}")
        #     pprint(f"Incorrect columns: {incorrect_columns}")
        #     pprint(f"Expected columns: {expected_columns}")
        #     return

        if set(expected_columns).intersection(actual_columns):
            # Validate the columns
            missed_columns = (list(
                set(expected_columns).difference(actual_columns)))
            logger.error(f"Column validation failed: "
                         f"Could not find some expected columns. "
                         f"For Excel file: {file_path}. ")
            logger.error(f"Missed columns: {missed_columns}")
            logger.info(f"Expected columns: {expected_columns}")
            print(f"Column validation failed: "
                  f"Could not find some expected columns. "
                  f"For Excel file: {file_path}")
            pprint(f"Missed columns: {missed_columns}")
            pprint(f"Expected columns: {expected_columns}")
            return


def parse_extract_to_excel(df: pd.DataFrame,
                           ind: int,
                           out_filename: str) -> None:
    """Clean up unnecessary columns and extract data to Excel.
    """
    try:
        # Remove extra columns(with empty titles)/rows, correct column names
        df.drop(df.index[:ind], inplace=True)
        correct_column_names = df.iloc[0].tolist()
        df.columns = correct_column_names
        df.drop(df.index[:2], inplace=True)
        df = df.loc[:, df.columns.notna()]

        # Prepeare df only with extracted columns
        df = df[expected_columns]

        # Adding two columns with values from cover
        df.insert(0, material_req_name, material_req_value)
        df.insert(1, equipment_name, equipment_value)

        # Extractining data to Excel
        df.to_excel(out_filename,
                    index=False,
                    # header=False,
                    sheet_name='Vendor Document Register')
        logger.info(f"Data were successfully extracted to Excel file: "
                    f"{out_filename}")
        print(f"Data were successfully extracted to Excel file: "
              f"{out_filename}")
    except Exception as e:
        logger.error(f"Error while extracting output data to Excel file: "
                     f"{out_filename}. Error: {e}")
        print(f"Error while extracting output data to Excel file: "
              f"{out_filename}. Error: {e}")


def main() -> None:
    """Main function running.
    """
    # Set variables
    ROOT_PATH: str = os.path.dirname(os.path.abspath(__file__))
    config_path: str = os.path.join(ROOT_PATH, 'config')
    input_path: str = os.path.join(ROOT_PATH, 'input')
    output_path: str = os.path.join(ROOT_PATH, 'output')
    logs_path: str = os.path.join(ROOT_PATH, 'log')
    file_log_path: str = join(logs_path, 'log.txt')
    config_file_name = 'config.xlsx'
    config_sheet_name = 'config_info'
    config_column_name = 'Title list'
    sheet_name: str = 'Vendor Document Register'
    xlsx_file_exten: str = '*.xlsx'
    xls_file_exten: str = '*.xls'

    # Read/validate config file (headers list)
    global expected_columns
    expected_columns = read_headers_to_list(config_path,
                                            config_file_name,
                                            config_sheet_name,
                                            config_column_name)
    if not expected_columns:
        return

    # Logging configuration (file handler)
    file_handler = logging.FileHandler(file_log_path, encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Checking for files in the target directory
    check_files_with_extension(input_path,
                               xlsx_file_exten,
                               xls_file_exten)
    # Starting loop for files in input
    for inp_filename in os.listdir(input_path):
        """Looking for excel files in input folder.
        """
        if (fnmatch(inp_filename, xlsx_file_exten
                    ) or fnmatch(inp_filename, xls_file_exten
                                 )) and inp_filename[:2] != '~$':
            file_input_path: str = join(input_path, inp_filename)
            file_output_path: str = join(output_path,
                                         f'{inp_filename.rsplit(
                                             ".", 1)[0]}.xlsx')

            try:
                df, ind = find_and_validate_columns(file_input_path,
                                                    sheet_name,
                                                    expected_columns)
                parse_extract_to_excel(df, ind, file_output_path)
            except Exception:
                continue


if __name__ == "__main__":
    main()
