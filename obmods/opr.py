# OB - the object library !
#
#

import ob, os, threading, time

from ob.dbs import Db, last
from ob.err import ENOCLASS
from ob.isp import find_shorts
from ob.krn import Cfg, k, starttime
from ob.prs import parse
from ob.tms import elapsed, fntime
from ob.utl import cdir, get_cls, get_type

def __dir__():
    return ("edt", "fnd", "krn", "tsk", "ver", "wd")

def list_files(wd):
    path = os.path.join(wd, "store")
    if not os.path.exists(path):
        return ""
    return "|".join(os.listdir(path))

def edt(event):
    if not event.args:
        event.reply(list_files(ob.workdir) or "no files yet")
        return
    cn = event.args[0]
    shorts = find_shorts("mods")
    if shorts:
        cn = shorts[0]
    db = Db()
    l = db.last(cn)
    if not l:
        try:
            c = get_cls(cn)
            l = c()
            event.reply("created %s" % cn)
        except ENOCLASS:
            event.reply(list_files(ob.workdir) or "no files yet")
            return
    if len(event.args) == 1:
        event.reply(l)
        return
    if len(event.args) == 2:
        setter = {event.args[1]: ""}
    else:
        setter = {event.args[1]: event.args[2]}
    ob.edit(l, setter)
    ob.save(l)
    event.reply("ok")

def krn(event):
    event.reply(k)

def tsk(event):
    psformat = "%-8s %-50s"
    result = []
    for thr in sorted(threading.enumerate(), key=lambda x: x.getName()):
        if str(thr).startswith("<_"):
            continue
        d = vars(thr)
        o = ob.Object()
        ob.update(o, d)
        if ob.get(o, "sleep", None):
            up = o.sleep - int(time.time() - o.state.latest)
        else:
            up = int(time.time() - starttime)
        result.append((up, thr.getName(), o))
    nr = -1
    for up, thrname, o in sorted(result, key=lambda x: x[0]):
        nr += 1
        res = "%s %s" % (nr, psformat % (elapsed(up), thrname[:60]))
        if res:
            event.reply(res.rstrip())

def ver(event):
    from ob.krn import __version__
    event.reply("OB %s" % __version__)
    for mod in k.walk("mods"):
        try:
            event.reply("%s %s" % (mod.__name__, mod.__version__))
        except AttributeError:
            continue

def wd(event):
    event.reply(ob.workdir)
