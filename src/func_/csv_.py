import pyarrow as pa
import pyarrow.csv as pa_csv_
from colorama import init as colorama_init_, Fore

from src.constants import echo_info
from src.utils.time_ import to_str_datetime

colorama_init_(autoreset=True)


def csv2xlsx(input_path: str, output_path: str = None, query_str_: str = '', limit: int = -1):
    if not isinstance(query_str_, str):
        raise TypeError('query must be of string type')
    if not isinstance(limit, int):
        raise TypeError("limit must be an integer type")

    if output_path is None:
        output_path = f'{input_path}_{to_str_datetime()}.csv'

    import pandas
    import pyarrow.csv as pa_csv_
    pa_df_ = pa_csv_.read_csv(input_path)
    pylist = pa_df_.to_pylist()
    print(pylist)


    # pd_df_ = pandas.read_csv(input_path, encoding='utf-8')
    # if query_str_:
    #     pd_df_ = pd_df_.query(query_str_)

    # doc_list_ =  pd_df_.values.tolist()

    # import xlwings as xw
    # app = xw.App(visible=False, add_book=False)
    # app.display_alerts = True
    # app.screen_updating = True
    # wb = app.books.open(output_path)
    # sheet1 = wb.sheets[0]
    # sheet1.name = "Sheet1"

    # sheet1.range('A1').expand('table').value = pd_df_
    # for index, doc in enumerate(doc_list_):
    #     sheet1.range(f'A{index+2}').options().value = doc

    # wb.save()
    # wb.close()
    # app.quit()

    result_ = echo_info.format(Fore.GREEN, input_path, output_path)
    print(result_)
    return result_


if __name__ == '__main__':
    csv2xlsx(input_path='../../src/test_files/318线路列表.csv',
             output_path='../../src/test_files/318线路列表_.xlsx',
             # query_str_='线路景点所在城市 == "四川" & 途经此景点价格 == "150元"'
             )
