import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return pd.melt(report,id_vars = "product",value_vars = ["quarter_1","quarter_2","quarter_3","quarter_4"],var_name = "quarter",value_name = "sales")


# The DataFrame is reshaped from wide to long format. Each row represents the sales of a product in a quarter.
# The id_vars parameter specifies the columns that should remain unchanged.



# sample Input:


# +-------------+-----------+-----------+-----------+-----------+
# | product     | quarter_1 | quarter_2 | quarter_3 | quarter_4 |
# +-------------+-----------+-----------+-----------+-----------+
# | Umbrella    | 417       | 224       | 379       | 611       |
# | SleepingBag | 800       | 936       | 93        | 875       |
# +-------------+-----------+-----------+-----------+-----------+


#sample Output:


# +-------------+-----------+-------+
# | product     | quarter   | sales |
# +-------------+-----------+-------+
# | Umbrella    | quarter_1 | 417   |
# | SleepingBag | quarter_1 | 800   |
# | Umbrella    | quarter_2 | 224   |
# | SleepingBag | quarter_2 | 936   |
# | Umbrella    | quarter_3 | 379   |
# | SleepingBag | quarter_3 | 93    |
# | Umbrella    | quarter_4 | 611   |
# | SleepingBag | quarter_4 | 875   |
# +-------------+-----------+-------+