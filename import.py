import os

HHDC_ROOT = os.path.dirname(os.path.realpath(__file__))
HHDC_DATA_FILE = os.path.join(HHDC_ROOT, 'data/data.csv')
HHDC_OUTPUT_DIRECTORY = os.path.join(HHDC_ROOT, 'output')

if __name__ == '__main__':
    print(HHDC_DATA_FILE)
    print(HHDC_OUTPUT_DIRECTORY)
