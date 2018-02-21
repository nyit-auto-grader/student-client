import argparse


def build_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--github', type=str, help='github username')
    parser.add_argument('--password', type=str, help='github password')
    parser.add_argument('--organization', type=str, help='github classroom organization', default='csci125-spring2018')
    parser.add_argument('command', type=str, choices=['list-projects', 'submit-project'])
    return parser
