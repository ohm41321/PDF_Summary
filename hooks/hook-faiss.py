# -*- coding: utf-8 -*-
"""
PyInstaller hook for FAISS
"""

from PyInstaller.utils.hooks import collect_data_files, collect_dynamic_libs

datas = collect_data_files('faiss')
binaries = collect_dynamic_libs('faiss')
hiddenimports = ['faiss', 'faiss.cpu']
