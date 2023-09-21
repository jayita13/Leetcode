# https://leetcode.com/problems/combine-two-tables/

import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    result = pd.merge(person, address, on='personId', how='left')
    result = result[['firstName', 'lastName', 'city', 'state']]
    return result

""" Runtime Details
706ms Beats 5.44%of users with Pandas
Memory Details
60.56MB Beats 99.32%of users with Pandas """
