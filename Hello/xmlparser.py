# Reading xml using ElementTree
# =============================
print('=============================')
print('Reading xml using ElementTree')
print('=============================')

import xml.etree.ElementTree as ET
import pandas as pd

fileName = 'd:/report/MGM/testng-results-83.xml'

def parseTestNGXML(fileName):
    tree = ET.parse(fileName)
    root = tree.getroot()
    #print(root.tag) # Returns testng-results
    recDict = {}
    dictList = []
    dictList1 = []
    keys = ['suite', 'suiteDuration', 'module', 'moduleDuration', 'testclass', 'testclassDuration', 'method', 'methodDuration', 'status', 'is.config', 'class', 'message', 'full-stacktrace']
    values = []
    for elem in root:
    #    print(' '*4, elem.tag)
        if (elem.tag == 'suite'): # Fetch Suite Name
            suite = elem.attrib['name']
            suiteDuration = elem.attrib['duration-ms']
            #print(' '*4, suite)
            for subelem in elem: # Fetch Module Name
                if (subelem.tag == 'test'):
                    module = subelem.attrib['name']
                    moduleDuration = elem.attrib['duration-ms']
                    #print(' '*8, module)
                    for ssubelem in subelem: # Fetch TestClass Name
                        testclass = ssubelem.attrib['name']
                        testclassDuration = elem.attrib['duration-ms']
                        #print(' '*12, testclass)
                        for sssubelem in ssubelem: # Fetch Method Name, Status, Is-Config
                            method = sssubelem.attrib['name']
                            methodDuration = elem.attrib['duration-ms']
                            # isConfig = sssubelem.attrib['is-config']
                            if method in ('afterMethod', 'afterSuite', 'beforeMethod', 'beforeSuite', 'beforeWebMethod', 'beforeWebTest'):
                                isConfig = 'TRUE'
                            else:
                                isConfig = ''
                            #print(method, isConfig)
                            status = sssubelem.attrib['status']
                            # print(' ' * 16, method, ' - ', isConfig, ' - ', 'status')
                            if status == 'FAIL':
                                for ssssubelem in sssubelem: # Fetch exception details
                                    if ssssubelem.tag == 'exception':
                                        vClass = ssssubelem.attrib['class']
                                        #print(' ' * 20, vClass)
                                        for sssssubelem in ssssubelem:
                                            if sssssubelem.tag == 'message':
                                                message = sssssubelem.text
                                                #print(' '*24, message)
                                            if sssssubelem.tag == 'full-stacktrace':
                                                full_stacktrace = sssssubelem.text
                                                #print(' '*24, full_stacktrace)
                                                values = [suite, suiteDuration, module, moduleDuration, testclass, testclassDuration, method, methodDuration, status, isConfig, vClass, message, full_stacktrace]
                                                dictList.append(dict(zip(keys, values)))
                            else:
                                values = [suite, suiteDuration, module, moduleDuration, testclass, testclassDuration, method, methodDuration, status, isConfig, '', '', '']
                                dictList.append(dict(zip(keys, values)))
    df = pd.DataFrame(dictList)
    df = df[['suite', 'suiteDuration', 'module', 'moduleDuration', 'testclass', 'testclassDuration', 'method', 'methodDuration', 'status', 'is.config', 'class', 'message', 'full-stacktrace']]
    #print(df)

    writer = pd.ExcelWriter("d:/report/MGM/" +"final" + ".xls", engine=None)
    df.to_excel(writer, sheet_name='Sheet1')
    writer.save()

parseTestNGXML(fileName)

