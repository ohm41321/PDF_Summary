# -*- coding: utf-8 -*-
"""
PyInstaller hook for uvicorn
"""

hiddenimports = [
    'uvicorn',
    'uvicorn.logging',
    'uvicorn.loops',
    'uvicorn.loops.auto',
    'uvicorn.protocols',
    'uvicorn.protocols.http',
    'uvicorn.protocols.http.auto',
    'uvicorn.protocols.http.h11_impl',
    'uvicorn.protocols.http.httptools_impl',
    'uvicorn.protocols.websockets',
    'uvicorn.protocols.websockets.auto',
    'uvicorn.protocols.websockets.websockets_impl',
    'uvicorn.protocols.websockets.wsproto_impl',
    'uvicorn.lifespan',
    'uvicorn.lifespan.on',
    'uvicorn.main',
    'uvicorn.config',
    'uvicorn.server',
    'uvicorn.supervisors',
    'uvicorn.supervisors.multiprocess',
    'uvicorn.supervisors.statreload',
    'uvicorn.supervisors.h11_impl',
    'uvicorn.workers',
    'h11',
    'httptools',
    'websockets',
    'wsproto',
]
