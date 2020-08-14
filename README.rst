R E A D M E

OB is a object library and uses timestamped, type in filename, JSON stringified, files on filesystem backend.
OB has been placed in the Public Domain and contains no copyright or LICENSE.

if you need OB to have access to your local directory use this: 

 > export PYTHONPATH="."

this will add your current directory to the pythonpath so the packages in it can be found by OB.

installation is through pypi:

 > sudo pip3 install ob 


lastely, you can also run directly from the tarball, see https://pypi.org/project/ob/#files


U S A G E


OB has it's own CLI, you can run it by giving the ob command on the prompt, it will return with no response:

:: 

 $ ob
 $ 

you can use ob <cmd> to run a command directly:

::

 $ ob cmds
 cfg|cmd|cor|dne|edt|eml|flt|fnd|krn|log|mbx|tdo|tsk|upt|ver|wd

OB can load user defined modules from a "mods" directory, you can put your modules overthere.

if you run ob as root it will use /var/lib/ob/mods as the modules directory.


M O D U L E S


OB has the following modules:

::

    bus             - list of objects
    clk             - clock/repeater
    csl             - console
    dbs             - database
    err             - errors
    hdl             - handler
    isp             - introspect
    krn             - core handler
    obj             - base classes
    prs             - parse
    spc             - specifications
    tsk             - tasks
    tms             - time
    trc             - trace
    utl             - utilities


P R O G R A M M I N G


installing from the github repository is also possible:

 > git clone http://github.com/bthate/ob


commands look like this:

::

 def command(event):
     event.reply("ok")


H A V E   F U N 


enjoy the coding ! ;]


C O N T A C T


Bart Thate

bthate@dds.nl | botfather #dunkbots irc.freenode.net | https://pypi.org/project/ob 
