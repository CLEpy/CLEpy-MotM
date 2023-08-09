import argparse
from pathlib import Path
from pprint import pprint

parser = argparse.ArgumentParser("")
sub_parser = parser.add_subparsers(
    dest="command", title="available commands", metavar="command [options ...]"
)

y2b_parser = sub_parser.add_parser("yaml2bookmark", help="Convert YAML to bookmark.")
b2y_parser = sub_parser.add_parser("bookmark2yaml", help="Convert bookmark to YAML.")


y2b_parser.add_argument("yaml_path", metavar="INPUT", help="YAML file.", type=Path)
y2b_parser.add_argument(
    "-o",
    "--output-bookmark",
    help="output bookmark file.",
    default="bookmarks.html",
    type=Path,
)

b2y_parser.add_argument("html_path", metavar="INPUT", help="Bookmark file.", type=Path)
b2y_parser.add_argument(
    "-o",
    "--output-yaml",
    help="output yaml file.",
    default="bookmarks.yaml",
    type=Path,
)


def main():
    cmd_args = parser.parse_args()

    if cmd_args.command == "yaml2bookmark":
        print("Parsing yaml2bookmark Command")
        pprint(vars(cmd_args), compact=True)
    elif cmd_args.command == "bookmark2yaml":
        print("Parsing bookmark2yaml Command")
        pprint(vars(cmd_args), compact=True)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
