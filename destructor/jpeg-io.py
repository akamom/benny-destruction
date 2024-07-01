in_file = "./test.jpg"
out_file = "./out"

with open(in_file, "rb") as f:
    file_content_bytes = f.read()

byte_array = bytearray(file_content_bytes)
string_byte_array = byte_array.hex()

with open(out_file, "w") as f:
    f.write(string_byte_array)