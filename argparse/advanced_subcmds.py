import argparse
from functools import wraps
from pathlib import Path
from pprint import pprint

parser = argparse.ArgumentParser("")
sub_parsers = parser.add_subparsers(
    dest="command", title="available commands", metavar="command [options ...]"
)


def argument(*args, **kwargs):
    return args, kwargs


def command(*arguments, help_: str = "⎼", parent=sub_parsers):
    def decorator(func):
        group_store = {}
        func_name = func.__name__.replace("_", "-")
        func_descr = func.__doc__

        cmd_parser = parent.add_parser(func_name, description=func_descr, help=help_)

        @wraps(func)
        def wrapper(kwargs):
            return func(**{"cmd_parser": cmd_parser, **vars(kwargs)})

        for args in arguments:
            cmd_args, cmd_kwargs = args

            if "exclusive_group" in cmd_kwargs:
                group_key = cmd_kwargs.pop("exclusive_group")

                if group_key not in group_store:
                    group_store[group_key] = cmd_parser.add_mutually_exclusive_group()

                group_store[group_key].add_argument(*cmd_args, **cmd_kwargs)
            else:
                cmd_parser.add_argument(*cmd_args, **cmd_kwargs)
            cmd_parser.set_defaults(func=wrapper)

    return decorator


@command(
    argument(
        "yaml_path",
        metavar="INPUT ...",
        nargs="?",
        type=Path,
        help_="YAML file.",
    ),
    argument(
        "-o",
        "--output-bookmark",
        dest="output_bookmark",
        default="bookmarks.html",
        help_="output bookmark file.",
        type=Path,
    ),
    help_="Convert YAML to bookmark.",
)
def yaml2bookmark(yaml_path: Path, output_bookmark: Path, **meta_args):
    """Converts a YAML file to a HTML bookmark file"""
    print("Parsing yaml2bookmark Command")
    print(f"{yaml_path=}, -> {output_bookmark=}")
    pprint(meta_args, compact=True)


@command(
    argument(
        "html_path",
        metavar="INPUT ...",
        nargs="?",
        type=Path,
        help_="Bookmark file.",
    ),
    argument(
        "-o",
        "--output-yaml",
        dest="output_yaml",
        default="bookmarks.yaml",
        help_="output yaml file.",
        type=Path,
    ),
    help_="Convert bookmark to YAML.",
)
def bookmark2yaml(html_path: Path, output_yaml: Path, **meta_args):
    print("Parsing bookmark2yaml Command")
    print(f"{html_path=}, -> {output_yaml=}")
    pprint(meta_args, compact=True)


def main():
    cmd_args = parser.parse_args()

    if cmd_args.command is None:
        parser.print_help()
    else:
        cmd_args.func(cmd_args)


if __name__ == "__main__":
    main()
