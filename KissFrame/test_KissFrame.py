import unittest

from KissFrame import KissFrame


class MyTestCase(unittest.TestCase):

    # 1st move: build a kiss frame without parameters
    def test_initializing(self):
        frame = KissFrame()
        assert frame.raw == bytearray.fromhex('c0 00 c0')
        assert frame.payload == bytearray.fromhex('')
        assert frame.detect() == True

    # 2nd move: build a frame received from radio
    # kiss frames received from radio have escaped data, so we have to build and unescape
    # test invalid frames too!
    def test_receiving(self):
        data_from_radio = bytearray.fromhex('c0 00 a1 a2 a3 db dc c0')
        data_unescaped = bytearray.fromhex('c0 00 a1 a2 a3 c0 c0')
        data_invalid = bytearray.fromhex('c0 00 a1 a2 a3')
        frame = KissFrame(data_from_radio)
        assert frame.detect() == True
        assert frame.unescape() == data_unescaped
        assert frame.mode == "unescaped"

        frame2 = KissFrame(data_invalid)
        assert len(frame2.unescape())<1
        assert frame2.detect() == False
        assert frame2.mode == "invalid"

    # 3rd move: build encode a frame to radio
    # kiss frames received from radio have escaped data, so we have to build and unescape
    def test_sending(self):
        data_for_radio = bytearray.fromhex('a1 a2 a3 c0')
        data_escaped = bytearray.fromhex('c0 00 a1 a2 a3 db dc c0')
        frame = KissFrame(data_for_radio)
        print(frame.escape())
        assert frame.escape() == data_escaped
        #test if data is not enconding 2 times!
        assert frame.escape() == data_escaped
        assert frame.mode == "escaped"


if __name__ == '__main__':
    unittest.main()
