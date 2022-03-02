from win32com.client import constants, gencache


def word2pdf(source_file: str, target_file: str = None):
    """
    word转pdf 只作用于 windows 平台
    :param wordPath: word文件路径
    :param pdfPath:  生成pdf文件路径
    """
    word = gencache.EnsureDispatch('Word.Application')
    doc = word.Documents.Open(source_file, ReadOnly=1)
    doc.ExportAsFixedFormat(target_file, constants.wdExportFormatPDF,
                            Item=constants.wdExportDocumentWithMarkup,
                            CreateBookmarks=constants.wdExportCreateHeadingBookmarks)
    word.Quit(constants.wdDoNotSaveChanges)
