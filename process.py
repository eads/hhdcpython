#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Data processing script for the Hacks/Hackers DC workshop.

This is the file we'll be editing.
"""
import os

HHDC_ROOT = os.path.dirname(os.path.realpath(__file__))
HHDC_DATA_FILE = os.path.join(HHDC_ROOT, 'data/MC_por_SGAR-trimmed.txt')
HHDC_OUTPUT_DIRECTORY = os.path.join(HHDC_ROOT, 'output')


def process_data():
    """
    Process data.

    You must modify this function to shape the data the way you need.
    """

    # Make an empty list to hold the processed data.
    output_list = list()

    # Open the data file
    with open(HHDC_DATA_FILE) as datafile:
        data = datafile.read().splitlines()

    # Loop over each line of the data file. Each time the loop runs, the current
    # line is assigned to a variable called `line`.
    for line in data:

        # Remove any whitespace characters from beginning and end of line
        line = line.strip()

        # If the line is not empty, add it to the output
        if line != '':
            output_list.append(line)

    # Return the processed data
    return output_list

"""
This cryptic thing calls our process data function when the file is run
from the command line or from PythonAnywhere using the ">>>" icon.
"""
if __name__ == '__main__':
    # Print start message.
    print('It works! Running `process_data()`')

    # Assign return values of `process_data()` function to `output` variable.
    output = process_data()

    # Print the `output` variable.
    print('Here is the first line of output data:')
    print('    {0}'.format(output[0]))
    print('See you in class!')

    # Print that we're done.
    print('Done.')
