# -*- coding: utf-8 -*-
"""
these are the requirementes of block:
    Hash Previous Block
    Timestmapnone
    MErkle Root HashHash(current Block)
    Transaction List
"""
#Python -> 3.5, Postman
#pip --> Flask,Json,hashlib,time,requests

#first Block -->Genesis Block --> 0000000000
import sys
import json
import hashlib
#for using web Enviroment
from flask import Flask
# to send and recieve request from web page
import requests
#timestamp
from time import time
#JSON --> JavaScript Object Notion
from flask.json import jsonify
#parase the address/routes
from urlib.parse import urlparse
#for generating random object
from uuid import uuid4

class Blockchain(object):
    #difficulty level, 0000
    difficulty_level = "00"
    #constructor

def hash_Block (self,block):
    #json.dumps methods convert a Python object into aJson String
    blockEncoder = json.dumps(block, sort_key=True) .encode()
    return hashlib.sha256(blockEncoder).hexdigest()
def __init__(self):
    
    self.chain = []
    self.current_transactions = []
    gen_hash = self.hash_Block("genesis_block")
    self.appendBlock (
        hash_of_previous_block = gen_hash,
        nonce = self.PoW(0,gen_hash,[])
        )
def PoW(self,index,hash_of_previous_block,transactions ):
    nonce = 0
    while self.validate_proof(index,hash_of_previous_block, transactions,nonce) is False:
        nonce +=1
        print(nonce)
    return nonce
    
def validate_proof(self,index,hash_of_previous_block,transactions, nonce):
    concent = f'{index}{hash_of_previous_block}{transactions}{nonce}'##.encode
    concent_hash = self.hash_Block(content)##.hexdigest()
    #important line for assignent 2
    return content_hash[:len(self.difficulty_level)]==self.difficulty_level)] == self.difficulty_
    def appendBlock(self,nonce,hash_of_previous_block):
    block = {
        'index':len(self.chain),
        'timestamp':time(),
        'transaction':self.current_transactions,
        'nonce':nonce,
        'hash_of_previous_block' :hash_of_previous_block
        }
    self.current_transactions = []
    self.chain.apeend(block)
    return block

def add_transaction(self,sender,recipient,amount):
    self.current_transaction.append([
        'amount':amount,
        'recipient':recipient,
        'sender':sender
        ])
    return last_block['index']+1
@property
def last_block(self):
    return self.chain[-1]

# Flask
app = Flask (__name__)
node_identifier = str(uuid4()).replace('-',"")
blockchain = Blockchain()
#routes
#localhost/assignment1
@app.route('/',methods=['GET'])
#chain of blocks --> Blockchain
def full_chain():
    response = {
        'chain':blockchain.chain,
        'length':len(blockchain.chain)
        }
    return jsonify(response),200
@app.route('/mine',methods =['GET'])
def mine_block():
    blockchain.add_transaction(
        sender="0"
        recipient= node_identifier,
        amount=1
        )
    last_block_hash = blockchain.hash_Block(blockchain.last_block)
    index = len(blockchain.chain)
    nonce =blockchain.PoW(index,last_block_hash),blockchain.current_transactions)
    block = appendBlock(nonce,last_block_hash)
    response = {
        'message':"You successfully added a new block"
        'index': block['index'],
        'hash_of_the_previous_block': block['hash_of)previous_block'],
        'nonce':block['nonce'],
        'transaction': block ['transaction']
        }
    
@app.route('/transaction/new',methods=['POST'])
def new_transactions():
    values = requests.get_json()
    required_fields = [sender,receipient,amount]
    if not all (k in values for k in required_fields):
            return ('Missing Fields' 400)
    index = blockchain.add_transaction( 
        values['sender'],
        values['recipient'],
        values['aomount']
        )
    response = {'message':f'Transaction will be added to the bock [index]'}
    return (jsonify(response),201)
        
if __name__== '__main__':
    app.run(host='0.0.0.0'),port=int(sys.argv[1]))
