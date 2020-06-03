#!/usr/bin/python3
"""
this module imports json
"""
import json
from sys import argv


save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

try:
    l_a_s = load_from_json_file("add_item.json")
except FileNotFoundError:
    l_a_s = []

l_a_s = l_a_s + argv[1:]
save_to_json_file(l_a_s, "add_item.json")
