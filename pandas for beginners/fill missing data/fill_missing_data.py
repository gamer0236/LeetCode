import pandas as pd
import numpy as np

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products["quantity"].replace(np.nan,0,inplace = True)
    return products    



# in products dataframe there is a qunatity column which has some None values.
# I have to replace those None values with 0.
# by using fillMissingValues function, we can replace those None values with 0.
# this function use numpy library and pandas library
# also there is a another way to do this with  only use of pandas library.


# sample input :- Input:+-----------------+----------+-------+


# | name            | quantity | price |
# +-----------------+----------+-------+
# | Wristwatch      | None     | 135   |
# | WirelessEarbuds | None     | 821   |
# | GolfClubs       | 779      | 9319  |
# | Printer         | 849      | 3051  |
# +-----------------+----------+-------+


#sample  Output:

# +-----------------+----------+-------+
# | name            | quantity | price |
# +-----------------+----------+-------+
# | Wristwatch      | 0        | 135   |
# | WirelessEarbuds | 0        | 821   |
# | GolfClubs       | 779      | 9319  |
# | Printer         | 849      | 3051  |
# +-----------------+----------+-------+


# Explanation: 
# The quantity for Wristwatch and WirelessEarbuds are filled by 0.