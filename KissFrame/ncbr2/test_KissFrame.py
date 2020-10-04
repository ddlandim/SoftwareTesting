import unittest
import KissFrame
class NCBR2_TestFunctions(unittest.TestCase):
  
  def test_utilfunctions(self):
    # Valid cases
    assert valid_hex_digits("abcdef1234567890")
    assert valid_hex_digits("1234567890abcdef")
    assert valid_hex_digits("1234567890")
    assert valid_hex_digits("abcdef")
    assert valid_hex_digits("af")
    assert valid_hex_digits("10")
    assert valid_hex_digits("a1b2c3d4e5f6")
    assert valid_hex_digits("A1b2C3d4e5f6")
    
    # Invalid cases
    # impar
    assert not valid_hex_digits("A1b2C3d4e5f")
    # another alpha chars
    assert not valid_hex_digits("A1b2C3d4e5f6G")
    # especial chars
    assert not valid_hex_digits("A1b2C3d4e5f!")
  
  # Particionamento por classes de equivalencia
  # 1st class : Endianess
  def test1_endianess(self):
      # Valid cases
      assert u8ToBig(0) == "00"
      assert u8ToBig(255) == "ff"

      assert u16ToBig(0) == "0000"
      assert u16ToBig(257) == "0101"

      assert u32ToBig(0) == "00000000"
      assert u32ToBig(65536) == "00010000"

      # Test case with wrong type
      assert u8ToBig(1.5) == "U8_SIZE_ERROR"

      # Invalid cases
      assert u8ToBig(256) == "U8_SIZE_ERROR"

      assert u16ToBig(65536) == "U16_SIZE_ERROR"

      assert u32ToBig(4294967296) == "U32_SIZE_ERROR"
  # 2nd class : Kiss frame
  def test2_kiss(self):
      # Valid cases
      assert kiss_detect("c000c0")
      assert kiss_send("abcd") == "c000abcdc0"
      assert kiss_escape("c0dbdcdd") == "dbdcdbdbdddd"
      assert kiss_send(kiss_escape("c0dbdcdd")) == "c000dbdcdbdbddddc0"
      assert kiss_unescape("c000dbdcdbdbddddc0") ==  "c000c0dbdcddc0"
      assert kiss_receive(kiss_unescape("c000dbdcdbdbddddc0")) == "c0dbdcdd"