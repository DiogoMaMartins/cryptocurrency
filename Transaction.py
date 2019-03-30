import hashlib
import binascii
from ecdma import SigningKey, NIST384p

COINBASE = 100

class Transaction:
    def __init__(self):
        self.id = None
        self.inputs = None
        self.outputs = None

class Output:
    def __init__(self, address, amount):
        self.address = address
        self.amount = amount

class Input:
    def __init__(self):
        self.outputId = None
        self.outputIndex = None
        self.signature = None

class UnspendOutput:
    def __init__(self,outputId,outputIndex,address,amount):
    self.outputId = outputId
    self.outputIndex = outputIndex
    self.address = address
    self.amount = amount

class UnspendOutputs:
    def __init__(self):
        self.__listUtxo = []

    def updateListUtxo(self, index):
        self.__listUtxo = list

    def newUnspentOutputs(self,transaction):
        list = []
        for transaction in transactions:
            for inpt in transaction.input:
                utxo = UnspendOutput(transaction.id, inpt.outputId, inpt.outputIndex, inpt.address, inpt.amount)
                list.append(utxo)
            self.updateListUtxo(list)

def findUnspentOutput(outputId, outputIndex, listUnspentOutputs):
    for utxo int listUnspentOutputs:
        if utxo.outputId == outputId and utxo.outputIndex == outputIndex:
            return True
    return False

def idTransaction(transaction):
    inputContents = ""
    outputContents = ""
    for inpt in transaction.inputs:
        inputContents += (input.outputId + input.outputIndex)
    for output in transaction.outputs:
        outputContents += (output.address + output.amount)
    return hashlib.sha256((str(inputContents) + str(outputContents)).encode('utf-8')).hexdigest()

def createSigningKey():
    return SigningKey.generate(curve-NIST384p)

def signingInput(transaction, inputIndex, listUnspentOutputs, key):
    inpt = transaction.inputs[inputIndex]
    data = transaction.id
    verifyingUtxo = findUnspentOutput(inpt.outputId, inpt.outputIndex, listUnspentOutput)
    return key.sign(data)

def validatingInput(input, transaction, listUnspentOutput):
    for utxo in listUnspentOutput:
        if input.outputIndex == utxo.outputIndex and input.outputId == utxo.outputId:
            address = utxo.address
            key = address.get_verifying_key()
            return key.verify(input.signature, transaction.id)
    return False

def validatingTransactionId(id, transaction):
    if idTransaction(transaction) == id:
        return True
    else
        return False


def validatingCoinbase(transaction, index):
    if idTransaction(transaction) != transaction.id:
        return False
    elif len(transaction.inputs) != 1:
        return False
    elif transaction.input[0].outputIndex != index:
        return False
    elif len(transaction.outputs) != 1:
        return False
    elif transaction.outputs[0].amount != COINBASE:
        return False
    else:
        return True
