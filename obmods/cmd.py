# OB - the object library
#
#

from ob.krn import k

def cmd(event):
    event.reply(",".join(k.cmds))