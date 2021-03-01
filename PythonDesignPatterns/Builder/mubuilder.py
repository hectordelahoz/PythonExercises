from builder import Builder

class ProtectionMuBuilder(Builder):
    def addModel(self):
        self._product._model = 'Protection SAMU'
    
    def addChassis(self):
        self._product._chasis = '80TE'

    def addAnalogBoard(self):
        self._product._analogboard = 'TMU321'
    
    def addBinaryBoard(self):
        self._product._binaryboard = 'DOU211'

class MeteringMuBuilder(Builder):
    def addModel(self):
        self._product._model = 'Metering SAMU'
    
    def addChassis(self):
        self._product._chasis = '40TE'

    def addAnalogBoard(self):
        self._product._analogboard = 'TMU311'
    
    def addBinaryBoard(self):
        self._product._binaryboard = None