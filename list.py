
class FurCerealList:
    def __init__(
            self,
            ptrsize=4,
            indexsize=4,
            chunksize=256,
    ):
        self.ptrsize = ptrsize
        self.indexsize = indexsize
        self.stride = ptrsize * indexsize

        self.chunksize = chunksize

        self.buffer = bytearray(self.stride + chunksize)

        self.items = 0
        self.length = 0

    def get(self, ix):
        #buffer[ix
        pass

    def _ix2ptr(self, ix):
        #  ptrs     data     ptrs     data      ...
        # |____|____________|____|____________| ...

        x = ix * self.ptrsize
        return x + (x // self.stride) * self.chunksize

    def _getptr(self, ptr):
        return int.from_bytes(self.buffer[ptr:ptr+self.ptrsize], 'little')

    def _setptr(self, ptr, ix):
        self.buffer[ptr:ptr+self.ptrsize] = ix.to_bytes(self.ptrsize, 'little')

    def append(self, b):
        ptr = self.stride + self.length

        self.buffer[self.items:self.ptrsize] = ptr.to_bytes(4, 'little')
        self.buffer[ptr:] = b

        self.length += len(b)
        self.items += 1

    def delete(self, ix):
        pass

