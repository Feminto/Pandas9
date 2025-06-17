# Method 1
import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    # intialize a dictionary to store each customer and their number of orders
    cust = {}
    for i in range(len(orders)):
        c = orders['customer_number'][i]

        if c in cust:
            cust[c] += 1
        else:
            cust[c] = 1
    
    # convert it into a list of tuples
    cust_list = []
    for k,v in cust.items():
        cust_list.append((k,v))
    print(cust_list)

    # invalid case
    if not cust_list:
        return pd.DataFrame(columns=['customer_number'])

    # find the max number of orders in the list
    max_o = max(cust_list, key = lambda x: x[1])[1]
    print(max_o)

    # compare the list and find customers with max order value
    result = []
    for i in cust_list:
        if i[1] == max_o:
            result.append(i[0])
    print(result)

    return pd.DataFrame(result, columns = ['customer_number'])

# Method 2
import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    df = orders.groupby('customer_number')['order_number'].nunique().reset_index()
    print(df)

    df = df[df['order_number'] == df['order_number'].max()]
    print(df)

    return df[['customer_number']]