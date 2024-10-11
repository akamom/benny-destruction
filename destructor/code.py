import base64
import hashlib

class DataCreator:
    
    def __init__(self, num_chunks, in_file, out_file):
        self.num_chunks = num_chunks
        self.in_file = in_file
        self.out_file = out_file

    def create(self):
        with open(self.in_file, 'rb') as image_file:
            file_byte_string = base64.b64encode(image_file.read()).decode('utf-8')

        chunk_size = len(file_byte_string) // self.num_chunks
        remainder = len(file_byte_string) % self.num_chunks
        chunks = []

        start = 0
        for i in range(self.num_chunks):
            extra_char = 1 if i < remainder else 0
            end = start + chunk_size + extra_char
            chunks.append(file_byte_string[start:end])
            start = end


        # 'test.jpg' -> (string) "ajksdhkajghiasdhja/lkdghjnsdlkjhdfASLdjlo;kdghjlASKdjmAL;SDJ;SJKDFGHL;"
        # Wir wollen 5 chunks
        # Der string hat 40 characters, darum muss jeder chunk 40 / 5 characters haben = 8 characters / chunk
        # Wir erstellen einen Array
        # Array[0] == string[0:7] == "ajksdhka"
        # Array[1] == string[8:15] == "jghiasdh"
        #
        # hashSha256(Array[0]) = aa
        # hashSha256(Array[1]) = ba
        #
        # Wir bauen wie gehashten Strings wieder zusammen == aaba....

        sha256_hash = hashlib.sha256()

        hashed_chunked_file = ''
        for i in range(len(chunks)):
            sha256_hash.update(chunks[i].encode('utf-8'))
            hashed_chunk = sha256_hash.hexdigest()
            hashed_chunked_file = ''.join([hashed_chunked_file, hashed_chunk])

        with open(self.out_file, "w") as file:
            file.write(hashed_chunked_file)

