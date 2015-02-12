
BUS_NAME = "org.augeasproject.Augeas"
BUS_PATH = "/org/augeasproject/Augeas"

BUS_NAME = "org.example"
BUS_PATH = "/org/example"

import sys
import dbus
import dbus.service
from dbus.mainloop.glib import DBusGMainLoop
import gobject
import augeas



BUS_NAME = "org.augeasproject.Augeas"
BUS_PATH = "/org/augeasproject/Augeas"

BUS_NAME = "org.example.Augeas"
BUS_PATH = "/org/example/Augeas/1"

import sys
import dbus
import dbus.service
from dbus.mainloop.glib import DBusGMainLoop
import gobject
import augeas
from pprint import pprint

DBusGMainLoop(set_as_default=True)

def e(f):
    print "k"
    return dbus.service.method("org.foo.Bar")(f)

class DBusBackend(dbus.service.Object):
    name = None
    path = None

    def __init__(self, name):
        bus = dbus.SessionBus()
        uid = dbus.service.BusName(name, bus=bus)
        path = "/" + name.replace(".", "/")
        dbus.service.Object.__init__(self, uid, path)
        self.path = path
        self.name = name
        print "of"

#    def __call__(self):
        for n, v in self.__class__.__dict__.items():
            if hasattr(v, "_dbus_export"):
                print v
                dbus.service.method(self.name)(v)
                x = lambda _v=v: dbus.service.method(self.name)(_v)
                #print ("use", self.name, n, v, x)
                #self.__dict__[n] = x

    @staticmethod
    def export(f):
        f._dbus_export = True
        return f

class Dummy(DBusBackend):
    def __init__(self):
        DBusBackend.__init__(self, "org.foo.Bar")

#    @dbus.service.method("org.foo.Bar")
    @DBusBackend.export
    @e
    def foo(self, stri=None):
        return "hello"

    def bar(self):
        pass


d = Dummy()

loop = gobject.MainLoop()
print "listening ..."
loop.run()

raise SystemExit()


if __name__ == "__main__":
    if "-d" in sys.argv:
        DBusGMainLoop(set_as_default=True)
        myservice = AugeasService()
        loop = gobject.MainLoop()
        print "listening ..."
        loop.run()

    elif "-c" in sys.argv:
        bus = dbus.SessionBus()
        helloservice = bus.get_object(BUS_NAME, BUS_PATH+"/Service")
        hello = helloservice.get_dbus_method('get', BUS_NAME)
        print hello("/files/etc/hostname/hostname")

