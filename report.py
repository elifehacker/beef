from readwow import processWow
from readcoles import processColes
from readhf import processHF
from readmm import processMM
from readm4u import processM4U

from dailyreport import produceReport

def makeReportfromList(webs):
    total = list()
    i = 1
    for w in webs:
        if "coles" in w:
            total += processColes('webs\\'+str(i)+'.html')
        elif "woolworths" in w:
            total += processWow('webs\\'+str(i)+'.html')
        elif "pendlehillmeatmarket" in w:
            total += processMM('webs\\'+str(i)+'.html')
        elif "meat4u" in w:
            total += processM4U('webs\\'+str(i)+'.html')
        elif "harrisfarm" in w:
            total += processHF('webs\\'+str(i)+'.html')
        i +=1
    produceReport(total)

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