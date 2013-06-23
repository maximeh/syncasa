#syncasa

syncasa helps you keep in sync a folder on your machine and your albums online
on G+ (originally it worked with Picasa, but Picasa is now the backend photo of
        G+)

The way I use it is pretty simple, I have a folder in which I put all the albums
I want to appear online so I can share pictures with my family and friends
without the hassle.
G+ photos is kind of my own private photo gallery.

### Synchronise with Google+

Keep your albums in sync with G+ without thinking about it.
It's just a little hack I use to publish albums easily, so don't expect much
from it.

The sync works only in one way: local --> G+
So local is considered to be the truth, any change you do online will be lost.
But any change you will do locally (or on your remote machine) will be done
online.

## install

    python setup.py install

That's it.

## usage

Just give syncasa the path to the folder that keeps the albums you want to keeep
synchronised with your G+ account.
If your credential files does not exists, syncasa will help you create one.

    syncasa /path/to/my/folder

For the help, as usual :

    syncasa -h

## blacklist

There is a blacklist feature, if you have an album online and you don't want to
syncchronise it.
Look at the config example to see how to do it.

Note: There is almost always a "Profile Picture" album that will exists,
    I *strongly* suggest that you put it in the blacklist, otherwise, it will be
    deleted and you'll lost your avatar.

That's about it :)
