from subprocess import Popen, PIPE, check_output, check_call, TimeoutExpired
from time import time
import sys
import os

class gradeFile (object):

    def __init__(self, filename, runtime = 10, testCases = list()):
        self._filename = filename
        self._runtime = runtime
        self._testcases = testCases
        self._results = []


    def getFilename(self):
        return self._filename

    def setTimeout(self, runtime):
        self._runtime = runtime

    def getRuntime(self):
        return self._runtime

    def setTestCases(self, cases):
        self._testcases = cases

    def runTestcases(self):
        for tuple in self._testcases:
            self._results.append(self._IOtest(tuple[0], tuple[1]))
        return self._results

    def _IOtest(self, input, output):
        proc = Popen("python3.5 "+self._filename, stdin = PIPE, stdout=PIPE, stderr= PIPE, shell = True )
        try:
            realoutput = proc.communicate(input = input.encode('utf-8'), timeout= self._runtime)[0]
            realoutput = realoutput.decode()
            outtuple = (input, output, format(realoutput), output in realoutput)
        except:
            e = sys.exc_info()
            print ("Error: "+format(e))
            outtuple = (input, output, "Error", False)
        proc.terminate()
        return (outtuple)

    def __str__(self):
        for result in self._results:
            return ("Input: "+result[0]+"\nExpected Output: "+result[1]+"\nActual Output: "+result[2]+"\nActual in Expected:"+result[3])


class allFiles(object):

    def __init__(self, directory, timeout = 10, testcases = list()):
        self._directory = directory
        self._timeout = timeout
        self._testcases = testcases
        self._files = list()
        os.chdir(directory)
        for file in os.listdir(self._directory):
            if ".py" in file:
                self._files.append(gradeFile(file, self._timeout, self._testcases))

    def setTimeout(self, timeout):
        self._timeout = timeout

    def createAlltests(self, listoftuples):
        self._testcases.clear()
        self._testcases = listoftuples
        for item in self._files:\
            item.setTestCases(self._testcases)

    def createTest(self, inp, outp):
        self._testcases.append((str(inp), str(outp)))
        for item in self._files:\
            item.setTestCases(self._testcases)

    def clearFiles(self):
        self._files.clear()

    def clearTestcases(self):
        self._testcases.clear()
        for file in self._files:
            file.setTestCases(self._testcases)

    def runTests(self):
        for file in self._files:
            file.runTestcases()
        

#
# g = gradeFile("brokenprogram.py", runtime=5)
# g.setTestCases([(str(1),str(2)), (str(2),str(3)), (str(3),str(5))])
# g.runTestcases()