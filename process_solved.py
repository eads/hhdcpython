#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A solution to the Hacks/Hackers DC workshop exercise.

Feel free to study this code, but we aware that we'll be covering the
solution in class. This file is here so your instructor can complete the
task for the workshop.
"""

import csv
import os

HHDC_ROOT = os.path.dirname(os.path.realpath(__file__))
HHDC_DATA_FILE = os.path.join(HHDC_ROOT, 'data/MC_por_SGAR-trimmed.txt')
HHDC_OUTPUT_DIRECTORY = os.path.join(HHDC_ROOT, 'output')


def process_data():
    """
    Process data.
    """

    # Make an empty list to hold the processed data.
    output_list = list()

    # Open the data file
    with open(HHDC_DATA_FILE) as datafile:
        data = datafile.read().splitlines()

    # The first 10 lines are junk
    trimmed_data = data[9:]

    for line in trimmed_data:

        line = line.strip()
        line = line.replace('?', 'Ñ')

        if line.startswith('SGAR'):
            identifier, church = line.split(' ', 1)
            church = church.replace('"', '')
            church = church.title()

        elif not any([
                line == 'www.asociacionesreligiosas.gob.mx',
                line == '',
                line == 'Total',
                line == 'Nombre Completo',
                line.startswith('Página'),
                line.isdigit()
            ]):

            line = line.title()

            new_row = [line, church, identifier]
            output_list.append(new_row)

    return output_list

"""
This cryptic thing calls our process data function when the file is run
from the command line or from PythonAnywhere using the ">>>" icon.
"""
if __name__ == '__main__':
    print('Running `process_data()`')
    output = process_data()

    output_path = os.path.join(HHDC_OUTPUT_DIRECTORY, 'output.csv')
    with open(output_path, 'w') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(['name', 'church', 'identifier'])
        writer.writerows(output)

    print('Created {0}'.format(output_path))
    print('Done.')
