#syncasa
### Synchronise your Picasa folder with your machine

Keep your account in sync with your machine, without thinking about it.
It's just a little hack I use to publish albums easily, so don't expect much
from it.

The sync is done local -> google, and local is considered to be the truth.
Nothing that happens online is taken into account, also if you change an album
name online, some weird stuff may happens.

## install

    python setup.py install

That's it.

## usage

Just give syncasa the path of the folder you want to keeep synchronised with
your Picasa account.
If your credential files does not exists, syncasa will help you create one.

    syncasa /path/to/my/folder

For the help, as usual :

    syncasa -h

## blacklist

There is a blacklist feature, if you have an album online and you don't want
syncasa to touch it.
Look at the config example to see how to do it.

That's about it :)
