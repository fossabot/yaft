"""Contains the main function."""

from peewee import PostgresqlDatabase
from .config import parse_config_file
from .models import (
    database_proxy,
    migrate_database,
)
from .runtime_args import parse_runtime_args


def main():
    """The main function."""
    # Get runtime arguments
    cli_args = parse_runtime_args()

    # Parse config file
    config_dict = parse_config_file(config_path=cli_args.config)

    # Connect to database
    db = PostgresqlDatabase(
        database=config_dict['postgres-database-name'],
        user=config_dict['postgres-database-user'],
        password=config_dict['postgres-database-user-password'],
        host=config_dict['postgres-database-host'],
        port=config_dict['postgres-database-port'], # TODO: this *might* need to be an int
    )

    database_proxy.initialize(db)

    # Do specific things based on the sub-command passed in
    if cli_args.subcommand is None:
        # Default action here
        print("This is a default")
    elif cli_args.subcommand == 'migrate':
        # Migrate the database and exit
        # TODO: add some kind of warning here, I think this might drop
        # existing tables and recreate them
        migrate_database(db)
