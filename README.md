#syncasa
### Synchronise your Picasa folder with your machine

Keep your account in sync with your machine, without thinking about it.

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
