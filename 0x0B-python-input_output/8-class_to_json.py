#!/usr/bin/bash
""" script to return a dict representation from an object """
import json


def class_to_json(obj):
    """
    returns a ditionary

    """
    return obj.__dict__
