import os
try:
    import polars as pl
    import xlwings as xw
except ModuleNotFoundError as e:
    print("install polars xlwings")
    os.system("pip install polars")
    os.system("pip install xlwings")
    import polars as pl
    import xlwings as xw

from colorama import init as colorama_init_, Fore
from src.constants import echo_info
from src.utils.time_ import to_str_datetime

colorama_init_(autoreset=True)


def csv2xlsx(input_path: str, output_path: str = None, query_str_: str = '', encoding:str='utf-8'):
    """
    :param input_path: 输入源
    :param output_path: 输出源
    :param query_str_: 查询条件、未加入
    :return:
    """
    if not isinstance(query_str_, str):
        raise TypeError('query must be of string type')

    if output_path is None:
        output_path = f'{input_path}_{to_str_datetime()}.csv'

    pl_df_ = pl.read_csv(input_path, has_header=True)
    columns = pl_df_.columns
    doc_list_ = pl_df_.to_numpy()

    app = xw.App(visible=False, add_book=False)
    app.display_alerts = True
    app.screen_updating = True
    wb_ = app.books.add()
    ws_ = wb_.sheets.active  # 当前激活的sheet

    try:
        ws_.range('A1').options().value = columns
        for index, doc in enumerate(doc_list_):
            ws_.range(f'A{index + 2}').options().value = doc
    except:
        ...
    finally:
        wb_.save(output_path)
        wb_.close()
        app.quit()

    result_ = echo_info.format(Fore.GREEN, input_path, output_path)
    return result_


if __name__ == '__main__':
    csv2xlsx(input_path='../../src/test_files/318线路列表.csv',
             output_path='../../src/test_files/318线路列表_.xlsx')
