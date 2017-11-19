import dataset
import pyspeedtest
import datetime

class NetworkTest(object):
    def __init__(self):
        self.db = dataset.connect('sqlite:///data/network.db')
        self.speedtestresult = self.runSpeedTest()
        self.savespeedtestresult(self.speedtestresult)

    def getDate(self):
        dt = datetime.datetime.now()
        date = dt.date().isoformat()
        time = dt.time().isoformat()
        return({'date': date, 'time': time})

    def runSpeedTest(self):
        st = pyspeedtest.SpeedTest()
        rundate = self.getDate()
        ping = st.ping()
        download = st.download()
        upload = st.upload()
        result = {'ping': ping, 'download': download, 'upload': upload}
        result.update(rundate)
        return(result)

    def savespeedtestresult(self, speedtestresult):
        table = self.db['speedtest']
        table.insert(speedtestresult)

if __name__ == '__main__':
    nt = NetworkTest()

