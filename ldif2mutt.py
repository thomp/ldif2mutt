#!/usr/bin/python3
# -*- coding: utf-8 -*-

# (c) 2016 David A. Thompson <thompdump@gmail.com>
#
# ldif2mutt.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ldif2mutt.py is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with ldif2mutt.py. If not, see <http://www.gnu.org/licenses/>.

#
# ldif2mutt.py myaddresses.ldif
#
#   accept an LDIF file and 
#   extract address data therein
#
import argparse
import os
import sys
import ldif3

import imp
import json

import logging

import json1

# define logger
lg = logging

try:
    imp.find_module('ldif3')
except ImportError:
    lg.error(json1.json_msg_module_not_accessible('ldif3'))
    sys.exit()
import ldif3

def ldif2mutt(ldif_file_spec):
    """Parse file specified by LDIF_FILE_SPEC, generating corresponding mutt alias entries. LDIF_FILE_SPEC is a string specifying a single file."""
    # DEBUGP should be either True or False (any other value will interpreted as False)
    debugp = False
    ldif_file = ldif_file_spec[0]    
    parser = ldif3.LDIFParser(open(ldif_file, 'rb'))
    for dn, entry in parser.parse():
        mail = entry['mail']
        mail = mail[0]
        disp_name = entry['displayName']
        disp_name = disp_name[0]
        # attempt to distinguish between several possibilities:
        # 1. displayName is the same as mail
        # 2. displayName corresponds to actual name of individual
        mail_only_p = False
        if "@" in disp_name:
            mail_only_p = True
        if mail_only_p:
            nick = disp_name.replace(" ", "")
            nick = downcase_char(nick,0);
            print('alias {} {}'.format(nick, mail))
        else:
            nick = disp_name.replace(" ", "")
            nick = downcase_char(nick,0); 
            # use quoted string and angle address (RFC 5322) for email
            print('alias {} "{}" <{}>'.format(nick, disp_name, mail))


def downcase_char(s,n):
    """Make character at position N downpercase."""
    return s[:n] + s[n].lower() + s[n+1:]


def main():
    """Handle command-line invocation of busca.py. Expect all arguments to be filenames for PDF files."""
    parser = argparse.ArgumentParser(description="This is ldif2mutt.py") 
    parser.add_argument("input_files", help="one or more input (LDIF) files", nargs="+", type=str)
    args = parser.parse_args()
    #
    # define logging (level, file, message format, ...)
    #
    log_level = 40 # args.log_level
    if isinstance(log_level, int) and log_level >= 0 and log_level <= 51:
        log_level = log_level
    else:
        # standard python default
        #log_level = logging.WARN
        # since this function doesn't necessarily exit quickly
        log_level = logging.INFO
    logfile = 'ldif2mutt.log'
    debug_log_format = '%(levelname)s:%(funcName)s:%(message)s'
    json_log_format = '%(message)s'
    lg.basicConfig(filename=logfile, filemode='w', level=log_level, format=json_log_format)
    ldif_files = args.input_files
    lg.debug("ldif_files: %s", ldif_files)
    ldif2mutt(ldif_files)


if __name__ == "__main__":
    main()
