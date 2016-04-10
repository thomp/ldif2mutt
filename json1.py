# -*- coding: utf-8 -*-

# (c) 2014,2015 David A. Thompson <thompdump@gmail.com>
#
# This file is part of Busca
#
# Busca is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Busca is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Busca. If not, see <http://www.gnu.org/licenses/>.

import json


#
# convenience functions for returning, as strings, JSON-encoded messages and data
#
def json_msg(code,message,outfile):
    """Return a string or, if outfile is a string, send to the file corresponding to outfile."""
    # if appendp is True (the default), create file if nonexistent; append if existent
    appendp=True
    if appendp:
        openMode='a+'
    else:
        openMode='w+'
    obj = {
        'code': code,
        'message': message
    }
    if outfile:
        with open(outfile, openMode) as outfp:
            json.dump(obj, outfp)
    else:
        return json.dumps(obj)


#
# messages
#
def json_msg_barcode_not_found(files,msg):
    """FILES is an array where each member is a string specifying the location of a diagnostic image file. MSG is additional data encapsulated as a string"""
    message = 'Anticipated a barcode but barcode was not found; see diagnostic image file(s) at {}'.format(files)
    if msg:
        message = message + '; ' + msg;
    return json_msg(135, message, False)


def json_blank_page_on_deskew(file):
    """Return a string"""
    obj = {
        'code': 121,
        'message': "encountered blank page on attempt to deskew",
        'file': file
        }
    return json.dumps(obj)


def json_completed_pdf_to_ppm(page_number,number_of_pages):
    """Return a string"""
    obj = {
        'code': 11,
        'message': 'Completed PDF to PPM conversion: page {} / {}'.format(page_number,number_of_pages),
        }
    return json.dumps(obj)


def json_converting_pdf(file):
    """Return a string"""
    obj = {
        'code': 0,
        'message': "Converting the PDF to PNG images... this may take some time...",
        'file': file
        }
    return json.dumps(obj)


def json_msg_executable_not_accessible(executable_name):
    """EXECUTABLE_NAME is a string."""
    return json_msg(134,
             'The executable ' + executable_name + ' is not accessible. Is it installed?',
             False)


def json_failed_to_convert_pdf(exception,PDFFileSpec):
    return json_msg(110,
             'failed to convert PDF to PNG(s): {} {}'.format(exception,PDFFileSpec),
             False
    )


def json_failed_to_deskew(pngFile,pageNumber,comment=''):
    return json_msg(120,
             'failed to deskew {} at page {} {}'.format(pngFile,pageNumber,comment),
             False)


def json_failed_to_parse_file(someFile):
    return json_msg(131,
             'failed to parse {}'.format(someFile),
             False)


def json_zero_page_test(xyFile):
    return json_msg(132,
             'XY file suggests that the test has 0 pages; file: {}'.format(xyFile),
             False)


def json_msg_bubble_not_found(files,msg):
    """FILES is an array where each member is a string specifying the location of a diagnostic image file. MSG is additional data encapsulated as a string"""
    message = 'anticipated a bubble at position but bubble was not found; see diagnostic image file at {}'.format(files)
    if msg:
        message = message + '; ' + msg
    return json_msg(133, message, False)


def json_msg_module_not_accessible(module_name):
    """MODULE_NAME is a string."""
    return json_msg(134,
             'The python module ' + module_name + ' is not accessible. Is it installed?',
             False)


def json_pdf_to_pngs_success(pdffile,pngfiles):
    """Return a string"""
    obj = {
        'code': 10,
        'message': "Successfully converted PDF to PNG(s)",
        'pdffile': pdffile,
        'pngfiles': pngfiles
        }
    return json.dumps(obj)


def json_scansets(scanSets):
    return json.dumps(scanSets)


def json_successful_deskew(file):
    """Return a string"""
    obj = {
        'code': 20,
        'message': "successful deskew",
        'file': file
        }
    return json.dumps(obj)
