import unittest
import os
# from subprocess import run
import subprocess
import filecmp

## ===== Utility Fucntions =====

def copyFile(src, dest):
    srcFile = open(src, 'r')
    destFile = open(dest, 'w+')
    srcFileInput = srcFile.readlines()
    for line in srcFileInput:
        destFile.write(line)

def compareFiles(src, dest):
    return filecmp.cmp(src,dest)        

## ===== TestCases =====

class sanityTestCase(unittest.TestCase):
    def setUp(self):
        self.testCases = ['1','2','3','4','5']

    def runTest(self):
        for caseId in self.testCases:
            copyFile("functional_spec/tests/testCases/input/" + caseId + ".txt", "functional_spec/fixtures/file_input.txt")            
            temp_file = open("functional_spec/tests/testCases/tmp/" + caseId + ".txt",'w')
            subprocess.call(['bin/parking_lot'], stdout=temp_file)
            self.assertTrue(compareFiles("functional_spec/tests/testCases/output/" + caseId + ".txt", "functional_spec/tests/testCases/output/" + caseId + ".txt"),True)
        self.revertChange()

    def revertChange(self):
        copyFile("functional_spec/tests/testCases/raw.txt", "functional_spec/fixtures/file_input.txt")
        for caseId in self.testCases:
            os.remove("functional_spec/tests/testCases/tmp/" + caseId + ".txt")

## ===== Main =====
suite = unittest.TestLoader().loadTestsFromTestCase(sanityTestCase)
unittest.TextTestRunner(verbosity=2).run(suite)
