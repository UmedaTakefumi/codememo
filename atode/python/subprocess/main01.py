#!/usr/bin/env python
# -*- coding:utf-8 -*-

import subprocess

subprocess.call(["ls", "-l"])

print("------------------------------------------------------")


cmd_opt = "-lasF"

subprocess.call(["ls", cmd_opt])



