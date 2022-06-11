import ctypes


class RustLibrary:

    def __init__(self, libfile):
        self.libfile = libfile
        self.lib = ctypes.WinDLL(libfile)

    def call(self, fn, *args):
        if getattr(self.lib, fn) is None:
            raise ReferenceError(
                f"function {fn!r} not found in DLL"
            )
        return getattr(self.lib, fn)(*args)


lib = RustLibrary("./target/debug/test.dll")
res = lib.call("add", 5, 3)
print(res)