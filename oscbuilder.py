import struct


class OscBuilder:
    def __init__(self, addr, *args):
        self.addr = addr
        self.args = args

    def check_type(self, arg):
        if type(arg) == str:
            return 's'
        elif type(arg) == int:
            return 'i'
        elif type(arg) == float:
            return 'f'
        else:
            raise TypeError('Invalid type: ' + str(type(arg)))

    def write_string(self, string):
        return_bytes = string.encode('utf-8')
        return_bytes += b'\x00' * (4 - (len(return_bytes) % 4))
        return return_bytes

    def build(self):
        """
        OSCメッセージの作成
        [OSCアドレス][,][引数の型][引数1][引数2]...
        ,以降は32bit区切り
        """
        message = b''
        # アドレスの追加
        message += self.write_string(self.addr)
        arg_types = ""
        for val in self.args:
            val_type = self.check_type(val)
            arg_types += val_type
        # 引数の型の追加
        message += self.write_string("," + arg_types)
        # 引数の追加
        for val in self.args:
            if type(val) == str:
                message += self.write_string(val)
            elif type(val) == int:
                message += struct.pack(">i", val)
            elif type(val) == float:
                message += struct.pack(">f", val)
        return message
