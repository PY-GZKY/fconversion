import subprocess
import sys


def get_configuration_():
    if sys.platform == 'win32':
        wkhtmltopdf_path = "E:/Py_Word_Code/fconversion/src/bin/wkhtmltoimage.exe"
    else:
        for find_cmd in ("where", "which"):
            try:
                wkhtmltopdf_path = (
                    subprocess.check_output([find_cmd, "wkhtmltoimage"]).strip().decode("utf-8")
                )
                break
            except subprocess.CalledProcessError:
                wkhtmltopdf_path = "command not found"
            except OSError:
                wkhtmltopdf_path = "command not found"

    return wkhtmltopdf_path
