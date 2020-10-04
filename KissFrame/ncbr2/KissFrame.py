import string

def is_integer_num(n):
    if isinstance(n, int):
        return True
    if isinstance(n, float):
        return n.is_integer()
    return False

def u8ToBig(_value):
  _uint = _value
  if _uint < 0 or _uint > 255 or (not is_integer_num(_value)):
    return "U8_SIZE_ERROR"
  else:
   return str(hex((_uint))).split('0x')[1].rjust(2,'0')

def u16ToBig(_value):
  _uint = _value
  if _uint < 0 or _uint > 65535 or (not is_integer_num(_value)):
    return "U16_SIZE_ERROR"
  else:
    return str(hex((_uint))).split('0x')[1].rjust(4,'0')

def u32ToBig(_value):
  _uint = _value
  if _uint < 0 or _uint > 4294967295 or (not is_integer_num(_value)):
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

def kiss_escape(A):
  A=A.lower()
  if not valid_hex_digits(A):
    return "HEX_DATA_INVALID"
  escaped = ""
  while len(A) > 0:
    if (A[0] + A[1]) == "c0":
      escaped += "dbdc"
    elif (A[0] + A[1]) == "dc":
      escaped += "dbdd"
    else:
      escaped += (A[0] + A[1])
    A = A[2:]
  return escaped

def kiss_unescape(A):
  A=A.lower()
  if not valid_hex_digits(A):
    return "HEX_DATA_INVALID"
  unescaped = ""
  while len(A) > 0:
    if len(A) >= 4 and (A[0] + A[1] + A[2] + A[3]) == "dbdc":
      unescaped += "c0"
      A = A[4:]
    elif len(A) >= 4 and (A[0] + A[1] + A[2] + A[3]) == "dbdd":
      unescaped += "dc"
      A = A[4:]
    else:
      unescaped += (A[0] + A[1])
      A = A[2:]
  return unescaped

def kiss_detect(A):
  A=A.lower()
  if not valid_hex_digits(A):
    return "HEX_DATA_INVALID"
  return A.startswith("c000") and A.endswith("c0")

def kiss_send(A):
  A=A.lower()
  if not valid_hex_digits(A):
    return "HEX_DATA_INVALID"
  return "c000" + A + "c0"

def kiss_receive(A):
  A=A.lower()
  if not valid_hex_digits(A):
    return "HEX_DATA_INVALID"
  if kiss_detect(A):
    return A[4:-2]

def kiss_needEscape(A):
  A=A.lower()
  if not valid_hex_digits(A):
    return "HEX_DATA_INVALID"
  return "c0" in A or "dc" in A

def kiss_needUnescape(A):
  A=A.lower()
  if not valid_hex_digits(A):
    return "HEX_DATA_INVALID"
  return "dbdc" in A or "dbdd" in A