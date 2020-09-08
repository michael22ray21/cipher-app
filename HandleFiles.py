BUFFER_SIZE = 4096

def read_file_as_bytearray(filename: str) -> bytearray:
    with open(filename, "rb") as file:
        data = bytearray()

        bytes_read = file.read(BUFFER_SIZE)
        while bytes_read:
            data += bytes_read
            bytes_read = file.read(BUFFER_SIZE)

        return data

def read_file_as_string_list(filename: str) -> list:
    with open(filename) as file:
        return file.readlines()

def read_file_as_string_list_stripped(filename: str) -> list:
    return [line.strip() for line in read_file_as_string_list(filename)]

def read_file_as_string_single(filename: str) -> str:
    return ''.join(read_file_as_string_list(filename))

def read_file_as_string_single_stripped(filename: str) -> str:
    return ''.join(read_file_as_string_list_stripped(filename))

def write_file_from_string(string: str, filename: str):
    with open(filename, "w") as file:
        file.write(string)

def write_file_from_bytearray(data: bytearray, filename: str):
    with open(filename, "wb") as file:
        file.write(data)
