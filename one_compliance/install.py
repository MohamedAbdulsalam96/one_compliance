# Copyright (c) 2023, efeone and contributors
# For license information, please see license.txt

import click

# import frappe


def after_install():
    try:
        print("Setting up One Compliance")
        click.secho("Thank you for installing One Compliance!", fg="green")

    except Exception as e:
        BUG_REPORT_URL = "https://github.com/efeone/one_compliance/issues/new"
        click.secho(
            "Installation for One Compliance app failed due to an error."
            " Please try re-installing the app or"
            f" report the issue on {BUG_REPORT_URL} if not resolved.",
            fg="bright_red",
        )
        raise e
