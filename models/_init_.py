#!/usr/bin/python3
"""update storage"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
