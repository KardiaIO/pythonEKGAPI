import collections
import datetime
import isodate

class RWaveAnalysis:

  def __init__(self, notch, featureThreshold, timespan, bufferLength):
    self.notch = notch
    self.featureThreshold = featureThreshold
    self.timespan = timespan
    self.bufferLength = bufferLength
    self.rWaveBuffer = collections.deque()
    # self.rWaveBuffer.append(datetime.datetime(1,1,1,1))
    self.rWaveMaxBuffer = []
    self.captureStream = False
    self.heartRate = 60

  def addToBuffer(self, timeStamp):
    dateTimeObj = isodate.parse_datetime(timeStamp).replace(tzinfo=None)
    self.rWaveBuffer.append(dateTimeObj)
    if len(self.rWaveBuffer) > self.bufferLength:
      self.rWaveBuffer.popleft()

  def checkBuffer(self):
    # print self.rWaveBuffer
    timeDiffs = [(self.rWaveBuffer[i+1] - self.rWaveBuffer[i]).total_seconds() for i in range(len(self.rWaveBuffer)-1)]
    self.getHeartRate(timeDiffs)
    significantFeatures = [timeDiffs[i] for i in range(len(timeDiffs)) if timeDiffs[i] < self.featureThreshold]
    if len(significantFeatures) > self.featureThreshold:
      self.resetFeatures()
      return {'statusCode':'404', 'heartRate': self.heartRate}
    else:
      self.resetFeatures()
      return {'statusCode':'200', 'heartRate': self.heartRate}

  def findRWavePeak(self, data):
    if len(data['amplitude']) > 5:
      data['amplitude'] = data['amplitude'][0:5]  
    if float(data['amplitude']) > self.notch and not self.captureStream: # and isodate.parse_datetime(data['time']).replace(tzinfo=None) > ((self.rWaveBuffer[len(self.rWaveBuffer) - 1] + datetime.timedelta(0, 0, 0, 600))):
      self.captureStream = True
      self.rWaveMaxBuffer.append(data)
    # elif self.captureStream and float(data['amplitude']) > self.notch:
    #   self.rWaveMaxBuffer.append(data)
    if len(self.rWaveMaxBuffer):
      self.captureStream = False
      rWavePeakTime = max(self.rWaveMaxBuffer, key=lambda x: float(x['amplitude']))['time']
      self.addToBuffer(rWavePeakTime)
      print rWavePeakTime
      self.resetRWaveMaxBuffer()

  def analyze(self, data):
    self.findRWavePeak(data)
    # self.drawData(data)
    print self.heartRate
    return self.checkBuffer()

  def getHeartRate(self, timeDiffs):
    def flatten(a, b):
      return a + b
    if not timeDiffs:
      self.heartRate = self.heartRate
    else:
      self.heartRate = format(60 / (reduce(flatten, timeDiffs) / len(timeDiffs)), '.0f')

  def resetFeatures(self):
    self.significantFeatures = 0

  def resetRWaveMaxBuffer(self):
    self.rWaveMaxBuffer = []

  # visualize data with console graph, adjusted by offset
  def drawData(self, data):
    offset = 90
    for idx in xrange(int(float(data['amplitude']) ** 3 - offset)): 
      print('|'),
    print('\n'),