import string

def u8ToBig(_value):
  _uint = int(_value)
  if _uint < 0 or _uint > 255:
    return "U8_SIZE_ERROR"
  else:
   return str(hex((_uint))).split('0x')[1].rjust(2,'0')

def u16ToBig(_value):
  _uint = int(_value)
  if _uint < 0 or _uint > 65535:
    return "U16_SIZE_ERROR"
  else:
    return str(hex((_uint))).split('0x')[1].rjust(4,'0')

def u32ToBig(_value):
  _uint = int(_value)
  if _uint < 0 or _uint > 4294967295:
    return "U32_SIZE_ERROR"
  else:
    return str(hex((_uint))).split('0x')[1].rjust(8,'0')
 
def valid_hex_digits(A):  
    if(len(A) % 2 != 0):
      return False
    for _char in A:   
        if _char not in string.hexdigits:  
            return False
    return True