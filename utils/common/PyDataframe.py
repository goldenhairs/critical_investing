# *_*coding:utf-8 *_*
"""
Author：szj
Descri：
"""
import pandas as pd
from pandas.core.series import Series

__all__ = ["iterrows"]


def iterrows(df):
    """
    因为pandas自带的iterrows遍历元素时有时会有问题，故用此方法替代
    :param df:  Dataframe类型的数据
    :return:
    """
    """
            Iterate over DataFrame rows as (index, Series) pairs.

            Yields
            ------
            index : label or tuple of label
                The index of the row. A tuple for a `MultiIndex`.
            data : Series
                The data of the row as a Series.

            it : generator
                A generator that iterates over the rows of the frame.

            See Also
            --------
            itertuples : Iterate over DataFrame rows as namedtuples of the values.
            items : Iterate over (column name, Series) pairs.

            Notes
            -----

            1. Because ``iterrows`` returns a Series for each row,
               it does **not** preserve dtypes across the rows (dtypes are
               preserved across columns for DataFrames). For example,

               >>> df = pd.DataFrame([[1, 1.5]], columns=['int', 'float'])
               >>> row = next(df.iterrows())[1]
               >>> row
               int      1.0
               float    1.5
               Name: 0, dtype: float64
               >>> print(row['int'].dtype)
               float64
               >>> print(df['int'].dtype)
               int64

               To preserve dtypes while iterating over the rows, it is better
               to use :meth:`itertuples` which returns namedtuples of the values
               and which is generally faster than ``iterrows``.

            2. You should **never modify** something you are iterating over.
               This is not guaranteed to work in all cases. Depending on the
               data types, the iterator returns a copy and not a view, and writing
               to it will have no effect.
            """
    columns = df.columns
    klass = Series
    for k, v in zip(df.index, df.values):
        s = klass(v, index=columns, name=k)
        yield k, s
