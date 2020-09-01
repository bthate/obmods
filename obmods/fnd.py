# OB - write your own commands.
#
# find (fnd)

"find objects."

# imports

import os, time
import olib

from olib import cdir, find, format, fntime, get, keys
from ob.prs import elapsed, parse
from ob.utl import find_shorts

# defines

def __dir__():
    return ("fnd",)

# commands

def fnd(event):
    "!fnd <loweredclassname> - find object by provding key==value pairs"
    if not event.args:
        wd = os.path.join(olib.workdir, "store", "")
        cdir(wd)
        fns = os.listdir(wd)
        fns = sorted({x.split(os.sep)[0] for x in fns})
        if fns:
            event.reply("|".join(fns))
        return
    parse(event, event.txt)
    otype = event.args[0]
    shorts = find_shorts("ob")
    otypes = get(shorts, otype, [otype,])
    args = list(keys(event.gets))
    try:
        arg = event.args[1:]
    except ValueError:
        arg = []
    args.extend(arg)
    nr = -1
    for otype in otypes:
        for o in find(otype, event.gets, event.index, event.timed):
            nr += 1
            if "f" in event.opts:
                pure = False
            else:
                pure = True
            txt = "%s %s" % (str(nr), format(o, args, pure))
            if "t" in event.opts:
                txt += " %s" % (elapsed(time.time() - fntime(o.__stamp__)))
            event.reply(txt)
    if nr == -1:
        event.reply("no matching objects found.")
