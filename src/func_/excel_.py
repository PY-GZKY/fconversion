from colorama import init as colorama_init_, Fore
import xlwings as xw
from src.constants import echo_info
from src.utils.time_ import to_str_datetime

colorama_init_(autoreset=True)


def xlsx2csv(input_path: str, sheet_name: str = None, output_path: str = None, query_str_: str = '', limit: int = -1):
    if not isinstance(query_str_, str):
        raise TypeError('query must be of string type')
    if not isinstance(limit, int):
        raise TypeError("limit must be an integer type")
    if sheet_name is None:
        sheet_name = 'Sheet1'
    if output_path is None:
        output_path = f'{input_path}_{to_str_datetime()}.csv'

    app = xw.App(visible=False, add_book=False)
    app.display_alerts = True
    app.screen_updating = True
    wb = app.books.open(input_path)

    try:
        sheet_ = wb.sheets[sheet_name]
        last_cell = sheet_.used_range.last_cell
        last_row = last_cell.row
        last_col = last_cell.column
        doc_list_ = sheet_.range((1, 1), (last_row, last_col)).value
        import polars as pl
        df = pl.DataFrame(doc_list_[1:], columns=doc_list_[0])
        df.to_csv(file=output_path)
    except:
        ...
    finally:
        wb.save()
        wb.close()
        app.quit()

    result_ = echo_info.format(Fore.GREEN, input_path, output_path)
    return result_


if __name__ == '__main__':
    xlsx2csv(input_path='../../src/test_files/318线路列表.xlsx',
             sheet_name='318线路列表',
             output_path='../../src/test_files/318线路列表.csv',
             )
