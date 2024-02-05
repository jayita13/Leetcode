# https://leetcode.com/problems/display-the-first-three-rows/

import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)
