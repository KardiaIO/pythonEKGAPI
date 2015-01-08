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
    self.rWaveMaxBuffer = []
    self.significantFeatures = 0
    self.captureStream = False
    self.counter = 0

  def addToBuffer(self, timeStamp):
    dateTimeObj = isodate.parse_datetime(timeStamp)
    self.rWaveBuffer.append(dateTimeObj)
    if len(self.rWaveBuffer) > self.bufferLength:
      self.rWaveBuffer.popleft()

  def checkBuffer(self):
    for idx in xrange(len(self.rWaveBuffer)-1):
      diff = (self.rWaveBuffer[idx+1] - self.rWaveBuffer[idx]).total_seconds()
      if (diff < self.timespan):
        self.significantFeatures += 1
    if self.significantFeatures > self.featureThreshold:
      self.resetFeatures()
      #print '404'
      return '404'
    else:
      self.resetFeatures()
      #print '200'
      return '200'

  def findRWavePeak(self, data):
    if data['amplitude'] > self.notch and not self.captureStream:
      # print 'START CAPTURE>>>>>>>>>>>>>>>>>>>>>'
      self.captureStream = True
      self.rWaveMaxBuffer.append(data)
    elif self.captureStream and data['amplitude'] > self.notch - .3:
      self.rWaveMaxBuffer.append(data)      
    elif len(self.rWaveMaxBuffer):
      # print 'END CAPTURE>>>>>>>>>>>>>>>>>>>>>>>'
      self.captureStream = False
      rWavePeakTime = max(self.rWaveMaxBuffer, key=lambda x: x['amplitude'])['time']
      # print 'rWaveMaxBuffer:', self.rWaveMaxBuffer
      # print 'rWavePeakTime:', rWavePeakTime
      self.addToBuffer(rWavePeakTime)
      self.resetRWaveMaxBuffer()

  def analyze(self, data):
    self.findRWavePeak(data)
    # self.drawData(data)
    return self.checkBuffer()

  def resetFeatures(self):
    self.significantFeatures = 0

  def resetRWaveMaxBuffer(self):
    self.rWaveMaxBuffer = []

  # visualize data with console graph, adjusted by offset
  def drawData(self, data):
    offset = 90
    # count datapoints
    print self.counter, 
    for idx in xrange(int(data['amplitude'] ** 3 - offset)): 
      print('>'),
    print('\n'),
    self.counter += 1
