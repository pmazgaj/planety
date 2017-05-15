"""
Definitions for entire project - path of project plus path of csv folder
"""
import os
from pylint.lint import Run


def run_py_lint():
    """Run py lint for code"""
    Run(['--errors-only', os.path.abspath(__file__)])


__author__ = "Przemek"

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))  # This is my Project Root

CSV_PATH = os.path.join(ROOT_DIR, 'csv')  # This is root for csv files
