import pandas as pd

def create_df(customer_list):
    customers = pd.DataFrame(customer_list,columns=["customer_id","name","email"])
    return customers

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    customers.drop_duplicates(subset=["email"],inplace=True)
    return customers    


customer_list = [
    [1, "John Doe", "john.doe@example.com"],
    [2, "Jane Doe", "jane.doe@example.com"],
    [3, "John Doe", "john.doe@example.com"],
    [4, "Jane Smith", "jane.smith@example.com"],
    [5, "John Smith", "john.smith@example.com"],]


customers = create_df(customer_list)
print(dropDuplicateEmails(customers))