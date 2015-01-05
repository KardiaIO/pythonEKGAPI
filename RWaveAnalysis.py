import collections
import datetime
import isodate

class RWaveAnalysis:

  def __init__(self, threshold, timespan):
    self.threshold = threshold
    self.timespan = timespan
    self.rWaveBuffer = collections.deque()
    self.significantFeatures = 0

  def addToBuffer(self, timeStamp):
    dateTimeObj = isodate.parse_datetime(timeStamp)
    self.rWaveBuffer.append(dateTimeObj)
    if len(self.rWaveBuffer) > 10:
      self.rWaveBuffer.popleft()

  def checkBuffer(self):
    for idx in xrange(len(self.rWaveBuffer)-1):
      diff = (self.rWaveBuffer[idx+1] - self.rWaveBuffer[idx]).total_seconds()
      if (diff < self.timespan):
        self.significantFeatures += 1
    if self.significantFeatures > self.threshold:
      self.resetFeatures()
      print '404'
      return '404'
    else:
      self.resetFeatures()
      print '200'
      return '200'

  def resetFeatures(self):
    self.significantFeatures = 0