
import pudb
from struct import *

b = pack('hhl', 1, 2, 3)
# b'\x00\x01\x00\x02\x00\x00\x00\x03'
unpack('hhl', b)
(1, 2, 3)
pudb.set_trace()
calcsize('hhl')
