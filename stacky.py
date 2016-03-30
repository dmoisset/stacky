#!/usr/bin/env python3
import sys
import parser, evaluator

fn = sys.argv[1]
program = parser.parse(open(fn, "rb"))
evaluator.evaluator(program)
