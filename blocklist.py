"""
blocklist.py

This file just contains the blocklist of the KWT tokens. It will be imported by
app and logout resource so that tokens can be added to the blocklist when the user logs out.
"""
BLOCKLIST = set()