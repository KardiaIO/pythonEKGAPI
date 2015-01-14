import collections
import datetime
import isodate

class RWaveAnalysis:

  def __init__(self, notch, featureThreshold, timespan, bufferLength):
    self.notch = notch
    self.featureThreshold = featureThreshold
    self.timespan = timespan
    self.bufferLength = bufferLength
    # initializes rWaveBuffer as a Python deque, a doubly linked list for O(1) pushing and popping
    self.rWaveBuffer = collections.deque()
    self.rWaveMaxBuffer = []
    self.captureStream = False
    # sets default heartrate before buffer builds
    self.heartRate = '65'
    
  def addToBuffer(self, timeStamp):
    # converts ISO 8601 string timestamp to Python Datetime Object without timezone info
    dateTimeObj = isodate.parse_datetime(timeStamp).replace(tzinfo=None)
    self.rWaveBuffer.append(dateTimeObj)
    if len(self.rWaveBuffer) > self.bufferLength:
      self.rWaveBuffer.popleft()

  def checkBuffer(self):
    # creates list of RR-intervals
    timeDiffs = [(self.rWaveBuffer[i+1] - self.rWaveBuffer[i]).total_seconds() for i in range(len(self.rWaveBuffer)-1)]
    self.getHeartRate(timeDiffs)
    # filters list of RR-intervals for abnormal length intervals specified by timespan
    significantFeatures = [timeDiffs[i] for i in range(len(timeDiffs)) if timeDiffs[i] < self.timespan]
    if len(significantFeatures) > self.featureThreshold:
      self.resetFeatures()
      return {'statusCode':'404', 'heartRate': self.heartRate}
    else:
      self.resetFeatures()
      return {'statusCode':'200', 'heartRate': self.heartRate}

  def findRWavePeak(self, data):
    # catches cases where incoming data has abnormal amplitude buildup from data pipe, i.e. data['amplitude'] = 4.512.2553.233
    if len(data['amplitude']) > 5:
      data['amplitude'] = data['amplitude'][0:5]
    # starts recording when notch threshold is broken. Commented part can be used for real data and adjusted for accuracy
    if float(data['amplitude']) > self.notch and not self.captureStream: # and isodate.parse_datetime(data['time']) > ((self.rWaveBuffer[len(self.rWaveBuffer) - 1] + datetime.timedelta(0, 0, 0, 600))):
      self.captureStream = True
      self.rWaveMaxBuffer.append(data)
    # commented section below should be used for real data. builds real rWaveMaxBuffer to extract peak
    # elif self.captureStream and float(data['amplitude']) > self.notch:
    #   self.rWaveMaxBuffer.append(data)
    if len(self.rWaveMaxBuffer):
      self.captureStream = False
      # finds peak in rWaveMaxBuffer and records time of peak
      rWavePeakTime = max(self.rWaveMaxBuffer, key=lambda x: float(x['amplitude']))['time']
      self.addToBuffer(rWavePeakTime)
      self.resetRWaveMaxBuffer()

  def analyze(self, data):
    self.findRWavePeak(data)
    # self.drawData(data)
    return self.checkBuffer()

  def getHeartRate(self, timeDiffs):
    if not timeDiffs or len(timeDiffs) < 5:
      self.heartRate = self.heartRate
    else:
      # calculates BPM
      self.heartRate = format(60 / (reduce(lambda x, y: x + y, timeDiffs) / len(timeDiffs)), '.0f')

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