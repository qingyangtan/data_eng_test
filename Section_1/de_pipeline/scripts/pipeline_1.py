import os
import pandas as pd


def get_first_last_name(name):
    """Return a person first and last name"""
    name = name.split()
    name = [x for x in name if '.' not in x]
    if len(name) == 2:
        return name
    if len(name) == 3:
        return name[:-1]
    if len(name) == 4:
        return name[1:-1]
    return None, None


def get_above_100(price):
    """Return price that is above 100 as True"""
    if price > 100:
        return True
    return False


def remove_prepend_zeros(price):
    """Return price without zeros prepended"""
    return str(price).strip("0")


def main(df):
    # Process first and last name
    df['first_name'], df['last_name'] = zip(*df['name'].apply(get_first_last_name))

    # Drop rows that are empty or None
    df = df[(df['name'] != '') | (df['name'] is not None)]

    # Get prices above 100
    df['above_100'] = df['price'].apply(get_above_100)

    # Remove preprend 0
    df['price'] = df['price'].apply(remove_prepend_zeros)

    print(len(df))
    print(df.head(10))

    df.to_csv(f'{DIR}/data/output/p_dataset.csv', index=False)


if __name__ == "__main__":
    DIR = os.environ['cwd']
    df = pd.read_csv(f'{DIR}/data/input/dataset.csv')
    main(df)
