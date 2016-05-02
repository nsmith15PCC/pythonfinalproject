from testsuite import *
from checkcomments import *

class tabulate(object):
    def __init__ (self, outputTuplesList, linecount=0, commentcount=0, functioncount=0, correctweight=10, wrongweight = 5, errorweight= 0,
                  commentfreq=10, functionfreq=25, includeComments = False, includeFunctions = False):
        self._iopossible = len(outputTuplesList) * correctweight
        self._iopoints = 0
        self._includeComments = includeComments
        self._includeFunctions = includeFunctions
        for tuple in outputTuplesList:
            if tuple[3] == True:
                self._iopoints += correctweight
            elif tuple[2] == "" or tuple[2] == "Error":
                self._iopoints += errorweight
            else:
                self._iopoints += wrongweight
        self._iopercent = 0
        if self._iopossible != 0:
            self._iopercent = self._iopoints/self._iopossible
        expectedcomments = 0
        expectedfunctions = 0
        if commentfreq != 0:
            expectedcomments = linecount/commentfreq
        if functionfreq != 0:
            expectedfunctions = linecount/functionfreq
        self._commentpercent = 1
        self._functionpercent = 1
        if commentcount < expectedcomments:
            self._commentpercent = commentcount/expectedcomments
        if functioncount < expectedfunctions:
            self._functionpercent = functioncount / expectedfunctions

    def getScore(self):
        score = (.5 * self._iopercent + self._includeComments * .25 * self._commentpercent + self._includeFunctions * .25 * self._functionpercent) / (.5 +  self._includeComments * .25 + self._includeFunctions * .25)
        return score
    def getIOScore(self):
        return self._iopercent * 100
    def getCommentScore(self):
        return self._commentpercent * 100
    def getFunctionScore(self):
        return self._functionpercent * 100

b = tabulate([(0,0,"Error",False), (0,0,0, True), (0,0,0,True), (0,0,0,True)],100,10,4,includeComments= True, includeFunctions=True)
print(b.getScore())
print(b.getCommentScore())
print(b.getFunctionScore())