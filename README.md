**clean.py**: Goes through your account and saves all of your comments, overwrites them with a single full stop, and then deletes them.

Technically, it goes through all of your comments, stores them in memory, does the overwrite and delete, and *then* stores them locally, which is something that was on my "fix this" list until the API was updated and I stopped commenting on Reddit. In my defense, this is intended for personal use, and it *is* a tool designed to nuke your entire account, one which requires you to set up an API token and enter your credentials into the script, so... I think the cap on it is pretty childproof.