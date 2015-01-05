from operator import attrgetter
import collections
import datetime
import isodate

class RWaveAnalysis:

  def __init__(self, notch, threshold, timespan, bufferLength):
    self.notch = notch
    self.threshold = threshold
    self.timespan = timespan
    self.bufferLength = bufferLength
    self.rWaveBuffer = collections.deque()
    self.rWaveMaxBuffer = []
    self.significantFeatures = 0

  def addToBuffer(self, timeStamp):
    dateTimeObj = timeStamp #isodate.parse_datetime(timeStamp)
    self.rWaveBuffer.append(dateTimeObj)
    if len(self.rWaveBuffer) > self.bufferLength:
      self.rWaveBuffer.popleft()

  def checkBuffer(self):
    for idx in xrange(len(self.rWaveBuffer)-1):
      diff = (self.rWaveBuffer[idx+1] - self.rWaveBuffer[idx]) #.total_seconds()
      if (diff < self.timespan):
        self.significantFeatures += 1
    if self.significantFeatures > self.threshold:
      self.resetFeatures()
      print '404'
      return '404'
    else:
      self.resetFeatures()
      #print '200'
      return '200'

  def findRWavePeak(self, data):
    if data['amplitude'] > self.notch:
      self.rWaveMaxBuffer.append(data);
    elif len(self.rWaveMaxBuffer):
      rWavePeakTime = max(self.rWaveMaxBuffer, key=lambda x: x['amplitude'])['time']
      print 'rWaveMaxBuffer:', self.rWaveMaxBuffer
      print 'rWavePeakTime:', rWavePeakTime
      self.addToBuffer(rWavePeakTime)
      self.resetRWaveMaxBuffer()

  def analyze(self, data):
    self.findRWavePeak(data)
    return self.checkBuffer()

  def resetFeatures(self):
    self.significantFeatures = 0

  def resetRWaveMaxBuffer(self):
    self.rWaveMaxBuffer = []