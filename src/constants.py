# SETTING
import os

default_wkhtmltopdf_path = r'src/bin/wkhtmltopdf.exe'
default_wkhtmltoimage_path = r'src/bin/wkhtmltoimage.exe'
# default_wkhtmltopdf_path = r'D:/wkhtmltopdf/bin/wkhtmltopdf.exe'
# default_wkhtmltoimage_path = r'D:/wkhtmltopdf/bin/wkhtmltoimage.exe'
encoding_ = 'utf_8_sig'
time_zone = 'Asia/Shanghai'
pool_max_workers = 8
default_options_ = {
    'encoding': encoding_,
}
base_dir = os.path.dirname(os.path.abspath(__file__)).replace("\\","/")
static_dir = os.path.join(base_dir, 'static').replace("\\","/")
print(static_dir)