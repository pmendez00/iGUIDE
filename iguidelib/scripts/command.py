import sys
import argparse
import subprocess
import iguidelib
#from iguidelib.scripts.run import main as Run
#from iguidelib.scripts.init import main as Init
#from iguidelib.scripts._config import main as Config
#from iguidelib.scripts.list_samples import main as ListSamples
#from iguidelib.scripts.get import main as Get

def main():

    usage_str = "%(prog)s [-h/--help,-v/--version] <subcommand>"
    description_str = (
        "subcommands:\n"
        "  init         \tCreate a new config file for a project using local data.\n"
        "  get          \tCreate a new config file for a project using SRA data.\n"
        "  run          \tExecute the pipeline.\n"
        "  config       \tModify or update config files.\n"
        "  list_samples \tMake a list of samples from a directory.\n"
    ).format(version=iguidelib.__version__)

    parser = argparse.ArgumentParser(
        prog="iguide",
        usage=usage_str,
        description=description_str,
        epilog="For more help, see the docs at http://iguide.readthedocs.io.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        add_help=False
    )

    parser.add_argument("command", help=argparse.SUPPRESS, nargs="?")
    parser.add_argument(
        "-v", "--version", action="version",
        version="%(prog)s v{}".format(iguidelib.__version__))

    args, remaining = parser.parse_known_args()

    if args.command == "run":
        Run(remaining)
    elif args.command == "init":
        Init(remaining)
    elif args.command == "config":
        Config(remaining)
    elif args.command == "list_samples":
        ListSamples(remaining)
    elif args.command == "get":
        Get(remaining)
    else:
        parser.print_help()
        sys.stderr.write("Unrecognized command.\n")
