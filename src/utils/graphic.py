PADDING_COLUMN = 5
def is_matrix(array: list):
    """
    Check the given array is matrix or not, two validate jobs do are:
    - Check all 1-deep array is instance of the list.
    - Check all 2-deep array is not instance of the list.
    @params:
    + array: the array to check.
    @returns:
    + None
    """
    assert isinstance(array, list), ...
    if not all([isinstance(element, list) for element in array]):
        return False
    if any([any(isinstance(element, list) for element in row) for row in array]):
        return False
    return True

def generate_table(headers: list[str], rows: list[list[any]], data: dict, *, table_name: str):
    """
    Genrate the table with given data, by the default, the headers include the column's name, and the rows\
    correspond with the headers. If the data is define, the headers and rows will be overwrite by the keys and\
    value of the data dictionary.
    @params
    + headers: column's name.
    + rows: data correspond to the headers.
    + table_name: the name of the table.
    + data: the dictionary contain the data with key is column and value is the list of value.
    @returns
    + None
    """
    if data:
        headers = data.keys()
        rows = [row for row in data.values()]
    assert isinstance(table_name, str), ...
    assert isinstance(headers, list), ...
    assert is_matrix(rows, list), ...
    assert len(headers) == len(rows[0])
    column_widths = [max(len(str(item)) + PADDING_COLUMN for item in column) for column in zip(headers, *rows)]
    table_width = sum(column_widths) + (len(headers) - 1) * 3
    print(f'{table_name: ^{table_width}}')
    print(' | '.join([header.ljust(width) for header, width in zip(headers, column_widths)]))
    print('-+-'.join('-' * width for width in column_widths))
    for row in rows:
        print(' | '.join(str(item).ljust(width) for item, width in zip(row, column_widths)))
    print('-' * table_width)

