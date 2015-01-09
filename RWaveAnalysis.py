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
    self.rWaveBuffer.append(datetime.datetime(1,1,1,1))
    self.rWaveMaxBuffer = []
    self.captureStream = False

  def addToBuffer(self, timeStamp):
    dateTimeObj = isodate.parse_datetime(timeStamp).replace(tzinfo=None)
    self.rWaveBuffer.append(dateTimeObj)
    if len(self.rWaveBuffer) > self.bufferLength:
      self.rWaveBuffer.popleft()

  def checkBuffer(self):
    timeDiffs = [self.rWaveBuffer[i+1] - self.rWaveBuffer[i] for i in range(len(self.rWaveBuffer)-1)]
    significantFeatures = [timeDiffs[i] for i in range(len(timeDiffs)) if timeDiffs[i].total_seconds() < self.featureThreshold]
    if len(significantFeatures) > self.featureThreshold:
      self.resetFeatures()
      return '404'
    else:
      self.resetFeatures()
      return '200'

  def findRWavePeak(self, data):
    if float(data['amplitude']) > self.notch and not self.captureStream and isodate.parse_datetime(data['time']).replace(tzinfo=None) > ((self.rWaveBuffer[len(self.rWaveBuffer) - 1] + datetime.timedelta(0, 0, 0, 600))):
      self.captureStream = True
    elif self.captureStream and float(data['amplitude']) > self.notch - .2:
      self.rWaveMaxBuffer.append(data)
    elif len(self.rWaveMaxBuffer):
      self.captureStream = False
      rWavePeakTime = max(self.rWaveMaxBuffer, key=lambda x: float(x['amplitude']))['time']
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
    for idx in xrange(int(float(data['amplitude']) ** 3 - offset)): 
      print('|'),
    print('\n'),