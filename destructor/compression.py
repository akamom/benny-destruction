from PIL import ImageStat

class Compressor:

    def __init__(self, chunks_x, chunks_y):
        self.chunks_x = chunks_x
        self.chunks_y = chunks_y

    def _chunk(self, image):
        width, height = image.size

        x_chunk_size = width // self.chunks_x
        y_chunk_size = height // self.chunks_y

        chunks = []

        # Loop through the grid and crop the chunks
        for i in range(self.chunks_x):
            for j in range(self.chunks_y):
                # Define the box (left, upper, right, lower) for each chunk
                left = i * x_chunk_size
                upper = j * y_chunk_size
                right = left + x_chunk_size
                lower = upper + y_chunk_size
                
                # Crop the image to the defined box
                chunk = image.crop((left, upper, right, lower))
                chunks.append(chunk)

        # print(f"x_chunk_size: {x_chunk_size}")
        # print(f"y_chunk_size: {y_chunk_size}")
        # print(f"number_chunks: {len(chunks)}")

        return chunks

    def execute(self, image):
        chunks = self._chunk(image)
        
        avg_chunks = []
        for chunk in chunks:
            stat = ImageStat.Stat(chunk)
            avg_chunks.append(stat.mean)
            
        return avg_chunks