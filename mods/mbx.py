# BOTLIB - the bot library
#
#

import mailbox, ob, os, time

from ob.dbs import Db
from ob.prs import parse
from ob.tms import elapsed, fntime

bdmonths = ['Bo', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug',
            'Sep', 'Oct', 'Nov', 'Dec']

monthint = {
    'Jan': 1,
    'Feb': 2,
    'Mar': 3,
    'Apr': 4,
    'May': 5,
    'Jun': 6,
    'Jul': 7,
    'Aug': 8,
    'Sep': 9,
    'Oct': 10,
    'Nov': 11,
    'Dec': 12
}

class Email(ob.Object):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.text = ""

def to_date(date):
    date = date.replace("_", ":")
    res = date.split()
    ddd = ""
    try:
        if "+" in res[3]:
            raise ValueError
        if "-" in res[3]:
            raise ValueError
        int(res[3])
        ddd = "{:4}-{:#02}-{:#02} {:6}".format(res[3], monthint[res[2]], int(res[1]), res[4])
    except (IndexError, KeyError, ValueError):
        try:
            if "+" in res[4]:
                raise ValueError
            if "-" in res[4]:
                raise ValueError
            int(res[4])
            ddd = "{:4}-{:#02}-{:02} {:6}".format(res[4], monthint[res[1]], int(res[2]), res[3])
        except (IndexError, KeyError, ValueError):
            try:
                ddd = "{:4}-{:#02}-{:02} {:6}".format(res[2], monthint[res[1]], int(res[0]), res[3])
            except (IndexError, KeyError):
                try:
                    ddd = "{:4}-{:#02}-{:02}".format(res[2], monthint[res[1]], int(res[0]))
                except (IndexError, KeyError):
                    try:
                        ddd = "{:4}-{:#02}".format(res[2], monthint[res[1]])
                    except (IndexError, KeyError):
                        try:
                            ddd = "{:4}".format(res[2])
                        except (IndexError, KeyError):
                            ddd = ""
    return ddd

def cor(event):
    if not event.args:
        event.reply("cor <email>")
        return
    parse(event, event.txt)
    event.gets["From"] = event.args[0]
    event.args = list(ob.keys(event.gets)) + event.rest.split()
    event.otype = "mods.mbx.Email"
    nr = -1
    db = Db()
    for email in db.find_event(event):
        nr += 1
        event.reply("%s %s %s" % (nr, ob.format(email, event.args, True, event.skip), elapsed(time.time() - fntime(email.__stamp__))))

def eml(event):
    parse(event, event.txt)
    event.args = ["From"] + list(ob.keys(event.gets)) + event.rest.split()
    event.otype = "bot.mbx.Email"
    nr = -1
    db = Db()
    for o in db.find_event(event):
        nr += 1
        event.reply("%s %s %s" % (nr, ob.format(o, event.args, True, event.skip), elapsed(time.time() - fntime(o.__stamp__))))

def mbx(event):
    if not event.args:
        event.reply("mbx <path>")
        return
    fn = os.path.expanduser(event.args[0])
    event.reply("reading from %s" % fn)
    nr = 0
    if os.path.isdir(fn):
        thing = mailbox.Maildir(fn, create=False)
    elif os.path.isfile(fn):
        thing = mailbox.mbox(fn, create=False)
    else:
        event.reply("need a mbox or maildir.")
        return
    try:
        thing.lock()
    except FileNotFoundError:
        pass
    for m in thing:
        o = Email()
        ob.update(o, m)
        try:
            sdate = os.sep.join(to_date(o.Date).split())
        except AttributeError:
            sdate = None
        o.text = ""
        for payload in m.walk():
            if payload.get_content_type() == 'text/plain':
                o.text += payload.get_payload()
        o.text = o.text.replace("\\n", "\n")
        ob.save(o, stime=sdate)
        nr += 1
    if nr:
        event.reply("ok %s" % nr)
