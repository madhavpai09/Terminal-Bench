import click
import sys
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if base_dir not in sys.path:
    sys.path.append(base_dir)

from client import client_user

@click.command("import_csv")
@click.option("--file", help="Path to the CSV file", prompt="filename")
def import_csv(file):
    result = client_user.import_csv_request(os.path.abspath(file))
    if "error" in result:
        click.secho(f"Error: {result['error']}")
    else:
        click.secho(f"Success: {result['message']}")

if __name__ == '__main__':
    import_csv()
