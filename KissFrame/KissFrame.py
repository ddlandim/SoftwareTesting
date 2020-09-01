class KissFrame:
    FEND = bytearray.fromhex('c0')
    FESC = bytearray.fromhex('db')
    TFEND = bytearray.fromhex('dc')
    TFESC = bytearray.fromhex('dd')
    CMD = bytearray.fromhex('00')
    HEADER = FEND + CMD
    SUFFIX = FEND

    def __init__(self, data=bytearray.fromhex('c000c0')):
        self.payload = bytearray.fromhex('')
        self.raw = data
        self.mode = "initialized"

    def detect(self):
        n = len(self.raw)
        if n > 2 and self.raw[0] == self.FEND[0] and self.raw[1] == self.CMD[0] and self.raw[n - 1] == self.FEND[0]:
            return True
        else:
            return False

    # this is a method when we receive a kiss frame from a TNC and need to unescape the bytes scaped from radio
    def unescape(self):
        # frame reduction
        if not self.detect():
            self.mode = "invalid"
            return bytearray.fromhex('')
        if self.mode == "unescaped":
            return self.HEADER + self.payload + self.SUFFIX
        else:
            unescaped = self.raw[2:-1]
            unescaped = unescaped.replace(b'\xdb\xdc', b'\xc0')
            self.payload = unescaped
            self.mode = "unescaped"
            return self.HEADER + self.payload + self.SUFFIX

    # this is a method when we want to send a kiss frame to a TNC and need to scape the bytes, the radio will
    # unescape this frame from it side
    def escape(self):
        # frame expansion
        if self.mode == "escaped":
            return self.HEADER + self.payload + self.SUFFIX
        else:
            unescaped = self.raw
            unescaped = unescaped.replace(b'\xc0', b'\xdb\xdc')
            self.payload = unescaped
            self.mode = "escaped"
            return self.HEADER + self.payload + self.SUFFIX
            return self.payload
