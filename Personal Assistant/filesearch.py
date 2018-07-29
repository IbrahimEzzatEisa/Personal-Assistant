import time
startTime=time.time()
import os
class FileSearch :
    def search(self,fileName) :
        path = '/media/abdo/24BC4D9DBC4D6A7E'

        # x = 'Call of Duty 4 - Modern Warfare'
        fileName=fileName
        listOfPath = []
        for root, dirs, files in os.walk(path):
            # print('root :', root)
            # print('dirs :', dirs)
            # print('files :', files)
            # print('__________________')
            for d in dirs:
                if fileName == d:
                    # print('Found1')
                    listOfPath.append(root + '//' + d)
            for f in files:
                if fileName == f.split('.')[0]:
                    # print('Found')
                    listOfPath.append(root + '//' + f)
        # print('__________________')
        # print('List:',lis)

        # time = startTime.time() - startTime
        # print('Time : ',time)
        return listOfPath
# x=FileSearch().search('Call of Duty 4 - Modern Warfare')
# print(type(x[0]))