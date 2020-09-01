# OB - write your own commands.
#
#

"list of commands."

# imports

from ob.krn import get_kernel

# defines

def __dir__():
    return ("cmd",)

k = get_kernel()

# commands

def cmd(event):
    "!cmd - show list of commands."
    event.reply(",".join(sorted(k.cmds)))
