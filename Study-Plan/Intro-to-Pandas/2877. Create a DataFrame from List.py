# https://leetcode.com/problems/create-a-dataframe-from-list/

import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    return pd.DataFrame(
        data=student_data,
        columns=['student_id', 'age'],
    )
