# -*- coding: utf-8 -*-
"""
PyInstaller hook for EasyOCR
"""

from PyInstaller.utils.hooks import collect_data_files, collect_dynamic_libs

datas = collect_data_files('easyocr')
binaries = collect_dynamic_libs('easyocr')
hiddenimports = ['easyocr', 'easyocr.easyocr', 'easyocr.utils']
