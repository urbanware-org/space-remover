#!/usr/bin/env python

# ============================================================================
# space-remover - Script to remove trailing spaces and tabs from files
# Copyright (C) 2018 by Ralf Kilian
# Distributed under the MIT License (https://opensource.org/licenses/MIT)
#
# GitHub: https://github.com/urbanware-org/space-remover
# GitLab: https://gitlab.com/urbanware-org/space-remover
# ============================================================================

__version__ = "1.1.0"

import os
import shutil
import sys
import tempfile

temp = "spacerem_" + str(os.getpid()) + ".tmp"

file_in = sys.argv[1]
file_out = os.path.join(tempfile.gettempdir(), temp)

if not os.path.exists(file_in):
    print "error: The file '%s' does not exist" % file_in
    sys.exit(1)

if os.path.isfile(file_in):
    fh_input = open(file_in, "r")
    fh_output = open(file_out, "w")

    for line in fh_input:
        # Remove tabs at the end of lines
        while "\t\n" in line:
            line = line.replace("t\n", "\n")
        while "\t\r\n" in line:
            line = line.replace("\t\r\n", "\r\n")
            
        # Remove spaces at the end of lines
        while " \n" in line:
            line = line.replace(" \n", "\n")
        while " \r\n" in line:
            line = line.replace(" \r\n", "\r\n")

        # Write output
        fh_output.write(line)

    fh_input.close()
    fh_output.close()

    shutil.move(file_out, file_in)
else:
    print "error: The path '%s' is not a file" % file_in
    sys.exit(1)

# EOF
