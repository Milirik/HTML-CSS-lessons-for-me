from sys import getsizeof


class CompressedGene:
    def __init__(self, gene: str) -> None:
        self._compress(gene)
    
    def _compress(self, gene: str) -> str:
        self.bit_string: int = 1
        for nucleotid in gene.upper():
            self.bit_string <<= 2
            if nucleotid == 'A':
                self.bit_string |= 0b00
            elif nucleotid == 'C':
                self.bit_string |= 0b01
            elif nucleotid == 'G':
                self.bit_string |= 0b10
            elif nucleotid == 'T':
                self.bit_string |= 0b11
            else:
                raise ValueError("Invalid Nucleoticde:{}".format(nucleotid))

    def decompress(self) -> str:
        gene: str = ''
        for i in range(0, self.bit_string.bit_length() - 1, 2):
            bits: int = self.bit_string >> i & 0b11
            if bits == 0b00:
                gene += 'A'
            elif bits == 0b01:
                gene += 'C'
            elif bits == 0b10:
                gene += 'G'
            elif bits == 0b11:
                gene += 'T'
            else:
                raise ValueError("Invalid bits:{}".format(bits))
        return gene[::-1]
                
    def __str__(self):
        return self.decompress()
    
if __name__ == '__main__':
    original: str = 'TAGTAGTATGATGTAGTTATTTTTTTATAATAAAGGGGTGTTGTTATT'*100      
    print('original is {} bytes'.format(getsizeof(original)))
    
    compressed = CompressedGene(original)
    print('compressed if {} bytes'.format(getsizeof(compressed.bit_string)))
    print(compressed)
    print('compressed and decompressed are the same: {}'. format(original == compressed.decompress()))
    
    
    
    
    
    
    
    
    
    
    
    
        
        
        
        
        