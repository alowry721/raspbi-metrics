import logging, os
from datetime import datetime

logger = logging.getLogger('metrics')
formatter = logging.Formatter('%(asctime)s, %(message)s')


def get_timestamp():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')


def add_logging_args(parser):
    parser.add_argument('--verbose', action='store_true', default=False)
    parser.add_argument('--output_file', '-o', help='Store console output to file specified')


def add_logging(args):
    if args.output_file is not None:
        _add_logging_file(args.output_file)
    _add_logging_std(args.verbose)


def _add_logging_file(file_name):
    file_dir = os.path.abspath(os.path.dirname(__file__))
    level = _get_log_level(verbose=True)
    fh = logging.FileHandler(os.path.join(file_dir, file_name))
    fh.setLevel(level)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

def _add_logging_std(verbose=False):
    level = _get_log_level(verbose=verbose)
    ch = logging.StreamHandler()
    ch.setLevel(level)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

def _get_log_level(verbose=False):
    if verbose:
        return logging.DEBUG
    return logging.INFO
