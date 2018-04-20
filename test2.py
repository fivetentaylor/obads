#!/usr/bin/env python

import pudb
import json

types = {
    'Int': (),
    'Func': (),
}

lut = {
    'print': lambda code: print(code),
    'lut': lambda _: print(lut),
}

WHITESPACE = ' \t\n\r'

def def_func(code):
    if len(code) != 3:
        raise 'Invalid type for def'

    def new_func(params):
        if len(code[1]) != len(params):
            raise 'Invalid type for %s' % code[0]

        # bind new params
        for k,v in zip(code[1], params):
            lut[k] = v

        run(code[2])

    lut[code[0]] = new_func

lut['def'] = def_func

def parse_sym(source, i_beg):
    i_end = i_beg + 1
    while i_end < len(source):
        if source[i_end] in WHITESPACE + '()':
            break
        i_end += 1

    return i_end, ('sym', source[i_beg: i_end])

def parse_number(source, i_beg):
    pass

def parse_string(source, i_beg):
    i_end = i_beg + 1
    while i_end < len(source):
        if source[i_end] == "'":
            break

        # skip past escaped char
        i_end += int(source[i_end] == "\\")
        i_end += 1

    return i_end+1, ('str', source[i_beg: i_end])

def parse(source, ix):
    program = []

    while ix < len(source):
        c = source[ix]

        if c == ')':
            return ix+1, program

        if c in WHITESPACE:
            ix += 1
            continue
        
        if c == "'": 
            ix, s = parse_string(source, ix+1)
        elif c == '(':
            ix, s = parse(source, ix+1)
        else:
            ix, s = parse_sym(source, ix)

        program.append(s)

    return ix, ('code', program)

def run(program):
    i = 0
    while i < len(program):
        p = program[i]

        if type(p) is list:
            run(p)
        elif p in lut:
            i += 1
            if i < len(program):
                lut[p](program[i])

        i += 1

while True:
    _, program = parse(input('> '), 0)
    print(json.dumps(program))
    run(program)
