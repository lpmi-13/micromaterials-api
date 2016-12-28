# -*- coding: utf-8 -*-

import json


def json_pretty(data):
    return json.dumps(data, indent=2)
