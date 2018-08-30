# coding=utf-8
""" Copyright (C) 2011 Javier Rivera
    This file is free software: you can redistribute it and/or modify it under
    the terms of the GNU Lesser General Public License as published by the Free
    Software Foundation, either version 3 of the License, or (at your option)
    any later version.

    You should have received a copy of the GNU Lesser General Public License
    along with this file.  If not, see <http://www.gnu.org/licenses/>.

"""

from distutils.core import setup

from descargar import VERSION

import sys

try:
    import py2exe
except ImportError:
    pass  # We are likely not running this under windows.

descripcion_larga = "Un programa simple para descargar partidas de Umbria"

if sys.platform[:3] == 'win':
    setup(
        name='exportadorUmbria',
        version=VERSION,
        packages=['umbria'],
        scripts=['descargar.py'],
        maintainer='Javier Rivera',
        maintainer_email='javier@isotecsl.com',
        description='Descargador para www.comunidadumbria.com',
        long_description=descripcion_larga,
        url='https://github.com/javierriveracastro/exportadorUmbria/tree/gui',
        download_url='https://github.com/javierriveracastro/exportadorUmbria'
                     '/tree/gui',
        windows=[{'script': 'descargar.py'}],
        options={'py2exe': {'includes': ['sip']}},
        )
else:
    setup(
        name='exportadorUmbria',
        version=VERSION,
        packages=['umbria'],
        scripts=['descargar.py'],
        maintainer='Javier Rivera',
        maintainer_email='javier@isotecsl.com',
        description='Descargador para www.comunidadumbria.com',
        long_description=descripcion_larga,
        license='GPLv2',
        url='https://launchpad.net/notificadorumbria',
        download_url='https://github.com/javierriveracastro/exportadorUmbria'
                     '/tree/gui',
        )
