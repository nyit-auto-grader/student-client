import sys, os

sys.path.insert(0, os.getcwd())

if __name__ == '__main__':
    from autograder.parser import build_parser
    from autograder.handlers import handlers
    from getpass import getpass

    if __name__ == '__main__':

        parser = build_parser()
        args = parser.parse_args()

        if args.github and not args.password:
            args.password = getpass('enter your github password: ')

        # TODO: check password

        handlers[args.command](**args.__dict__)
