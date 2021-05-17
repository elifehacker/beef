from readwow import processWow
from readcoles import processColes
from readhf import processHF
from readmm import processMM
from readm4u import processM4U

from dailyreport import produceReport

def makeReport():
    total = list()

    total += processColes('webs\\1.html')
    total += processColes('webs\\2.html')
    total += processColes('webs\\3.html')

    total += processWow('webs\\4.html')
    total += processWow('webs\\5.html')

    total += processMM('webs\\6.html')

    total += processM4U('webs\\7.html')
    total += processM4U('webs\\8.html')
    total += processM4U('webs\\9.html')

    total += processHF('webs\\10.html')
    total += processHF('webs\\11.html')

    produceReport(total)


if __name__ == "__main__":
    makeReport()