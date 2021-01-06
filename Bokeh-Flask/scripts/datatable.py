import pandas as pd

def datatable():
    # create dataframe
    df = pd.DataFrame({'Metric': ['Average', 'Max Rev', 'Min Rev', 'Expenditure'],
        'Month1': [68, 74, 77, 78],
        'Month2': [84, 56, 73, 69],
        'Month3': [78, 88, 82, 87]})
    # render dataframe as html
    datatable = df.to_html(index=False)
    return datatable