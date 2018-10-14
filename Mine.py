from socket import *
import Block
import Hasher
import sys
import random

#PORT = 13000
#peerSocket = socket(AF_INET, SOCK_STREAM)
#peerSocket.bind(('', PORT))
#peerSocket.listen(1)

def mine(new_block):
    while Hasher.hash_string(new_block.__str__())[:4] != "0000":
        new_block.nonce = random.randint(0, sys.maxsize)
        print(Hasher.hash_string(new_block.__str__()))
    print(new_block.nonce)
    
blocao = Block.Block(1, 1234)
mine(blocao)
#while True:
#    peerSocket, addr = peerSocket.accept()