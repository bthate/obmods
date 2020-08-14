# OB - the object library !
#
#

import ob, os, sys, time

from ob.dbs import Db
from ob.prs import parse
from ob.tms import elapsed, fntime
from ob.isp import find_shorts
from ob.utl import cdir

def fnd(event):
    if not event.args:
        wd = os.path.join(ob.workdir, "store", "")
        cdir(wd)
        fns = os.listdir(wd)
        fns = sorted({x.split(os.sep)[0] for x in fns})
        if fns:
            event.reply("|".join(fns))
        return
    parse(event, event.txt)
    db = Db()
    otype = event.args[0]
    shorts = find_shorts("ob")
    otypes = ob.get(shorts, otype, [otype,])
    args = list(ob.keys(event.gets))
    try:
        arg = event.args[1:]
    except ValueError:
        arg = []
    args.extend(arg)
    nr = -1
    for otype in otypes:
        for o in db.find(otype, event.gets, event.index, event.timed):
            nr += 1
            if "f" in event.opts:
                pure = False
            else:
                pure = True
            txt = "%s %s" % (str(nr), ob.format(o, args, pure))
            if "t" in event.opts:
                txt += " %s" % (elapsed(time.time() - fntime(o.__stamp__)))
            event.reply(txt)
    if nr == -1:
        event.reply("no matching objects found.")
