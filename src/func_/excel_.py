import pyarrow as pa
import pyarrow.csv as pa_csv_
from pyarrow import compute as pc
from colorama import init as colorama_init_, Fore

from src.constants import echo_info
from src.utils.time_ import to_str_datetime

colorama_init_(autoreset=True)


def xlsx2csv(input_path: str, sheet_name: str = None, output_path: str = None, query=None, limit: int = -1):
    """
    """
    if query is None:
        query = {}
    if not isinstance(query, dict):
        raise TypeError('query must be of dict type')
    if not isinstance(limit, int):
        raise TypeError("limit must be an integer type")
    if sheet_name is None:
        sheet_name = 'Sheet1'
    if output_path is None:
        output_path = f'{input_path}_{to_str_datetime()}.csv'

    """
    import xlwings as xw
    app = xw.App(visible=False, add_book=False)
    app.display_alerts = True
    app.screen_updating = True
    wb = app.books.open('../../src/test_files/318线路列表.xlsx')
    sheet1 = wb.sheets['318线路列表']
    info = sheet1.used_range.shape
    print("info: ", info)
    doc_list_ = sheet1.range('A1').expand().value
    """
    import pandas
    pd_df_ = pandas.read_excel(input_path, sheet_name)
    _ = (pd_df_['线路景点所在城市'] == '四川') & (pd_df_['途经此景点价格'] == '150元')
    pd_df_ = pd_df_[_]

    """
    doc_list_ = data_.to_dict(orient='records')
    df_schema = type_convert(doc_list_[0])
    df = pa.Table.from_pylist(doc_list_,schema=df_schema)
    """
    pa_df_ = pa.Table.from_pandas(df=pd_df_)
    df_schema = pa.Schema.from_pandas(df=pd_df_)
    with pa_csv_.CSVWriter(output_path, df_schema) as writer:
        writer.write_table(pa_df_)

    result_ = echo_info.format(Fore.GREEN, input_path, output_path)
    print(result_)
    return result_


if __name__ == '__main__':
    xlsx2csv(input_path='../../src/test_files/318线路列表.xlsx',
             sheet_name='318线路列表',
             output_path='../../src/test_files/318线路列表.csv',
             query={'线路景点所在城市':'四川','途经此景点价格':'150元'}
             )
