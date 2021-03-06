# -*- coding: utf-8 -*-
"""
ENERPIWEB __main__
    - Install configuration & CRON task for web resources generation
    - Uninstall CRON task
    - Run Flask server

"""
import os
# noinspection PyUnresolvedReferences
from enerpiweb import app as application
from enerpiweb import SERVER_FILE_LOGGING, LOGGING_LEVEL_SERVER
from enerpiweb.command_enerpiweb import main, check_resource_files
from enerpi.base import set_logging_conf


# logging conf
check_resource_files(os.path.dirname(SERVER_FILE_LOGGING), verbose=True)
set_logging_conf(SERVER_FILE_LOGGING, level=LOGGING_LEVEL_SERVER,
                 verbose=True, with_initial_log=True)


if __name__ == '__main__':
    # Para ejecutar 'a mano'
    main()
