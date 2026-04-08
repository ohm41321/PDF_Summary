# -*- coding: utf-8 -*-
"""
PyInstaller hook for PyMuPDF (fitz)
"""

from PyInstaller.utils.hooks import collect_data_files, collect_dynamic_libs

datas = collect_data_files('fitz')
binaries = collect_dynamic_libs('fitz')
hiddenimports = ['fitz', 'PyMuPDF']
