#!/usr/bin/env python
# coding=utf-8
"""
# pychee: Client for Lychee, written in Python.

For additional information, visit: https://github.com/LycheeOrg/Lychee.
"""

from dataclasses import dataclass

@dataclass
class AlbumTree:
    """Album Tree Response."""
    id: str