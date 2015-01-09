from RWaveAnalysis import RWaveAnalysis
from operator import attrgetter
import collections
import datetime
import isodate

sampleData = [
{
    "time": 0 ,
    "amplitude": 4.995
  },
{
    "time": 0.003 ,
    "amplitude": 4.995
  },
{
    "time": 0.006 ,
    "amplitude": 4.995
  },
{
    "time": 0.008 ,
    "amplitude": 4.995
  },
{
    "time": 0.011 ,
    "amplitude": 4.995
  },
{
    "time": 0.014 ,
    "amplitude": 4.995
  },
{
    "time": 0.017 ,
    "amplitude": 4.995
  },
{
    "time": 0.019 ,
    "amplitude": 4.995
  },
{
    "time": 0.022 ,
    "amplitude": 4.985
  },
{
    "time": 0.025 ,
    "amplitude": 4.995
  },
{
    "time": 0.028 ,
    "amplitude": 4.995
  },
{
    "time": 0.031 ,
    "amplitude": 5
  },
{
    "time": 0.033 ,
    "amplitude": 5.025
  },
{
    "time": 0.036 ,
    "amplitude": 5.035
  },
{
    "time": 0.039 ,
    "amplitude": 5.015
  },
{
    "time": 0.042 ,
    "amplitude": 4.95
  },
{
    "time": 0.044 ,
    "amplitude": 4.895
  },
{
    "time": 0.047 ,
    "amplitude": 4.865
  },
{
    "time": 0.05 ,
    "amplitude": 4.84
  },
{
    "time": 0.053 ,
    "amplitude": 4.825
  },
{
    "time": 0.056 ,
    "amplitude": 4.78
  },
{
    "time": 0.058 ,
    "amplitude": 4.725
  },
{
    "time": 0.061 ,
    "amplitude": 4.71
  },
{
    "time": 0.064 ,
    "amplitude": 4.715
  },
{
    "time": 0.067 ,
    "amplitude": 4.74
  },
{
    "time": 0.069 ,
    "amplitude": 4.75
  },
{
    "time": 0.072 ,
    "amplitude": 4.73
  },
{
    "time": 0.075 ,
    "amplitude": 4.71
  },
{
    "time": 0.078 ,
    "amplitude": 4.695
  },
{
    "time": 0.081 ,
    "amplitude": 4.7
  },
{
    "time": 0.083 ,
    "amplitude": 4.715
  },
{
    "time": 0.086 ,
    "amplitude": 4.75
  },
{
    "time": 0.089 ,
    "amplitude": 4.745
  },
{
    "time": 0.092 ,
    "amplitude": 4.73
  },
{
    "time": 0.094 ,
    "amplitude": 4.71
  },
{
    "time": 0.097 ,
    "amplitude": 4.715
  },
{
    "time": 0.1 ,
    "amplitude": 4.725
  },
{
    "time": 0.103 ,
    "amplitude": 4.745
  },
{
    "time": 0.106 ,
    "amplitude": 4.73
  },
{
    "time": 0.108 ,
    "amplitude": 4.725
  },
{
    "time": 0.111 ,
    "amplitude": 4.725
  },
{
    "time": 0.114 ,
    "amplitude": 4.725
  },
{
    "time": 0.117 ,
    "amplitude": 4.735
  },
{
    "time": 0.119 ,
    "amplitude": 4.74
  },
{
    "time": 0.122 ,
    "amplitude": 4.735
  },
{
    "time": 0.125 ,
    "amplitude": 4.72
  },
{
    "time": 0.128 ,
    "amplitude": 4.715
  },
{
    "time": 0.131 ,
    "amplitude": 4.715
  },
{
    "time": 0.133 ,
    "amplitude": 4.715
  },
{
    "time": 0.136 ,
    "amplitude": 4.705
  },
{
    "time": 0.139 ,
    "amplitude": 4.685
  },
{
    "time": 0.142 ,
    "amplitude": 4.695
  },
{
    "time": 0.144 ,
    "amplitude": 4.695
  },
{
    "time": 0.147 ,
    "amplitude": 4.73
  },
{
    "time": 0.15 ,
    "amplitude": 4.745
  },
{
    "time": 0.153 ,
    "amplitude": 4.755
  },
{
    "time": 0.156 ,
    "amplitude": 4.75
  },
{
    "time": 0.158 ,
    "amplitude": 4.755
  },
{
    "time": 0.161 ,
    "amplitude": 4.74
  },
{
    "time": 0.164 ,
    "amplitude": 4.715
  },
{
    "time": 0.167 ,
    "amplitude": 4.715
  },
{
    "time": 0.169 ,
    "amplitude": 4.73
  },
{
    "time": 0.172 ,
    "amplitude": 4.755
  },
{
    "time": 0.175 ,
    "amplitude": 4.79
  },
{
    "time": 0.178 ,
    "amplitude": 4.8
  },
{
    "time": 0.181 ,
    "amplitude": 4.825
  },
{
    "time": 0.183 ,
    "amplitude": 4.85
  },
{
    "time": 0.186 ,
    "amplitude": 4.84
  },
{
    "time": 0.189 ,
    "amplitude": 4.78
  },
{
    "time": 0.192 ,
    "amplitude": 4.68
  },
{
    "time": 0.194 ,
    "amplitude": 4.61
  },
{
    "time": 0.197 ,
    "amplitude": 4.6
  },
{
    "time": 0.2 ,
    "amplitude": 4.61
  },
{
    "time": 0.203 ,
    "amplitude": 4.61
  },
{
    "time": 0.206 ,
    "amplitude": 4.585
  },
{
    "time": 0.208 ,
    "amplitude": 4.58
  },
{
    "time": 0.211 ,
    "amplitude": 4.535
  },
{
    "time": 0.214 ,
    "amplitude": 4.495
  },
{
    "time": 0.217 ,
    "amplitude": 4.48
  },
{
    "time": 0.219 ,
    "amplitude": 4.47
  },
{
    "time": 0.222 ,
    "amplitude": 4.435
  },
{
    "time": 0.225 ,
    "amplitude": 4.39
  },
{
    "time": 0.228 ,
    "amplitude": 4.34
  },
{
    "time": 0.231 ,
    "amplitude": 4.285
  },
{
    "time": 0.233 ,
    "amplitude": 4.235
  },
{
    "time": 0.236 ,
    "amplitude": 4.205
  },
{
    "time": 0.239 ,
    "amplitude": 4.18
  },
{
    "time": 0.242 ,
    "amplitude": 4.145
  },
{
    "time": 0.244 ,
    "amplitude": 4.14
  },
{
    "time": 0.247 ,
    "amplitude": 4.18
  },
{
    "time": 0.25 ,
    "amplitude": 4.205
  },
{
    "time": 0.253 ,
    "amplitude": 4.225
  },
{
    "time": 0.256 ,
    "amplitude": 4.23
  },
{
    "time": 0.258 ,
    "amplitude": 4.29
  },
{
    "time": 0.261 ,
    "amplitude": 4.36
  },
{
    "time": 0.264 ,
    "amplitude": 4.42
  },
{
    "time": 0.267 ,
    "amplitude": 4.495
  },
{
    "time": 0.269 ,
    "amplitude": 4.54
  },
{
    "time": 0.272 ,
    "amplitude": 4.575
  },
{
    "time": 0.275 ,
    "amplitude": 4.615
  },
{
    "time": 0.278 ,
    "amplitude": 4.635
  },
{
    "time": 0.281 ,
    "amplitude": 4.675
  },
{
    "time": 0.283 ,
    "amplitude": 4.725
  },
{
    "time": 0.286 ,
    "amplitude": 4.75
  },
{
    "time": 0.289 ,
    "amplitude": 4.75
  },
{
    "time": 0.292 ,
    "amplitude": 4.76
  },
{
    "time": 0.294 ,
    "amplitude": 4.76
  },
{
    "time": 0.297 ,
    "amplitude": 4.765
  },
{
    "time": 0.3 ,
    "amplitude": 4.795
  },
{
    "time": 0.303 ,
    "amplitude": 4.805
  },
{
    "time": 0.306 ,
    "amplitude": 4.8
  },
{
    "time": 0.308 ,
    "amplitude": 4.775
  },
{
    "time": 0.311 ,
    "amplitude": 4.775
  },
{
    "time": 0.314 ,
    "amplitude": 4.79
  },
{
    "time": 0.317 ,
    "amplitude": 4.82
  },
{
    "time": 0.319 ,
    "amplitude": 4.835
  },
{
    "time": 0.322 ,
    "amplitude": 4.82
  },
{
    "time": 0.325 ,
    "amplitude": 4.83
  },
{
    "time": 0.328 ,
    "amplitude": 4.825
  },
{
    "time": 0.331 ,
    "amplitude": 4.82
  },
{
    "time": 0.333 ,
    "amplitude": 4.83
  },
{
    "time": 0.336 ,
    "amplitude": 4.84
  },
{
    "time": 0.339 ,
    "amplitude": 4.835
  },
{
    "time": 0.342 ,
    "amplitude": 4.8
  },
{
    "time": 0.344 ,
    "amplitude": 4.8
  },
{
    "time": 0.347 ,
    "amplitude": 4.81
  },
{
    "time": 0.35 ,
    "amplitude": 4.825
  },
{
    "time": 0.353 ,
    "amplitude": 4.835
  },
{
    "time": 0.356 ,
    "amplitude": 4.845
  },
{
    "time": 0.358 ,
    "amplitude": 4.835
  },
{
    "time": 0.361 ,
    "amplitude": 4.83
  },
{
    "time": 0.364 ,
    "amplitude": 4.825
  },
{
    "time": 0.367 ,
    "amplitude": 4.835
  },
{
    "time": 0.369 ,
    "amplitude": 4.835
  },
{
    "time": 0.372 ,
    "amplitude": 4.83
  },
{
    "time": 0.375 ,
    "amplitude": 4.835
  },
{
    "time": 0.378 ,
    "amplitude": 4.845
  },
{
    "time": 0.381 ,
    "amplitude": 4.84
  },
{
    "time": 0.383 ,
    "amplitude": 4.85
  },
{
    "time": 0.386 ,
    "amplitude": 4.86
  },
{
    "time": 0.389 ,
    "amplitude": 4.85
  },
{
    "time": 0.392 ,
    "amplitude": 4.85
  },
{
    "time": 0.394 ,
    "amplitude": 4.845
  },
{
    "time": 0.397 ,
    "amplitude": 4.86
  },
{
    "time": 0.4 ,
    "amplitude": 4.88
  },
{
    "time": 0.403 ,
    "amplitude": 4.895
  },
{
    "time": 0.406 ,
    "amplitude": 4.88
  },
{
    "time": 0.408 ,
    "amplitude": 4.855
  },
{
    "time": 0.411 ,
    "amplitude": 4.84
  },
{
    "time": 0.414 ,
    "amplitude": 4.845
  },
{
    "time": 0.417 ,
    "amplitude": 4.88
  },
{
    "time": 0.419 ,
    "amplitude": 4.9
  },
{
    "time": 0.422 ,
    "amplitude": 4.9
  },
{
    "time": 0.425 ,
    "amplitude": 4.895
  },
{
    "time": 0.428 ,
    "amplitude": 4.88
  },
{
    "time": 0.431 ,
    "amplitude": 4.9
  },
{
    "time": 0.433 ,
    "amplitude": 4.92
  },
{
    "time": 0.436 ,
    "amplitude": 4.93
  },
{
    "time": 0.439 ,
    "amplitude": 4.935
  },
{
    "time": 0.442 ,
    "amplitude": 4.9
  },
{
    "time": 0.444 ,
    "amplitude": 4.875
  },
{
    "time": 0.447 ,
    "amplitude": 4.895
  },
{
    "time": 0.45 ,
    "amplitude": 4.925
  },
{
    "time": 0.453 ,
    "amplitude": 4.935
  },
{
    "time": 0.456 ,
    "amplitude": 4.955
  },
{
    "time": 0.458 ,
    "amplitude": 4.94
  },
{
    "time": 0.461 ,
    "amplitude": 4.93
  },
{
    "time": 0.464 ,
    "amplitude": 4.935
  },
{
    "time": 0.467 ,
    "amplitude": 4.94
  },
{
    "time": 0.469 ,
    "amplitude": 4.955
  },
{
    "time": 0.472 ,
    "amplitude": 4.95
  },
{
    "time": 0.475 ,
    "amplitude": 4.965
  },
{
    "time": 0.478 ,
    "amplitude": 4.96
  },
{
    "time": 0.481 ,
    "amplitude": 4.945
  },
{
    "time": 0.483 ,
    "amplitude": 4.945
  },
{
    "time": 0.486 ,
    "amplitude": 4.975
  },
{
    "time": 0.489 ,
    "amplitude": 4.95
  },
{
    "time": 0.492 ,
    "amplitude": 4.96
  },
{
    "time": 0.494 ,
    "amplitude": 4.955
  },
{
    "time": 0.497 ,
    "amplitude": 4.955
  },
{
    "time": 0.5 ,
    "amplitude": 4.96
  },
{
    "time": 0.503 ,
    "amplitude": 4.965
  },
{
    "time": 0.506 ,
    "amplitude": 4.955
  },
{
    "time": 0.508 ,
    "amplitude": 4.95
  },
{
    "time": 0.511 ,
    "amplitude": 4.93
  },
{
    "time": 0.514 ,
    "amplitude": 4.925
  },
{
    "time": 0.517 ,
    "amplitude": 4.925
  },
{
    "time": 0.519 ,
    "amplitude": 4.94
  },
{
    "time": 0.522 ,
    "amplitude": 4.94
  },
{
    "time": 0.525 ,
    "amplitude": 4.92
  },
{
    "time": 0.528 ,
    "amplitude": 4.92
  },
{
    "time": 0.531 ,
    "amplitude": 4.915
  },
{
    "time": 0.533 ,
    "amplitude": 4.92
  },
{
    "time": 0.536 ,
    "amplitude": 4.93
  },
{
    "time": 0.539 ,
    "amplitude": 4.93
  },
{
    "time": 0.542 ,
    "amplitude": 4.92
  },
{
    "time": 0.544 ,
    "amplitude": 4.89
  },
{
    "time": 0.547 ,
    "amplitude": 4.895
  },
{
    "time": 0.55 ,
    "amplitude": 4.91
  },
{
    "time": 0.553 ,
    "amplitude": 4.905
  },
{
    "time": 0.556 ,
    "amplitude": 4.915
  },
{
    "time": 0.558 ,
    "amplitude": 4.905
  },
{
    "time": 0.561 ,
    "amplitude": 4.89
  },
{
    "time": 0.564 ,
    "amplitude": 4.86
  },
{
    "time": 0.567 ,
    "amplitude": 4.865
  },
{
    "time": 0.569 ,
    "amplitude": 4.87
  },
{
    "time": 0.572 ,
    "amplitude": 4.88
  },
{
    "time": 0.575 ,
    "amplitude": 4.875
  },
{
    "time": 0.578 ,
    "amplitude": 4.87
  },
{
    "time": 0.581 ,
    "amplitude": 4.855
  },
{
    "time": 0.583 ,
    "amplitude": 4.85
  },
{
    "time": 0.586 ,
    "amplitude": 4.865
  },
{
    "time": 0.589 ,
    "amplitude": 4.855
  },
{
    "time": 0.592 ,
    "amplitude": 4.855
  },
{
    "time": 0.594 ,
    "amplitude": 4.85
  },
{
    "time": 0.597 ,
    "amplitude": 4.84
  },
{
    "time": 0.6 ,
    "amplitude": 4.86
  },
{
    "time": 0.603 ,
    "amplitude": 4.865
  },
{
    "time": 0.606 ,
    "amplitude": 4.86
  },
{
    "time": 0.608 ,
    "amplitude": 4.85
  },
{
    "time": 0.611 ,
    "amplitude": 4.845
  },
{
    "time": 0.614 ,
    "amplitude": 4.85
  },
{
    "time": 0.617 ,
    "amplitude": 4.865
  },
{
    "time": 0.619 ,
    "amplitude": 4.865
  },
{
    "time": 0.622 ,
    "amplitude": 4.86
  },
{
    "time": 0.625 ,
    "amplitude": 4.85
  },
{
    "time": 0.628 ,
    "amplitude": 4.845
  },
{
    "time": 0.631 ,
    "amplitude": 4.85
  },
{
    "time": 0.633 ,
    "amplitude": 4.855
  },
{
    "time": 0.636 ,
    "amplitude": 4.865
  },
{
    "time": 0.639 ,
    "amplitude": 4.855
  },
{
    "time": 0.642 ,
    "amplitude": 4.84
  },
{
    "time": 0.644 ,
    "amplitude": 4.835
  },
{
    "time": 0.647 ,
    "amplitude": 4.835
  },
{
    "time": 0.65 ,
    "amplitude": 4.84
  },
{
    "time": 0.653 ,
    "amplitude": 4.86
  },
{
    "time": 0.656 ,
    "amplitude": 4.855
  },
{
    "time": 0.658 ,
    "amplitude": 4.85
  },
{
    "time": 0.661 ,
    "amplitude": 4.84
  },
{
    "time": 0.664 ,
    "amplitude": 4.835
  },
{
    "time": 0.667 ,
    "amplitude": 4.835
  },
{
    "time": 0.669 ,
    "amplitude": 4.86
  },
{
    "time": 0.672 ,
    "amplitude": 4.865
  },
{
    "time": 0.675 ,
    "amplitude": 4.85
  },
{
    "time": 0.678 ,
    "amplitude": 4.845
  },
{
    "time": 0.681 ,
    "amplitude": 4.835
  },
{
    "time": 0.683 ,
    "amplitude": 4.85
  },
{
    "time": 0.686 ,
    "amplitude": 4.845
  },
{
    "time": 0.689 ,
    "amplitude": 4.83
  },
{
    "time": 0.692 ,
    "amplitude": 4.815
  },
{
    "time": 0.694 ,
    "amplitude": 4.8
  },
{
    "time": 0.697 ,
    "amplitude": 4.815
  },
{
    "time": 0.7 ,
    "amplitude": 4.83
  },
{
    "time": 0.703 ,
    "amplitude": 4.845
  },
{
    "time": 0.706 ,
    "amplitude": 4.835
  },
{
    "time": 0.708 ,
    "amplitude": 4.81
  },
{
    "time": 0.711 ,
    "amplitude": 4.795
  },
{
    "time": 0.714 ,
    "amplitude": 4.805
  },
{
    "time": 0.717 ,
    "amplitude": 4.805
  },
{
    "time": 0.719 ,
    "amplitude": 4.82
  },
{
    "time": 0.722 ,
    "amplitude": 4.81
  },
{
    "time": 0.725 ,
    "amplitude": 4.785
  },
{
    "time": 0.728 ,
    "amplitude": 4.78
  },
{
    "time": 0.731 ,
    "amplitude": 4.755
  },
{
    "time": 0.733 ,
    "amplitude": 4.765
  },
{
    "time": 0.736 ,
    "amplitude": 4.785
  },
{
    "time": 0.739 ,
    "amplitude": 4.78
  },
{
    "time": 0.742 ,
    "amplitude": 4.78
  },
{
    "time": 0.744 ,
    "amplitude": 4.745
  },
{
    "time": 0.747 ,
    "amplitude": 4.755
  },
{
    "time": 0.75 ,
    "amplitude": 4.77
  },
{
    "time": 0.753 ,
    "amplitude": 4.78
  },
{
    "time": 0.756 ,
    "amplitude": 4.76
  },
{
    "time": 0.758 ,
    "amplitude": 4.76
  },
{
    "time": 0.761 ,
    "amplitude": 4.745
  },
{
    "time": 0.764 ,
    "amplitude": 4.75
  },
{
    "time": 0.767 ,
    "amplitude": 4.765
  },
{
    "time": 0.769 ,
    "amplitude": 4.77
  },
{
    "time": 0.772 ,
    "amplitude": 4.77
  },
{
    "time": 0.775 ,
    "amplitude": 4.76
  },
{
    "time": 0.778 ,
    "amplitude": 4.75
  },
{
    "time": 0.781 ,
    "amplitude": 4.745
  },
{
    "time": 0.783 ,
    "amplitude": 4.745
  },
{
    "time": 0.786 ,
    "amplitude": 4.77
  },
{
    "time": 0.789 ,
    "amplitude": 4.76
  },
{
    "time": 0.792 ,
    "amplitude": 4.76
  },
{
    "time": 0.794 ,
    "amplitude": 4.74
  },
{
    "time": 0.797 ,
    "amplitude": 4.745
  },
{
    "time": 0.8 ,
    "amplitude": 4.765
  },
{
    "time": 0.803 ,
    "amplitude": 4.775
  },
{
    "time": 0.806 ,
    "amplitude": 4.78
  },
{
    "time": 0.808 ,
    "amplitude": 4.775
  },
{
    "time": 0.811 ,
    "amplitude": 4.765
  },
{
    "time": 0.814 ,
    "amplitude": 4.76
  },
{
    "time": 0.817 ,
    "amplitude": 4.775
  },
{
    "time": 0.819 ,
    "amplitude": 4.785
  },
{
    "time": 0.822 ,
    "amplitude": 4.775
  },
{
    "time": 0.825 ,
    "amplitude": 4.78
  },
{
    "time": 0.828 ,
    "amplitude": 4.78
  },
{
    "time": 0.831 ,
    "amplitude": 4.78
  },
{
    "time": 0.833 ,
    "amplitude": 4.79
  },
{
    "time": 0.836 ,
    "amplitude": 4.79
  },
{
    "time": 0.839 ,
    "amplitude": 4.795
  },
{
    "time": 0.842 ,
    "amplitude": 4.79
  },
{
    "time": 0.844 ,
    "amplitude": 4.785
  },
{
    "time": 0.847 ,
    "amplitude": 4.79
  },
{
    "time": 0.85 ,
    "amplitude": 4.81
  },
{
    "time": 0.853 ,
    "amplitude": 4.825
  },
{
    "time": 0.856 ,
    "amplitude": 4.82
  },
{
    "time": 0.858 ,
    "amplitude": 4.8
  },
{
    "time": 0.861 ,
    "amplitude": 4.79
  },
{
    "time": 0.864 ,
    "amplitude": 4.775
  },
{
    "time": 0.867 ,
    "amplitude": 4.795
  },
{
    "time": 0.869 ,
    "amplitude": 4.805
  },
{
    "time": 0.872 ,
    "amplitude": 4.81
  },
{
    "time": 0.875 ,
    "amplitude": 4.805
  },
{
    "time": 0.878 ,
    "amplitude": 4.775
  },
{
    "time": 0.881 ,
    "amplitude": 4.79
  },
{
    "time": 0.883 ,
    "amplitude": 4.81
  },
{
    "time": 0.886 ,
    "amplitude": 4.83
  },
{
    "time": 0.889 ,
    "amplitude": 4.805
  },
{
    "time": 0.892 ,
    "amplitude": 4.785
  },
{
    "time": 0.894 ,
    "amplitude": 4.785
  },
{
    "time": 0.897 ,
    "amplitude": 4.775
  },
{
    "time": 0.9 ,
    "amplitude": 4.795
  },
{
    "time": 0.903 ,
    "amplitude": 4.815
  },
{
    "time": 0.906 ,
    "amplitude": 4.82
  },
{
    "time": 0.908 ,
    "amplitude": 4.815
  },
{
    "time": 0.911 ,
    "amplitude": 4.815
  },
{
    "time": 0.914 ,
    "amplitude": 4.805
  },
{
    "time": 0.917 ,
    "amplitude": 4.82
  },
{
    "time": 0.919 ,
    "amplitude": 4.83
  },
{
    "time": 0.922 ,
    "amplitude": 4.82
  },
{
    "time": 0.925 ,
    "amplitude": 4.8
  },
{
    "time": 0.928 ,
    "amplitude": 4.795
  },
{
    "time": 0.931 ,
    "amplitude": 4.8
  },
{
    "time": 0.933 ,
    "amplitude": 4.815
  },
{
    "time": 0.936 ,
    "amplitude": 4.815
  },
{
    "time": 0.939 ,
    "amplitude": 4.81
  },
{
    "time": 0.942 ,
    "amplitude": 4.81
  },
{
    "time": 0.944 ,
    "amplitude": 4.81
  },
{
    "time": 0.947 ,
    "amplitude": 4.815
  },
{
    "time": 0.95 ,
    "amplitude": 4.82
  },
{
    "time": 0.953 ,
    "amplitude": 4.84
  },
{
    "time": 0.956 ,
    "amplitude": 4.855
  },
{
    "time": 0.958 ,
    "amplitude": 4.845
  },
{
    "time": 0.961 ,
    "amplitude": 4.84
  },
{
    "time": 0.964 ,
    "amplitude": 4.855
  },
{
    "time": 0.967 ,
    "amplitude": 4.87
  },
{
    "time": 0.969 ,
    "amplitude": 4.885
  },
{
    "time": 0.972 ,
    "amplitude": 4.895
  },
{
    "time": 0.975 ,
    "amplitude": 4.895
  },
{
    "time": 0.978 ,
    "amplitude": 4.89
  },
{
    "time": 0.981 ,
    "amplitude": 4.92
  },
{
    "time": 0.983 ,
    "amplitude": 4.94
  },
{
    "time": 0.986 ,
    "amplitude": 4.965
  },
{
    "time": 0.989 ,
    "amplitude": 4.975
  },
{
    "time": 0.992 ,
    "amplitude": 4.97
  },
{
    "time": 0.994 ,
    "amplitude": 4.97
  },
{
    "time": 0.997 ,
    "amplitude": 5
  },
{
    "time": 1 ,
    "amplitude": 5.015
  },
{
    "time": 1.003 ,
    "amplitude": 5.025
  },
{
    "time": 1.006 ,
    "amplitude": 5.035
  },
{
    "time": 1.008 ,
    "amplitude": 5.03
  },
{
    "time": 1.011 ,
    "amplitude": 5.025
  },
{
    "time": 1.014 ,
    "amplitude": 5.025
  },
{
    "time": 1.017 ,
    "amplitude": 5.045
  },
{
    "time": 1.019 ,
    "amplitude": 5.065
  },
{
    "time": 1.022 ,
    "amplitude": 5.07
  },
{
    "time": 1.025 ,
    "amplitude": 5.055
  },
{
    "time": 1.028 ,
    "amplitude": 5.01
  },
{
    "time": 1.031 ,
    "amplitude": 4.985
  },
{
    "time": 1.033 ,
    "amplitude": 4.955
  },
{
    "time": 1.036 ,
    "amplitude": 4.935
  },
{
    "time": 1.039 ,
    "amplitude": 4.9
  },
{
    "time": 1.042 ,
    "amplitude": 4.845
  },
{
    "time": 1.044 ,
    "amplitude": 4.8
  },
{
    "time": 1.047 ,
    "amplitude": 4.77
  },
{
    "time": 1.05 ,
    "amplitude": 4.75
  },
{
    "time": 1.053 ,
    "amplitude": 4.77
  },
{
    "time": 1.056 ,
    "amplitude": 4.77
  },
{
    "time": 1.058 ,
    "amplitude": 4.765
  },
{
    "time": 1.061 ,
    "amplitude": 4.76
  },
{
    "time": 1.064 ,
    "amplitude": 4.755
  },
{
    "time": 1.067 ,
    "amplitude": 4.76
  },
{
    "time": 1.069 ,
    "amplitude": 4.775
  },
{
    "time": 1.072 ,
    "amplitude": 4.78
  },
{
    "time": 1.075 ,
    "amplitude": 4.765
  },
{
    "time": 1.078 ,
    "amplitude": 4.75
  },
{
    "time": 1.081 ,
    "amplitude": 4.74
  },
{
    "time": 1.083 ,
    "amplitude": 4.73
  },
{
    "time": 1.086 ,
    "amplitude": 4.76
  },
{
    "time": 1.089 ,
    "amplitude": 4.78
  },
{
    "time": 1.092 ,
    "amplitude": 4.8
  },
{
    "time": 1.094 ,
    "amplitude": 4.78
  },
{
    "time": 1.097 ,
    "amplitude": 4.76
  },
{
    "time": 1.1 ,
    "amplitude": 4.765
  },
{
    "time": 1.103 ,
    "amplitude": 4.775
  },
{
    "time": 1.106 ,
    "amplitude": 4.78
  },
{
    "time": 1.108 ,
    "amplitude": 4.765
  },
{
    "time": 1.111 ,
    "amplitude": 4.77
  },
{
    "time": 1.114 ,
    "amplitude": 4.77
  },
{
    "time": 1.117 ,
    "amplitude": 4.775
  },
{
    "time": 1.119 ,
    "amplitude": 4.77
  },
{
    "time": 1.122 ,
    "amplitude": 4.765
  },
{
    "time": 1.125 ,
    "amplitude": 4.75
  },
{
    "time": 1.128 ,
    "amplitude": 4.75
  },
{
    "time": 1.131 ,
    "amplitude": 4.76
  },
{
    "time": 1.133 ,
    "amplitude": 4.775
  },
{
    "time": 1.136 ,
    "amplitude": 4.79
  },
{
    "time": 1.139 ,
    "amplitude": 4.79
  },
{
    "time": 1.142 ,
    "amplitude": 4.77
  },
{
    "time": 1.144 ,
    "amplitude": 4.76
  },
{
    "time": 1.147 ,
    "amplitude": 4.75
  },
{
    "time": 1.15 ,
    "amplitude": 4.745
  },
{
    "time": 1.153 ,
    "amplitude": 4.735
  },
{
    "time": 1.156 ,
    "amplitude": 4.73
  },
{
    "time": 1.158 ,
    "amplitude": 4.745
  },
{
    "time": 1.161 ,
    "amplitude": 4.775
  },
{
    "time": 1.164 ,
    "amplitude": 4.805
  },
{
    "time": 1.167 ,
    "amplitude": 4.845
  },
{
    "time": 1.169 ,
    "amplitude": 4.87
  },
{
    "time": 1.172 ,
    "amplitude": 4.855
  },
{
    "time": 1.175 ,
    "amplitude": 4.78
  },
{
    "time": 1.178 ,
    "amplitude": 4.695
  },
{
    "time": 1.181 ,
    "amplitude": 4.625
  },
{
    "time": 1.183 ,
    "amplitude": 4.61
  },
{
    "time": 1.186 ,
    "amplitude": 4.625
  },
{
    "time": 1.189 ,
    "amplitude": 4.635
  },
{
    "time": 1.192 ,
    "amplitude": 4.625
  },
{
    "time": 1.194 ,
    "amplitude": 4.59
  },
{
    "time": 1.197 ,
    "amplitude": 4.545
  },
{
    "time": 1.2 ,
    "amplitude": 4.52
  },
{
    "time": 1.203 ,
    "amplitude": 4.49
  },
{
    "time": 1.206 ,
    "amplitude": 4.465
  },
{
    "time": 1.208 ,
    "amplitude": 4.44
  },
{
    "time": 1.211 ,
    "amplitude": 4.395
  },
{
    "time": 1.214 ,
    "amplitude": 4.34
  },
{
    "time": 1.217 ,
    "amplitude": 4.275
  },
{
    "time": 1.219 ,
    "amplitude": 4.22
  },
{
    "time": 1.222 ,
    "amplitude": 4.205
  },
{
    "time": 1.225 ,
    "amplitude": 4.185
  },
{
    "time": 1.228 ,
    "amplitude": 4.185
  },
{
    "time": 1.231 ,
    "amplitude": 4.205
  },
{
    "time": 1.233 ,
    "amplitude": 4.24
  },
{
    "time": 1.236 ,
    "amplitude": 4.265
  },
{
    "time": 1.239 ,
    "amplitude": 4.3
  },
{
    "time": 1.242 ,
    "amplitude": 4.365
  },
{
    "time": 1.244 ,
    "amplitude": 4.435
  },
{
    "time": 1.247 ,
    "amplitude": 4.51
  },
{
    "time": 1.25 ,
    "amplitude": 4.57
  },
{
    "time": 1.253 ,
    "amplitude": 4.61
  },
{
    "time": 1.256 ,
    "amplitude": 4.64
  },
{
    "time": 1.258 ,
    "amplitude": 4.68
  },
{
    "time": 1.261 ,
    "amplitude": 4.73
  },
{
    "time": 1.264 ,
    "amplitude": 4.765
  },
{
    "time": 1.267 ,
    "amplitude": 4.805
  },
{
    "time": 1.269 ,
    "amplitude": 4.82
  },
{
    "time": 1.272 ,
    "amplitude": 4.82
  },
{
    "time": 1.275 ,
    "amplitude": 4.82
  },
{
    "time": 1.278 ,
    "amplitude": 4.82
  },
{
    "time": 1.281 ,
    "amplitude": 4.83
  },
{
    "time": 1.283 ,
    "amplitude": 4.845
  },
{
    "time": 1.286 ,
    "amplitude": 4.855
  },
{
    "time": 1.289 ,
    "amplitude": 4.845
  },
{
    "time": 1.292 ,
    "amplitude": 4.83
  },
{
    "time": 1.294 ,
    "amplitude": 4.82
  },
{
    "time": 1.297 ,
    "amplitude": 4.845
  },
{
    "time": 1.3 ,
    "amplitude": 4.865
  },
{
    "time": 1.303 ,
    "amplitude": 4.875
  },
{
    "time": 1.306 ,
    "amplitude": 4.86
  },
{
    "time": 1.308 ,
    "amplitude": 4.84
  },
{
    "time": 1.311 ,
    "amplitude": 4.845
  },
{
    "time": 1.314 ,
    "amplitude": 4.86
  },
{
    "time": 1.317 ,
    "amplitude": 4.875
  },
{
    "time": 1.319 ,
    "amplitude": 4.88
  },
{
    "time": 1.322 ,
    "amplitude": 4.87
  },
{
    "time": 1.325 ,
    "amplitude": 4.875
  },
{
    "time": 1.328 ,
    "amplitude": 4.86
  },
{
    "time": 1.331 ,
    "amplitude": 4.855
  },
{
    "time": 1.333 ,
    "amplitude": 4.85
  },
{
    "time": 1.336 ,
    "amplitude": 4.88
  },
{
    "time": 1.339 ,
    "amplitude": 4.89
  },
{
    "time": 1.342 ,
    "amplitude": 4.9
  },
{
    "time": 1.344 ,
    "amplitude": 4.895
  },
{
    "time": 1.347 ,
    "amplitude": 4.9
  },
{
    "time": 1.35 ,
    "amplitude": 4.895
  },
{
    "time": 1.353 ,
    "amplitude": 4.895
  },
{
    "time": 1.356 ,
    "amplitude": 4.895
  },
{
    "time": 1.358 ,
    "amplitude": 4.88
  },
{
    "time": 1.361 ,
    "amplitude": 4.88
  },
{
    "time": 1.364 ,
    "amplitude": 4.88
  },
{
    "time": 1.367 ,
    "amplitude": 4.89
  },
{
    "time": 1.369 ,
    "amplitude": 4.92
  },
{
    "time": 1.372 ,
    "amplitude": 4.925
  },
{
    "time": 1.375 ,
    "amplitude": 4.92
  },
{
    "time": 1.378 ,
    "amplitude": 4.905
  },
{
    "time": 1.381 ,
    "amplitude": 4.89
  },
{
    "time": 1.383 ,
    "amplitude": 4.905
  },
{
    "time": 1.386 ,
    "amplitude": 4.94
  },
{
    "time": 1.389 ,
    "amplitude": 4.94
  },
{
    "time": 1.392 ,
    "amplitude": 4.935
  },
{
    "time": 1.394 ,
    "amplitude": 4.925
  },
{
    "time": 1.397 ,
    "amplitude": 4.92
  },
{
    "time": 1.4 ,
    "amplitude": 4.925
  },
{
    "time": 1.403 ,
    "amplitude": 4.945
  },
{
    "time": 1.406 ,
    "amplitude": 4.965
  },
{
    "time": 1.408 ,
    "amplitude": 4.965
  },
{
    "time": 1.411 ,
    "amplitude": 4.945
  },
{
    "time": 1.414 ,
    "amplitude": 4.95
  },
{
    "time": 1.417 ,
    "amplitude": 4.975
  },
{
    "time": 1.419 ,
    "amplitude": 4.98
  },
{
    "time": 1.422 ,
    "amplitude": 4.97
  },
{
    "time": 1.425 ,
    "amplitude": 4.96
  },
{
    "time": 1.428 ,
    "amplitude": 4.965
  },
{
    "time": 1.431 ,
    "amplitude": 4.98
  },
{
    "time": 1.433 ,
    "amplitude": 4.985
  },
{
    "time": 1.436 ,
    "amplitude": 5.005
  },
{
    "time": 1.439 ,
    "amplitude": 5
  },
{
    "time": 1.442 ,
    "amplitude": 5.01
  },
{
    "time": 1.444 ,
    "amplitude": 5.005
  },
{
    "time": 1.447 ,
    "amplitude": 5.01
  },
{
    "time": 1.45 ,
    "amplitude": 5.01
  },
{
    "time": 1.453 ,
    "amplitude": 5.025
  },
{
    "time": 1.456 ,
    "amplitude": 5.01
  },
{
    "time": 1.458 ,
    "amplitude": 5.005
  },
{
    "time": 1.461 ,
    "amplitude": 4.99
  },
{
    "time": 1.464 ,
    "amplitude": 5
  },
{
    "time": 1.467 ,
    "amplitude": 5.015
  },
{
    "time": 1.469 ,
    "amplitude": 5.02
  },
{
    "time": 1.472 ,
    "amplitude": 5.01
  },
{
    "time": 1.475 ,
    "amplitude": 5.005
  },
{
    "time": 1.478 ,
    "amplitude": 5
  },
{
    "time": 1.481 ,
    "amplitude": 5.015
  },
{
    "time": 1.483 ,
    "amplitude": 5.035
  },
{
    "time": 1.486 ,
    "amplitude": 5.03
  },
{
    "time": 1.489 ,
    "amplitude": 5.02
  },
{
    "time": 1.492 ,
    "amplitude": 5.005
  },
{
    "time": 1.494 ,
    "amplitude": 4.99
  },
{
    "time": 1.497 ,
    "amplitude": 4.995
  },
{
    "time": 1.5 ,
    "amplitude": 5.02
  },
{
    "time": 1.503 ,
    "amplitude": 5.02
  },
{
    "time": 1.506 ,
    "amplitude": 5.005
  },
{
    "time": 1.508 ,
    "amplitude": 4.99
  },
{
    "time": 1.511 ,
    "amplitude": 4.975
  },
{
    "time": 1.514 ,
    "amplitude": 4.965
  },
{
    "time": 1.517 ,
    "amplitude": 4.96
  },
{
    "time": 1.519 ,
    "amplitude": 4.98
  },
{
    "time": 1.522 ,
    "amplitude": 4.98
  },
{
    "time": 1.525 ,
    "amplitude": 4.975
  },
{
    "time": 1.528 ,
    "amplitude": 4.955
  },
{
    "time": 1.531 ,
    "amplitude": 4.93
  },
{
    "time": 1.533 ,
    "amplitude": 4.925
  },
{
    "time": 1.536 ,
    "amplitude": 4.95
  },
{
    "time": 1.539 ,
    "amplitude": 4.955
  },
{
    "time": 1.542 ,
    "amplitude": 4.94
  },
{
    "time": 1.544 ,
    "amplitude": 4.93
  },
{
    "time": 1.547 ,
    "amplitude": 4.915
  },
{
    "time": 1.55 ,
    "amplitude": 4.92
  },
{
    "time": 1.553 ,
    "amplitude": 4.95
  },
{
    "time": 1.556 ,
    "amplitude": 4.93
  },
{
    "time": 1.558 ,
    "amplitude": 4.915
  },
{
    "time": 1.561 ,
    "amplitude": 4.91
  },
{
    "time": 1.564 ,
    "amplitude": 4.905
  },
{
    "time": 1.567 ,
    "amplitude": 4.905
  },
{
    "time": 1.569 ,
    "amplitude": 4.915
  },
{
    "time": 1.572 ,
    "amplitude": 4.915
  },
{
    "time": 1.575 ,
    "amplitude": 4.905
  },
{
    "time": 1.578 ,
    "amplitude": 4.895
  },
{
    "time": 1.581 ,
    "amplitude": 4.91
  },
{
    "time": 1.583 ,
    "amplitude": 4.92
  },
{
    "time": 1.586 ,
    "amplitude": 4.925
  },
{
    "time": 1.589 ,
    "amplitude": 4.91
  },
{
    "time": 1.592 ,
    "amplitude": 4.895
  },
{
    "time": 1.594 ,
    "amplitude": 4.88
  },
{
    "time": 1.597 ,
    "amplitude": 4.88
  },
{
    "time": 1.6 ,
    "amplitude": 4.88
  },
{
    "time": 1.603 ,
    "amplitude": 4.875
  },
{
    "time": 1.606 ,
    "amplitude": 4.875
  },
{
    "time": 1.608 ,
    "amplitude": 4.89
  },
{
    "time": 1.611 ,
    "amplitude": 4.895
  },
{
    "time": 1.614 ,
    "amplitude": 4.9
  },
{
    "time": 1.617 ,
    "amplitude": 4.895
  },
{
    "time": 1.619 ,
    "amplitude": 4.885
  },
{
    "time": 1.622 ,
    "amplitude": 4.885
  },
{
    "time": 1.625 ,
    "amplitude": 4.86
  },
{
    "time": 1.628 ,
    "amplitude": 4.855
  },
{
    "time": 1.631 ,
    "amplitude": 4.87
  },
{
    "time": 1.633 ,
    "amplitude": 4.885
  },
{
    "time": 1.636 ,
    "amplitude": 4.895
  },
{
    "time": 1.639 ,
    "amplitude": 4.885
  },
{
    "time": 1.642 ,
    "amplitude": 4.87
  },
{
    "time": 1.644 ,
    "amplitude": 4.835
  },
{
    "time": 1.647 ,
    "amplitude": 4.84
  },
{
    "time": 1.65 ,
    "amplitude": 4.86
  },
{
    "time": 1.653 ,
    "amplitude": 4.87
  },
{
    "time": 1.656 ,
    "amplitude": 4.86
  },
{
    "time": 1.658 ,
    "amplitude": 4.85
  },
{
    "time": 1.661 ,
    "amplitude": 4.845
  },
{
    "time": 1.664 ,
    "amplitude": 4.835
  },
{
    "time": 1.667 ,
    "amplitude": 4.855
  },
{
    "time": 1.669 ,
    "amplitude": 4.86
  },
{
    "time": 1.672 ,
    "amplitude": 4.85
  },
{
    "time": 1.675 ,
    "amplitude": 4.82
  },
{
    "time": 1.678 ,
    "amplitude": 4.815
  },
{
    "time": 1.681 ,
    "amplitude": 4.82
  },
{
    "time": 1.683 ,
    "amplitude": 4.81
  },
{
    "time": 1.686 ,
    "amplitude": 4.83
  },
{
    "time": 1.689 ,
    "amplitude": 4.85
  },
{
    "time": 1.692 ,
    "amplitude": 4.82
  },
{
    "time": 1.694 ,
    "amplitude": 4.8
  },
{
    "time": 1.697 ,
    "amplitude": 4.81
  },
{
    "time": 1.7 ,
    "amplitude": 4.815
  },
{
    "time": 1.703 ,
    "amplitude": 4.835
  },
{
    "time": 1.706 ,
    "amplitude": 4.835
  },
{
    "time": 1.708 ,
    "amplitude": 4.825
  },
{
    "time": 1.711 ,
    "amplitude": 4.805
  },
{
    "time": 1.714 ,
    "amplitude": 4.8
  },
{
    "time": 1.717 ,
    "amplitude": 4.8
  },
{
    "time": 1.719 ,
    "amplitude": 4.805
  },
{
    "time": 1.722 ,
    "amplitude": 4.8
  },
{
    "time": 1.725 ,
    "amplitude": 4.805
  },
{
    "time": 1.728 ,
    "amplitude": 4.78
  },
{
    "time": 1.731 ,
    "amplitude": 4.785
  },
{
    "time": 1.733 ,
    "amplitude": 4.805
  },
{
    "time": 1.736 ,
    "amplitude": 4.81
  },
{
    "time": 1.739 ,
    "amplitude": 4.8
  },
{
    "time": 1.742 ,
    "amplitude": 4.785
  },
{
    "time": 1.744 ,
    "amplitude": 4.78
  },
{
    "time": 1.747 ,
    "amplitude": 4.775
  },
{
    "time": 1.75 ,
    "amplitude": 4.79
  },
{
    "time": 1.753 ,
    "amplitude": 4.805
  },
{
    "time": 1.756 ,
    "amplitude": 4.8
  },
{
    "time": 1.758 ,
    "amplitude": 4.795
  },
{
    "time": 1.761 ,
    "amplitude": 4.78
  },
{
    "time": 1.764 ,
    "amplitude": 4.775
  },
{
    "time": 1.767 ,
    "amplitude": 4.78
  },
{
    "time": 1.769 ,
    "amplitude": 4.79
  },
{
    "time": 1.772 ,
    "amplitude": 4.79
  },
{
    "time": 1.775 ,
    "amplitude": 4.81
  },
{
    "time": 1.778 ,
    "amplitude": 4.805
  },
{
    "time": 1.781 ,
    "amplitude": 4.815
  },
{
    "time": 1.783 ,
    "amplitude": 4.81
  },
{
    "time": 1.786 ,
    "amplitude": 4.81
  },
{
    "time": 1.789 ,
    "amplitude": 4.815
  },
{
    "time": 1.792 ,
    "amplitude": 4.805
  },
{
    "time": 1.794 ,
    "amplitude": 4.8
  },
{
    "time": 1.797 ,
    "amplitude": 4.815
  },
{
    "time": 1.8 ,
    "amplitude": 4.82
  },
{
    "time": 1.803 ,
    "amplitude": 4.82
  },
{
    "time": 1.806 ,
    "amplitude": 4.815
  },
{
    "time": 1.808 ,
    "amplitude": 4.815
  },
{
    "time": 1.811 ,
    "amplitude": 4.8
  },
{
    "time": 1.814 ,
    "amplitude": 4.8
  },
{
    "time": 1.817 ,
    "amplitude": 4.81
  },
{
    "time": 1.819 ,
    "amplitude": 4.81
  },
{
    "time": 1.822 ,
    "amplitude": 4.815
  },
{
    "time": 1.825 ,
    "amplitude": 4.825
  },
{
    "time": 1.828 ,
    "amplitude": 4.825
  },
{
    "time": 1.831 ,
    "amplitude": 4.82
  },
{
    "time": 1.833 ,
    "amplitude": 4.825
  },
{
    "time": 1.836 ,
    "amplitude": 4.82
  },
{
    "time": 1.839 ,
    "amplitude": 4.825
  },
{
    "time": 1.842 ,
    "amplitude": 4.815
  },
{
    "time": 1.844 ,
    "amplitude": 4.815
  },
{
    "time": 1.847 ,
    "amplitude": 4.835
  },
{
    "time": 1.85 ,
    "amplitude": 4.845
  },
{
    "time": 1.853 ,
    "amplitude": 4.83
  },
{
    "time": 1.856 ,
    "amplitude": 4.835
  },
{
    "time": 1.858 ,
    "amplitude": 4.835
  },
{
    "time": 1.861 ,
    "amplitude": 4.805
  },
{
    "time": 1.864 ,
    "amplitude": 4.82
  },
{
    "time": 1.867 ,
    "amplitude": 4.83
  },
{
    "time": 1.869 ,
    "amplitude": 4.835
  },
{
    "time": 1.872 ,
    "amplitude": 4.825
  },
{
    "time": 1.875 ,
    "amplitude": 4.82
  },
{
    "time": 1.878 ,
    "amplitude": 4.83
  },
{
    "time": 1.881 ,
    "amplitude": 4.835
  },
{
    "time": 1.883 ,
    "amplitude": 4.855
  },
{
    "time": 1.886 ,
    "amplitude": 4.85
  },
{
    "time": 1.889 ,
    "amplitude": 4.84
  },
{
    "time": 1.892 ,
    "amplitude": 4.83
  },
{
    "time": 1.894 ,
    "amplitude": 4.825
  },
{
    "time": 1.897 ,
    "amplitude": 4.82
  },
{
    "time": 1.9 ,
    "amplitude": 4.835
  },
{
    "time": 1.903 ,
    "amplitude": 4.845
  },
{
    "time": 1.906 ,
    "amplitude": 4.85
  },
{
    "time": 1.908 ,
    "amplitude": 4.85
  },
{
    "time": 1.911 ,
    "amplitude": 4.835
  },
{
    "time": 1.914 ,
    "amplitude": 4.83
  },
{
    "time": 1.917 ,
    "amplitude": 4.84
  },
{
    "time": 1.919 ,
    "amplitude": 4.845
  },
{
    "time": 1.922 ,
    "amplitude": 4.845
  },
{
    "time": 1.925 ,
    "amplitude": 4.845
  },
{
    "time": 1.928 ,
    "amplitude": 4.845
  },
{
    "time": 1.931 ,
    "amplitude": 4.86
  },
{
    "time": 1.933 ,
    "amplitude": 4.895
  },
{
    "time": 1.936 ,
    "amplitude": 4.915
  },
{
    "time": 1.939 ,
    "amplitude": 4.92
  },
{
    "time": 1.942 ,
    "amplitude": 4.915
  },
{
    "time": 1.944 ,
    "amplitude": 4.905
  },
{
    "time": 1.947 ,
    "amplitude": 4.915
  },
{
    "time": 1.95 ,
    "amplitude": 4.92
  },
{
    "time": 1.953 ,
    "amplitude": 4.945
  },
{
    "time": 1.956 ,
    "amplitude": 4.97
  },
{
    "time": 1.958 ,
    "amplitude": 5
  },
{
    "time": 1.961 ,
    "amplitude": 5.005
  },
{
    "time": 1.964 ,
    "amplitude": 5.03
  },
{
    "time": 1.967 ,
    "amplitude": 5.035
  },
{
    "time": 1.969 ,
    "amplitude": 5.055
  },
{
    "time": 1.972 ,
    "amplitude": 5.055
  },
{
    "time": 1.975 ,
    "amplitude": 5.035
  },
{
    "time": 1.978 ,
    "amplitude": 5.04
  },
{
    "time": 1.981 ,
    "amplitude": 5.08
  },
{
    "time": 1.983 ,
    "amplitude": 5.125
  },
{
    "time": 1.986 ,
    "amplitude": 5.13
  },
{
    "time": 1.989 ,
    "amplitude": 5.125
  },
{
    "time": 1.992 ,
    "amplitude": 5.11
  },
{
    "time": 1.994 ,
    "amplitude": 5.08
  },
{
    "time": 1.997 ,
    "amplitude": 5.04
  },
{
    "time": 2 ,
    "amplitude": 5
  },
{
    "time": 2.003 ,
    "amplitude": 4.985
  },
{
    "time": 2.006 ,
    "amplitude": 4.945
  },
{
    "time": 2.008 ,
    "amplitude": 4.905
  },
{
    "time": 2.011 ,
    "amplitude": 4.855
  },
{
    "time": 2.014 ,
    "amplitude": 4.815
  },
{
    "time": 2.017 ,
    "amplitude": 4.805
  },
{
    "time": 2.019 ,
    "amplitude": 4.805
  },
{
    "time": 2.022 ,
    "amplitude": 4.805
  },
{
    "time": 2.025 ,
    "amplitude": 4.815
  },
{
    "time": 2.028 ,
    "amplitude": 4.8
  },
{
    "time": 2.031 ,
    "amplitude": 4.805
  },
{
    "time": 2.033 ,
    "amplitude": 4.815
  },
{
    "time": 2.036 ,
    "amplitude": 4.83
  },
{
    "time": 2.039 ,
    "amplitude": 4.815
  },
{
    "time": 2.042 ,
    "amplitude": 4.805
  },
{
    "time": 2.044 ,
    "amplitude": 4.795
  },
{
    "time": 2.047 ,
    "amplitude": 4.805
  },
{
    "time": 2.05 ,
    "amplitude": 4.805
  },
{
    "time": 2.053 ,
    "amplitude": 4.815
  },
{
    "time": 2.056 ,
    "amplitude": 4.81
  },
{
    "time": 2.058 ,
    "amplitude": 4.81
  },
{
    "time": 2.061 ,
    "amplitude": 4.805
  },
{
    "time": 2.064 ,
    "amplitude": 4.8
  },
{
    "time": 2.067 ,
    "amplitude": 4.805
  },
{
    "time": 2.069 ,
    "amplitude": 4.815
  },
{
    "time": 2.072 ,
    "amplitude": 4.835
  },
{
    "time": 2.075 ,
    "amplitude": 4.835
  },
{
    "time": 2.078 ,
    "amplitude": 4.81
  },
{
    "time": 2.081 ,
    "amplitude": 4.8
  },
{
    "time": 2.083 ,
    "amplitude": 4.8
  },
{
    "time": 2.086 ,
    "amplitude": 4.81
  },
{
    "time": 2.089 ,
    "amplitude": 4.775
  },
{
    "time": 2.092 ,
    "amplitude": 4.78
  },
{
    "time": 2.094 ,
    "amplitude": 4.77
  },
{
    "time": 2.097 ,
    "amplitude": 4.775
  },
{
    "time": 2.1 ,
    "amplitude": 4.775
  },
{
    "time": 2.103 ,
    "amplitude": 4.8
  },
{
    "time": 2.106 ,
    "amplitude": 4.805
  },
{
    "time": 2.108 ,
    "amplitude": 4.805
  },
{
    "time": 2.111 ,
    "amplitude": 4.775
  },
{
    "time": 2.114 ,
    "amplitude": 4.78
  },
{
    "time": 2.117 ,
    "amplitude": 4.8
  },
{
    "time": 2.119 ,
    "amplitude": 4.805
  },
{
    "time": 2.122 ,
    "amplitude": 4.795
  },
{
    "time": 2.125 ,
    "amplitude": 4.77
  },
{
    "time": 2.128 ,
    "amplitude": 4.78
  },
{
    "time": 2.131 ,
    "amplitude": 4.8
  },
{
    "time": 2.133 ,
    "amplitude": 4.835
  },
{
    "time": 2.136 ,
    "amplitude": 4.85
  },
{
    "time": 2.139 ,
    "amplitude": 4.855
  },
{
    "time": 2.142 ,
    "amplitude": 4.84
  },
{
    "time": 2.144 ,
    "amplitude": 4.77
  },
{
    "time": 2.147 ,
    "amplitude": 4.695
  },
{
    "time": 2.15 ,
    "amplitude": 4.655
  },
{
    "time": 2.153 ,
    "amplitude": 4.65
  },
{
    "time": 2.156 ,
    "amplitude": 4.63
  },
{
    "time": 2.158 ,
    "amplitude": 4.61
  },
{
    "time": 2.161 ,
    "amplitude": 4.59
  },
{
    "time": 2.164 ,
    "amplitude": 4.555
  },
{
    "time": 2.167 ,
    "amplitude": 4.515
  },
{
    "time": 2.169 ,
    "amplitude": 4.495
  },
{
    "time": 2.172 ,
    "amplitude": 4.465
  },
{
    "time": 2.175 ,
    "amplitude": 4.44
  },
{
    "time": 2.178 ,
    "amplitude": 4.415
  },
{
    "time": 2.181 ,
    "amplitude": 4.36
  },
{
    "time": 2.183 ,
    "amplitude": 4.3
  },
{
    "time": 2.186 ,
    "amplitude": 4.26
  },
{
    "time": 2.189 ,
    "amplitude": 4.22
  },
{
    "time": 2.192 ,
    "amplitude": 4.205
  },
{
    "time": 2.194 ,
    "amplitude": 4.195
  },
{
    "time": 2.197 ,
    "amplitude": 4.225
  },
{
    "time": 2.2 ,
    "amplitude": 4.28
  },
{
    "time": 2.203 ,
    "amplitude": 4.305
  },
{
    "time": 2.206 ,
    "amplitude": 4.33
  },
{
    "time": 2.208 ,
    "amplitude": 4.375
  },
{
    "time": 2.211 ,
    "amplitude": 4.45
  },
{
    "time": 2.214 ,
    "amplitude": 4.54
  },
{
    "time": 2.217 ,
    "amplitude": 4.605
  },
{
    "time": 2.219 ,
    "amplitude": 4.645
  },
{
    "time": 2.222 ,
    "amplitude": 4.66
  },
{
    "time": 2.225 ,
    "amplitude": 4.695
  },
{
    "time": 2.228 ,
    "amplitude": 4.725
  },
{
    "time": 2.231 ,
    "amplitude": 4.775
  },
{
    "time": 2.233 ,
    "amplitude": 4.805
  },
{
    "time": 2.236 ,
    "amplitude": 4.825
  },
{
    "time": 2.239 ,
    "amplitude": 4.83
  },
{
    "time": 2.242 ,
    "amplitude": 4.84
  },
{
    "time": 2.244 ,
    "amplitude": 4.84
  },
{
    "time": 2.247 ,
    "amplitude": 4.835
  },
{
    "time": 2.25 ,
    "amplitude": 4.85
  },
{
    "time": 2.253 ,
    "amplitude": 4.86
  },
{
    "time": 2.256 ,
    "amplitude": 4.865
  },
{
    "time": 2.258 ,
    "amplitude": 4.855
  },
{
    "time": 2.261 ,
    "amplitude": 4.855
  },
{
    "time": 2.264 ,
    "amplitude": 4.855
  },
{
    "time": 2.267 ,
    "amplitude": 4.855
  },
{
    "time": 2.269 ,
    "amplitude": 4.855
  },
{
    "time": 2.272 ,
    "amplitude": 4.86
  },
{
    "time": 2.275 ,
    "amplitude": 4.85
  },
{
    "time": 2.278 ,
    "amplitude": 4.835
  },
{
    "time": 2.281 ,
    "amplitude": 4.86
  },
{
    "time": 2.283 ,
    "amplitude": 4.905
  },
{
    "time": 2.286 ,
    "amplitude": 4.93
  },
{
    "time": 2.289 ,
    "amplitude": 4.91
  },
{
    "time": 2.292 ,
    "amplitude": 4.89
  },
{
    "time": 2.294 ,
    "amplitude": 4.865
  },
{
    "time": 2.297 ,
    "amplitude": 4.865
  },
{
    "time": 2.3 ,
    "amplitude": 4.89
  },
{
    "time": 2.303 ,
    "amplitude": 4.885
  },
{
    "time": 2.306 ,
    "amplitude": 4.885
  },
{
    "time": 2.308 ,
    "amplitude": 4.875
  },
{
    "time": 2.311 ,
    "amplitude": 4.89
  },
{
    "time": 2.314 ,
    "amplitude": 4.905
  },
{
    "time": 2.317 ,
    "amplitude": 4.9
  },
{
    "time": 2.319 ,
    "amplitude": 4.9
  },
{
    "time": 2.322 ,
    "amplitude": 4.9
  },
{
    "time": 2.325 ,
    "amplitude": 4.895
  },
{
    "time": 2.328 ,
    "amplitude": 4.89
  },
{
    "time": 2.331 ,
    "amplitude": 4.895
  },
{
    "time": 2.333 ,
    "amplitude": 4.915
  },
{
    "time": 2.336 ,
    "amplitude": 4.93
  },
{
    "time": 2.339 ,
    "amplitude": 4.92
  },
{
    "time": 2.342 ,
    "amplitude": 4.905
  },
{
    "time": 2.344 ,
    "amplitude": 4.89
  },
{
    "time": 2.347 ,
    "amplitude": 4.9
  },
{
    "time": 2.35 ,
    "amplitude": 4.935
  },
{
    "time": 2.353 ,
    "amplitude": 4.95
  },
{
    "time": 2.356 ,
    "amplitude": 4.96
  },
{
    "time": 2.358 ,
    "amplitude": 4.94
  },
{
    "time": 2.361 ,
    "amplitude": 4.92
  },
{
    "time": 2.364 ,
    "amplitude": 4.915
  },
{
    "time": 2.367 ,
    "amplitude": 4.945
  },
{
    "time": 2.369 ,
    "amplitude": 4.985
  },
{
    "time": 2.372 ,
    "amplitude": 5.01
  },
{
    "time": 2.375 ,
    "amplitude": 4.975
  },
{
    "time": 2.378 ,
    "amplitude": 4.945
  },
{
    "time": 2.381 ,
    "amplitude": 4.94
  },
{
    "time": 2.383 ,
    "amplitude": 4.965
  },
{
    "time": 2.386 ,
    "amplitude": 4.985
  },
{
    "time": 2.389 ,
    "amplitude": 4.995
  },
{
    "time": 2.392 ,
    "amplitude": 4.975
  },
{
    "time": 2.394 ,
    "amplitude": 4.97
  },
{
    "time": 2.397 ,
    "amplitude": 4.98
  },
{
    "time": 2.4 ,
    "amplitude": 4.975
  },
{
    "time": 2.403 ,
    "amplitude": 5
  },
{
    "time": 2.406 ,
    "amplitude": 5.025
  },
{
    "time": 2.408 ,
    "amplitude": 5.02
  },
{
    "time": 2.411 ,
    "amplitude": 5
  },
{
    "time": 2.414 ,
    "amplitude": 5.015
  },
{
    "time": 2.417 ,
    "amplitude": 5.01
  },
{
    "time": 2.419 ,
    "amplitude": 5.01
  },
{
    "time": 2.422 ,
    "amplitude": 5.005
  },
{
    "time": 2.425 ,
    "amplitude": 5.005
  },
{
    "time": 2.428 ,
    "amplitude": 4.995
  },
{
    "time": 2.431 ,
    "amplitude": 5.015
  },
{
    "time": 2.433 ,
    "amplitude": 5.025
  },
{
    "time": 2.436 ,
    "amplitude": 5.03
  },
{
    "time": 2.439 ,
    "amplitude": 5.035
  },
{
    "time": 2.442 ,
    "amplitude": 5.02
  },
{
    "time": 2.444 ,
    "amplitude": 4.99
  },
{
    "time": 2.447 ,
    "amplitude": 4.97
  },
{
    "time": 2.45 ,
    "amplitude": 4.98
  },
{
    "time": 2.453 ,
    "amplitude": 5.01
  },
{
    "time": 2.456 ,
    "amplitude": 5.05
  },
{
    "time": 2.458 ,
    "amplitude": 5.055
  },
{
    "time": 2.461 ,
    "amplitude": 5.015
  },
{
    "time": 2.464 ,
    "amplitude": 4.985
  },
{
    "time": 2.467 ,
    "amplitude": 4.98
  },
{
    "time": 2.469 ,
    "amplitude": 5.01
  },
{
    "time": 2.472 ,
    "amplitude": 5.03
  },
{
    "time": 2.475 ,
    "amplitude": 5.015
  },
{
    "time": 2.478 ,
    "amplitude": 4.995
  },
{
    "time": 2.481 ,
    "amplitude": 4.99
  },
{
    "time": 2.483 ,
    "amplitude": 4.975
  },
{
    "time": 2.486 ,
    "amplitude": 4.99
  },
{
    "time": 2.489 ,
    "amplitude": 4.97
  },
{
    "time": 2.492 ,
    "amplitude": 4.94
  },
{
    "time": 2.494 ,
    "amplitude": 4.935
  },
{
    "time": 2.497 ,
    "amplitude": 4.93
  },
{
    "time": 2.5 ,
    "amplitude": 4.935
  },
{
    "time": 2.503 ,
    "amplitude": 4.95
  },
{
    "time": 2.506 ,
    "amplitude": 4.945
  },
{
    "time": 2.508 ,
    "amplitude": 4.92
  },
{
    "time": 2.511 ,
    "amplitude": 4.91
  },
{
    "time": 2.514 ,
    "amplitude": 4.905
  },
{
    "time": 2.517 ,
    "amplitude": 4.91
  },
{
    "time": 2.519 ,
    "amplitude": 4.91
  },
{
    "time": 2.522 ,
    "amplitude": 4.895
  },
{
    "time": 2.525 ,
    "amplitude": 4.885
  },
{
    "time": 2.528 ,
    "amplitude": 4.875
  },
{
    "time": 2.531 ,
    "amplitude": 4.87
  },
{
    "time": 2.533 ,
    "amplitude": 4.89
  },
{
    "time": 2.536 ,
    "amplitude": 4.9
  },
{
    "time": 2.539 ,
    "amplitude": 4.895
  },
{
    "time": 2.542 ,
    "amplitude": 4.885
  },
{
    "time": 2.544 ,
    "amplitude": 4.855
  },
{
    "time": 2.547 ,
    "amplitude": 4.865
  },
{
    "time": 2.55 ,
    "amplitude": 4.87
  },
{
    "time": 2.553 ,
    "amplitude": 4.88
  },
{
    "time": 2.556 ,
    "amplitude": 4.88
  },
{
    "time": 2.558 ,
    "amplitude": 4.865
  },
{
    "time": 2.561 ,
    "amplitude": 4.85
  },
{
    "time": 2.564 ,
    "amplitude": 4.845
  },
{
    "time": 2.567 ,
    "amplitude": 4.855
  },
{
    "time": 2.569 ,
    "amplitude": 4.87
  },
{
    "time": 2.572 ,
    "amplitude": 4.855
  },
{
    "time": 2.575 ,
    "amplitude": 4.85
  },
{
    "time": 2.578 ,
    "amplitude": 4.82
  },
{
    "time": 2.581 ,
    "amplitude": 4.845
  },
{
    "time": 2.583 ,
    "amplitude": 4.855
  },
{
    "time": 2.586 ,
    "amplitude": 4.855
  },
{
    "time": 2.589 ,
    "amplitude": 4.86
  },
{
    "time": 2.592 ,
    "amplitude": 4.85
  },
{
    "time": 2.594 ,
    "amplitude": 4.825
  },
{
    "time": 2.597 ,
    "amplitude": 4.825
  },
{
    "time": 2.6 ,
    "amplitude": 4.835
  },
{
    "time": 2.603 ,
    "amplitude": 4.845
  },
{
    "time": 2.606 ,
    "amplitude": 4.845
  },
{
    "time": 2.608 ,
    "amplitude": 4.825
  },
{
    "time": 2.611 ,
    "amplitude": 4.81
  },
{
    "time": 2.614 ,
    "amplitude": 4.795
  },
{
    "time": 2.617 ,
    "amplitude": 4.81
  },
{
    "time": 2.619 ,
    "amplitude": 4.83
  },
{
    "time": 2.622 ,
    "amplitude": 4.83
  },
{
    "time": 2.625 ,
    "amplitude": 4.825
  },
{
    "time": 2.628 ,
    "amplitude": 4.815
  },
{
    "time": 2.631 ,
    "amplitude": 4.805
  },
{
    "time": 2.633 ,
    "amplitude": 4.81
  },
{
    "time": 2.636 ,
    "amplitude": 4.815
  },
{
    "time": 2.639 ,
    "amplitude": 4.83
  },
{
    "time": 2.642 ,
    "amplitude": 4.81
  },
{
    "time": 2.644 ,
    "amplitude": 4.785
  },
{
    "time": 2.647 ,
    "amplitude": 4.775
  },
{
    "time": 2.65 ,
    "amplitude": 4.775
  },
{
    "time": 2.653 ,
    "amplitude": 4.785
  },
{
    "time": 2.656 ,
    "amplitude": 4.79
  },
{
    "time": 2.658 ,
    "amplitude": 4.79
  },
{
    "time": 2.661 ,
    "amplitude": 4.78
  },
{
    "time": 2.664 ,
    "amplitude": 4.77
  },
{
    "time": 2.667 ,
    "amplitude": 4.775
  },
{
    "time": 2.669 ,
    "amplitude": 4.79
  },
{
    "time": 2.672 ,
    "amplitude": 4.79
  },
{
    "time": 2.675 ,
    "amplitude": 4.775
  },
{
    "time": 2.678 ,
    "amplitude": 4.745
  },
{
    "time": 2.681 ,
    "amplitude": 4.76
  },
{
    "time": 2.683 ,
    "amplitude": 4.77
  },
{
    "time": 2.686 ,
    "amplitude": 4.78
  },
{
    "time": 2.689 ,
    "amplitude": 4.775
  },
{
    "time": 2.692 ,
    "amplitude": 4.75
  },
{
    "time": 2.694 ,
    "amplitude": 4.75
  },
{
    "time": 2.697 ,
    "amplitude": 4.76
  },
{
    "time": 2.7 ,
    "amplitude": 4.755
  },
{
    "time": 2.703 ,
    "amplitude": 4.775
  },
{
    "time": 2.706 ,
    "amplitude": 4.765
  },
{
    "time": 2.708 ,
    "amplitude": 4.75
  },
{
    "time": 2.711 ,
    "amplitude": 4.75
  },
{
    "time": 2.714 ,
    "amplitude": 4.745
  },
{
    "time": 2.717 ,
    "amplitude": 4.765
  },
{
    "time": 2.719 ,
    "amplitude": 4.775
  },
{
    "time": 2.722 ,
    "amplitude": 4.78
  },
{
    "time": 2.725 ,
    "amplitude": 4.77
  },
{
    "time": 2.728 ,
    "amplitude": 4.755
  },
{
    "time": 2.731 ,
    "amplitude": 4.75
  },
{
    "time": 2.733 ,
    "amplitude": 4.755
  },
{
    "time": 2.736 ,
    "amplitude": 4.765
  },
{
    "time": 2.739 ,
    "amplitude": 4.755
  },
{
    "time": 2.742 ,
    "amplitude": 4.745
  },
{
    "time": 2.744 ,
    "amplitude": 4.75
  },
{
    "time": 2.747 ,
    "amplitude": 4.755
  },
{
    "time": 2.75 ,
    "amplitude": 4.78
  },
{
    "time": 2.753 ,
    "amplitude": 4.805
  },
{
    "time": 2.756 ,
    "amplitude": 4.785
  },
{
    "time": 2.758 ,
    "amplitude": 4.77
  },
{
    "time": 2.761 ,
    "amplitude": 4.755
  },
{
    "time": 2.764 ,
    "amplitude": 4.77
  },
{
    "time": 2.767 ,
    "amplitude": 4.77
  },
{
    "time": 2.769 ,
    "amplitude": 4.785
  },
{
    "time": 2.772 ,
    "amplitude": 4.78
  },
{
    "time": 2.775 ,
    "amplitude": 4.765
  },
{
    "time": 2.778 ,
    "amplitude": 4.77
  },
{
    "time": 2.781 ,
    "amplitude": 4.785
  },
{
    "time": 2.783 ,
    "amplitude": 4.78
  },
{
    "time": 2.786 ,
    "amplitude": 4.79
  },
{
    "time": 2.789 ,
    "amplitude": 4.77
  },
{
    "time": 2.792 ,
    "amplitude": 4.765
  },
{
    "time": 2.794 ,
    "amplitude": 4.77
  },
{
    "time": 2.797 ,
    "amplitude": 4.795
  },
{
    "time": 2.8 ,
    "amplitude": 4.805
  },
{
    "time": 2.803 ,
    "amplitude": 4.795
  },
{
    "time": 2.806 ,
    "amplitude": 4.78
  },
{
    "time": 2.808 ,
    "amplitude": 4.755
  },
{
    "time": 2.811 ,
    "amplitude": 4.76
  },
{
    "time": 2.814 ,
    "amplitude": 4.78
  },
{
    "time": 2.817 ,
    "amplitude": 4.795
  },
{
    "time": 2.819 ,
    "amplitude": 4.8
  },
{
    "time": 2.822 ,
    "amplitude": 4.79
  },
{
    "time": 2.825 ,
    "amplitude": 4.78
  },
{
    "time": 2.828 ,
    "amplitude": 4.765
  },
{
    "time": 2.831 ,
    "amplitude": 4.79
  },
{
    "time": 2.833 ,
    "amplitude": 4.8
  },
{
    "time": 2.836 ,
    "amplitude": 4.795
  },
{
    "time": 2.839 ,
    "amplitude": 4.785
  },
{
    "time": 2.842 ,
    "amplitude": 4.795
  },
{
    "time": 2.844 ,
    "amplitude": 4.79
  },
{
    "time": 2.847 ,
    "amplitude": 4.795
  },
{
    "time": 2.85 ,
    "amplitude": 4.8
  },
{
    "time": 2.853 ,
    "amplitude": 4.79
  },
{
    "time": 2.856 ,
    "amplitude": 4.78
  },
{
    "time": 2.858 ,
    "amplitude": 4.775
  },
{
    "time": 2.861 ,
    "amplitude": 4.795
  },
{
    "time": 2.864 ,
    "amplitude": 4.81
  },
{
    "time": 2.867 ,
    "amplitude": 4.81
  },
{
    "time": 2.869 ,
    "amplitude": 4.81
  },
{
    "time": 2.872 ,
    "amplitude": 4.81
  },
{
    "time": 2.875 ,
    "amplitude": 4.795
  },
{
    "time": 2.878 ,
    "amplitude": 4.8
  },
{
    "time": 2.881 ,
    "amplitude": 4.815
  },
{
    "time": 2.883 ,
    "amplitude": 4.82
  },
{
    "time": 2.886 ,
    "amplitude": 4.815
  },
{
    "time": 2.889 ,
    "amplitude": 4.785
  },
{
    "time": 2.892 ,
    "amplitude": 4.785
  },
{
    "time": 2.894 ,
    "amplitude": 4.785
  },
{
    "time": 2.897 ,
    "amplitude": 4.815
  },
{
    "time": 2.9 ,
    "amplitude": 4.83
  },
{
    "time": 2.903 ,
    "amplitude": 4.82
  },
{
    "time": 2.906 ,
    "amplitude": 4.805
  },
{
    "time": 2.908 ,
    "amplitude": 4.785
  },
{
    "time": 2.911 ,
    "amplitude": 4.8
  },
{
    "time": 2.914 ,
    "amplitude": 4.815
  },
{
    "time": 2.917 ,
    "amplitude": 4.83
  },
{
    "time": 2.919 ,
    "amplitude": 4.825
  },
{
    "time": 2.922 ,
    "amplitude": 4.82
  },
{
    "time": 2.925 ,
    "amplitude": 4.8
  },
{
    "time": 2.928 ,
    "amplitude": 4.815
  },
{
    "time": 2.931 ,
    "amplitude": 4.835
  },
{
    "time": 2.933 ,
    "amplitude": 4.84
  },
{
    "time": 2.936 ,
    "amplitude": 4.845
  },
{
    "time": 2.939 ,
    "amplitude": 4.855
  },
{
    "time": 2.942 ,
    "amplitude": 4.87
  },
{
    "time": 2.944 ,
    "amplitude": 4.89
  },
{
    "time": 2.947 ,
    "amplitude": 4.9
  },
{
    "time": 2.95 ,
    "amplitude": 4.91
  },
{
    "time": 2.953 ,
    "amplitude": 4.925
  },
{
    "time": 2.956 ,
    "amplitude": 4.93
  },
{
    "time": 2.958 ,
    "amplitude": 4.94
  },
{
    "time": 2.961 ,
    "amplitude": 4.955
  },
{
    "time": 2.964 ,
    "amplitude": 4.985
  },
{
    "time": 2.967 ,
    "amplitude": 5.01
  },
{
    "time": 2.969 ,
    "amplitude": 5.03
  },
{
    "time": 2.972 ,
    "amplitude": 5.025
  },
{
    "time": 2.975 ,
    "amplitude": 5.02
  },
{
    "time": 2.978 ,
    "amplitude": 5.01
  },
{
    "time": 2.981 ,
    "amplitude": 5.005
  },
{
    "time": 2.983 ,
    "amplitude": 5.03
  },
{
    "time": 2.986 ,
    "amplitude": 5.045
  },
{
    "time": 2.989 ,
    "amplitude": 5.045
  },
{
    "time": 2.992 ,
    "amplitude": 5.05
  },
{
    "time": 2.994 ,
    "amplitude": 5.065
  },
{
    "time": 2.997 ,
    "amplitude": 5.08
  },
{
    "time": 3 ,
    "amplitude": 5.055
  },
{
    "time": 3.003 ,
    "amplitude": 5.005
  },
{
    "time": 3.006 ,
    "amplitude": 4.955
  },
{
    "time": 3.008 ,
    "amplitude": 4.895
  },
{
    "time": 3.011 ,
    "amplitude": 4.875
  },
{
    "time": 3.014 ,
    "amplitude": 4.835
  },
{
    "time": 3.017 ,
    "amplitude": 4.815
  },
{
    "time": 3.019 ,
    "amplitude": 4.77
  },
{
    "time": 3.022 ,
    "amplitude": 4.755
  },
{
    "time": 3.025 ,
    "amplitude": 4.75
  },
{
    "time": 3.028 ,
    "amplitude": 4.765
  },
{
    "time": 3.031 ,
    "amplitude": 4.77
  },
{
    "time": 3.033 ,
    "amplitude": 4.775
  },
{
    "time": 3.036 ,
    "amplitude": 4.775
  },
{
    "time": 3.039 ,
    "amplitude": 4.76
  },
{
    "time": 3.042 ,
    "amplitude": 4.76
  },
{
    "time": 3.044 ,
    "amplitude": 4.77
  },
{
    "time": 3.047 ,
    "amplitude": 4.78
  },
{
    "time": 3.05 ,
    "amplitude": 4.785
  },
{
    "time": 3.053 ,
    "amplitude": 4.765
  },
{
    "time": 3.056 ,
    "amplitude": 4.755
  },
{
    "time": 3.058 ,
    "amplitude": 4.74
  },
{
    "time": 3.061 ,
    "amplitude": 4.75
  },
{
    "time": 3.064 ,
    "amplitude": 4.765
  },
{
    "time": 3.067 ,
    "amplitude": 4.79
  },
{
    "time": 3.069 ,
    "amplitude": 4.78
  },
{
    "time": 3.072 ,
    "amplitude": 4.77
  },
{
    "time": 3.075 ,
    "amplitude": 4.765
  },
{
    "time": 3.078 ,
    "amplitude": 4.765
  },
{
    "time": 3.081 ,
    "amplitude": 4.77
  },
{
    "time": 3.083 ,
    "amplitude": 4.78
  },
{
    "time": 3.086 ,
    "amplitude": 4.775
  },
{
    "time": 3.089 ,
    "amplitude": 4.765
  },
{
    "time": 3.092 ,
    "amplitude": 4.76
  },
{
    "time": 3.094 ,
    "amplitude": 4.77
  },
{
    "time": 3.097 ,
    "amplitude": 4.77
  },
{
    "time": 3.1 ,
    "amplitude": 4.79
  },
{
    "time": 3.103 ,
    "amplitude": 4.785
  },
{
    "time": 3.106 ,
    "amplitude": 4.765
  },
{
    "time": 3.108 ,
    "amplitude": 4.755
  },
{
    "time": 3.111 ,
    "amplitude": 4.765
  },
{
    "time": 3.114 ,
    "amplitude": 4.765
  },
{
    "time": 3.117 ,
    "amplitude": 4.77
  },
{
    "time": 3.119 ,
    "amplitude": 4.775
  },
{
    "time": 3.122 ,
    "amplitude": 4.78
  },
{
    "time": 3.125 ,
    "amplitude": 4.78
  },
{
    "time": 3.128 ,
    "amplitude": 4.77
  },
{
    "time": 3.131 ,
    "amplitude": 4.76
  },
{
    "time": 3.133 ,
    "amplitude": 4.75
  },
{
    "time": 3.136 ,
    "amplitude": 4.74
  },
{
    "time": 3.139 ,
    "amplitude": 4.775
  },
{
    "time": 3.142 ,
    "amplitude": 4.795
  },
{
    "time": 3.144 ,
    "amplitude": 4.84
  },
{
    "time": 3.147 ,
    "amplitude": 4.88
  },
{
    "time": 3.15 ,
    "amplitude": 4.9
  },
{
    "time": 3.153 ,
    "amplitude": 4.875
  },
{
    "time": 3.156 ,
    "amplitude": 4.8
  },
{
    "time": 3.158 ,
    "amplitude": 4.68
  },
{
    "time": 3.161 ,
    "amplitude": 4.605
  },
{
    "time": 3.164 ,
    "amplitude": 4.605
  },
{
    "time": 3.167 ,
    "amplitude": 4.61
  },
{
    "time": 3.169 ,
    "amplitude": 4.62
  },
{
    "time": 3.172 ,
    "amplitude": 4.615
  },
{
    "time": 3.175 ,
    "amplitude": 4.565
  },
{
    "time": 3.178 ,
    "amplitude": 4.52
  },
{
    "time": 3.181 ,
    "amplitude": 4.485
  },
{
    "time": 3.183 ,
    "amplitude": 4.47
  },
{
    "time": 3.186 ,
    "amplitude": 4.445
  },
{
    "time": 3.189 ,
    "amplitude": 4.415
  },
{
    "time": 3.192 ,
    "amplitude": 4.375
  },
{
    "time": 3.194 ,
    "amplitude": 4.335
  },
{
    "time": 3.197 ,
    "amplitude": 4.275
  },
{
    "time": 3.2 ,
    "amplitude": 4.25
  },
{
    "time": 3.203 ,
    "amplitude": 4.22
  },
{
    "time": 3.206 ,
    "amplitude": 4.185
  },
{
    "time": 3.208 ,
    "amplitude": 4.175
  },
{
    "time": 3.211 ,
    "amplitude": 4.21
  },
{
    "time": 3.214 ,
    "amplitude": 4.25
  },
{
    "time": 3.217 ,
    "amplitude": 4.275
  },
{
    "time": 3.219 ,
    "amplitude": 4.3
  },
{
    "time": 3.222 ,
    "amplitude": 4.355
  },
{
    "time": 3.225 ,
    "amplitude": 4.43
  },
{
    "time": 3.228 ,
    "amplitude": 4.51
  },
{
    "time": 3.231 ,
    "amplitude": 4.57
  },
{
    "time": 3.233 ,
    "amplitude": 4.605
  },
{
    "time": 3.236 ,
    "amplitude": 4.645
  },
{
    "time": 3.239 ,
    "amplitude": 4.68
  },
{
    "time": 3.242 ,
    "amplitude": 4.735
  },
{
    "time": 3.244 ,
    "amplitude": 4.75
  },
{
    "time": 3.247 ,
    "amplitude": 4.79
  },
{
    "time": 3.25 ,
    "amplitude": 4.815
  },
{
    "time": 3.253 ,
    "amplitude": 4.84
  },
{
    "time": 3.256 ,
    "amplitude": 4.84
  },
{
    "time": 3.258 ,
    "amplitude": 4.825
  },
{
    "time": 3.261 ,
    "amplitude": 4.815
  },
{
    "time": 3.264 ,
    "amplitude": 4.83
  },
{
    "time": 3.267 ,
    "amplitude": 4.84
  },
{
    "time": 3.269 ,
    "amplitude": 4.83
  },
{
    "time": 3.272 ,
    "amplitude": 4.83
  },
{
    "time": 3.275 ,
    "amplitude": 4.83
  },
{
    "time": 3.278 ,
    "amplitude": 4.835
  },
{
    "time": 3.281 ,
    "amplitude": 4.845
  },
{
    "time": 3.283 ,
    "amplitude": 4.85
  },
{
    "time": 3.286 ,
    "amplitude": 4.835
  },
{
    "time": 3.289 ,
    "amplitude": 4.84
  },
{
    "time": 3.292 ,
    "amplitude": 4.82
  },
{
    "time": 3.294 ,
    "amplitude": 4.82
  },
{
    "time": 3.297 ,
    "amplitude": 4.85
  },
{
    "time": 3.3 ,
    "amplitude": 4.865
  },
{
    "time": 3.303 ,
    "amplitude": 4.86
  },
{
    "time": 3.306 ,
    "amplitude": 4.86
  },
{
    "time": 3.308 ,
    "amplitude": 4.84
  },
{
    "time": 3.311 ,
    "amplitude": 4.85
  },
{
    "time": 3.314 ,
    "amplitude": 4.85
  },
{
    "time": 3.317 ,
    "amplitude": 4.865
  },
{
    "time": 3.319 ,
    "amplitude": 4.85
  },
{
    "time": 3.322 ,
    "amplitude": 4.86
  },
{
    "time": 3.325 ,
    "amplitude": 4.84
  },
{
    "time": 3.328 ,
    "amplitude": 4.845
  },
{
    "time": 3.331 ,
    "amplitude": 4.85
  },
{
    "time": 3.333 ,
    "amplitude": 4.87
  },
{
    "time": 3.336 ,
    "amplitude": 4.88
  },
{
    "time": 3.339 ,
    "amplitude": 4.885
  },
{
    "time": 3.342 ,
    "amplitude": 4.855
  },
{
    "time": 3.344 ,
    "amplitude": 4.855
  },
{
    "time": 3.347 ,
    "amplitude": 4.875
  },
{
    "time": 3.35 ,
    "amplitude": 4.875
  },
{
    "time": 3.353 ,
    "amplitude": 4.88
  },
{
    "time": 3.356 ,
    "amplitude": 4.88
  },
{
    "time": 3.358 ,
    "amplitude": 4.875
  },
{
    "time": 3.361 ,
    "amplitude": 4.885
  },
{
    "time": 3.364 ,
    "amplitude": 4.915
  },
{
    "time": 3.367 ,
    "amplitude": 4.935
  },
{
    "time": 3.369 ,
    "amplitude": 4.92
  },
{
    "time": 3.372 ,
    "amplitude": 4.915
  },
{
    "time": 3.375 ,
    "amplitude": 4.9
  },
{
    "time": 3.378 ,
    "amplitude": 4.905
  },
{
    "time": 3.381 ,
    "amplitude": 4.915
  },
{
    "time": 3.383 ,
    "amplitude": 4.92
  },
{
    "time": 3.386 ,
    "amplitude": 4.92
  },
{
    "time": 3.389 ,
    "amplitude": 4.925
  },
{
    "time": 3.392 ,
    "amplitude": 4.925
  },
{
    "time": 3.394 ,
    "amplitude": 4.935
  },
{
    "time": 3.397 ,
    "amplitude": 4.94
  },
{
    "time": 3.4 ,
    "amplitude": 4.94
  },
{
    "time": 3.403 ,
    "amplitude": 4.95
  },
{
    "time": 3.406 ,
    "amplitude": 4.95
  },
{
    "time": 3.408 ,
    "amplitude": 4.93
  },
{
    "time": 3.411 ,
    "amplitude": 4.925
  },
{
    "time": 3.414 ,
    "amplitude": 4.96
  },
{
    "time": 3.417 ,
    "amplitude": 4.97
  },
{
    "time": 3.419 ,
    "amplitude": 4.985
  },
{
    "time": 3.422 ,
    "amplitude": 4.96
  },
{
    "time": 3.425 ,
    "amplitude": 4.95
  },
{
    "time": 3.428 ,
    "amplitude": 4.96
  },
{
    "time": 3.431 ,
    "amplitude": 4.97
  },
{
    "time": 3.433 ,
    "amplitude": 4.99
  },
{
    "time": 3.436 ,
    "amplitude": 4.99
  },
{
    "time": 3.439 ,
    "amplitude": 4.97
  },
{
    "time": 3.442 ,
    "amplitude": 4.965
  },
{
    "time": 3.444 ,
    "amplitude": 4.96
  },
{
    "time": 3.447 ,
    "amplitude": 4.97
  },
{
    "time": 3.45 ,
    "amplitude": 4.96
  },
{
    "time": 3.453 ,
    "amplitude": 4.96
  },
{
    "time": 3.456 ,
    "amplitude": 4.97
  },
{
    "time": 3.458 ,
    "amplitude": 4.975
  },
{
    "time": 3.461 ,
    "amplitude": 4.97
  },
{
    "time": 3.464 ,
    "amplitude": 4.97
  },
{
    "time": 3.467 ,
    "amplitude": 4.98
  },
{
    "time": 3.469 ,
    "amplitude": 4.965
  },
{
    "time": 3.472 ,
    "amplitude": 4.97
  },
{
    "time": 3.475 ,
    "amplitude": 4.945
  },
{
    "time": 3.478 ,
    "amplitude": 4.94
  },
{
    "time": 3.481 ,
    "amplitude": 4.95
  },
{
    "time": 3.483 ,
    "amplitude": 4.945
  },
{
    "time": 3.486 ,
    "amplitude": 4.94
  },
{
    "time": 3.489 ,
    "amplitude": 4.92
  },
{
    "time": 3.492 ,
    "amplitude": 4.905
  },
{
    "time": 3.494 ,
    "amplitude": 4.905
  },
{
    "time": 3.497 ,
    "amplitude": 4.91
  },
{
    "time": 3.5 ,
    "amplitude": 4.92
  },
{
    "time": 3.503 ,
    "amplitude": 4.91
  },
{
    "time": 3.506 ,
    "amplitude": 4.905
  },
{
    "time": 3.508 ,
    "amplitude": 4.885
  },
{
    "time": 3.511 ,
    "amplitude": 4.875
  },
{
    "time": 3.514 ,
    "amplitude": 4.88
  },
{
    "time": 3.517 ,
    "amplitude": 4.87
  },
{
    "time": 3.519 ,
    "amplitude": 4.865
  },
{
    "time": 3.522 ,
    "amplitude": 4.87
  },
{
    "time": 3.525 ,
    "amplitude": 4.855
  },
{
    "time": 3.528 ,
    "amplitude": 4.86
  },
{
    "time": 3.531 ,
    "amplitude": 4.87
  },
{
    "time": 3.533 ,
    "amplitude": 4.865
  },
{
    "time": 3.536 ,
    "amplitude": 4.88
  },
{
    "time": 3.539 ,
    "amplitude": 4.88
  },
{
    "time": 3.542 ,
    "amplitude": 4.865
  },
{
    "time": 3.544 ,
    "amplitude": 4.855
  },
{
    "time": 3.547 ,
    "amplitude": 4.85
  },
{
    "time": 3.55 ,
    "amplitude": 4.865
  },
{
    "time": 3.553 ,
    "amplitude": 4.865
  },
{
    "time": 3.556 ,
    "amplitude": 4.87
  },
{
    "time": 3.558 ,
    "amplitude": 4.87
  },
{
    "time": 3.561 ,
    "amplitude": 4.865
  },
{
    "time": 3.564 ,
    "amplitude": 4.86
  },
{
    "time": 3.567 ,
    "amplitude": 4.875
  },
{
    "time": 3.569 ,
    "amplitude": 4.87
  },
{
    "time": 3.572 ,
    "amplitude": 4.87
  },
{
    "time": 3.575 ,
    "amplitude": 4.845
  },
{
    "time": 3.578 ,
    "amplitude": 4.855
  },
{
    "time": 3.581 ,
    "amplitude": 4.855
  },
{
    "time": 3.583 ,
    "amplitude": 4.87
  },
{
    "time": 3.586 ,
    "amplitude": 4.865
  },
{
    "time": 3.589 ,
    "amplitude": 4.85
  },
{
    "time": 3.592 ,
    "amplitude": 4.845
  },
{
    "time": 3.594 ,
    "amplitude": 4.85
  },
{
    "time": 3.597 ,
    "amplitude": 4.84
  },
{
    "time": 3.6 ,
    "amplitude": 4.855
  },
{
    "time": 3.603 ,
    "amplitude": 4.855
  },
{
    "time": 3.606 ,
    "amplitude": 4.84
  },
{
    "time": 3.608 ,
    "amplitude": 4.835
  },
{
    "time": 3.611 ,
    "amplitude": 4.83
  },
{
    "time": 3.614 ,
    "amplitude": 4.85
  },
{
    "time": 3.617 ,
    "amplitude": 4.86
  },
{
    "time": 3.619 ,
    "amplitude": 4.845
  },
{
    "time": 3.622 ,
    "amplitude": 4.82
  },
{
    "time": 3.625 ,
    "amplitude": 4.825
  },
{
    "time": 3.628 ,
    "amplitude": 4.845
  },
{
    "time": 3.631 ,
    "amplitude": 4.845
  },
{
    "time": 3.633 ,
    "amplitude": 4.845
  },
{
    "time": 3.636 ,
    "amplitude": 4.845
  },
{
    "time": 3.639 ,
    "amplitude": 4.83
  },
{
    "time": 3.642 ,
    "amplitude": 4.805
  },
{
    "time": 3.644 ,
    "amplitude": 4.815
  },
{
    "time": 3.647 ,
    "amplitude": 4.805
  },
{
    "time": 3.65 ,
    "amplitude": 4.83
  },
{
    "time": 3.653 ,
    "amplitude": 4.835
  },
{
    "time": 3.656 ,
    "amplitude": 4.815
  },
{
    "time": 3.658 ,
    "amplitude": 4.81
  },
{
    "time": 3.661 ,
    "amplitude": 4.8
  },
{
    "time": 3.664 ,
    "amplitude": 4.815
  },
{
    "time": 3.667 ,
    "amplitude": 4.805
  },
{
    "time": 3.669 ,
    "amplitude": 4.81
  },
{
    "time": 3.672 ,
    "amplitude": 4.775
  },
{
    "time": 3.675 ,
    "amplitude": 4.765
  },
{
    "time": 3.678 ,
    "amplitude": 4.77
  },
{
    "time": 3.681 ,
    "amplitude": 4.785
  },
{
    "time": 3.683 ,
    "amplitude": 4.805
  },
{
    "time": 3.686 ,
    "amplitude": 4.805
  },
{
    "time": 3.689 ,
    "amplitude": 4.77
  },
{
    "time": 3.692 ,
    "amplitude": 4.77
  },
{
    "time": 3.694 ,
    "amplitude": 4.785
  },
{
    "time": 3.697 ,
    "amplitude": 4.785
  },
{
    "time": 3.7 ,
    "amplitude": 4.795
  },
{
    "time": 3.703 ,
    "amplitude": 4.795
  },
{
    "time": 3.706 ,
    "amplitude": 4.78
  },
{
    "time": 3.708 ,
    "amplitude": 4.77
  },
{
    "time": 3.711 ,
    "amplitude": 4.765
  },
{
    "time": 3.714 ,
    "amplitude": 4.77
  },
{
    "time": 3.717 ,
    "amplitude": 4.785
  },
{
    "time": 3.719 ,
    "amplitude": 4.785
  },
{
    "time": 3.722 ,
    "amplitude": 4.78
  },
{
    "time": 3.725 ,
    "amplitude": 4.745
  },
{
    "time": 3.728 ,
    "amplitude": 4.75
  },
{
    "time": 3.731 ,
    "amplitude": 4.775
  },
{
    "time": 3.733 ,
    "amplitude": 4.81
  },
{
    "time": 3.736 ,
    "amplitude": 4.815
  },
{
    "time": 3.739 ,
    "amplitude": 4.8
  },
{
    "time": 3.742 ,
    "amplitude": 4.785
  },
{
    "time": 3.744 ,
    "amplitude": 4.79
  },
{
    "time": 3.747 ,
    "amplitude": 4.805
  },
{
    "time": 3.75 ,
    "amplitude": 4.82
  },
{
    "time": 3.753 ,
    "amplitude": 4.83
  },
{
    "time": 3.756 ,
    "amplitude": 4.815
  },
{
    "time": 3.758 ,
    "amplitude": 4.8
  },
{
    "time": 3.761 ,
    "amplitude": 4.81
  },
{
    "time": 3.764 ,
    "amplitude": 4.8
  },
{
    "time": 3.767 ,
    "amplitude": 4.81
  },
{
    "time": 3.769 ,
    "amplitude": 4.805
  },
{
    "time": 3.772 ,
    "amplitude": 4.79
  },
{
    "time": 3.775 ,
    "amplitude": 4.8
  },
{
    "time": 3.778 ,
    "amplitude": 4.8
  },
{
    "time": 3.781 ,
    "amplitude": 4.81
  },
{
    "time": 3.783 ,
    "amplitude": 4.83
  },
{
    "time": 3.786 ,
    "amplitude": 4.815
  },
{
    "time": 3.789 ,
    "amplitude": 4.82
  },
{
    "time": 3.792 ,
    "amplitude": 4.805
  },
{
    "time": 3.794 ,
    "amplitude": 4.805
  },
{
    "time": 3.797 ,
    "amplitude": 4.8
  },
{
    "time": 3.8 ,
    "amplitude": 4.81
  },
{
    "time": 3.803 ,
    "amplitude": 4.815
  },
{
    "time": 3.806 ,
    "amplitude": 4.815
  },
{
    "time": 3.808 ,
    "amplitude": 4.81
  },
{
    "time": 3.811 ,
    "amplitude": 4.825
  },
{
    "time": 3.814 ,
    "amplitude": 4.84
  },
{
    "time": 3.817 ,
    "amplitude": 4.84
  },
{
    "time": 3.819 ,
    "amplitude": 4.83
  },
{
    "time": 3.822 ,
    "amplitude": 4.805
  },
{
    "time": 3.825 ,
    "amplitude": 4.78
  },
{
    "time": 3.828 ,
    "amplitude": 4.78
  },
{
    "time": 3.831 ,
    "amplitude": 4.805
  },
{
    "time": 3.833 ,
    "amplitude": 4.85
  },
{
    "time": 3.836 ,
    "amplitude": 4.86
  },
{
    "time": 3.839 ,
    "amplitude": 4.85
  },
{
    "time": 3.842 ,
    "amplitude": 4.83
  },
{
    "time": 3.844 ,
    "amplitude": 4.835
  },
{
    "time": 3.847 ,
    "amplitude": 4.83
  },
{
    "time": 3.85 ,
    "amplitude": 4.84
  },
{
    "time": 3.853 ,
    "amplitude": 4.84
  },
{
    "time": 3.856 ,
    "amplitude": 4.82
  },
{
    "time": 3.858 ,
    "amplitude": 4.82
  },
{
    "time": 3.861 ,
    "amplitude": 4.81
  },
{
    "time": 3.864 ,
    "amplitude": 4.83
  },
{
    "time": 3.867 ,
    "amplitude": 4.84
  },
{
    "time": 3.869 ,
    "amplitude": 4.835
  },
{
    "time": 3.872 ,
    "amplitude": 4.83
  },
{
    "time": 3.875 ,
    "amplitude": 4.815
  },
{
    "time": 3.878 ,
    "amplitude": 4.81
  },
{
    "time": 3.881 ,
    "amplitude": 4.84
  },
{
    "time": 3.883 ,
    "amplitude": 4.86
  },
{
    "time": 3.886 ,
    "amplitude": 4.865
  },
{
    "time": 3.889 ,
    "amplitude": 4.88
  },
{
    "time": 3.892 ,
    "amplitude": 4.875
  },
{
    "time": 3.894 ,
    "amplitude": 4.885
  },
{
    "time": 3.897 ,
    "amplitude": 4.9
  },
{
    "time": 3.9 ,
    "amplitude": 4.905
  },
{
    "time": 3.903 ,
    "amplitude": 4.91
  },
{
    "time": 3.906 ,
    "amplitude": 4.92
  },
{
    "time": 3.908 ,
    "amplitude": 4.935
  },
{
    "time": 3.911 ,
    "amplitude": 4.95
  },
{
    "time": 3.914 ,
    "amplitude": 4.98
  },
{
    "time": 3.917 ,
    "amplitude": 4.995
  },
{
    "time": 3.919 ,
    "amplitude": 5.005
  },
{
    "time": 3.922 ,
    "amplitude": 5.015
  },
{
    "time": 3.925 ,
    "amplitude": 5.02
  },
{
    "time": 3.928 ,
    "amplitude": 5.04
  },
{
    "time": 3.931 ,
    "amplitude": 5.055
  },
{
    "time": 3.933 ,
    "amplitude": 5.065
  },
{
    "time": 3.936 ,
    "amplitude": 5.06
  },
{
    "time": 3.939 ,
    "amplitude": 5.06
  },
{
    "time": 3.942 ,
    "amplitude": 5.06
  },
{
    "time": 3.944 ,
    "amplitude": 5.055
  },
{
    "time": 3.947 ,
    "amplitude": 5.06
  },
{
    "time": 3.95 ,
    "amplitude": 5.065
  },
{
    "time": 3.953 ,
    "amplitude": 5.05
  },
{
    "time": 3.956 ,
    "amplitude": 5.03
  },
{
    "time": 3.958 ,
    "amplitude": 4.975
  },
{
    "time": 3.961 ,
    "amplitude": 4.93
  },
{
    "time": 3.964 ,
    "amplitude": 4.895
  },
{
    "time": 3.967 ,
    "amplitude": 4.85
  },
{
    "time": 3.969 ,
    "amplitude": 4.81
  },
{
    "time": 3.972 ,
    "amplitude": 4.775
  },
{
    "time": 3.975 ,
    "amplitude": 4.76
  },
{
    "time": 3.978 ,
    "amplitude": 4.76
  },
{
    "time": 3.981 ,
    "amplitude": 4.775
  },
{
    "time": 3.983 ,
    "amplitude": 4.8
  },
{
    "time": 3.986 ,
    "amplitude": 4.805
  },
{
    "time": 3.989 ,
    "amplitude": 4.795
  },
{
    "time": 3.992 ,
    "amplitude": 4.78
  },
{
    "time": 3.994 ,
    "amplitude": 4.775
  },
{
    "time": 3.997 ,
    "amplitude": 4.775
  },
{
    "time": 4 ,
    "amplitude": 4.78
  },
{
    "time": 4.003 ,
    "amplitude": 4.775
  },
{
    "time": 4.006 ,
    "amplitude": 4.75
  },
{
    "time": 4.008 ,
    "amplitude": 4.755
  },
{
    "time": 4.011 ,
    "amplitude": 4.775
  },
{
    "time": 4.014 ,
    "amplitude": 4.785
  },
{
    "time": 4.017 ,
    "amplitude": 4.805
  },
{
    "time": 4.019 ,
    "amplitude": 4.795
  },
{
    "time": 4.022 ,
    "amplitude": 4.775
  },
{
    "time": 4.025 ,
    "amplitude": 4.75
  },
{
    "time": 4.028 ,
    "amplitude": 4.76
  },
{
    "time": 4.031 ,
    "amplitude": 4.785
  },
{
    "time": 4.033 ,
    "amplitude": 4.78
  },
{
    "time": 4.036 ,
    "amplitude": 4.78
  },
{
    "time": 4.039 ,
    "amplitude": 4.785
  },
{
    "time": 4.042 ,
    "amplitude": 4.76
  },
{
    "time": 4.044 ,
    "amplitude": 4.76
  },
{
    "time": 4.047 ,
    "amplitude": 4.77
  },
{
    "time": 4.05 ,
    "amplitude": 4.79
  },
{
    "time": 4.053 ,
    "amplitude": 4.785
  },
{
    "time": 4.056 ,
    "amplitude": 4.795
  },
{
    "time": 4.058 ,
    "amplitude": 4.785
  },
{
    "time": 4.061 ,
    "amplitude": 4.78
  },
{
    "time": 4.064 ,
    "amplitude": 4.775
  },
{
    "time": 4.067 ,
    "amplitude": 4.795
  },
{
    "time": 4.069 ,
    "amplitude": 4.795
  },
{
    "time": 4.072 ,
    "amplitude": 4.78
  },
{
    "time": 4.075 ,
    "amplitude": 4.745
  },
{
    "time": 4.078 ,
    "amplitude": 4.73
  },
{
    "time": 4.081 ,
    "amplitude": 4.75
  },
{
    "time": 4.083 ,
    "amplitude": 4.79
  },
{
    "time": 4.086 ,
    "amplitude": 4.81
  },
{
    "time": 4.089 ,
    "amplitude": 4.82
  },
{
    "time": 4.092 ,
    "amplitude": 4.83
  },
{
    "time": 4.094 ,
    "amplitude": 4.825
  },
{
    "time": 4.097 ,
    "amplitude": 4.775
  },
{
    "time": 4.1 ,
    "amplitude": 4.675
  },
{
    "time": 4.103 ,
    "amplitude": 4.625
  },
{
    "time": 4.106 ,
    "amplitude": 4.595
  },
{
    "time": 4.108 ,
    "amplitude": 4.59
  },
{
    "time": 4.111 ,
    "amplitude": 4.605
  },
{
    "time": 4.114 ,
    "amplitude": 4.595
  },
{
    "time": 4.117 ,
    "amplitude": 4.58
  },
{
    "time": 4.119 ,
    "amplitude": 4.525
  },
{
    "time": 4.122 ,
    "amplitude": 4.48
  },
{
    "time": 4.125 ,
    "amplitude": 4.43
  },
{
    "time": 4.128 ,
    "amplitude": 4.41
  },
{
    "time": 4.131 ,
    "amplitude": 4.39
  },
{
    "time": 4.133 ,
    "amplitude": 4.36
  },
{
    "time": 4.136 ,
    "amplitude": 4.295
  },
{
    "time": 4.139 ,
    "amplitude": 4.245
  },
{
    "time": 4.142 ,
    "amplitude": 4.205
  },
{
    "time": 4.144 ,
    "amplitude": 4.2
  },
{
    "time": 4.147 ,
    "amplitude": 4.205
  },
{
    "time": 4.15 ,
    "amplitude": 4.24
  },
{
    "time": 4.153 ,
    "amplitude": 4.255
  },
{
    "time": 4.156 ,
    "amplitude": 4.27
  },
{
    "time": 4.158 ,
    "amplitude": 4.285
  },
{
    "time": 4.161 ,
    "amplitude": 4.35
  },
{
    "time": 4.164 ,
    "amplitude": 4.455
  },
{
    "time": 4.167 ,
    "amplitude": 4.535
  },
{
    "time": 4.169 ,
    "amplitude": 4.59
  },
{
    "time": 4.172 ,
    "amplitude": 4.635
  },
{
    "time": 4.175 ,
    "amplitude": 4.665
  },
{
    "time": 4.178 ,
    "amplitude": 4.715
  },
{
    "time": 4.181 ,
    "amplitude": 4.765
  },
{
    "time": 4.183 ,
    "amplitude": 4.795
  },
{
    "time": 4.186 ,
    "amplitude": 4.82
  },
{
    "time": 4.189 ,
    "amplitude": 4.825
  },
{
    "time": 4.192 ,
    "amplitude": 4.82
  },
{
    "time": 4.194 ,
    "amplitude": 4.82
  },
{
    "time": 4.197 ,
    "amplitude": 4.83
  },
{
    "time": 4.2 ,
    "amplitude": 4.845
  },
{
    "time": 4.203 ,
    "amplitude": 4.84
  },
{
    "time": 4.206 ,
    "amplitude": 4.835
  },
{
    "time": 4.208 ,
    "amplitude": 4.835
  },
{
    "time": 4.211 ,
    "amplitude": 4.855
  },
{
    "time": 4.214 ,
    "amplitude": 4.875
  },
{
    "time": 4.217 ,
    "amplitude": 4.875
  },
{
    "time": 4.219 ,
    "amplitude": 4.87
  },
{
    "time": 4.222 ,
    "amplitude": 4.84
  },
{
    "time": 4.225 ,
    "amplitude": 4.82
  },
{
    "time": 4.228 ,
    "amplitude": 4.845
  },
{
    "time": 4.231 ,
    "amplitude": 4.89
  },
{
    "time": 4.233 ,
    "amplitude": 4.905
  },
{
    "time": 4.236 ,
    "amplitude": 4.91
  },
{
    "time": 4.239 ,
    "amplitude": 4.9
  },
{
    "time": 4.242 ,
    "amplitude": 4.88
  },
{
    "time": 4.244 ,
    "amplitude": 4.87
  },
{
    "time": 4.247 ,
    "amplitude": 4.865
  },
{
    "time": 4.25 ,
    "amplitude": 4.875
  },
{
    "time": 4.253 ,
    "amplitude": 4.88
  },
{
    "time": 4.256 ,
    "amplitude": 4.87
  },
{
    "time": 4.258 ,
    "amplitude": 4.875
  },
{
    "time": 4.261 ,
    "amplitude": 4.875
  },
{
    "time": 4.264 ,
    "amplitude": 4.885
  },
{
    "time": 4.267 ,
    "amplitude": 4.89
  },
{
    "time": 4.269 ,
    "amplitude": 4.9
  },
{
    "time": 4.272 ,
    "amplitude": 4.895
  },
{
    "time": 4.275 ,
    "amplitude": 4.89
  },
{
    "time": 4.278 ,
    "amplitude": 4.915
  },
{
    "time": 4.281 ,
    "amplitude": 4.92
  },
{
    "time": 4.283 ,
    "amplitude": 4.93
  },
{
    "time": 4.286 ,
    "amplitude": 4.935
  },
{
    "time": 4.289 ,
    "amplitude": 4.94
  },
{
    "time": 4.292 ,
    "amplitude": 4.925
  },
{
    "time": 4.294 ,
    "amplitude": 4.91
  },
{
    "time": 4.297 ,
    "amplitude": 4.905
  },
{
    "time": 4.3 ,
    "amplitude": 4.93
  },
{
    "time": 4.303 ,
    "amplitude": 4.94
  },
{
    "time": 4.306 ,
    "amplitude": 4.945
  },
{
    "time": 4.308 ,
    "amplitude": 4.935
  },
{
    "time": 4.311 ,
    "amplitude": 4.925
  },
{
    "time": 4.314 ,
    "amplitude": 4.94
  },
{
    "time": 4.317 ,
    "amplitude": 4.96
  },
{
    "time": 4.319 ,
    "amplitude": 4.975
  },
{
    "time": 4.322 ,
    "amplitude": 4.96
  },
{
    "time": 4.325 ,
    "amplitude": 4.955
  },
{
    "time": 4.328 ,
    "amplitude": 4.975
  },
{
    "time": 4.331 ,
    "amplitude": 4.975
  },
{
    "time": 4.333 ,
    "amplitude": 4.99
  },
{
    "time": 4.336 ,
    "amplitude": 4.96
  },
{
    "time": 4.339 ,
    "amplitude": 4.95
  },
{
    "time": 4.342 ,
    "amplitude": 4.935
  },
{
    "time": 4.344 ,
    "amplitude": 4.96
  },
{
    "time": 4.347 ,
    "amplitude": 5.005
  },
{
    "time": 4.35 ,
    "amplitude": 5.02
  },
{
    "time": 4.353 ,
    "amplitude": 5.015
  },
{
    "time": 4.356 ,
    "amplitude": 4.995
  },
{
    "time": 4.358 ,
    "amplitude": 4.985
  },
{
    "time": 4.361 ,
    "amplitude": 5.015
  },
{
    "time": 4.364 ,
    "amplitude": 5.05
  },
{
    "time": 4.367 ,
    "amplitude": 5.075
  },
{
    "time": 4.369 ,
    "amplitude": 5.075
  },
{
    "time": 4.372 ,
    "amplitude": 5.02
  },
{
    "time": 4.375 ,
    "amplitude": 5.005
  },
{
    "time": 4.378 ,
    "amplitude": 5.015
  },
{
    "time": 4.381 ,
    "amplitude": 5.025
  },
{
    "time": 4.383 ,
    "amplitude": 5.05
  },
{
    "time": 4.386 ,
    "amplitude": 5.045
  },
{
    "time": 4.389 ,
    "amplitude": 5.03
  },
{
    "time": 4.392 ,
    "amplitude": 5.005
  },
{
    "time": 4.394 ,
    "amplitude": 4.99
  },
{
    "time": 4.397 ,
    "amplitude": 4.995
  },
{
    "time": 4.4 ,
    "amplitude": 5.025
  },
{
    "time": 4.403 ,
    "amplitude": 5.015
  },
{
    "time": 4.406 ,
    "amplitude": 4.975
  },
{
    "time": 4.408 ,
    "amplitude": 4.995
  },
{
    "time": 4.411 ,
    "amplitude": 5.02
  },
{
    "time": 4.414 ,
    "amplitude": 5.02
  },
{
    "time": 4.417 ,
    "amplitude": 5
  },
{
    "time": 4.419 ,
    "amplitude": 4.965
  },
{
    "time": 4.422 ,
    "amplitude": 4.955
  },
{
    "time": 4.425 ,
    "amplitude": 4.945
  },
{
    "time": 4.428 ,
    "amplitude": 4.935
  },
{
    "time": 4.431 ,
    "amplitude": 4.95
  },
{
    "time": 4.433 ,
    "amplitude": 4.95
  },
{
    "time": 4.436 ,
    "amplitude": 4.925
  },
{
    "time": 4.439 ,
    "amplitude": 4.885
  },
{
    "time": 4.442 ,
    "amplitude": 4.88
  },
{
    "time": 4.444 ,
    "amplitude": 4.92
  },
{
    "time": 4.447 ,
    "amplitude": 4.955
  },
{
    "time": 4.45 ,
    "amplitude": 4.97
  },
{
    "time": 4.453 ,
    "amplitude": 4.94
  },
{
    "time": 4.456 ,
    "amplitude": 4.915
  },
{
    "time": 4.458 ,
    "amplitude": 4.9
  },
{
    "time": 4.461 ,
    "amplitude": 4.935
  },
{
    "time": 4.464 ,
    "amplitude": 4.95
  },
{
    "time": 4.467 ,
    "amplitude": 4.96
  },
{
    "time": 4.469 ,
    "amplitude": 4.96
  },
{
    "time": 4.472 ,
    "amplitude": 4.93
  },
{
    "time": 4.475 ,
    "amplitude": 4.895
  },
{
    "time": 4.478 ,
    "amplitude": 4.9
  },
{
    "time": 4.481 ,
    "amplitude": 4.92
  },
{
    "time": 4.483 ,
    "amplitude": 4.925
  },
{
    "time": 4.486 ,
    "amplitude": 4.905
  },
{
    "time": 4.489 ,
    "amplitude": 4.93
  },
{
    "time": 4.492 ,
    "amplitude": 4.92
  },
{
    "time": 4.494 ,
    "amplitude": 4.91
  },
{
    "time": 4.497 ,
    "amplitude": 4.905
  },
{
    "time": 4.5 ,
    "amplitude": 4.91
  },
{
    "time": 4.503 ,
    "amplitude": 4.905
  },
{
    "time": 4.506 ,
    "amplitude": 4.9
  },
{
    "time": 4.508 ,
    "amplitude": 4.915
  },
{
    "time": 4.511 ,
    "amplitude": 4.925
  },
{
    "time": 4.514 ,
    "amplitude": 4.945
  },
{
    "time": 4.517 ,
    "amplitude": 4.97
  },
{
    "time": 4.519 ,
    "amplitude": 4.95
  },
{
    "time": 4.522 ,
    "amplitude": 4.92
  },
{
    "time": 4.525 ,
    "amplitude": 4.89
  },
{
    "time": 4.528 ,
    "amplitude": 4.885
  },
{
    "time": 4.531 ,
    "amplitude": 4.895
  },
{
    "time": 4.533 ,
    "amplitude": 4.91
  },
{
    "time": 4.536 ,
    "amplitude": 4.91
  },
{
    "time": 4.539 ,
    "amplitude": 4.905
  },
{
    "time": 4.542 ,
    "amplitude": 4.89
  },
{
    "time": 4.544 ,
    "amplitude": 4.895
  },
{
    "time": 4.547 ,
    "amplitude": 4.9
  },
{
    "time": 4.55 ,
    "amplitude": 4.895
  },
{
    "time": 4.553 ,
    "amplitude": 4.885
  },
{
    "time": 4.556 ,
    "amplitude": 4.88
  },
{
    "time": 4.558 ,
    "amplitude": 4.875
  },
{
    "time": 4.561 ,
    "amplitude": 4.88
  },
{
    "time": 4.564 ,
    "amplitude": 4.875
  },
{
    "time": 4.567 ,
    "amplitude": 4.87
  },
{
    "time": 4.569 ,
    "amplitude": 4.86
  },
{
    "time": 4.572 ,
    "amplitude": 4.845
  },
{
    "time": 4.575 ,
    "amplitude": 4.83
  },
{
    "time": 4.578 ,
    "amplitude": 4.85
  },
{
    "time": 4.581 ,
    "amplitude": 4.89
  },
{
    "time": 4.583 ,
    "amplitude": 4.87
  },
{
    "time": 4.586 ,
    "amplitude": 4.84
  },
{
    "time": 4.589 ,
    "amplitude": 4.815
  },
{
    "time": 4.592 ,
    "amplitude": 4.825
  },
{
    "time": 4.594 ,
    "amplitude": 4.81
  },
{
    "time": 4.597 ,
    "amplitude": 4.79
  },
{
    "time": 4.6 ,
    "amplitude": 4.77
  },
{
    "time": 4.603 ,
    "amplitude": 4.78
  },
{
    "time": 4.606 ,
    "amplitude": 4.775
  },
{
    "time": 4.608 ,
    "amplitude": 4.745
  },
{
    "time": 4.611 ,
    "amplitude": 4.71
  },
{
    "time": 4.614 ,
    "amplitude": 4.775
  },
{
    "time": 4.617 ,
    "amplitude": 4.86
  },
{
    "time": 4.619 ,
    "amplitude": 4.87
  },
{
    "time": 4.622 ,
    "amplitude": 4.82
  },
{
    "time": 4.625 ,
    "amplitude": 4.82
  },
{
    "time": 4.628 ,
    "amplitude": 4.845
  },
{
    "time": 4.631 ,
    "amplitude": 4.875
  },
{
    "time": 4.633 ,
    "amplitude": 4.89
  },
{
    "time": 4.636 ,
    "amplitude": 4.875
  },
{
    "time": 4.639 ,
    "amplitude": 4.84
  },
{
    "time": 4.642 ,
    "amplitude": 4.835
  },
{
    "time": 4.644 ,
    "amplitude": 4.885
  },
{
    "time": 4.647 ,
    "amplitude": 4.925
  },
{
    "time": 4.65 ,
    "amplitude": 4.92
  },
{
    "time": 4.653 ,
    "amplitude": 4.895
  },
{
    "time": 4.656 ,
    "amplitude": 4.88
  },
{
    "time": 4.658 ,
    "amplitude": 4.88
  },
{
    "time": 4.661 ,
    "amplitude": 4.89
  },
{
    "time": 4.664 ,
    "amplitude": 4.895
  },
{
    "time": 4.667 ,
    "amplitude": 4.89
  },
{
    "time": 4.669 ,
    "amplitude": 4.885
  },
{
    "time": 4.672 ,
    "amplitude": 4.875
  },
{
    "time": 4.675 ,
    "amplitude": 4.855
  },
{
    "time": 4.678 ,
    "amplitude": 4.87
  },
{
    "time": 4.681 ,
    "amplitude": 4.9
  },
{
    "time": 4.683 ,
    "amplitude": 4.895
  },
{
    "time": 4.686 ,
    "amplitude": 4.9
  },
{
    "time": 4.689 ,
    "amplitude": 4.88
  },
{
    "time": 4.692 ,
    "amplitude": 4.865
  },
{
    "time": 4.694 ,
    "amplitude": 4.86
  },
{
    "time": 4.697 ,
    "amplitude": 4.885
  },
{
    "time": 4.7 ,
    "amplitude": 4.895
  },
{
    "time": 4.703 ,
    "amplitude": 4.89
  },
{
    "time": 4.706 ,
    "amplitude": 4.875
  },
{
    "time": 4.708 ,
    "amplitude": 4.875
  },
{
    "time": 4.711 ,
    "amplitude": 4.875
  },
{
    "time": 4.714 ,
    "amplitude": 4.89
  },
{
    "time": 4.717 ,
    "amplitude": 4.89
  },
{
    "time": 4.719 ,
    "amplitude": 4.895
  },
{
    "time": 4.722 ,
    "amplitude": 4.875
  },
{
    "time": 4.725 ,
    "amplitude": 4.865
  },
{
    "time": 4.728 ,
    "amplitude": 4.87
  },
{
    "time": 4.731 ,
    "amplitude": 4.885
  },
{
    "time": 4.733 ,
    "amplitude": 4.91
  },
{
    "time": 4.736 ,
    "amplitude": 4.9
  },
{
    "time": 4.739 ,
    "amplitude": 4.865
  },
{
    "time": 4.742 ,
    "amplitude": 4.855
  },
{
    "time": 4.744 ,
    "amplitude": 4.855
  },
{
    "time": 4.747 ,
    "amplitude": 4.86
  },
{
    "time": 4.75 ,
    "amplitude": 4.89
  },
{
    "time": 4.753 ,
    "amplitude": 4.895
  },
{
    "time": 4.756 ,
    "amplitude": 4.895
  },
{
    "time": 4.758 ,
    "amplitude": 4.85
  },
{
    "time": 4.761 ,
    "amplitude": 4.865
  },
{
    "time": 4.764 ,
    "amplitude": 4.855
  },
{
    "time": 4.767 ,
    "amplitude": 4.86
  },
{
    "time": 4.769 ,
    "amplitude": 4.85
  },
{
    "time": 4.772 ,
    "amplitude": 4.87
  },
{
    "time": 4.775 ,
    "amplitude": 4.885
  },
{
    "time": 4.778 ,
    "amplitude": 4.895
  },
{
    "time": 4.781 ,
    "amplitude": 4.87
  },
{
    "time": 4.783 ,
    "amplitude": 4.835
  },
{
    "time": 4.786 ,
    "amplitude": 4.82
  },
{
    "time": 4.789 ,
    "amplitude": 4.85
  },
{
    "time": 4.792 ,
    "amplitude": 4.915
  },
{
    "time": 4.794 ,
    "amplitude": 5
  },
{
    "time": 4.797 ,
    "amplitude": 5.015
  },
{
    "time": 4.8 ,
    "amplitude": 4.975
  },
{
    "time": 4.803 ,
    "amplitude": 4.975
  },
{
    "time": 4.806 ,
    "amplitude": 4.98
  },
{
    "time": 4.808 ,
    "amplitude": 4.975
  },
{
    "time": 4.811 ,
    "amplitude": 4.97
  },
{
    "time": 4.814 ,
    "amplitude": 4.96
  },
{
    "time": 4.817 ,
    "amplitude": 4.975
  },
{
    "time": 4.819 ,
    "amplitude": 5.01
  },
{
    "time": 4.822 ,
    "amplitude": 5.03
  },
{
    "time": 4.825 ,
    "amplitude": 5.025
  },
{
    "time": 4.828 ,
    "amplitude": 5.04
  },
{
    "time": 4.831 ,
    "amplitude": 5.055
  },
{
    "time": 4.833 ,
    "amplitude": 5.075
  },
{
    "time": 4.836 ,
    "amplitude": 5.085
  },
{
    "time": 4.839 ,
    "amplitude": 5.075
  },
{
    "time": 4.842 ,
    "amplitude": 5.085
  },
{
    "time": 4.844 ,
    "amplitude": 5.105
  },
{
    "time": 4.847 ,
    "amplitude": 5.115
  },
{
    "time": 4.85 ,
    "amplitude": 5.12
  },
{
    "time": 4.853 ,
    "amplitude": 5.105
  },
{
    "time": 4.856 ,
    "amplitude": 5.12
  },
{
    "time": 4.858 ,
    "amplitude": 5.125
  },
{
    "time": 4.861 ,
    "amplitude": 5.13
  },
{
    "time": 4.864 ,
    "amplitude": 5.13
  },
{
    "time": 4.867 ,
    "amplitude": 5.125
  },
{
    "time": 4.869 ,
    "amplitude": 5.09
  },
{
    "time": 4.872 ,
    "amplitude": 5.04
  },
{
    "time": 4.875 ,
    "amplitude": 4.99
  },
{
    "time": 4.878 ,
    "amplitude": 4.955
  },
{
    "time": 4.881 ,
    "amplitude": 4.915
  },
{
    "time": 4.883 ,
    "amplitude": 4.87
  },
{
    "time": 4.886 ,
    "amplitude": 4.84
  },
{
    "time": 4.889 ,
    "amplitude": 4.835
  },
{
    "time": 4.892 ,
    "amplitude": 4.845
  },
{
    "time": 4.894 ,
    "amplitude": 4.88
  },
{
    "time": 4.897 ,
    "amplitude": 4.9
  },
{
    "time": 4.9 ,
    "amplitude": 4.875
  },
{
    "time": 4.903 ,
    "amplitude": 4.84
  },
{
    "time": 4.906 ,
    "amplitude": 4.805
  },
{
    "time": 4.908 ,
    "amplitude": 4.79
  },
{
    "time": 4.911 ,
    "amplitude": 4.82
  },
{
    "time": 4.914 ,
    "amplitude": 4.855
  },
{
    "time": 4.917 ,
    "amplitude": 4.87
  },
{
    "time": 4.919 ,
    "amplitude": 4.855
  },
{
    "time": 4.922 ,
    "amplitude": 4.81
  },
{
    "time": 4.925 ,
    "amplitude": 4.755
  },
{
    "time": 4.928 ,
    "amplitude": 4.73
  },
{
    "time": 4.931 ,
    "amplitude": 4.73
  },
{
    "time": 4.933 ,
    "amplitude": 4.76
  },
{
    "time": 4.936 ,
    "amplitude": 4.82
  },
{
    "time": 4.939 ,
    "amplitude": 4.865
  },
{
    "time": 4.942 ,
    "amplitude": 4.85
  },
{
    "time": 4.944 ,
    "amplitude": 4.825
  },
{
    "time": 4.947 ,
    "amplitude": 4.835
  },
{
    "time": 4.95 ,
    "amplitude": 4.815
  },
{
    "time": 4.953 ,
    "amplitude": 4.795
  },
{
    "time": 4.956 ,
    "amplitude": 4.84
  },
{
    "time": 4.958 ,
    "amplitude": 4.89
  },
{
    "time": 4.961 ,
    "amplitude": 4.915
  },
{
    "time": 4.964 ,
    "amplitude": 4.89
  },
{
    "time": 4.967 ,
    "amplitude": 4.865
  },
{
    "time": 4.969 ,
    "amplitude": 4.865
  },
{
    "time": 4.972 ,
    "amplitude": 4.85
  },
{
    "time": 4.975 ,
    "amplitude": 4.82
  },
{
    "time": 4.978 ,
    "amplitude": 4.81
  },
{
    "time": 4.981 ,
    "amplitude": 4.84
  },
{
    "time": 4.983 ,
    "amplitude": 4.855
  },
{
    "time": 4.986 ,
    "amplitude": 4.86
  },
{
    "time": 4.989 ,
    "amplitude": 4.82
  },
{
    "time": 4.992 ,
    "amplitude": 4.735
  },
{
    "time": 4.994 ,
    "amplitude": 4.69
  },
{
    "time": 4.997 ,
    "amplitude": 4.72
  },
{
    "time": 5 ,
    "amplitude": 4.76
  },
{
    "time": 5.003 ,
    "amplitude": 4.74
  },
{
    "time": 5.006 ,
    "amplitude": 4.72
  },
{
    "time": 5.008 ,
    "amplitude": 4.695
  },
{
    "time": 5.011 ,
    "amplitude": 4.655
  },
{
    "time": 5.014 ,
    "amplitude": 4.61
  },
{
    "time": 5.017 ,
    "amplitude": 4.56
  },
{
    "time": 5.019 ,
    "amplitude": 4.53
  },
{
    "time": 5.022 ,
    "amplitude": 4.545
  },
{
    "time": 5.025 ,
    "amplitude": 4.53
  },
{
    "time": 5.028 ,
    "amplitude": 4.51
  },
{
    "time": 5.031 ,
    "amplitude": 4.49
  },
{
    "time": 5.033 ,
    "amplitude": 4.445
  },
{
    "time": 5.036 ,
    "amplitude": 4.415
  },
{
    "time": 5.039 ,
    "amplitude": 4.39
  },
{
    "time": 5.042 ,
    "amplitude": 4.385
  },
{
    "time": 5.044 ,
    "amplitude": 4.37
  },
{
    "time": 5.047 ,
    "amplitude": 4.34
  },
{
    "time": 5.05 ,
    "amplitude": 4.28
  },
{
    "time": 5.053 ,
    "amplitude": 4.215
  },
{
    "time": 5.056 ,
    "amplitude": 4.175
  },
{
    "time": 5.058 ,
    "amplitude": 4.165
  },
{
    "time": 5.061 ,
    "amplitude": 4.22
  },
{
    "time": 5.064 ,
    "amplitude": 4.295
  },
{
    "time": 5.067 ,
    "amplitude": 4.36
  },
{
    "time": 5.069 ,
    "amplitude": 4.39
  },
{
    "time": 5.072 ,
    "amplitude": 4.42
  },
{
    "time": 5.075 ,
    "amplitude": 4.485
  },
{
    "time": 5.078 ,
    "amplitude": 4.555
  },
{
    "time": 5.081 ,
    "amplitude": 4.62
  },
{
    "time": 5.083 ,
    "amplitude": 4.67
  },
{
    "time": 5.086 ,
    "amplitude": 4.715
  },
{
    "time": 5.089 ,
    "amplitude": 4.805
  },
{
    "time": 5.092 ,
    "amplitude": 4.885
  },
{
    "time": 5.094 ,
    "amplitude": 4.905
  },
{
    "time": 5.097 ,
    "amplitude": 4.91
  },
{
    "time": 5.1 ,
    "amplitude": 4.925
  },
{
    "time": 5.103 ,
    "amplitude": 4.925
  },
{
    "time": 5.106 ,
    "amplitude": 4.925
  },
{
    "time": 5.108 ,
    "amplitude": 4.895
  },
{
    "time": 5.111 ,
    "amplitude": 4.905
  },
{
    "time": 5.114 ,
    "amplitude": 4.915
  },
{
    "time": 5.117 ,
    "amplitude": 4.945
  },
{
    "time": 5.119 ,
    "amplitude": 4.93
  },
{
    "time": 5.122 ,
    "amplitude": 4.905
  },
{
    "time": 5.125 ,
    "amplitude": 4.885
  },
{
    "time": 5.128 ,
    "amplitude": 4.89
  },
{
    "time": 5.131 ,
    "amplitude": 4.915
  },
{
    "time": 5.133 ,
    "amplitude": 4.93
  },
{
    "time": 5.136 ,
    "amplitude": 4.94
  },
{
    "time": 5.139 ,
    "amplitude": 4.955
  },
{
    "time": 5.142 ,
    "amplitude": 4.97
  },
{
    "time": 5.144 ,
    "amplitude": 4.97
  },
{
    "time": 5.147 ,
    "amplitude": 4.945
  },
{
    "time": 5.15 ,
    "amplitude": 4.905
  },
{
    "time": 5.153 ,
    "amplitude": 4.86
  },
{
    "time": 5.156 ,
    "amplitude": 4.885
  },
{
    "time": 5.158 ,
    "amplitude": 4.935
  },
{
    "time": 5.161 ,
    "amplitude": 5.005
  },
{
    "time": 5.164 ,
    "amplitude": 5.045
  },
{
    "time": 5.167 ,
    "amplitude": 5.055
  },
{
    "time": 5.169 ,
    "amplitude": 5.02
  },
{
    "time": 5.172 ,
    "amplitude": 4.995
  },
{
    "time": 5.175 ,
    "amplitude": 4.98
  },
{
    "time": 5.178 ,
    "amplitude": 4.955
  },
{
    "time": 5.181 ,
    "amplitude": 4.98
  },
{
    "time": 5.183 ,
    "amplitude": 4.975
  },
{
    "time": 5.186 ,
    "amplitude": 4.985
  },
{
    "time": 5.189 ,
    "amplitude": 4.99
  },
{
    "time": 5.192 ,
    "amplitude": 4.99
  },
{
    "time": 5.194 ,
    "amplitude": 4.995
  },
{
    "time": 5.197 ,
    "amplitude": 5
  },
{
    "time": 5.2 ,
    "amplitude": 5.01
  },
{
    "time": 5.203 ,
    "amplitude": 5.01
  },
{
    "time": 5.206 ,
    "amplitude": 5.01
  },
{
    "time": 5.208 ,
    "amplitude": 4.99
  },
{
    "time": 5.211 ,
    "amplitude": 5
  },
{
    "time": 5.214 ,
    "amplitude": 5.025
  },
{
    "time": 5.217 ,
    "amplitude": 5.05
  },
{
    "time": 5.219 ,
    "amplitude": 5.06
  },
{
    "time": 5.222 ,
    "amplitude": 5.06
  },
{
    "time": 5.225 ,
    "amplitude": 5.06
  },
{
    "time": 5.228 ,
    "amplitude": 5.045
  },
{
    "time": 5.231 ,
    "amplitude": 5.04
  },
{
    "time": 5.233 ,
    "amplitude": 5.045
  },
{
    "time": 5.236 ,
    "amplitude": 5.05
  },
{
    "time": 5.239 ,
    "amplitude": 5.055
  },
{
    "time": 5.242 ,
    "amplitude": 5.055
  },
{
    "time": 5.244 ,
    "amplitude": 5.055
  },
{
    "time": 5.247 ,
    "amplitude": 5.05
  },
{
    "time": 5.25 ,
    "amplitude": 5.05
  },
{
    "time": 5.253 ,
    "amplitude": 5.045
  },
{
    "time": 5.256 ,
    "amplitude": 5.085
  },
{
    "time": 5.258 ,
    "amplitude": 5.105
  },
{
    "time": 5.261 ,
    "amplitude": 5.09
  },
{
    "time": 5.264 ,
    "amplitude": 5.065
  },
{
    "time": 5.267 ,
    "amplitude": 5.075
  },
{
    "time": 5.269 ,
    "amplitude": 5.095
  },
{
    "time": 5.272 ,
    "amplitude": 5.105
  },
{
    "time": 5.275 ,
    "amplitude": 5.1
  },
{
    "time": 5.278 ,
    "amplitude": 5.115
  },
{
    "time": 5.281 ,
    "amplitude": 5.125
  },
{
    "time": 5.283 ,
    "amplitude": 5.11
  },
{
    "time": 5.286 ,
    "amplitude": 5.11
  },
{
    "time": 5.289 ,
    "amplitude": 5.11
  },
{
    "time": 5.292 ,
    "amplitude": 5.11
  },
{
    "time": 5.294 ,
    "amplitude": 5.105
  },
{
    "time": 5.297 ,
    "amplitude": 5.11
  },
{
    "time": 5.3 ,
    "amplitude": 5.11
  },
{
    "time": 5.303 ,
    "amplitude": 5.08
  },
{
    "time": 5.306 ,
    "amplitude": 5.055
  },
{
    "time": 5.308 ,
    "amplitude": 5.04
  },
{
    "time": 5.311 ,
    "amplitude": 5.03
  },
{
    "time": 5.314 ,
    "amplitude": 5.03
  },
{
    "time": 5.317 ,
    "amplitude": 5.065
  },
{
    "time": 5.319 ,
    "amplitude": 5.085
  },
{
    "time": 5.322 ,
    "amplitude": 5.08
  },
{
    "time": 5.325 ,
    "amplitude": 5.045
  },
{
    "time": 5.328 ,
    "amplitude": 5.02
  },
{
    "time": 5.331 ,
    "amplitude": 5.03
  },
{
    "time": 5.333 ,
    "amplitude": 5.045
  },
{
    "time": 5.336 ,
    "amplitude": 5.05
  },
{
    "time": 5.339 ,
    "amplitude": 5.035
  },
{
    "time": 5.342 ,
    "amplitude": 5.005
  },
{
    "time": 5.344 ,
    "amplitude": 4.99
  },
{
    "time": 5.347 ,
    "amplitude": 4.995
  },
{
    "time": 5.35 ,
    "amplitude": 4.995
  },
{
    "time": 5.353 ,
    "amplitude": 4.985
  },
{
    "time": 5.356 ,
    "amplitude": 4.96
  },
{
    "time": 5.358 ,
    "amplitude": 4.95
  },
{
    "time": 5.361 ,
    "amplitude": 4.96
  },
{
    "time": 5.364 ,
    "amplitude": 4.96
  },
{
    "time": 5.367 ,
    "amplitude": 4.955
  },
{
    "time": 5.369 ,
    "amplitude": 4.965
  },
{
    "time": 5.372 ,
    "amplitude": 4.95
  },
{
    "time": 5.375 ,
    "amplitude": 4.94
  },
{
    "time": 5.378 ,
    "amplitude": 4.94
  },
{
    "time": 5.381 ,
    "amplitude": 4.945
  },
{
    "time": 5.383 ,
    "amplitude": 4.94
  },
{
    "time": 5.386 ,
    "amplitude": 4.935
  },
{
    "time": 5.389 ,
    "amplitude": 4.925
  },
{
    "time": 5.392 ,
    "amplitude": 4.915
  },
{
    "time": 5.394 ,
    "amplitude": 4.91
  },
{
    "time": 5.397 ,
    "amplitude": 4.905
  },
{
    "time": 5.4 ,
    "amplitude": 4.915
  },
{
    "time": 5.403 ,
    "amplitude": 4.92
  },
{
    "time": 5.406 ,
    "amplitude": 4.91
  },
{
    "time": 5.408 ,
    "amplitude": 4.91
  },
{
    "time": 5.411 ,
    "amplitude": 4.905
  },
{
    "time": 5.414 ,
    "amplitude": 4.895
  },
{
    "time": 5.417 ,
    "amplitude": 4.895
  },
{
    "time": 5.419 ,
    "amplitude": 4.865
  },
{
    "time": 5.422 ,
    "amplitude": 4.87
  },
{
    "time": 5.425 ,
    "amplitude": 4.865
  },
{
    "time": 5.428 ,
    "amplitude": 4.875
  },
{
    "time": 5.431 ,
    "amplitude": 4.87
  },
{
    "time": 5.433 ,
    "amplitude": 4.87
  },
{
    "time": 5.436 ,
    "amplitude": 4.88
  },
{
    "time": 5.439 ,
    "amplitude": 4.905
  },
{
    "time": 5.442 ,
    "amplitude": 4.91
  },
{
    "time": 5.444 ,
    "amplitude": 4.9
  },
{
    "time": 5.447 ,
    "amplitude": 4.89
  },
{
    "time": 5.45 ,
    "amplitude": 4.895
  },
{
    "time": 5.453 ,
    "amplitude": 4.895
  },
{
    "time": 5.456 ,
    "amplitude": 4.875
  },
{
    "time": 5.458 ,
    "amplitude": 4.85
  },
{
    "time": 5.461 ,
    "amplitude": 4.86
  },
{
    "time": 5.464 ,
    "amplitude": 4.865
  },
{
    "time": 5.467 ,
    "amplitude": 4.875
  },
{
    "time": 5.469 ,
    "amplitude": 4.875
  },
{
    "time": 5.472 ,
    "amplitude": 4.855
  },
{
    "time": 5.475 ,
    "amplitude": 4.835
  },
{
    "time": 5.478 ,
    "amplitude": 4.835
  },
{
    "time": 5.481 ,
    "amplitude": 4.83
  },
{
    "time": 5.483 ,
    "amplitude": 4.835
  },
{
    "time": 5.486 ,
    "amplitude": 4.82
  },
{
    "time": 5.489 ,
    "amplitude": 4.81
  },
{
    "time": 5.492 ,
    "amplitude": 4.805
  },
{
    "time": 5.494 ,
    "amplitude": 4.805
  },
{
    "time": 5.497 ,
    "amplitude": 4.815
  },
{
    "time": 5.5 ,
    "amplitude": 4.815
  },
{
    "time": 5.503 ,
    "amplitude": 4.805
  },
{
    "time": 5.506 ,
    "amplitude": 4.78
  },
{
    "time": 5.508 ,
    "amplitude": 4.77
  },
{
    "time": 5.511 ,
    "amplitude": 4.77
  },
{
    "time": 5.514 ,
    "amplitude": 4.79
  },
{
    "time": 5.517 ,
    "amplitude": 4.795
  },
{
    "time": 5.519 ,
    "amplitude": 4.795
  },
{
    "time": 5.522 ,
    "amplitude": 4.785
  },
{
    "time": 5.525 ,
    "amplitude": 4.75
  },
{
    "time": 5.528 ,
    "amplitude": 4.75
  },
{
    "time": 5.531 ,
    "amplitude": 4.75
  },
{
    "time": 5.533 ,
    "amplitude": 4.775
  },
{
    "time": 5.536 ,
    "amplitude": 4.775
  },
{
    "time": 5.539 ,
    "amplitude": 4.77
  },
{
    "time": 5.542 ,
    "amplitude": 4.755
  },
{
    "time": 5.544 ,
    "amplitude": 4.745
  },
{
    "time": 5.547 ,
    "amplitude": 4.755
  },
{
    "time": 5.55 ,
    "amplitude": 4.765
  },
{
    "time": 5.553 ,
    "amplitude": 4.76
  },
{
    "time": 5.556 ,
    "amplitude": 4.76
  },
{
    "time": 5.558 ,
    "amplitude": 4.765
  },
{
    "time": 5.561 ,
    "amplitude": 4.775
  },
{
    "time": 5.564 ,
    "amplitude": 4.755
  },
{
    "time": 5.567 ,
    "amplitude": 4.715
  },
{
    "time": 5.569 ,
    "amplitude": 4.71
  },
{
    "time": 5.572 ,
    "amplitude": 4.755
  },
{
    "time": 5.575 ,
    "amplitude": 4.79
  },
{
    "time": 5.578 ,
    "amplitude": 4.8
  },
{
    "time": 5.581 ,
    "amplitude": 4.79
  },
{
    "time": 5.583 ,
    "amplitude": 4.76
  },
{
    "time": 5.586 ,
    "amplitude": 4.75
  },
{
    "time": 5.589 ,
    "amplitude": 4.75
  },
{
    "time": 5.592 ,
    "amplitude": 4.75
  },
{
    "time": 5.594 ,
    "amplitude": 4.75
  },
{
    "time": 5.597 ,
    "amplitude": 4.75
  },
{
    "time": 5.6 ,
    "amplitude": 4.755
  },
{
    "time": 5.603 ,
    "amplitude": 4.745
  },
{
    "time": 5.606 ,
    "amplitude": 4.75
  },
{
    "time": 5.608 ,
    "amplitude": 4.74
  },
{
    "time": 5.611 ,
    "amplitude": 4.76
  },
{
    "time": 5.614 ,
    "amplitude": 4.775
  },
{
    "time": 5.617 ,
    "amplitude": 4.78
  },
{
    "time": 5.619 ,
    "amplitude": 4.79
  },
{
    "time": 5.622 ,
    "amplitude": 4.785
  },
{
    "time": 5.625 ,
    "amplitude": 4.76
  },
{
    "time": 5.628 ,
    "amplitude": 4.75
  },
{
    "time": 5.631 ,
    "amplitude": 4.77
  },
{
    "time": 5.633 ,
    "amplitude": 4.78
  },
{
    "time": 5.636 ,
    "amplitude": 4.77
  },
{
    "time": 5.639 ,
    "amplitude": 4.75
  },
{
    "time": 5.642 ,
    "amplitude": 4.73
  },
{
    "time": 5.644 ,
    "amplitude": 4.735
  },
{
    "time": 5.647 ,
    "amplitude": 4.76
  },
{
    "time": 5.65 ,
    "amplitude": 4.77
  },
{
    "time": 5.653 ,
    "amplitude": 4.77
  },
{
    "time": 5.656 ,
    "amplitude": 4.77
  },
{
    "time": 5.658 ,
    "amplitude": 4.76
  },
{
    "time": 5.661 ,
    "amplitude": 4.765
  },
{
    "time": 5.664 ,
    "amplitude": 4.78
  },
{
    "time": 5.667 ,
    "amplitude": 4.765
  },
{
    "time": 5.669 ,
    "amplitude": 4.76
  },
{
    "time": 5.672 ,
    "amplitude": 4.745
  },
{
    "time": 5.675 ,
    "amplitude": 4.76
  },
{
    "time": 5.678 ,
    "amplitude": 4.765
  },
{
    "time": 5.681 ,
    "amplitude": 4.755
  },
{
    "time": 5.683 ,
    "amplitude": 4.745
  },
{
    "time": 5.686 ,
    "amplitude": 4.74
  },
{
    "time": 5.689 ,
    "amplitude": 4.75
  },
{
    "time": 5.692 ,
    "amplitude": 4.765
  },
{
    "time": 5.694 ,
    "amplitude": 4.77
  },
{
    "time": 5.697 ,
    "amplitude": 4.77
  },
{
    "time": 5.7 ,
    "amplitude": 4.76
  },
{
    "time": 5.703 ,
    "amplitude": 4.755
  },
{
    "time": 5.706 ,
    "amplitude": 4.745
  },
{
    "time": 5.708 ,
    "amplitude": 4.745
  },
{
    "time": 5.711 ,
    "amplitude": 4.765
  },
{
    "time": 5.714 ,
    "amplitude": 4.77
  },
{
    "time": 5.717 ,
    "amplitude": 4.775
  },
{
    "time": 5.719 ,
    "amplitude": 4.775
  },
{
    "time": 5.722 ,
    "amplitude": 4.755
  },
{
    "time": 5.725 ,
    "amplitude": 4.75
  },
{
    "time": 5.728 ,
    "amplitude": 4.78
  },
{
    "time": 5.731 ,
    "amplitude": 4.815
  },
{
    "time": 5.733 ,
    "amplitude": 4.82
  },
{
    "time": 5.736 ,
    "amplitude": 4.8
  },
{
    "time": 5.739 ,
    "amplitude": 4.78
  },
{
    "time": 5.742 ,
    "amplitude": 4.79
  },
{
    "time": 5.744 ,
    "amplitude": 4.83
  },
{
    "time": 5.747 ,
    "amplitude": 4.86
  },
{
    "time": 5.75 ,
    "amplitude": 4.86
  },
{
    "time": 5.753 ,
    "amplitude": 4.845
  },
{
    "time": 5.756 ,
    "amplitude": 4.835
  },
{
    "time": 5.758 ,
    "amplitude": 4.83
  },
{
    "time": 5.761 ,
    "amplitude": 4.825
  },
{
    "time": 5.764 ,
    "amplitude": 4.85
  },
{
    "time": 5.767 ,
    "amplitude": 4.88
  },
{
    "time": 5.769 ,
    "amplitude": 4.945
  },
{
    "time": 5.772 ,
    "amplitude": 4.97
  },
{
    "time": 5.775 ,
    "amplitude": 4.965
  },
{
    "time": 5.778 ,
    "amplitude": 4.965
  },
{
    "time": 5.781 ,
    "amplitude": 4.98
  },
{
    "time": 5.783 ,
    "amplitude": 5
  },
{
    "time": 5.786 ,
    "amplitude": 4.995
  },
{
    "time": 5.789 ,
    "amplitude": 4.985
  },
{
    "time": 5.792 ,
    "amplitude": 4.995
  },
{
    "time": 5.794 ,
    "amplitude": 4.995
  },
{
    "time": 5.797 ,
    "amplitude": 5.005
  },
{
    "time": 5.8 ,
    "amplitude": 5.02
  },
{
    "time": 5.803 ,
    "amplitude": 5.015
  },
{
    "time": 5.806 ,
    "amplitude": 4.985
  },
{
    "time": 5.808 ,
    "amplitude": 4.945
  },
{
    "time": 5.811 ,
    "amplitude": 4.92
  },
{
    "time": 5.814 ,
    "amplitude": 4.91
  },
{
    "time": 5.817 ,
    "amplitude": 4.885
  },
{
    "time": 5.819 ,
    "amplitude": 4.84
  },
{
    "time": 5.822 ,
    "amplitude": 4.78
  },
{
    "time": 5.825 ,
    "amplitude": 4.73
  },
{
    "time": 5.828 ,
    "amplitude": 4.71
  },
{
    "time": 5.831 ,
    "amplitude": 4.715
  },
{
    "time": 5.833 ,
    "amplitude": 4.735
  },
{
    "time": 5.836 ,
    "amplitude": 4.74
  },
{
    "time": 5.839 ,
    "amplitude": 4.735
  },
{
    "time": 5.842 ,
    "amplitude": 4.725
  },
{
    "time": 5.844 ,
    "amplitude": 4.74
  },
{
    "time": 5.847 ,
    "amplitude": 4.75
  },
{
    "time": 5.85 ,
    "amplitude": 4.755
  },
{
    "time": 5.853 ,
    "amplitude": 4.735
  },
{
    "time": 5.856 ,
    "amplitude": 4.725
  },
{
    "time": 5.858 ,
    "amplitude": 4.72
  },
{
    "time": 5.861 ,
    "amplitude": 4.75
  },
{
    "time": 5.864 ,
    "amplitude": 4.75
  },
{
    "time": 5.867 ,
    "amplitude": 4.75
  },
{
    "time": 5.869 ,
    "amplitude": 4.75
  },
{
    "time": 5.872 ,
    "amplitude": 4.745
  },
{
    "time": 5.875 ,
    "amplitude": 4.735
  },
{
    "time": 5.878 ,
    "amplitude": 4.72
  },
{
    "time": 5.881 ,
    "amplitude": 4.73
  },
{
    "time": 5.883 ,
    "amplitude": 4.76
  },
{
    "time": 5.886 ,
    "amplitude": 4.755
  },
{
    "time": 5.889 ,
    "amplitude": 4.74
  },
{
    "time": 5.892 ,
    "amplitude": 4.725
  },
{
    "time": 5.894 ,
    "amplitude": 4.715
  },
{
    "time": 5.897 ,
    "amplitude": 4.73
  },
{
    "time": 5.9 ,
    "amplitude": 4.755
  },
{
    "time": 5.903 ,
    "amplitude": 4.765
  },
{
    "time": 5.906 ,
    "amplitude": 4.76
  },
{
    "time": 5.908 ,
    "amplitude": 4.74
  },
{
    "time": 5.911 ,
    "amplitude": 4.73
  },
{
    "time": 5.914 ,
    "amplitude": 4.755
  },
{
    "time": 5.917 ,
    "amplitude": 4.775
  },
{
    "time": 5.919 ,
    "amplitude": 4.765
  },
{
    "time": 5.922 ,
    "amplitude": 4.73
  },
{
    "time": 5.925 ,
    "amplitude": 4.675
  },
{
    "time": 5.928 ,
    "amplitude": 4.675
  },
{
    "time": 5.931 ,
    "amplitude": 4.705
  },
{
    "time": 5.933 ,
    "amplitude": 4.735
  },
{
    "time": 5.936 ,
    "amplitude": 4.73
  },
{
    "time": 5.939 ,
    "amplitude": 4.725
  },
{
    "time": 5.942 ,
    "amplitude": 4.695
  },
{
    "time": 5.944 ,
    "amplitude": 4.655
  },
{
    "time": 5.947 ,
    "amplitude": 4.575
  },
{
    "time": 5.95 ,
    "amplitude": 4.51
  },
{
    "time": 5.953 ,
    "amplitude": 4.48
  },
{
    "time": 5.956 ,
    "amplitude": 4.48
  },
{
    "time": 5.958 ,
    "amplitude": 4.47
  },
{
    "time": 5.961 ,
    "amplitude": 4.465
  },
{
    "time": 5.964 ,
    "amplitude": 4.44
  },
{
    "time": 5.967 ,
    "amplitude": 4.4
  },
{
    "time": 5.969 ,
    "amplitude": 4.36
  },
{
    "time": 5.972 ,
    "amplitude": 4.3
  },
{
    "time": 5.975 ,
    "amplitude": 4.26
  },
{
    "time": 5.978 ,
    "amplitude": 4.28
  },
{
    "time": 5.981 ,
    "amplitude": 4.27
  },
{
    "time": 5.983 ,
    "amplitude": 4.22
  },
{
    "time": 5.986 ,
    "amplitude": 4.175
  },
{
    "time": 5.989 ,
    "amplitude": 4.135
  },
{
    "time": 5.992 ,
    "amplitude": 4.12
  },
{
    "time": 5.994 ,
    "amplitude": 4.16
  },
{
    "time": 5.997 ,
    "amplitude": 4.225
  },
{
    "time": 6 ,
    "amplitude": 4.265
  },
{
    "time": 6.003 ,
    "amplitude": 4.28
  },
{
    "time": 6.006 ,
    "amplitude": 4.315
  },
{
    "time": 6.008 ,
    "amplitude": 4.375
  },
{
    "time": 6.011 ,
    "amplitude": 4.455
  },
{
    "time": 6.014 ,
    "amplitude": 4.5
  },
{
    "time": 6.017 ,
    "amplitude": 4.555
  },
{
    "time": 6.019 ,
    "amplitude": 4.6
  },
{
    "time": 6.022 ,
    "amplitude": 4.675
  },
{
    "time": 6.025 ,
    "amplitude": 4.72
  },
{
    "time": 6.028 ,
    "amplitude": 4.765
  },
{
    "time": 6.031 ,
    "amplitude": 4.775
  },
{
    "time": 6.033 ,
    "amplitude": 4.785
  },
{
    "time": 6.036 ,
    "amplitude": 4.79
  },
{
    "time": 6.039 ,
    "amplitude": 4.785
  },
{
    "time": 6.042 ,
    "amplitude": 4.78
  },
{
    "time": 6.044 ,
    "amplitude": 4.805
  },
{
    "time": 6.047 ,
    "amplitude": 4.825
  },
{
    "time": 6.05 ,
    "amplitude": 4.835
  },
{
    "time": 6.053 ,
    "amplitude": 4.835
  },
{
    "time": 6.056 ,
    "amplitude": 4.81
  },
{
    "time": 6.058 ,
    "amplitude": 4.795
  },
{
    "time": 6.061 ,
    "amplitude": 4.805
  },
{
    "time": 6.064 ,
    "amplitude": 4.835
  },
{
    "time": 6.067 ,
    "amplitude": 4.845
  },
{
    "time": 6.069 ,
    "amplitude": 4.84
  },
{
    "time": 6.072 ,
    "amplitude": 4.82
  },
{
    "time": 6.075 ,
    "amplitude": 4.805
  },
{
    "time": 6.078 ,
    "amplitude": 4.82
  },
{
    "time": 6.081 ,
    "amplitude": 4.815
  },
{
    "time": 6.083 ,
    "amplitude": 4.835
  },
{
    "time": 6.086 ,
    "amplitude": 4.855
  },
{
    "time": 6.089 ,
    "amplitude": 4.845
  },
{
    "time": 6.092 ,
    "amplitude": 4.84
  },
{
    "time": 6.094 ,
    "amplitude": 4.84
  },
{
    "time": 6.097 ,
    "amplitude": 4.845
  },
{
    "time": 6.1 ,
    "amplitude": 4.84
  },
{
    "time": 6.103 ,
    "amplitude": 4.83
  },
{
    "time": 6.106 ,
    "amplitude": 4.82
  },
{
    "time": 6.108 ,
    "amplitude": 4.81
  },
{
    "time": 6.111 ,
    "amplitude": 4.835
  },
{
    "time": 6.114 ,
    "amplitude": 4.87
  },
{
    "time": 6.117 ,
    "amplitude": 4.9
  },
{
    "time": 6.119 ,
    "amplitude": 4.895
  },
{
    "time": 6.122 ,
    "amplitude": 4.875
  },
{
    "time": 6.125 ,
    "amplitude": 4.855
  },
{
    "time": 6.128 ,
    "amplitude": 4.87
  },
{
    "time": 6.131 ,
    "amplitude": 4.88
  },
{
    "time": 6.133 ,
    "amplitude": 4.895
  },
{
    "time": 6.136 ,
    "amplitude": 4.895
  },
{
    "time": 6.139 ,
    "amplitude": 4.905
  },
{
    "time": 6.142 ,
    "amplitude": 4.895
  },
{
    "time": 6.144 ,
    "amplitude": 4.9
  },
{
    "time": 6.147 ,
    "amplitude": 4.905
  },
{
    "time": 6.15 ,
    "amplitude": 4.92
  },
{
    "time": 6.153 ,
    "amplitude": 4.92
  },
{
    "time": 6.156 ,
    "amplitude": 4.92
  },
{
    "time": 6.158 ,
    "amplitude": 4.915
  },
{
    "time": 6.161 ,
    "amplitude": 4.915
  },
{
    "time": 6.164 ,
    "amplitude": 4.915
  },
{
    "time": 6.167 ,
    "amplitude": 4.93
  },
{
    "time": 6.169 ,
    "amplitude": 4.925
  },
{
    "time": 6.172 ,
    "amplitude": 4.93
  },
{
    "time": 6.175 ,
    "amplitude": 4.915
  },
{
    "time": 6.178 ,
    "amplitude": 4.93
  },
{
    "time": 6.181 ,
    "amplitude": 4.96
  },
{
    "time": 6.183 ,
    "amplitude": 4.985
  },
{
    "time": 6.186 ,
    "amplitude": 4.995
  },
{
    "time": 6.189 ,
    "amplitude": 4.975
  },
{
    "time": 6.192 ,
    "amplitude": 4.965
  },
{
    "time": 6.194 ,
    "amplitude": 4.98
  },
{
    "time": 6.197 ,
    "amplitude": 4.98
  },
{
    "time": 6.2 ,
    "amplitude": 4.99
  },
{
    "time": 6.203 ,
    "amplitude": 4.985
  },
{
    "time": 6.206 ,
    "amplitude": 4.97
  },
{
    "time": 6.208 ,
    "amplitude": 4.965
  },
{
    "time": 6.211 ,
    "amplitude": 4.97
  },
{
    "time": 6.214 ,
    "amplitude": 4.995
  },
{
    "time": 6.217 ,
    "amplitude": 5.02
  },
{
    "time": 6.219 ,
    "amplitude": 5.01
  },
{
    "time": 6.222 ,
    "amplitude": 5.01
  },
{
    "time": 6.225 ,
    "amplitude": 4.98
  },
{
    "time": 6.228 ,
    "amplitude": 4.99
  },
{
    "time": 6.231 ,
    "amplitude": 4.99
  },
{
    "time": 6.233 ,
    "amplitude": 5.01
  },
{
    "time": 6.236 ,
    "amplitude": 4.99
  },
{
    "time": 6.239 ,
    "amplitude": 5
  },
{
    "time": 6.242 ,
    "amplitude": 4.97
  },
{
    "time": 6.244 ,
    "amplitude": 4.975
  },
{
    "time": 6.247 ,
    "amplitude": 4.985
  },
{
    "time": 6.25 ,
    "amplitude": 4.985
  },
{
    "time": 6.253 ,
    "amplitude": 4.965
  },
{
    "time": 6.256 ,
    "amplitude": 4.945
  },
{
    "time": 6.258 ,
    "amplitude": 4.955
  },
{
    "time": 6.261 ,
    "amplitude": 4.98
  },
{
    "time": 6.264 ,
    "amplitude": 4.985
  },
{
    "time": 6.267 ,
    "amplitude": 4.97
  },
{
    "time": 6.269 ,
    "amplitude": 4.945
  },
{
    "time": 6.272 ,
    "amplitude": 4.92
  },
{
    "time": 6.275 ,
    "amplitude": 4.915
  },
{
    "time": 6.278 ,
    "amplitude": 4.92
  },
{
    "time": 6.281 ,
    "amplitude": 4.93
  },
{
    "time": 6.283 ,
    "amplitude": 4.93
  },
{
    "time": 6.286 ,
    "amplitude": 4.905
  },
{
    "time": 6.289 ,
    "amplitude": 4.905
  },
{
    "time": 6.292 ,
    "amplitude": 4.875
  },
{
    "time": 6.294 ,
    "amplitude": 4.885
  },
{
    "time": 6.297 ,
    "amplitude": 4.875
  },
{
    "time": 6.3 ,
    "amplitude": 4.875
  },
{
    "time": 6.303 ,
    "amplitude": 4.87
  },
{
    "time": 6.306 ,
    "amplitude": 4.865
  },
{
    "time": 6.308 ,
    "amplitude": 4.855
  },
{
    "time": 6.311 ,
    "amplitude": 4.87
  },
{
    "time": 6.314 ,
    "amplitude": 4.89
  },
{
    "time": 6.317 ,
    "amplitude": 4.89
  },
{
    "time": 6.319 ,
    "amplitude": 4.87
  },
{
    "time": 6.322 ,
    "amplitude": 4.86
  },
{
    "time": 6.325 ,
    "amplitude": 4.84
  },
{
    "time": 6.328 ,
    "amplitude": 4.86
  },
{
    "time": 6.331 ,
    "amplitude": 4.855
  },
{
    "time": 6.333 ,
    "amplitude": 4.855
  },
{
    "time": 6.336 ,
    "amplitude": 4.825
  },
{
    "time": 6.339 ,
    "amplitude": 4.805
  },
{
    "time": 6.342 ,
    "amplitude": 4.82
  },
{
    "time": 6.344 ,
    "amplitude": 4.865
  },
{
    "time": 6.347 ,
    "amplitude": 4.895
  },
{
    "time": 6.35 ,
    "amplitude": 4.89
  },
{
    "time": 6.353 ,
    "amplitude": 4.86
  },
{
    "time": 6.356 ,
    "amplitude": 4.835
  },
{
    "time": 6.358 ,
    "amplitude": 4.81
  },
{
    "time": 6.361 ,
    "amplitude": 4.815
  },
{
    "time": 6.364 ,
    "amplitude": 4.84
  },
{
    "time": 6.367 ,
    "amplitude": 4.86
  },
{
    "time": 6.369 ,
    "amplitude": 4.875
  },
{
    "time": 6.372 ,
    "amplitude": 4.87
  },
{
    "time": 6.375 ,
    "amplitude": 4.84
  },
{
    "time": 6.378 ,
    "amplitude": 4.84
  },
{
    "time": 6.381 ,
    "amplitude": 4.835
  },
{
    "time": 6.383 ,
    "amplitude": 4.845
  },
{
    "time": 6.386 ,
    "amplitude": 4.84
  },
{
    "time": 6.389 ,
    "amplitude": 4.84
  },
{
    "time": 6.392 ,
    "amplitude": 4.825
  },
{
    "time": 6.394 ,
    "amplitude": 4.815
  },
{
    "time": 6.397 ,
    "amplitude": 4.835
  },
{
    "time": 6.4 ,
    "amplitude": 4.845
  },
{
    "time": 6.403 ,
    "amplitude": 4.845
  },
{
    "time": 6.406 ,
    "amplitude": 4.825
  },
{
    "time": 6.408 ,
    "amplitude": 4.805
  },
{
    "time": 6.411 ,
    "amplitude": 4.81
  },
{
    "time": 6.414 ,
    "amplitude": 4.83
  },
{
    "time": 6.417 ,
    "amplitude": 4.845
  },
{
    "time": 6.419 ,
    "amplitude": 4.825
  },
{
    "time": 6.422 ,
    "amplitude": 4.81
  },
{
    "time": 6.425 ,
    "amplitude": 4.795
  },
{
    "time": 6.428 ,
    "amplitude": 4.815
  },
{
    "time": 6.431 ,
    "amplitude": 4.82
  },
{
    "time": 6.433 ,
    "amplitude": 4.84
  },
{
    "time": 6.436 ,
    "amplitude": 4.81
  },
{
    "time": 6.439 ,
    "amplitude": 4.8
  },
{
    "time": 6.442 ,
    "amplitude": 4.79
  },
{
    "time": 6.444 ,
    "amplitude": 4.815
  },
{
    "time": 6.447 ,
    "amplitude": 4.81
  },
{
    "time": 6.45 ,
    "amplitude": 4.815
  },
{
    "time": 6.453 ,
    "amplitude": 4.805
  },
{
    "time": 6.456 ,
    "amplitude": 4.775
  },
{
    "time": 6.458 ,
    "amplitude": 4.775
  },
{
    "time": 6.461 ,
    "amplitude": 4.78
  },
{
    "time": 6.464 ,
    "amplitude": 4.79
  },
{
    "time": 6.467 ,
    "amplitude": 4.8
  },
{
    "time": 6.469 ,
    "amplitude": 4.79
  },
{
    "time": 6.472 ,
    "amplitude": 4.775
  },
{
    "time": 6.475 ,
    "amplitude": 4.77
  },
{
    "time": 6.478 ,
    "amplitude": 4.77
  },
{
    "time": 6.481 ,
    "amplitude": 4.775
  },
{
    "time": 6.483 ,
    "amplitude": 4.775
  },
{
    "time": 6.486 ,
    "amplitude": 4.775
  },
{
    "time": 6.489 ,
    "amplitude": 4.75
  },
{
    "time": 6.492 ,
    "amplitude": 4.735
  },
{
    "time": 6.494 ,
    "amplitude": 4.745
  },
{
    "time": 6.497 ,
    "amplitude": 4.77
  },
{
    "time": 6.5 ,
    "amplitude": 4.785
  },
{
    "time": 6.503 ,
    "amplitude": 4.795
  },
{
    "time": 6.506 ,
    "amplitude": 4.775
  },
{
    "time": 6.508 ,
    "amplitude": 4.755
  },
{
    "time": 6.511 ,
    "amplitude": 4.74
  },
{
    "time": 6.514 ,
    "amplitude": 4.735
  },
{
    "time": 6.517 ,
    "amplitude": 4.745
  },
{
    "time": 6.519 ,
    "amplitude": 4.75
  },
{
    "time": 6.522 ,
    "amplitude": 4.755
  },
{
    "time": 6.525 ,
    "amplitude": 4.765
  },
{
    "time": 6.528 ,
    "amplitude": 4.77
  },
{
    "time": 6.531 ,
    "amplitude": 4.775
  },
{
    "time": 6.533 ,
    "amplitude": 4.79
  },
{
    "time": 6.536 ,
    "amplitude": 4.775
  },
{
    "time": 6.539 ,
    "amplitude": 4.76
  },
{
    "time": 6.542 ,
    "amplitude": 4.755
  },
{
    "time": 6.544 ,
    "amplitude": 4.77
  },
{
    "time": 6.547 ,
    "amplitude": 4.77
  },
{
    "time": 6.55 ,
    "amplitude": 4.77
  },
{
    "time": 6.553 ,
    "amplitude": 4.755
  },
{
    "time": 6.556 ,
    "amplitude": 4.745
  },
{
    "time": 6.558 ,
    "amplitude": 4.735
  },
{
    "time": 6.561 ,
    "amplitude": 4.745
  },
{
    "time": 6.564 ,
    "amplitude": 4.77
  },
{
    "time": 6.567 ,
    "amplitude": 4.795
  },
{
    "time": 6.569 ,
    "amplitude": 4.8
  },
{
    "time": 6.572 ,
    "amplitude": 4.795
  },
{
    "time": 6.575 ,
    "amplitude": 4.78
  },
{
    "time": 6.578 ,
    "amplitude": 4.78
  },
{
    "time": 6.581 ,
    "amplitude": 4.785
  },
{
    "time": 6.583 ,
    "amplitude": 4.79
  },
{
    "time": 6.586 ,
    "amplitude": 4.79
  },
{
    "time": 6.589 ,
    "amplitude": 4.805
  },
{
    "time": 6.592 ,
    "amplitude": 4.79
  },
{
    "time": 6.594 ,
    "amplitude": 4.79
  },
{
    "time": 6.597 ,
    "amplitude": 4.795
  },
{
    "time": 6.6 ,
    "amplitude": 4.8
  },
{
    "time": 6.603 ,
    "amplitude": 4.8
  },
{
    "time": 6.606 ,
    "amplitude": 4.79
  },
{
    "time": 6.608 ,
    "amplitude": 4.785
  },
{
    "time": 6.611 ,
    "amplitude": 4.8
  },
{
    "time": 6.614 ,
    "amplitude": 4.795
  },
{
    "time": 6.617 ,
    "amplitude": 4.82
  },
{
    "time": 6.619 ,
    "amplitude": 4.81
  },
{
    "time": 6.622 ,
    "amplitude": 4.805
  },
{
    "time": 6.625 ,
    "amplitude": 4.795
  },
{
    "time": 6.628 ,
    "amplitude": 4.8
  },
{
    "time": 6.631 ,
    "amplitude": 4.81
  },
{
    "time": 6.633 ,
    "amplitude": 4.815
  },
{
    "time": 6.636 ,
    "amplitude": 4.82
  },
{
    "time": 6.639 ,
    "amplitude": 4.81
  },
{
    "time": 6.642 ,
    "amplitude": 4.805
  },
{
    "time": 6.644 ,
    "amplitude": 4.815
  },
{
    "time": 6.647 ,
    "amplitude": 4.82
  },
{
    "time": 6.65 ,
    "amplitude": 4.83
  },
{
    "time": 6.653 ,
    "amplitude": 4.84
  },
{
    "time": 6.656 ,
    "amplitude": 4.82
  },
{
    "time": 6.658 ,
    "amplitude": 4.805
  },
{
    "time": 6.661 ,
    "amplitude": 4.805
  },
{
    "time": 6.664 ,
    "amplitude": 4.815
  },
{
    "time": 6.667 ,
    "amplitude": 4.83
  },
{
    "time": 6.669 ,
    "amplitude": 4.815
  },
{
    "time": 6.672 ,
    "amplitude": 4.815
  },
{
    "time": 6.675 ,
    "amplitude": 4.805
  },
{
    "time": 6.678 ,
    "amplitude": 4.805
  },
{
    "time": 6.681 ,
    "amplitude": 4.81
  },
{
    "time": 6.683 ,
    "amplitude": 4.83
  },
{
    "time": 6.686 ,
    "amplitude": 4.825
  },
{
    "time": 6.689 ,
    "amplitude": 4.81
  },
{
    "time": 6.692 ,
    "amplitude": 4.805
  },
{
    "time": 6.694 ,
    "amplitude": 4.815
  },
{
    "time": 6.697 ,
    "amplitude": 4.825
  },
{
    "time": 6.7 ,
    "amplitude": 4.82
  },
{
    "time": 6.703 ,
    "amplitude": 4.815
  },
{
    "time": 6.706 ,
    "amplitude": 4.83
  },
{
    "time": 6.708 ,
    "amplitude": 4.805
  },
{
    "time": 6.711 ,
    "amplitude": 4.8
  },
{
    "time": 6.714 ,
    "amplitude": 4.82
  },
{
    "time": 6.717 ,
    "amplitude": 4.875
  },
{
    "time": 6.719 ,
    "amplitude": 4.9
  },
{
    "time": 6.722 ,
    "amplitude": 4.91
  },
{
    "time": 6.725 ,
    "amplitude": 4.9
  },
{
    "time": 6.728 ,
    "amplitude": 4.9
  },
{
    "time": 6.731 ,
    "amplitude": 4.91
  },
{
    "time": 6.733 ,
    "amplitude": 4.93
  },
{
    "time": 6.736 ,
    "amplitude": 4.92
  },
{
    "time": 6.739 ,
    "amplitude": 4.95
  },
{
    "time": 6.742 ,
    "amplitude": 4.955
  },
{
    "time": 6.744 ,
    "amplitude": 4.99
  },
{
    "time": 6.747 ,
    "amplitude": 5
  },
{
    "time": 6.75 ,
    "amplitude": 5.01
  },
{
    "time": 6.753 ,
    "amplitude": 5.035
  },
{
    "time": 6.756 ,
    "amplitude": 5.025
  },
{
    "time": 6.758 ,
    "amplitude": 5.025
  },
{
    "time": 6.761 ,
    "amplitude": 5.02
  },
{
    "time": 6.764 ,
    "amplitude": 5.025
  },
{
    "time": 6.767 ,
    "amplitude": 5.035
  },
{
    "time": 6.769 ,
    "amplitude": 5.045
  },
{
    "time": 6.772 ,
    "amplitude": 5.05
  },
{
    "time": 6.775 ,
    "amplitude": 5.06
  },
{
    "time": 6.778 ,
    "amplitude": 5.06
  },
{
    "time": 6.781 ,
    "amplitude": 5.075
  },
{
    "time": 6.783 ,
    "amplitude": 5.05
  },
{
    "time": 6.786 ,
    "amplitude": 5.015
  },
{
    "time": 6.789 ,
    "amplitude": 4.96
  },
{
    "time": 6.792 ,
    "amplitude": 4.92
  },
{
    "time": 6.794 ,
    "amplitude": 4.905
  },
{
    "time": 6.797 ,
    "amplitude": 4.87
  },
{
    "time": 6.8 ,
    "amplitude": 4.84
  },
{
    "time": 6.803 ,
    "amplitude": 4.8
  },
{
    "time": 6.806 ,
    "amplitude": 4.785
  },
{
    "time": 6.808 ,
    "amplitude": 4.77
  },
{
    "time": 6.811 ,
    "amplitude": 4.775
  },
{
    "time": 6.814 ,
    "amplitude": 4.79
  },
{
    "time": 6.817 ,
    "amplitude": 4.78
  },
{
    "time": 6.819 ,
    "amplitude": 4.78
  },
{
    "time": 6.822 ,
    "amplitude": 4.76
  },
{
    "time": 6.825 ,
    "amplitude": 4.76
  },
{
    "time": 6.828 ,
    "amplitude": 4.74
  },
{
    "time": 6.831 ,
    "amplitude": 4.76
  },
{
    "time": 6.833 ,
    "amplitude": 4.8
  },
{
    "time": 6.836 ,
    "amplitude": 4.82
  },
{
    "time": 6.839 ,
    "amplitude": 4.805
  },
{
    "time": 6.842 ,
    "amplitude": 4.79
  },
{
    "time": 6.844 ,
    "amplitude": 4.775
  },
{
    "time": 6.847 ,
    "amplitude": 4.77
  },
{
    "time": 6.85 ,
    "amplitude": 4.79
  },
{
    "time": 6.853 ,
    "amplitude": 4.78
  },
{
    "time": 6.856 ,
    "amplitude": 4.76
  },
{
    "time": 6.858 ,
    "amplitude": 4.77
  },
{
    "time": 6.861 ,
    "amplitude": 4.77
  },
{
    "time": 6.864 ,
    "amplitude": 4.775
  },
{
    "time": 6.867 ,
    "amplitude": 4.775
  },
{
    "time": 6.869 ,
    "amplitude": 4.77
  },
{
    "time": 6.872 ,
    "amplitude": 4.76
  },
{
    "time": 6.875 ,
    "amplitude": 4.755
  },
{
    "time": 6.878 ,
    "amplitude": 4.765
  },
{
    "time": 6.881 ,
    "amplitude": 4.78
  },
{
    "time": 6.883 ,
    "amplitude": 4.785
  },
{
    "time": 6.886 ,
    "amplitude": 4.78
  },
{
    "time": 6.889 ,
    "amplitude": 4.78
  },
{
    "time": 6.892 ,
    "amplitude": 4.785
  },
{
    "time": 6.894 ,
    "amplitude": 4.77
  },
{
    "time": 6.897 ,
    "amplitude": 4.77
  },
{
    "time": 6.9 ,
    "amplitude": 4.765
  },
{
    "time": 6.903 ,
    "amplitude": 4.77
  },
{
    "time": 6.906 ,
    "amplitude": 4.77
  },
{
    "time": 6.908 ,
    "amplitude": 4.745
  },
{
    "time": 6.911 ,
    "amplitude": 4.73
  },
{
    "time": 6.914 ,
    "amplitude": 4.745
  },
{
    "time": 6.917 ,
    "amplitude": 4.74
  },
{
    "time": 6.919 ,
    "amplitude": 4.72
  },
{
    "time": 6.922 ,
    "amplitude": 4.7
  },
{
    "time": 6.925 ,
    "amplitude": 4.695
  },
{
    "time": 6.928 ,
    "amplitude": 4.705
  },
{
    "time": 6.931 ,
    "amplitude": 4.705
  },
{
    "time": 6.933 ,
    "amplitude": 4.73
  },
{
    "time": 6.936 ,
    "amplitude": 4.735
  },
{
    "time": 6.939 ,
    "amplitude": 4.685
  },
{
    "time": 6.942 ,
    "amplitude": 4.59
  },
{
    "time": 6.944 ,
    "amplitude": 4.535
  },
{
    "time": 6.947 ,
    "amplitude": 4.51
  },
{
    "time": 6.95 ,
    "amplitude": 4.535
  },
{
    "time": 6.953 ,
    "amplitude": 4.545
  },
{
    "time": 6.956 ,
    "amplitude": 4.515
  },
{
    "time": 6.958 ,
    "amplitude": 4.485
  },
{
    "time": 6.961 ,
    "amplitude": 4.455
  },
{
    "time": 6.964 ,
    "amplitude": 4.42
  },
{
    "time": 6.967 ,
    "amplitude": 4.395
  },
{
    "time": 6.969 ,
    "amplitude": 4.36
  },
{
    "time": 6.972 ,
    "amplitude": 4.33
  },
{
    "time": 6.975 ,
    "amplitude": 4.325
  },
{
    "time": 6.978 ,
    "amplitude": 4.32
  },
{
    "time": 6.981 ,
    "amplitude": 4.27
  },
{
    "time": 6.983 ,
    "amplitude": 4.21
  },
{
    "time": 6.986 ,
    "amplitude": 4.165
  },
{
    "time": 6.989 ,
    "amplitude": 4.155
  },
{
    "time": 6.992 ,
    "amplitude": 4.145
  },
{
    "time": 6.994 ,
    "amplitude": 4.17
  },
{
    "time": 6.997 ,
    "amplitude": 4.21
  },
{
    "time": 7 ,
    "amplitude": 4.25
  },
{
    "time": 7.003 ,
    "amplitude": 4.28
  },
{
    "time": 7.006 ,
    "amplitude": 4.31
  },
{
    "time": 7.008 ,
    "amplitude": 4.345
  },
{
    "time": 7.011 ,
    "amplitude": 4.425
  },
{
    "time": 7.014 ,
    "amplitude": 4.505
  },
{
    "time": 7.017 ,
    "amplitude": 4.565
  },
{
    "time": 7.019 ,
    "amplitude": 4.61
  },
{
    "time": 7.022 ,
    "amplitude": 4.635
  },
{
    "time": 7.025 ,
    "amplitude": 4.68
  },
{
    "time": 7.028 ,
    "amplitude": 4.76
  },
{
    "time": 7.031 ,
    "amplitude": 4.785
  },
{
    "time": 7.033 ,
    "amplitude": 4.805
  },
{
    "time": 7.036 ,
    "amplitude": 4.825
  },
{
    "time": 7.039 ,
    "amplitude": 4.835
  },
{
    "time": 7.042 ,
    "amplitude": 4.835
  },
{
    "time": 7.044 ,
    "amplitude": 4.835
  },
{
    "time": 7.047 ,
    "amplitude": 4.845
  },
{
    "time": 7.05 ,
    "amplitude": 4.855
  },
{
    "time": 7.053 ,
    "amplitude": 4.875
  },
{
    "time": 7.056 ,
    "amplitude": 4.865
  },
{
    "time": 7.058 ,
    "amplitude": 4.86
  },
{
    "time": 7.061 ,
    "amplitude": 4.86
  },
{
    "time": 7.064 ,
    "amplitude": 4.88
  },
{
    "time": 7.067 ,
    "amplitude": 4.895
  },
{
    "time": 7.069 ,
    "amplitude": 4.875
  },
{
    "time": 7.072 ,
    "amplitude": 4.87
  },
{
    "time": 7.075 ,
    "amplitude": 4.85
  },
{
    "time": 7.078 ,
    "amplitude": 4.85
  },
{
    "time": 7.081 ,
    "amplitude": 4.87
  },
{
    "time": 7.083 ,
    "amplitude": 4.88
  },
{
    "time": 7.086 ,
    "amplitude": 4.9
  },
{
    "time": 7.089 ,
    "amplitude": 4.875
  },
{
    "time": 7.092 ,
    "amplitude": 4.87
  },
{
    "time": 7.094 ,
    "amplitude": 4.88
  },
{
    "time": 7.097 ,
    "amplitude": 4.89
  },
{
    "time": 7.1 ,
    "amplitude": 4.9
  },
{
    "time": 7.103 ,
    "amplitude": 4.9
  },
{
    "time": 7.106 ,
    "amplitude": 4.9
  },
{
    "time": 7.108 ,
    "amplitude": 4.885
  },
{
    "time": 7.111 ,
    "amplitude": 4.905
  },
{
    "time": 7.114 ,
    "amplitude": 4.905
  },
{
    "time": 7.117 ,
    "amplitude": 4.905
  },
{
    "time": 7.119 ,
    "amplitude": 4.92
  },
{
    "time": 7.122 ,
    "amplitude": 4.905
  },
{
    "time": 7.125 ,
    "amplitude": 4.9
  },
{
    "time": 7.128 ,
    "amplitude": 4.905
  },
{
    "time": 7.131 ,
    "amplitude": 4.895
  },
{
    "time": 7.133 ,
    "amplitude": 4.905
  },
{
    "time": 7.136 ,
    "amplitude": 4.905
  },
{
    "time": 7.139 ,
    "amplitude": 4.9
  },
{
    "time": 7.142 ,
    "amplitude": 4.89
  },
{
    "time": 7.144 ,
    "amplitude": 4.91
  },
{
    "time": 7.147 ,
    "amplitude": 4.925
  },
{
    "time": 7.15 ,
    "amplitude": 4.92
  },
{
    "time": 7.153 ,
    "amplitude": 4.92
  },
{
    "time": 7.156 ,
    "amplitude": 4.935
  },
{
    "time": 7.158 ,
    "amplitude": 4.94
  },
{
    "time": 7.161 ,
    "amplitude": 4.95
  },
{
    "time": 7.164 ,
    "amplitude": 4.94
  },
{
    "time": 7.167 ,
    "amplitude": 4.93
  },
{
    "time": 7.169 ,
    "amplitude": 4.935
  },
{
    "time": 7.172 ,
    "amplitude": 4.945
  },
{
    "time": 7.175 ,
    "amplitude": 4.925
  },
{
    "time": 7.178 ,
    "amplitude": 4.95
  },
{
    "time": 7.181 ,
    "amplitude": 4.955
  },
{
    "time": 7.183 ,
    "amplitude": 4.98
  },
{
    "time": 7.186 ,
    "amplitude": 4.99
  },
{
    "time": 7.189 ,
    "amplitude": 4.99
  },
{
    "time": 7.192 ,
    "amplitude": 4.99
  },
{
    "time": 7.194 ,
    "amplitude": 4.985
  },
{
    "time": 7.197 ,
    "amplitude": 4.99
  },
{
    "time": 7.2 ,
    "amplitude": 4.985
  },
{
    "time": 7.203 ,
    "amplitude": 4.995
  },
{
    "time": 7.206 ,
    "amplitude": 5
  },
{
    "time": 7.208 ,
    "amplitude": 5.005
  },
{
    "time": 7.211 ,
    "amplitude": 5.005
  },
{
    "time": 7.214 ,
    "amplitude": 4.99
  },
{
    "time": 7.217 ,
    "amplitude": 5.005
  },
{
    "time": 7.219 ,
    "amplitude": 5.005
  },
{
    "time": 7.222 ,
    "amplitude": 5.01
  },
{
    "time": 7.225 ,
    "amplitude": 5.005
  },
{
    "time": 7.228 ,
    "amplitude": 5.035
  },
{
    "time": 7.231 ,
    "amplitude": 5.05
  },
{
    "time": 7.233 ,
    "amplitude": 5.04
  },
{
    "time": 7.236 ,
    "amplitude": 5.04
  },
{
    "time": 7.239 ,
    "amplitude": 5.015
  },
{
    "time": 7.242 ,
    "amplitude": 5.005
  },
{
    "time": 7.244 ,
    "amplitude": 5.005
  },
{
    "time": 7.247 ,
    "amplitude": 5.005
  },
{
    "time": 7.25 ,
    "amplitude": 5
  },
{
    "time": 7.253 ,
    "amplitude": 5
  },
{
    "time": 7.256 ,
    "amplitude": 5
  },
{
    "time": 7.258 ,
    "amplitude": 4.995
  },
{
    "time": 7.261 ,
    "amplitude": 4.99
  },
{
    "time": 7.264 ,
    "amplitude": 4.99
  },
{
    "time": 7.267 ,
    "amplitude": 4.985
  },
{
    "time": 7.269 ,
    "amplitude": 4.98
  },
{
    "time": 7.272 ,
    "amplitude": 4.965
  },
{
    "time": 7.275 ,
    "amplitude": 4.965
  },
{
    "time": 7.278 ,
    "amplitude": 4.975
  },
{
    "time": 7.281 ,
    "amplitude": 4.975
  },
{
    "time": 7.283 ,
    "amplitude": 4.965
  },
{
    "time": 7.286 ,
    "amplitude": 4.93
  },
{
    "time": 7.289 ,
    "amplitude": 4.915
  },
{
    "time": 7.292 ,
    "amplitude": 4.9
  },
{
    "time": 7.294 ,
    "amplitude": 4.91
  },
{
    "time": 7.297 ,
    "amplitude": 4.905
  },
{
    "time": 7.3 ,
    "amplitude": 4.89
  },
{
    "time": 7.303 ,
    "amplitude": 4.88
  },
{
    "time": 7.306 ,
    "amplitude": 4.875
  },
{
    "time": 7.308 ,
    "amplitude": 4.88
  },
{
    "time": 7.311 ,
    "amplitude": 4.87
  },
{
    "time": 7.314 ,
    "amplitude": 4.865
  },
{
    "time": 7.317 ,
    "amplitude": 4.89
  },
{
    "time": 7.319 ,
    "amplitude": 4.885
  },
{
    "time": 7.322 ,
    "amplitude": 4.87
  },
{
    "time": 7.325 ,
    "amplitude": 4.84
  },
{
    "time": 7.328 ,
    "amplitude": 4.85
  },
{
    "time": 7.331 ,
    "amplitude": 4.855
  },
{
    "time": 7.333 ,
    "amplitude": 4.855
  },
{
    "time": 7.336 ,
    "amplitude": 4.835
  },
{
    "time": 7.339 ,
    "amplitude": 4.845
  },
{
    "time": 7.342 ,
    "amplitude": 4.84
  },
{
    "time": 7.344 ,
    "amplitude": 4.865
  },
{
    "time": 7.347 ,
    "amplitude": 4.86
  },
{
    "time": 7.35 ,
    "amplitude": 4.85
  },
{
    "time": 7.353 ,
    "amplitude": 4.845
  },
{
    "time": 7.356 ,
    "amplitude": 4.83
  },
{
    "time": 7.358 ,
    "amplitude": 4.83
  },
{
    "time": 7.361 ,
    "amplitude": 4.815
  },
{
    "time": 7.364 ,
    "amplitude": 4.805
  },
{
    "time": 7.367 ,
    "amplitude": 4.815
  },
{
    "time": 7.369 ,
    "amplitude": 4.82
  },
{
    "time": 7.372 ,
    "amplitude": 4.82
  },
{
    "time": 7.375 ,
    "amplitude": 4.82
  },
{
    "time": 7.378 ,
    "amplitude": 4.82
  },
{
    "time": 7.381 ,
    "amplitude": 4.84
  },
{
    "time": 7.383 ,
    "amplitude": 4.84
  },
{
    "time": 7.386 ,
    "amplitude": 4.84
  },
{
    "time": 7.389 ,
    "amplitude": 4.82
  },
{
    "time": 7.392 ,
    "amplitude": 4.81
  },
{
    "time": 7.394 ,
    "amplitude": 4.815
  },
{
    "time": 7.397 ,
    "amplitude": 4.82
  },
{
    "time": 7.4 ,
    "amplitude": 4.83
  },
{
    "time": 7.403 ,
    "amplitude": 4.81
  },
{
    "time": 7.406 ,
    "amplitude": 4.775
  },
{
    "time": 7.408 ,
    "amplitude": 4.765
  },
{
    "time": 7.411 ,
    "amplitude": 4.785
  },
{
    "time": 7.414 ,
    "amplitude": 4.805
  },
{
    "time": 7.417 ,
    "amplitude": 4.8
  },
{
    "time": 7.419 ,
    "amplitude": 4.795
  },
{
    "time": 7.422 ,
    "amplitude": 4.78
  },
{
    "time": 7.425 ,
    "amplitude": 4.775
  },
{
    "time": 7.428 ,
    "amplitude": 4.755
  },
{
    "time": 7.431 ,
    "amplitude": 4.765
  },
{
    "time": 7.433 ,
    "amplitude": 4.8
  },
{
    "time": 7.436 ,
    "amplitude": 4.8
  },
{
    "time": 7.439 ,
    "amplitude": 4.78
  },
{
    "time": 7.442 ,
    "amplitude": 4.765
  },
{
    "time": 7.444 ,
    "amplitude": 4.77
  },
{
    "time": 7.447 ,
    "amplitude": 4.79
  },
{
    "time": 7.45 ,
    "amplitude": 4.81
  },
{
    "time": 7.453 ,
    "amplitude": 4.805
  },
{
    "time": 7.456 ,
    "amplitude": 4.785
  },
{
    "time": 7.458 ,
    "amplitude": 4.755
  },
{
    "time": 7.461 ,
    "amplitude": 4.75
  },
{
    "time": 7.464 ,
    "amplitude": 4.765
  },
{
    "time": 7.467 ,
    "amplitude": 4.775
  },
{
    "time": 7.469 ,
    "amplitude": 4.775
  },
{
    "time": 7.472 ,
    "amplitude": 4.74
  },
{
    "time": 7.475 ,
    "amplitude": 4.715
  },
{
    "time": 7.478 ,
    "amplitude": 4.725
  },
{
    "time": 7.481 ,
    "amplitude": 4.73
  },
{
    "time": 7.483 ,
    "amplitude": 4.74
  },
{
    "time": 7.486 ,
    "amplitude": 4.735
  },
{
    "time": 7.489 ,
    "amplitude": 4.73
  },
{
    "time": 7.492 ,
    "amplitude": 4.71
  },
{
    "time": 7.494 ,
    "amplitude": 4.72
  },
{
    "time": 7.497 ,
    "amplitude": 4.72
  },
{
    "time": 7.5 ,
    "amplitude": 4.71
  },
{
    "time": 7.503 ,
    "amplitude": 4.715
  },
{
    "time": 7.506 ,
    "amplitude": 4.725
  },
{
    "time": 7.508 ,
    "amplitude": 4.72
  },
{
    "time": 7.511 ,
    "amplitude": 4.735
  },
{
    "time": 7.514 ,
    "amplitude": 4.73
  },
{
    "time": 7.517 ,
    "amplitude": 4.73
  },
{
    "time": 7.519 ,
    "amplitude": 4.725
  },
{
    "time": 7.522 ,
    "amplitude": 4.71
  },
{
    "time": 7.525 ,
    "amplitude": 4.71
  },
{
    "time": 7.528 ,
    "amplitude": 4.715
  },
{
    "time": 7.531 ,
    "amplitude": 4.74
  },
{
    "time": 7.533 ,
    "amplitude": 4.735
  },
{
    "time": 7.536 ,
    "amplitude": 4.715
  },
{
    "time": 7.539 ,
    "amplitude": 4.71
  },
{
    "time": 7.542 ,
    "amplitude": 4.705
  },
{
    "time": 7.544 ,
    "amplitude": 4.72
  },
{
    "time": 7.547 ,
    "amplitude": 4.725
  },
{
    "time": 7.55 ,
    "amplitude": 4.72
  },
{
    "time": 7.553 ,
    "amplitude": 4.725
  },
{
    "time": 7.556 ,
    "amplitude": 4.725
  },
{
    "time": 7.558 ,
    "amplitude": 4.71
  },
{
    "time": 7.561 ,
    "amplitude": 4.71
  },
{
    "time": 7.564 ,
    "amplitude": 4.72
  },
{
    "time": 7.567 ,
    "amplitude": 4.735
  },
{
    "time": 7.569 ,
    "amplitude": 4.745
  },
{
    "time": 7.572 ,
    "amplitude": 4.745
  },
{
    "time": 7.575 ,
    "amplitude": 4.73
  },
{
    "time": 7.578 ,
    "amplitude": 4.72
  },
{
    "time": 7.581 ,
    "amplitude": 4.735
  },
{
    "time": 7.583 ,
    "amplitude": 4.74
  },
{
    "time": 7.586 ,
    "amplitude": 4.745
  },
{
    "time": 7.589 ,
    "amplitude": 4.73
  },
{
    "time": 7.592 ,
    "amplitude": 4.72
  },
{
    "time": 7.594 ,
    "amplitude": 4.745
  },
{
    "time": 7.597 ,
    "amplitude": 4.75
  },
{
    "time": 7.6 ,
    "amplitude": 4.74
  },
{
    "time": 7.603 ,
    "amplitude": 4.72
  },
{
    "time": 7.606 ,
    "amplitude": 4.72
  },
{
    "time": 7.608 ,
    "amplitude": 4.745
  },
{
    "time": 7.611 ,
    "amplitude": 4.775
  },
{
    "time": 7.614 ,
    "amplitude": 4.79
  },
{
    "time": 7.617 ,
    "amplitude": 4.79
  },
{
    "time": 7.619 ,
    "amplitude": 4.76
  },
{
    "time": 7.622 ,
    "amplitude": 4.73
  },
{
    "time": 7.625 ,
    "amplitude": 4.715
  },
{
    "time": 7.628 ,
    "amplitude": 4.745
  },
{
    "time": 7.631 ,
    "amplitude": 4.77
  },
{
    "time": 7.633 ,
    "amplitude": 4.775
  },
{
    "time": 7.636 ,
    "amplitude": 4.76
  },
{
    "time": 7.639 ,
    "amplitude": 4.765
  },
{
    "time": 7.642 ,
    "amplitude": 4.755
  },
{
    "time": 7.644 ,
    "amplitude": 4.77
  },
{
    "time": 7.647 ,
    "amplitude": 4.785
  },
{
    "time": 7.65 ,
    "amplitude": 4.77
  },
{
    "time": 7.653 ,
    "amplitude": 4.76
  },
{
    "time": 7.656 ,
    "amplitude": 4.76
  },
{
    "time": 7.658 ,
    "amplitude": 4.75
  },
{
    "time": 7.661 ,
    "amplitude": 4.765
  },
{
    "time": 7.664 ,
    "amplitude": 4.78
  },
{
    "time": 7.667 ,
    "amplitude": 4.775
  },
{
    "time": 7.669 ,
    "amplitude": 4.78
  },
{
    "time": 7.672 ,
    "amplitude": 4.77
  },
{
    "time": 7.675 ,
    "amplitude": 4.755
  },
{
    "time": 7.678 ,
    "amplitude": 4.74
  },
{
    "time": 7.681 ,
    "amplitude": 4.75
  },
{
    "time": 7.683 ,
    "amplitude": 4.77
  },
{
    "time": 7.686 ,
    "amplitude": 4.795
  },
{
    "time": 7.689 ,
    "amplitude": 4.79
  },
{
    "time": 7.692 ,
    "amplitude": 4.77
  },
{
    "time": 7.694 ,
    "amplitude": 4.76
  },
{
    "time": 7.697 ,
    "amplitude": 4.77
  },
{
    "time": 7.7 ,
    "amplitude": 4.77
  },
{
    "time": 7.703 ,
    "amplitude": 4.795
  },
{
    "time": 7.706 ,
    "amplitude": 4.81
  },
{
    "time": 7.708 ,
    "amplitude": 4.785
  },
{
    "time": 7.711 ,
    "amplitude": 4.775
  },
{
    "time": 7.714 ,
    "amplitude": 4.77
  },
{
    "time": 7.717 ,
    "amplitude": 4.775
  },
{
    "time": 7.719 ,
    "amplitude": 4.765
  },
{
    "time": 7.722 ,
    "amplitude": 4.77
  },
{
    "time": 7.725 ,
    "amplitude": 4.76
  },
{
    "time": 7.728 ,
    "amplitude": 4.765
  },
{
    "time": 7.731 ,
    "amplitude": 4.775
  },
{
    "time": 7.733 ,
    "amplitude": 4.78
  },
{
    "time": 7.736 ,
    "amplitude": 4.785
  },
{
    "time": 7.739 ,
    "amplitude": 4.775
  },
{
    "time": 7.742 ,
    "amplitude": 4.755
  },
{
    "time": 7.744 ,
    "amplitude": 4.73
  },
{
    "time": 7.747 ,
    "amplitude": 4.74
  },
{
    "time": 7.75 ,
    "amplitude": 4.78
  },
{
    "time": 7.753 ,
    "amplitude": 4.84
  },
{
    "time": 7.756 ,
    "amplitude": 4.86
  },
{
    "time": 7.758 ,
    "amplitude": 4.84
  },
{
    "time": 7.761 ,
    "amplitude": 4.84
  },
{
    "time": 7.764 ,
    "amplitude": 4.845
  },
{
    "time": 7.767 ,
    "amplitude": 4.86
  },
{
    "time": 7.769 ,
    "amplitude": 4.86
  },
{
    "time": 7.772 ,
    "amplitude": 4.85
  },
{
    "time": 7.775 ,
    "amplitude": 4.835
  },
{
    "time": 7.778 ,
    "amplitude": 4.875
  },
{
    "time": 7.781 ,
    "amplitude": 4.89
  },
{
    "time": 7.783 ,
    "amplitude": 4.915
  },
{
    "time": 7.786 ,
    "amplitude": 4.925
  },
{
    "time": 7.789 ,
    "amplitude": 4.935
  },
{
    "time": 7.792 ,
    "amplitude": 4.94
  },
{
    "time": 7.794 ,
    "amplitude": 4.98
  },
{
    "time": 7.797 ,
    "amplitude": 4.99
  },
{
    "time": 7.8 ,
    "amplitude": 5.015
  },
{
    "time": 7.803 ,
    "amplitude": 4.99
  },
{
    "time": 7.806 ,
    "amplitude": 4.97
  },
{
    "time": 7.808 ,
    "amplitude": 4.975
  },
{
    "time": 7.811 ,
    "amplitude": 5
  },
{
    "time": 7.814 ,
    "amplitude": 5.015
  },
{
    "time": 7.817 ,
    "amplitude": 5.05
  },
{
    "time": 7.819 ,
    "amplitude": 5.04
  },
{
    "time": 7.822 ,
    "amplitude": 5.035
  },
{
    "time": 7.825 ,
    "amplitude": 4.985
  },
{
    "time": 7.828 ,
    "amplitude": 4.91
  },
{
    "time": 7.831 ,
    "amplitude": 4.87
  },
{
    "time": 7.833 ,
    "amplitude": 4.86
  },
{
    "time": 7.836 ,
    "amplitude": 4.835
  },
{
    "time": 7.839 ,
    "amplitude": 4.805
  },
{
    "time": 7.842 ,
    "amplitude": 4.76
  },
{
    "time": 7.844 ,
    "amplitude": 4.745
  },
{
    "time": 7.847 ,
    "amplitude": 4.735
  },
{
    "time": 7.85 ,
    "amplitude": 4.755
  },
{
    "time": 7.853 ,
    "amplitude": 4.75
  },
{
    "time": 7.856 ,
    "amplitude": 4.75
  },
{
    "time": 7.858 ,
    "amplitude": 4.725
  },
{
    "time": 7.861 ,
    "amplitude": 4.735
  },
{
    "time": 7.864 ,
    "amplitude": 4.75
  },
{
    "time": 7.867 ,
    "amplitude": 4.745
  },
{
    "time": 7.869 ,
    "amplitude": 4.73
  },
{
    "time": 7.872 ,
    "amplitude": 4.725
  },
{
    "time": 7.875 ,
    "amplitude": 4.72
  },
{
    "time": 7.878 ,
    "amplitude": 4.73
  },
{
    "time": 7.881 ,
    "amplitude": 4.735
  },
{
    "time": 7.883 ,
    "amplitude": 4.735
  },
{
    "time": 7.886 ,
    "amplitude": 4.74
  },
{
    "time": 7.889 ,
    "amplitude": 4.72
  },
{
    "time": 7.892 ,
    "amplitude": 4.72
  },
{
    "time": 7.894 ,
    "amplitude": 4.735
  },
{
    "time": 7.897 ,
    "amplitude": 4.745
  },
{
    "time": 7.9 ,
    "amplitude": 4.76
  },
{
    "time": 7.903 ,
    "amplitude": 4.745
  },
{
    "time": 7.906 ,
    "amplitude": 4.73
  },
{
    "time": 7.908 ,
    "amplitude": 4.73
  },
{
    "time": 7.911 ,
    "amplitude": 4.715
  },
{
    "time": 7.914 ,
    "amplitude": 4.72
  },
{
    "time": 7.917 ,
    "amplitude": 4.73
  },
{
    "time": 7.919 ,
    "amplitude": 4.755
  },
{
    "time": 7.922 ,
    "amplitude": 4.735
  },
{
    "time": 7.925 ,
    "amplitude": 4.725
  },
{
    "time": 7.928 ,
    "amplitude": 4.72
  },
{
    "time": 7.931 ,
    "amplitude": 4.725
  },
{
    "time": 7.933 ,
    "amplitude": 4.73
  },
{
    "time": 7.936 ,
    "amplitude": 4.735
  },
{
    "time": 7.939 ,
    "amplitude": 4.735
  },
{
    "time": 7.942 ,
    "amplitude": 4.72
  },
{
    "time": 7.944 ,
    "amplitude": 4.735
  },
{
    "time": 7.947 ,
    "amplitude": 4.745
  },
{
    "time": 7.95 ,
    "amplitude": 4.735
  },
{
    "time": 7.953 ,
    "amplitude": 4.715
  },
{
    "time": 7.956 ,
    "amplitude": 4.67
  },
{
    "time": 7.958 ,
    "amplitude": 4.68
  },
{
    "time": 7.961 ,
    "amplitude": 4.705
  },
{
    "time": 7.964 ,
    "amplitude": 4.725
  },
{
    "time": 7.967 ,
    "amplitude": 4.745
  },
{
    "time": 7.969 ,
    "amplitude": 4.74
  },
{
    "time": 7.972 ,
    "amplitude": 4.725
  },
{
    "time": 7.975 ,
    "amplitude": 4.655
  },
{
    "time": 7.978 ,
    "amplitude": 4.58
  },
{
    "time": 7.981 ,
    "amplitude": 4.52
  },
{
    "time": 7.983 ,
    "amplitude": 4.5
  },
{
    "time": 7.986 ,
    "amplitude": 4.48
  },
{
    "time": 7.989 ,
    "amplitude": 4.465
  },
{
    "time": 7.992 ,
    "amplitude": 4.47
  },
{
    "time": 7.994 ,
    "amplitude": 4.47
  },
{
    "time": 7.997 ,
    "amplitude": 4.44
  },
{
    "time": 8 ,
    "amplitude": 4.385
  },
{
    "time": 8.003 ,
    "amplitude": 4.34
  },
{
    "time": 8.006 ,
    "amplitude": 4.3
  },
{
    "time": 8.008 ,
    "amplitude": 4.265
  },
{
    "time": 8.011 ,
    "amplitude": 4.265
  },
{
    "time": 8.014 ,
    "amplitude": 4.23
  },
{
    "time": 8.017 ,
    "amplitude": 4.185
  },
{
    "time": 8.019 ,
    "amplitude": 4.135
  },
{
    "time": 8.022 ,
    "amplitude": 4.105
  },
{
    "time": 8.025 ,
    "amplitude": 4.1
  },
{
    "time": 8.028 ,
    "amplitude": 4.105
  },
{
    "time": 8.031 ,
    "amplitude": 4.135
  },
{
    "time": 8.033 ,
    "amplitude": 4.19
  },
{
    "time": 8.036 ,
    "amplitude": 4.235
  },
{
    "time": 8.039 ,
    "amplitude": 4.24
  },
{
    "time": 8.042 ,
    "amplitude": 4.285
  },
{
    "time": 8.044 ,
    "amplitude": 4.38
  },
{
    "time": 8.047 ,
    "amplitude": 4.465
  },
{
    "time": 8.05 ,
    "amplitude": 4.535
  },
{
    "time": 8.053 ,
    "amplitude": 4.575
  },
{
    "time": 8.056 ,
    "amplitude": 4.595
  },
{
    "time": 8.058 ,
    "amplitude": 4.615
  },
{
    "time": 8.061 ,
    "amplitude": 4.67
  },
{
    "time": 8.064 ,
    "amplitude": 4.73
  },
{
    "time": 8.067 ,
    "amplitude": 4.785
  },
{
    "time": 8.069 ,
    "amplitude": 4.805
  },
{
    "time": 8.072 ,
    "amplitude": 4.81
  },
{
    "time": 8.075 ,
    "amplitude": 4.8
  },
{
    "time": 8.078 ,
    "amplitude": 4.81
  },
{
    "time": 8.081 ,
    "amplitude": 4.82
  },
{
    "time": 8.083 ,
    "amplitude": 4.835
  },
{
    "time": 8.086 ,
    "amplitude": 4.835
  },
{
    "time": 8.089 ,
    "amplitude": 4.835
  },
{
    "time": 8.092 ,
    "amplitude": 4.815
  },
{
    "time": 8.094 ,
    "amplitude": 4.83
  },
{
    "time": 8.097 ,
    "amplitude": 4.84
  },
{
    "time": 8.1 ,
    "amplitude": 4.84
  },
{
    "time": 8.103 ,
    "amplitude": 4.845
  },
{
    "time": 8.106 ,
    "amplitude": 4.84
  },
{
    "time": 8.108 ,
    "amplitude": 4.82
  },
{
    "time": 8.111 ,
    "amplitude": 4.83
  },
{
    "time": 8.114 ,
    "amplitude": 4.845
  },
{
    "time": 8.117 ,
    "amplitude": 4.86
  },
{
    "time": 8.119 ,
    "amplitude": 4.855
  },
{
    "time": 8.122 ,
    "amplitude": 4.85
  },
{
    "time": 8.125 ,
    "amplitude": 4.84
  },
{
    "time": 8.128 ,
    "amplitude": 4.835
  },
{
    "time": 8.131 ,
    "amplitude": 4.835
  },
{
    "time": 8.133 ,
    "amplitude": 4.845
  },
{
    "time": 8.136 ,
    "amplitude": 4.87
  },
{
    "time": 8.139 ,
    "amplitude": 4.87
  },
{
    "time": 8.142 ,
    "amplitude": 4.86
  },
{
    "time": 8.144 ,
    "amplitude": 4.84
  },
{
    "time": 8.147 ,
    "amplitude": 4.855
  },
{
    "time": 8.15 ,
    "amplitude": 4.87
  },
{
    "time": 8.153 ,
    "amplitude": 4.86
  },
{
    "time": 8.156 ,
    "amplitude": 4.865
  },
{
    "time": 8.158 ,
    "amplitude": 4.865
  },
{
    "time": 8.161 ,
    "amplitude": 4.86
  },
{
    "time": 8.164 ,
    "amplitude": 4.875
  },
{
    "time": 8.167 ,
    "amplitude": 4.875
  },
{
    "time": 8.169 ,
    "amplitude": 4.88
  },
{
    "time": 8.172 ,
    "amplitude": 4.89
  },
{
    "time": 8.175 ,
    "amplitude": 4.885
  },
{
    "time": 8.178 ,
    "amplitude": 4.895
  },
{
    "time": 8.181 ,
    "amplitude": 4.895
  },
{
    "time": 8.183 ,
    "amplitude": 4.92
  },
{
    "time": 8.186 ,
    "amplitude": 4.91
  },
{
    "time": 8.189 ,
    "amplitude": 4.895
  },
{
    "time": 8.192 ,
    "amplitude": 4.885
  },
{
    "time": 8.194 ,
    "amplitude": 4.89
  },
{
    "time": 8.197 ,
    "amplitude": 4.895
  },
{
    "time": 8.2 ,
    "amplitude": 4.92
  },
{
    "time": 8.203 ,
    "amplitude": 4.94
  },
{
    "time": 8.206 ,
    "amplitude": 4.935
  },
{
    "time": 8.208 ,
    "amplitude": 4.935
  },
{
    "time": 8.211 ,
    "amplitude": 4.93
  },
{
    "time": 8.214 ,
    "amplitude": 4.92
  },
{
    "time": 8.217 ,
    "amplitude": 4.935
  },
{
    "time": 8.219 ,
    "amplitude": 4.95
  },
{
    "time": 8.222 ,
    "amplitude": 4.96
  },
{
    "time": 8.225 ,
    "amplitude": 4.95
  },
{
    "time": 8.228 ,
    "amplitude": 4.95
  },
{
    "time": 8.231 ,
    "amplitude": 4.965
  },
{
    "time": 8.233 ,
    "amplitude": 4.965
  },
{
    "time": 8.236 ,
    "amplitude": 4.97
  },
{
    "time": 8.239 ,
    "amplitude": 4.97
  },
{
    "time": 8.242 ,
    "amplitude": 4.955
  },
{
    "time": 8.244 ,
    "amplitude": 4.96
  },
{
    "time": 8.247 ,
    "amplitude": 4.97
  },
{
    "time": 8.25 ,
    "amplitude": 4.97
  },
{
    "time": 8.253 ,
    "amplitude": 4.97
  },
{
    "time": 8.256 ,
    "amplitude": 4.97
  },
{
    "time": 8.258 ,
    "amplitude": 4.975
  },
{
    "time": 8.261 ,
    "amplitude": 4.985
  },
{
    "time": 8.264 ,
    "amplitude": 4.975
  },
{
    "time": 8.267 ,
    "amplitude": 4.97
  },
{
    "time": 8.269 ,
    "amplitude": 4.975
  },
{
    "time": 8.272 ,
    "amplitude": 4.97
  },
{
    "time": 8.275 ,
    "amplitude": 4.955
  },
{
    "time": 8.278 ,
    "amplitude": 4.97
  },
{
    "time": 8.281 ,
    "amplitude": 4.99
  },
{
    "time": 8.283 ,
    "amplitude": 5
  },
{
    "time": 8.286 ,
    "amplitude": 4.99
  },
{
    "time": 8.289 ,
    "amplitude": 4.985
  },
{
    "time": 8.292 ,
    "amplitude": 4.975
  },
{
    "time": 8.294 ,
    "amplitude": 4.975
  },
{
    "time": 8.297 ,
    "amplitude": 4.97
  },
{
    "time": 8.3 ,
    "amplitude": 4.965
  },
{
    "time": 8.303 ,
    "amplitude": 4.955
  },
{
    "time": 8.306 ,
    "amplitude": 4.945
  },
{
    "time": 8.308 ,
    "amplitude": 4.92
  },
{
    "time": 8.311 ,
    "amplitude": 4.905
  },
{
    "time": 8.314 ,
    "amplitude": 4.9
  },
{
    "time": 8.317 ,
    "amplitude": 4.915
  },
{
    "time": 8.319 ,
    "amplitude": 4.91
  },
{
    "time": 8.322 ,
    "amplitude": 4.9
  },
{
    "time": 8.325 ,
    "amplitude": 4.89
  },
{
    "time": 8.328 ,
    "amplitude": 4.885
  },
{
    "time": 8.331 ,
    "amplitude": 4.875
  },
{
    "time": 8.333 ,
    "amplitude": 4.885
  },
{
    "time": 8.336 ,
    "amplitude": 4.87
  },
{
    "time": 8.339 ,
    "amplitude": 4.85
  },
{
    "time": 8.342 ,
    "amplitude": 4.85
  },
{
    "time": 8.344 ,
    "amplitude": 4.84
  },
{
    "time": 8.347 ,
    "amplitude": 4.855
  },
{
    "time": 8.35 ,
    "amplitude": 4.865
  },
{
    "time": 8.353 ,
    "amplitude": 4.865
  },
{
    "time": 8.356 ,
    "amplitude": 4.835
  },
{
    "time": 8.358 ,
    "amplitude": 4.83
  },
{
    "time": 8.361 ,
    "amplitude": 4.84
  },
{
    "time": 8.364 ,
    "amplitude": 4.845
  },
{
    "time": 8.367 ,
    "amplitude": 4.85
  },
{
    "time": 8.369 ,
    "amplitude": 4.845
  },
{
    "time": 8.372 ,
    "amplitude": 4.855
  },
{
    "time": 8.375 ,
    "amplitude": 4.845
  },
{
    "time": 8.378 ,
    "amplitude": 4.835
  },
{
    "time": 8.381 ,
    "amplitude": 4.845
  },
{
    "time": 8.383 ,
    "amplitude": 4.855
  },
{
    "time": 8.386 ,
    "amplitude": 4.84
  },
{
    "time": 8.389 ,
    "amplitude": 4.83
  },
{
    "time": 8.392 ,
    "amplitude": 4.825
  },
{
    "time": 8.394 ,
    "amplitude": 4.835
  },
{
    "time": 8.397 ,
    "amplitude": 4.855
  },
{
    "time": 8.4 ,
    "amplitude": 4.85
  },
{
    "time": 8.403 ,
    "amplitude": 4.84
  },
{
    "time": 8.406 ,
    "amplitude": 4.825
  },
{
    "time": 8.408 ,
    "amplitude": 4.815
  },
{
    "time": 8.411 ,
    "amplitude": 4.82
  },
{
    "time": 8.414 ,
    "amplitude": 4.84
  },
{
    "time": 8.417 ,
    "amplitude": 4.835
  },
{
    "time": 8.419 ,
    "amplitude": 4.835
  },
{
    "time": 8.422 ,
    "amplitude": 4.815
  },
{
    "time": 8.425 ,
    "amplitude": 4.805
  },
{
    "time": 8.428 ,
    "amplitude": 4.805
  },
{
    "time": 8.431 ,
    "amplitude": 4.825
  },
{
    "time": 8.433 ,
    "amplitude": 4.825
  },
{
    "time": 8.436 ,
    "amplitude": 4.825
  },
{
    "time": 8.439 ,
    "amplitude": 4.82
  },
{
    "time": 8.442 ,
    "amplitude": 4.81
  },
{
    "time": 8.444 ,
    "amplitude": 4.8
  },
{
    "time": 8.447 ,
    "amplitude": 4.815
  },
{
    "time": 8.45 ,
    "amplitude": 4.82
  },
{
    "time": 8.453 ,
    "amplitude": 4.815
  },
{
    "time": 8.456 ,
    "amplitude": 4.815
  },
{
    "time": 8.458 ,
    "amplitude": 4.79
  },
{
    "time": 8.461 ,
    "amplitude": 4.785
  },
{
    "time": 8.464 ,
    "amplitude": 4.785
  },
{
    "time": 8.467 ,
    "amplitude": 4.805
  },
{
    "time": 8.469 ,
    "amplitude": 4.805
  },
{
    "time": 8.472 ,
    "amplitude": 4.79
  },
{
    "time": 8.475 ,
    "amplitude": 4.765
  },
{
    "time": 8.478 ,
    "amplitude": 4.785
  },
{
    "time": 8.481 ,
    "amplitude": 4.795
  },
{
    "time": 8.483 ,
    "amplitude": 4.795
  },
{
    "time": 8.486 ,
    "amplitude": 4.795
  },
{
    "time": 8.489 ,
    "amplitude": 4.79
  },
{
    "time": 8.492 ,
    "amplitude": 4.765
  },
{
    "time": 8.494 ,
    "amplitude": 4.76
  },
{
    "time": 8.497 ,
    "amplitude": 4.77
  },
{
    "time": 8.5 ,
    "amplitude": 4.77
  },
{
    "time": 8.503 ,
    "amplitude": 4.775
  },
{
    "time": 8.506 ,
    "amplitude": 4.765
  },
{
    "time": 8.508 ,
    "amplitude": 4.74
  },
{
    "time": 8.511 ,
    "amplitude": 4.745
  },
{
    "time": 8.514 ,
    "amplitude": 4.75
  },
{
    "time": 8.517 ,
    "amplitude": 4.755
  },
{
    "time": 8.519 ,
    "amplitude": 4.75
  },
{
    "time": 8.522 ,
    "amplitude": 4.735
  },
{
    "time": 8.525 ,
    "amplitude": 4.715
  },
{
    "time": 8.528 ,
    "amplitude": 4.72
  },
{
    "time": 8.531 ,
    "amplitude": 4.725
  },
{
    "time": 8.533 ,
    "amplitude": 4.75
  },
{
    "time": 8.536 ,
    "amplitude": 4.75
  },
{
    "time": 8.539 ,
    "amplitude": 4.73
  },
{
    "time": 8.542 ,
    "amplitude": 4.71
  },
{
    "time": 8.544 ,
    "amplitude": 4.72
  },
{
    "time": 8.547 ,
    "amplitude": 4.715
  },
{
    "time": 8.55 ,
    "amplitude": 4.735
  },
{
    "time": 8.553 ,
    "amplitude": 4.755
  },
{
    "time": 8.556 ,
    "amplitude": 4.745
  },
{
    "time": 8.558 ,
    "amplitude": 4.725
  },
{
    "time": 8.561 ,
    "amplitude": 4.715
  },
{
    "time": 8.564 ,
    "amplitude": 4.72
  },
{
    "time": 8.567 ,
    "amplitude": 4.74
  },
{
    "time": 8.569 ,
    "amplitude": 4.755
  },
{
    "time": 8.572 ,
    "amplitude": 4.755
  },
{
    "time": 8.575 ,
    "amplitude": 4.735
  },
{
    "time": 8.578 ,
    "amplitude": 4.725
  },
{
    "time": 8.581 ,
    "amplitude": 4.72
  },
{
    "time": 8.583 ,
    "amplitude": 4.735
  },
{
    "time": 8.586 ,
    "amplitude": 4.745
  },
{
    "time": 8.589 ,
    "amplitude": 4.73
  },
{
    "time": 8.592 ,
    "amplitude": 4.74
  },
{
    "time": 8.594 ,
    "amplitude": 4.765
  },
{
    "time": 8.597 ,
    "amplitude": 4.78
  },
{
    "time": 8.6 ,
    "amplitude": 4.76
  },
{
    "time": 8.603 ,
    "amplitude": 4.74
  },
{
    "time": 8.606 ,
    "amplitude": 4.73
  },
{
    "time": 8.608 ,
    "amplitude": 4.74
  },
{
    "time": 8.611 ,
    "amplitude": 4.755
  },
{
    "time": 8.614 ,
    "amplitude": 4.755
  },
{
    "time": 8.617 ,
    "amplitude": 4.765
  },
{
    "time": 8.619 ,
    "amplitude": 4.765
  },
{
    "time": 8.622 ,
    "amplitude": 4.75
  },
{
    "time": 8.625 ,
    "amplitude": 4.745
  },
{
    "time": 8.628 ,
    "amplitude": 4.735
  },
{
    "time": 8.631 ,
    "amplitude": 4.745
  },
{
    "time": 8.633 ,
    "amplitude": 4.745
  },
{
    "time": 8.636 ,
    "amplitude": 4.745
  },
{
    "time": 8.639 ,
    "amplitude": 4.775
  },
{
    "time": 8.642 ,
    "amplitude": 4.775
  },
{
    "time": 8.644 ,
    "amplitude": 4.77
  },
{
    "time": 8.647 ,
    "amplitude": 4.77
  },
{
    "time": 8.65 ,
    "amplitude": 4.77
  },
{
    "time": 8.653 ,
    "amplitude": 4.765
  },
{
    "time": 8.656 ,
    "amplitude": 4.775
  },
{
    "time": 8.658 ,
    "amplitude": 4.765
  },
{
    "time": 8.661 ,
    "amplitude": 4.77
  },
{
    "time": 8.664 ,
    "amplitude": 4.765
  },
{
    "time": 8.667 ,
    "amplitude": 4.765
  },
{
    "time": 8.669 ,
    "amplitude": 4.75
  },
{
    "time": 8.672 ,
    "amplitude": 4.76
  },
{
    "time": 8.675 ,
    "amplitude": 4.755
  },
{
    "time": 8.678 ,
    "amplitude": 4.76
  },
{
    "time": 8.681 ,
    "amplitude": 4.77
  },
{
    "time": 8.683 ,
    "amplitude": 4.775
  },
{
    "time": 8.686 ,
    "amplitude": 4.76
  },
{
    "time": 8.689 ,
    "amplitude": 4.765
  },
{
    "time": 8.692 ,
    "amplitude": 4.745
  },
{
    "time": 8.694 ,
    "amplitude": 4.76
  },
{
    "time": 8.697 ,
    "amplitude": 4.765
  },
{
    "time": 8.7 ,
    "amplitude": 4.76
  },
{
    "time": 8.703 ,
    "amplitude": 4.755
  },
{
    "time": 8.706 ,
    "amplitude": 4.76
  },
{
    "time": 8.708 ,
    "amplitude": 4.755
  },
{
    "time": 8.711 ,
    "amplitude": 4.76
  },
{
    "time": 8.714 ,
    "amplitude": 4.77
  },
{
    "time": 8.717 ,
    "amplitude": 4.78
  },
{
    "time": 8.719 ,
    "amplitude": 4.785
  },
{
    "time": 8.722 ,
    "amplitude": 4.785
  },
{
    "time": 8.725 ,
    "amplitude": 4.77
  },
{
    "time": 8.728 ,
    "amplitude": 4.79
  },
{
    "time": 8.731 ,
    "amplitude": 4.81
  },
{
    "time": 8.733 ,
    "amplitude": 4.8
  },
{
    "time": 8.736 ,
    "amplitude": 4.81
  },
{
    "time": 8.739 ,
    "amplitude": 4.815
  },
{
    "time": 8.742 ,
    "amplitude": 4.8
  },
{
    "time": 8.744 ,
    "amplitude": 4.81
  },
{
    "time": 8.747 ,
    "amplitude": 4.835
  },
{
    "time": 8.75 ,
    "amplitude": 4.845
  },
{
    "time": 8.753 ,
    "amplitude": 4.855
  },
{
    "time": 8.756 ,
    "amplitude": 4.9
  },
{
    "time": 8.758 ,
    "amplitude": 4.93
  },
{
    "time": 8.761 ,
    "amplitude": 4.95
  },
{
    "time": 8.764 ,
    "amplitude": 4.935
  },
{
    "time": 8.767 ,
    "amplitude": 4.945
  },
{
    "time": 8.769 ,
    "amplitude": 4.965
  },
{
    "time": 8.772 ,
    "amplitude": 4.97
  },
{
    "time": 8.775 ,
    "amplitude": 4.965
  },
{
    "time": 8.778 ,
    "amplitude": 4.965
  },
{
    "time": 8.781 ,
    "amplitude": 4.975
  },
{
    "time": 8.783 ,
    "amplitude": 5
  },
{
    "time": 8.786 ,
    "amplitude": 5.02
  },
{
    "time": 8.789 ,
    "amplitude": 5.01
  },
{
    "time": 8.792 ,
    "amplitude": 4.98
  },
{
    "time": 8.794 ,
    "amplitude": 4.97
  },
{
    "time": 8.797 ,
    "amplitude": 4.935
  },
{
    "time": 8.8 ,
    "amplitude": 4.91
  },
{
    "time": 8.803 ,
    "amplitude": 4.875
  },
{
    "time": 8.806 ,
    "amplitude": 4.835
  },
{
    "time": 8.808 ,
    "amplitude": 4.795
  },
{
    "time": 8.811 ,
    "amplitude": 4.75
  },
{
    "time": 8.814 ,
    "amplitude": 4.725
  },
{
    "time": 8.817 ,
    "amplitude": 4.72
  },
{
    "time": 8.819 ,
    "amplitude": 4.7
  },
{
    "time": 8.822 ,
    "amplitude": 4.71
  },
{
    "time": 8.825 ,
    "amplitude": 4.705
  },
{
    "time": 8.828 ,
    "amplitude": 4.695
  },
{
    "time": 8.831 ,
    "amplitude": 4.715
  },
{
    "time": 8.833 ,
    "amplitude": 4.715
  },
{
    "time": 8.836 ,
    "amplitude": 4.715
  },
{
    "time": 8.839 ,
    "amplitude": 4.705
  },
{
    "time": 8.842 ,
    "amplitude": 4.695
  },
{
    "time": 8.844 ,
    "amplitude": 4.68
  },
{
    "time": 8.847 ,
    "amplitude": 4.68
  },
{
    "time": 8.85 ,
    "amplitude": 4.71
  },
{
    "time": 8.853 ,
    "amplitude": 4.725
  },
{
    "time": 8.856 ,
    "amplitude": 4.715
  },
{
    "time": 8.858 ,
    "amplitude": 4.69
  },
{
    "time": 8.861 ,
    "amplitude": 4.69
  },
{
    "time": 8.864 ,
    "amplitude": 4.695
  },
{
    "time": 8.867 ,
    "amplitude": 4.715
  },
{
    "time": 8.869 ,
    "amplitude": 4.7
  },
{
    "time": 8.872 ,
    "amplitude": 4.71
  },
{
    "time": 8.875 ,
    "amplitude": 4.715
  },
{
    "time": 8.878 ,
    "amplitude": 4.72
  },
{
    "time": 8.881 ,
    "amplitude": 4.72
  },
{
    "time": 8.883 ,
    "amplitude": 4.72
  },
{
    "time": 8.886 ,
    "amplitude": 4.7
  },
{
    "time": 8.889 ,
    "amplitude": 4.69
  },
{
    "time": 8.892 ,
    "amplitude": 4.68
  },
{
    "time": 8.894 ,
    "amplitude": 4.69
  },
{
    "time": 8.897 ,
    "amplitude": 4.7
  },
{
    "time": 8.9 ,
    "amplitude": 4.695
  },
{
    "time": 8.903 ,
    "amplitude": 4.71
  },
{
    "time": 8.906 ,
    "amplitude": 4.72
  },
{
    "time": 8.908 ,
    "amplitude": 4.7
  },
{
    "time": 8.911 ,
    "amplitude": 4.705
  },
{
    "time": 8.914 ,
    "amplitude": 4.705
  },
{
    "time": 8.917 ,
    "amplitude": 4.71
  },
{
    "time": 8.919 ,
    "amplitude": 4.695
  },
{
    "time": 8.922 ,
    "amplitude": 4.675
  },
{
    "time": 8.925 ,
    "amplitude": 4.645
  },
{
    "time": 8.928 ,
    "amplitude": 4.66
  },
{
    "time": 8.931 ,
    "amplitude": 4.7
  },
{
    "time": 8.933 ,
    "amplitude": 4.74
  },
{
    "time": 8.936 ,
    "amplitude": 4.73
  },
{
    "time": 8.939 ,
    "amplitude": 4.71
  },
{
    "time": 8.942 ,
    "amplitude": 4.715
  },
{
    "time": 8.944 ,
    "amplitude": 4.685
  },
{
    "time": 8.947 ,
    "amplitude": 4.615
  },
{
    "time": 8.95 ,
    "amplitude": 4.515
  },
{
    "time": 8.953 ,
    "amplitude": 4.47
  },
{
    "time": 8.956 ,
    "amplitude": 4.455
  },
{
    "time": 8.958 ,
    "amplitude": 4.455
  },
{
    "time": 8.961 ,
    "amplitude": 4.44
  },
{
    "time": 8.964 ,
    "amplitude": 4.43
  },
{
    "time": 8.967 ,
    "amplitude": 4.425
  },
{
    "time": 8.969 ,
    "amplitude": 4.38
  },
{
    "time": 8.972 ,
    "amplitude": 4.325
  },
{
    "time": 8.975 ,
    "amplitude": 4.275
  },
{
    "time": 8.978 ,
    "amplitude": 4.235
  },
{
    "time": 8.981 ,
    "amplitude": 4.22
  },
{
    "time": 8.983 ,
    "amplitude": 4.205
  },
{
    "time": 8.986 ,
    "amplitude": 4.155
  },
{
    "time": 8.989 ,
    "amplitude": 4.1
  },
{
    "time": 8.992 ,
    "amplitude": 4.05
  },
{
    "time": 8.994 ,
    "amplitude": 4.055
  },
{
    "time": 8.997 ,
    "amplitude": 4.075
  },
{
    "time": 9 ,
    "amplitude": 4.115
  },
{
    "time": 9.003 ,
    "amplitude": 4.165
  },
{
    "time": 9.006 ,
    "amplitude": 4.195
  },
{
    "time": 9.008 ,
    "amplitude": 4.205
  },
{
    "time": 9.011 ,
    "amplitude": 4.245
  },
{
    "time": 9.014 ,
    "amplitude": 4.33
  },
{
    "time": 9.017 ,
    "amplitude": 4.425
  },
{
    "time": 9.019 ,
    "amplitude": 4.49
  },
{
    "time": 9.022 ,
    "amplitude": 4.52
  },
{
    "time": 9.025 ,
    "amplitude": 4.545
  },
{
    "time": 9.028 ,
    "amplitude": 4.605
  },
{
    "time": 9.031 ,
    "amplitude": 4.68
  },
{
    "time": 9.033 ,
    "amplitude": 4.725
  },
{
    "time": 9.036 ,
    "amplitude": 4.74
  },
{
    "time": 9.039 ,
    "amplitude": 4.735
  },
{
    "time": 9.042 ,
    "amplitude": 4.735
  },
{
    "time": 9.044 ,
    "amplitude": 4.745
  },
{
    "time": 9.047 ,
    "amplitude": 4.76
  },
{
    "time": 9.05 ,
    "amplitude": 4.78
  },
{
    "time": 9.053 ,
    "amplitude": 4.79
  },
{
    "time": 9.056 ,
    "amplitude": 4.78
  },
{
    "time": 9.058 ,
    "amplitude": 4.77
  },
{
    "time": 9.061 ,
    "amplitude": 4.77
  },
{
    "time": 9.064 ,
    "amplitude": 4.79
  },
{
    "time": 9.067 ,
    "amplitude": 4.795
  },
{
    "time": 9.069 ,
    "amplitude": 4.79
  },
{
    "time": 9.072 ,
    "amplitude": 4.785
  },
{
    "time": 9.075 ,
    "amplitude": 4.785
  },
{
    "time": 9.078 ,
    "amplitude": 4.795
  },
{
    "time": 9.081 ,
    "amplitude": 4.815
  },
{
    "time": 9.083 ,
    "amplitude": 4.825
  },
{
    "time": 9.086 ,
    "amplitude": 4.825
  },
{
    "time": 9.089 ,
    "amplitude": 4.815
  },
{
    "time": 9.092 ,
    "amplitude": 4.8
  },
{
    "time": 9.094 ,
    "amplitude": 4.8
  },
{
    "time": 9.097 ,
    "amplitude": 4.79
  },
{
    "time": 9.1 ,
    "amplitude": 4.81
  },
{
    "time": 9.103 ,
    "amplitude": 4.815
  },
{
    "time": 9.106 ,
    "amplitude": 4.825
  },
{
    "time": 9.108 ,
    "amplitude": 4.81
  },
{
    "time": 9.111 ,
    "amplitude": 4.82
  },
{
    "time": 9.114 ,
    "amplitude": 4.82
  },
{
    "time": 9.117 ,
    "amplitude": 4.83
  },
{
    "time": 9.119 ,
    "amplitude": 4.84
  },
{
    "time": 9.122 ,
    "amplitude": 4.835
  },
{
    "time": 9.125 ,
    "amplitude": 4.83
  },
{
    "time": 9.128 ,
    "amplitude": 4.84
  },
{
    "time": 9.131 ,
    "amplitude": 4.855
  },
{
    "time": 9.133 ,
    "amplitude": 4.87
  },
{
    "time": 9.136 ,
    "amplitude": 4.86
  },
{
    "time": 9.139 ,
    "amplitude": 4.85
  },
{
    "time": 9.142 ,
    "amplitude": 4.84
  },
{
    "time": 9.144 ,
    "amplitude": 4.86
  },
{
    "time": 9.147 ,
    "amplitude": 4.865
  },
{
    "time": 9.15 ,
    "amplitude": 4.85
  },
{
    "time": 9.153 ,
    "amplitude": 4.855
  },
{
    "time": 9.156 ,
    "amplitude": 4.865
  },
{
    "time": 9.158 ,
    "amplitude": 4.875
  },
{
    "time": 9.161 ,
    "amplitude": 4.885
  },
{
    "time": 9.164 ,
    "amplitude": 4.88
  },
{
    "time": 9.167 ,
    "amplitude": 4.89
  },
{
    "time": 9.169 ,
    "amplitude": 4.91
  },
{
    "time": 9.172 ,
    "amplitude": 4.91
  },
{
    "time": 9.175 ,
    "amplitude": 4.9
  },
{
    "time": 9.178 ,
    "amplitude": 4.895
  },
{
    "time": 9.181 ,
    "amplitude": 4.905
  },
{
    "time": 9.183 ,
    "amplitude": 4.915
  },
{
    "time": 9.186 ,
    "amplitude": 4.915
  },
{
    "time": 9.189 ,
    "amplitude": 4.915
  },
{
    "time": 9.192 ,
    "amplitude": 4.91
  },
{
    "time": 9.194 ,
    "amplitude": 4.92
  },
{
    "time": 9.197 ,
    "amplitude": 4.91
  },
{
    "time": 9.2 ,
    "amplitude": 4.93
  },
{
    "time": 9.203 ,
    "amplitude": 4.93
  },
{
    "time": 9.206 ,
    "amplitude": 4.93
  },
{
    "time": 9.208 ,
    "amplitude": 4.92
  },
{
    "time": 9.211 ,
    "amplitude": 4.91
  },
{
    "time": 9.214 ,
    "amplitude": 4.905
  },
{
    "time": 9.217 ,
    "amplitude": 4.945
  },
{
    "time": 9.219 ,
    "amplitude": 4.965
  },
{
    "time": 9.222 ,
    "amplitude": 4.955
  },
{
    "time": 9.225 ,
    "amplitude": 4.935
  },
{
    "time": 9.228 ,
    "amplitude": 4.94
  },
{
    "time": 9.231 ,
    "amplitude": 4.955
  },
{
    "time": 9.233 ,
    "amplitude": 4.97
  },
{
    "time": 9.236 ,
    "amplitude": 4.97
  },
{
    "time": 9.239 ,
    "amplitude": 4.955
  },
{
    "time": 9.242 ,
    "amplitude": 4.94
  },
{
    "time": 9.244 ,
    "amplitude": 4.93
  },
{
    "time": 9.247 ,
    "amplitude": 4.94
  },
{
    "time": 9.25 ,
    "amplitude": 4.935
  },
{
    "time": 9.253 ,
    "amplitude": 4.91
  },
{
    "time": 9.256 ,
    "amplitude": 4.9
  },
{
    "time": 9.258 ,
    "amplitude": 4.885
  },
{
    "time": 9.261 ,
    "amplitude": 4.885
  },
{
    "time": 9.264 ,
    "amplitude": 4.89
  },
{
    "time": 9.267 ,
    "amplitude": 4.895
  },
{
    "time": 9.269 ,
    "amplitude": 4.88
  },
{
    "time": 9.272 ,
    "amplitude": 4.865
  },
{
    "time": 9.275 ,
    "amplitude": 4.855
  },
{
    "time": 9.278 ,
    "amplitude": 4.845
  },
{
    "time": 9.281 ,
    "amplitude": 4.855
  },
{
    "time": 9.283 ,
    "amplitude": 4.85
  },
{
    "time": 9.286 ,
    "amplitude": 4.835
  },
{
    "time": 9.289 ,
    "amplitude": 4.825
  },
{
    "time": 9.292 ,
    "amplitude": 4.81
  },
{
    "time": 9.294 ,
    "amplitude": 4.815
  },
{
    "time": 9.297 ,
    "amplitude": 4.82
  },
{
    "time": 9.3 ,
    "amplitude": 4.815
  },
{
    "time": 9.303 ,
    "amplitude": 4.815
  },
{
    "time": 9.306 ,
    "amplitude": 4.795
  },
{
    "time": 9.308 ,
    "amplitude": 4.755
  },
{
    "time": 9.311 ,
    "amplitude": 4.775
  },
{
    "time": 9.314 ,
    "amplitude": 4.79
  },
{
    "time": 9.317 ,
    "amplitude": 4.805
  },
{
    "time": 9.319 ,
    "amplitude": 4.785
  },
{
    "time": 9.322 ,
    "amplitude": 4.8
  },
{
    "time": 9.325 ,
    "amplitude": 4.77
  },
{
    "time": 9.328 ,
    "amplitude": 4.785
  },
{
    "time": 9.331 ,
    "amplitude": 4.78
  },
{
    "time": 9.333 ,
    "amplitude": 4.79
  },
{
    "time": 9.336 ,
    "amplitude": 4.78
  },
{
    "time": 9.339 ,
    "amplitude": 4.77
  },
{
    "time": 9.342 ,
    "amplitude": 4.765
  },
{
    "time": 9.344 ,
    "amplitude": 4.745
  },
{
    "time": 9.347 ,
    "amplitude": 4.76
  },
{
    "time": 9.35 ,
    "amplitude": 4.785
  },
{
    "time": 9.353 ,
    "amplitude": 4.785
  },
{
    "time": 9.356 ,
    "amplitude": 4.78
  },
{
    "time": 9.358 ,
    "amplitude": 4.76
  },
{
    "time": 9.361 ,
    "amplitude": 4.765
  },
{
    "time": 9.364 ,
    "amplitude": 4.76
  },
{
    "time": 9.367 ,
    "amplitude": 4.775
  },
{
    "time": 9.369 ,
    "amplitude": 4.77
  },
{
    "time": 9.372 ,
    "amplitude": 4.77
  },
{
    "time": 9.375 ,
    "amplitude": 4.755
  },
{
    "time": 9.378 ,
    "amplitude": 4.765
  },
{
    "time": 9.381 ,
    "amplitude": 4.76
  },
{
    "time": 9.383 ,
    "amplitude": 4.775
  },
{
    "time": 9.386 ,
    "amplitude": 4.765
  },
{
    "time": 9.389 ,
    "amplitude": 4.765
  },
{
    "time": 9.392 ,
    "amplitude": 4.755
  },
{
    "time": 9.394 ,
    "amplitude": 4.745
  },
{
    "time": 9.397 ,
    "amplitude": 4.755
  },
{
    "time": 9.4 ,
    "amplitude": 4.77
  },
{
    "time": 9.403 ,
    "amplitude": 4.76
  },
{
    "time": 9.406 ,
    "amplitude": 4.775
  },
{
    "time": 9.408 ,
    "amplitude": 4.75
  },
{
    "time": 9.411 ,
    "amplitude": 4.755
  },
{
    "time": 9.414 ,
    "amplitude": 4.77
  },
{
    "time": 9.417 ,
    "amplitude": 4.78
  },
{
    "time": 9.419 ,
    "amplitude": 4.77
  },
{
    "time": 9.422 ,
    "amplitude": 4.75
  },
{
    "time": 9.425 ,
    "amplitude": 4.735
  },
{
    "time": 9.428 ,
    "amplitude": 4.73
  },
{
    "time": 9.431 ,
    "amplitude": 4.745
  },
{
    "time": 9.433 ,
    "amplitude": 4.755
  },
{
    "time": 9.436 ,
    "amplitude": 4.745
  },
{
    "time": 9.439 ,
    "amplitude": 4.725
  },
{
    "time": 9.442 ,
    "amplitude": 4.715
  },
{
    "time": 9.444 ,
    "amplitude": 4.71
  },
{
    "time": 9.447 ,
    "amplitude": 4.715
  },
{
    "time": 9.45 ,
    "amplitude": 4.72
  },
{
    "time": 9.453 ,
    "amplitude": 4.72
  },
{
    "time": 9.456 ,
    "amplitude": 4.715
  },
{
    "time": 9.458 ,
    "amplitude": 4.695
  },
{
    "time": 9.461 ,
    "amplitude": 4.71
  },
{
    "time": 9.464 ,
    "amplitude": 4.715
  },
{
    "time": 9.467 ,
    "amplitude": 4.735
  },
{
    "time": 9.469 ,
    "amplitude": 4.725
  },
{
    "time": 9.472 ,
    "amplitude": 4.715
  },
{
    "time": 9.475 ,
    "amplitude": 4.71
  },
{
    "time": 9.478 ,
    "amplitude": 4.7
  },
{
    "time": 9.481 ,
    "amplitude": 4.71
  },
{
    "time": 9.483 ,
    "amplitude": 4.71
  },
{
    "time": 9.486 ,
    "amplitude": 4.715
  },
{
    "time": 9.489 ,
    "amplitude": 4.72
  },
{
    "time": 9.492 ,
    "amplitude": 4.71
  },
{
    "time": 9.494 ,
    "amplitude": 4.7
  },
{
    "time": 9.497 ,
    "amplitude": 4.705
  },
{
    "time": 9.5 ,
    "amplitude": 4.705
  },
{
    "time": 9.503 ,
    "amplitude": 4.69
  },
{
    "time": 9.506 ,
    "amplitude": 4.695
  },
{
    "time": 9.508 ,
    "amplitude": 4.69
  },
{
    "time": 9.511 ,
    "amplitude": 4.685
  },
{
    "time": 9.514 ,
    "amplitude": 4.695
  },
{
    "time": 9.517 ,
    "amplitude": 4.705
  },
{
    "time": 9.519 ,
    "amplitude": 4.71
  },
{
    "time": 9.522 ,
    "amplitude": 4.725
  },
{
    "time": 9.525 ,
    "amplitude": 4.71
  },
{
    "time": 9.528 ,
    "amplitude": 4.69
  },
{
    "time": 9.531 ,
    "amplitude": 4.67
  },
{
    "time": 9.533 ,
    "amplitude": 4.7
  },
{
    "time": 9.536 ,
    "amplitude": 4.695
  },
{
    "time": 9.539 ,
    "amplitude": 4.7
  },
{
    "time": 9.542 ,
    "amplitude": 4.685
  },
{
    "time": 9.544 ,
    "amplitude": 4.7
  },
{
    "time": 9.547 ,
    "amplitude": 4.695
  },
{
    "time": 9.55 ,
    "amplitude": 4.7
  },
{
    "time": 9.553 ,
    "amplitude": 4.69
  },
{
    "time": 9.556 ,
    "amplitude": 4.695
  },
{
    "time": 9.558 ,
    "amplitude": 4.695
  },
{
    "time": 9.561 ,
    "amplitude": 4.72
  },
{
    "time": 9.564 ,
    "amplitude": 4.725
  },
{
    "time": 9.567 ,
    "amplitude": 4.715
  },
{
    "time": 9.569 ,
    "amplitude": 4.71
  },
{
    "time": 9.572 ,
    "amplitude": 4.72
  },
{
    "time": 9.575 ,
    "amplitude": 4.725
  },
{
    "time": 9.578 ,
    "amplitude": 4.74
  },
{
    "time": 9.581 ,
    "amplitude": 4.75
  },
{
    "time": 9.583 ,
    "amplitude": 4.745
  },
{
    "time": 9.586 ,
    "amplitude": 4.735
  },
{
    "time": 9.589 ,
    "amplitude": 4.715
  },
{
    "time": 9.592 ,
    "amplitude": 4.71
  },
{
    "time": 9.594 ,
    "amplitude": 4.71
  },
{
    "time": 9.597 ,
    "amplitude": 4.715
  },
{
    "time": 9.6 ,
    "amplitude": 4.73
  },
{
    "time": 9.603 ,
    "amplitude": 4.725
  },
{
    "time": 9.606 ,
    "amplitude": 4.71
  },
{
    "time": 9.608 ,
    "amplitude": 4.7
  },
{
    "time": 9.611 ,
    "amplitude": 4.73
  },
{
    "time": 9.614 ,
    "amplitude": 4.735
  },
{
    "time": 9.617 ,
    "amplitude": 4.74
  },
{
    "time": 9.619 ,
    "amplitude": 4.745
  },
{
    "time": 9.622 ,
    "amplitude": 4.74
  },
{
    "time": 9.625 ,
    "amplitude": 4.725
  },
{
    "time": 9.628 ,
    "amplitude": 4.73
  },
{
    "time": 9.631 ,
    "amplitude": 4.735
  },
{
    "time": 9.633 ,
    "amplitude": 4.73
  },
{
    "time": 9.636 ,
    "amplitude": 4.72
  },
{
    "time": 9.639 ,
    "amplitude": 4.705
  },
{
    "time": 9.642 ,
    "amplitude": 4.72
  },
{
    "time": 9.644 ,
    "amplitude": 4.71
  },
{
    "time": 9.647 ,
    "amplitude": 4.725
  },
{
    "time": 9.65 ,
    "amplitude": 4.72
  },
{
    "time": 9.653 ,
    "amplitude": 4.725
  },
{
    "time": 9.656 ,
    "amplitude": 4.715
  },
{
    "time": 9.658 ,
    "amplitude": 4.725
  },
{
    "time": 9.661 ,
    "amplitude": 4.75
  },
{
    "time": 9.664 ,
    "amplitude": 4.755
  },
{
    "time": 9.667 ,
    "amplitude": 4.76
  },
{
    "time": 9.669 ,
    "amplitude": 4.75
  },
{
    "time": 9.672 ,
    "amplitude": 4.735
  },
{
    "time": 9.675 ,
    "amplitude": 4.725
  },
{
    "time": 9.678 ,
    "amplitude": 4.73
  },
{
    "time": 9.681 ,
    "amplitude": 4.745
  },
{
    "time": 9.683 ,
    "amplitude": 4.755
  },
{
    "time": 9.686 ,
    "amplitude": 4.745
  },
{
    "time": 9.689 ,
    "amplitude": 4.725
  },
{
    "time": 9.692 ,
    "amplitude": 4.73
  },
{
    "time": 9.694 ,
    "amplitude": 4.735
  },
{
    "time": 9.697 ,
    "amplitude": 4.745
  },
{
    "time": 9.7 ,
    "amplitude": 4.755
  },
{
    "time": 9.703 ,
    "amplitude": 4.76
  },
{
    "time": 9.706 ,
    "amplitude": 4.75
  },
{
    "time": 9.708 ,
    "amplitude": 4.74
  },
{
    "time": 9.711 ,
    "amplitude": 4.76
  },
{
    "time": 9.714 ,
    "amplitude": 4.8
  },
{
    "time": 9.717 ,
    "amplitude": 4.83
  },
{
    "time": 9.719 ,
    "amplitude": 4.835
  },
{
    "time": 9.722 ,
    "amplitude": 4.81
  },
{
    "time": 9.725 ,
    "amplitude": 4.81
  },
{
    "time": 9.728 ,
    "amplitude": 4.835
  },
{
    "time": 9.731 ,
    "amplitude": 4.86
  },
{
    "time": 9.733 ,
    "amplitude": 4.88
  },
{
    "time": 9.736 ,
    "amplitude": 4.9
  },
{
    "time": 9.739 ,
    "amplitude": 4.91
  },
{
    "time": 9.742 ,
    "amplitude": 4.915
  },
{
    "time": 9.744 ,
    "amplitude": 4.91
  },
{
    "time": 9.747 ,
    "amplitude": 4.935
  },
{
    "time": 9.75 ,
    "amplitude": 4.97
  },
{
    "time": 9.753 ,
    "amplitude": 4.985
  },
{
    "time": 9.756 ,
    "amplitude": 4.98
  },
{
    "time": 9.758 ,
    "amplitude": 4.96
  },
{
    "time": 9.761 ,
    "amplitude": 4.95
  },
{
    "time": 9.764 ,
    "amplitude": 4.975
  },
{
    "time": 9.767 ,
    "amplitude": 4.99
  },
{
    "time": 9.769 ,
    "amplitude": 4.995
  },
{
    "time": 9.772 ,
    "amplitude": 5
  },
{
    "time": 9.775 ,
    "amplitude": 4.99
  },
{
    "time": 9.778 ,
    "amplitude": 4.98
  },
{
    "time": 9.781 ,
    "amplitude": 4.94
  },
{
    "time": 9.783 ,
    "amplitude": 4.89
  },
{
    "time": 9.786 ,
    "amplitude": 4.85
  },
{
    "time": 9.789 ,
    "amplitude": 4.81
  },
{
    "time": 9.792 ,
    "amplitude": 4.765
  },
{
    "time": 9.794 ,
    "amplitude": 4.71
  },
{
    "time": 9.797 ,
    "amplitude": 4.695
  },
{
    "time": 9.8 ,
    "amplitude": 4.7
  },
{
    "time": 9.803 ,
    "amplitude": 4.71
  },
{
    "time": 9.806 ,
    "amplitude": 4.71
  },
{
    "time": 9.808 ,
    "amplitude": 4.71
  },
{
    "time": 9.811 ,
    "amplitude": 4.715
  },
{
    "time": 9.814 ,
    "amplitude": 4.725
  },
{
    "time": 9.817 ,
    "amplitude": 4.72
  },
{
    "time": 9.819 ,
    "amplitude": 4.72
  },
{
    "time": 9.822 ,
    "amplitude": 4.7
  },
{
    "time": 9.825 ,
    "amplitude": 4.705
  },
{
    "time": 9.828 ,
    "amplitude": 4.705
  },
{
    "time": 9.831 ,
    "amplitude": 4.7
  },
{
    "time": 9.833 ,
    "amplitude": 4.69
  },
{
    "time": 9.836 ,
    "amplitude": 4.68
  },
{
    "time": 9.839 ,
    "amplitude": 4.69
  },
{
    "time": 9.842 ,
    "amplitude": 4.7
  },
{
    "time": 9.844 ,
    "amplitude": 4.705
  },
{
    "time": 9.847 ,
    "amplitude": 4.72
  },
{
    "time": 9.85 ,
    "amplitude": 4.715
  },
{
    "time": 9.853 ,
    "amplitude": 4.71
  },
{
    "time": 9.856 ,
    "amplitude": 4.705
  },
{
    "time": 9.858 ,
    "amplitude": 4.705
  },
{
    "time": 9.861 ,
    "amplitude": 4.71
  },
{
    "time": 9.864 ,
    "amplitude": 4.72
  },
{
    "time": 9.867 ,
    "amplitude": 4.725
  },
{
    "time": 9.869 ,
    "amplitude": 4.715
  },
{
    "time": 9.872 ,
    "amplitude": 4.71
  },
{
    "time": 9.875 ,
    "amplitude": 4.7
  },
{
    "time": 9.878 ,
    "amplitude": 4.705
  },
{
    "time": 9.881 ,
    "amplitude": 4.71
  },
{
    "time": 9.883 ,
    "amplitude": 4.71
  },
{
    "time": 9.886 ,
    "amplitude": 4.72
  },
{
    "time": 9.889 ,
    "amplitude": 4.715
  },
{
    "time": 9.892 ,
    "amplitude": 4.695
  },
{
    "time": 9.894 ,
    "amplitude": 4.715
  },
{
    "time": 9.897 ,
    "amplitude": 4.73
  },
{
    "time": 9.9 ,
    "amplitude": 4.735
  },
{
    "time": 9.903 ,
    "amplitude": 4.73
  },
{
    "time": 9.906 ,
    "amplitude": 4.705
  },
{
    "time": 9.908 ,
    "amplitude": 4.685
  },
{
    "time": 9.911 ,
    "amplitude": 4.69
  },
{
    "time": 9.914 ,
    "amplitude": 4.735
  },
{
    "time": 9.917 ,
    "amplitude": 4.76
  },
{
    "time": 9.919 ,
    "amplitude": 4.755
  },
{
    "time": 9.922 ,
    "amplitude": 4.745
  },
{
    "time": 9.925 ,
    "amplitude": 4.735
  },
{
    "time": 9.928 ,
    "amplitude": 4.7
  },
{
    "time": 9.931 ,
    "amplitude": 4.615
  },
{
    "time": 9.933 ,
    "amplitude": 4.55
  },
{
    "time": 9.936 ,
    "amplitude": 4.5
  },
{
    "time": 9.939 ,
    "amplitude": 4.5
  },
{
    "time": 9.942 ,
    "amplitude": 4.485
  },
{
    "time": 9.944 ,
    "amplitude": 4.485
  },
{
    "time": 9.947 ,
    "amplitude": 4.475
  },
{
    "time": 9.95 ,
    "amplitude": 4.44
  },
{
    "time": 9.953 ,
    "amplitude": 4.395
  },
{
    "time": 9.956 ,
    "amplitude": 4.355
  },
{
    "time": 9.958 ,
    "amplitude": 4.335
  },
{
    "time": 9.961 ,
    "amplitude": 4.3
  },
{
    "time": 9.964 ,
    "amplitude": 4.295
  },
{
    "time": 9.967 ,
    "amplitude": 4.26
  },
{
    "time": 9.969 ,
    "amplitude": 4.225
  },
{
    "time": 9.972 ,
    "amplitude": 4.19
  },
{
    "time": 9.975 ,
    "amplitude": 4.16
  },
{
    "time": 9.978 ,
    "amplitude": 4.14
  },
{
    "time": 9.981 ,
    "amplitude": 4.135
  },
{
    "time": 9.983 ,
    "amplitude": 4.135
  },
{
    "time": 9.986 ,
    "amplitude": 4.18
  },
{
    "time": 9.989 ,
    "amplitude": 4.225
  },
{
    "time": 9.992 ,
    "amplitude": 4.24
  },
{
    "time": 9.994 ,
    "amplitude": 4.27
  },
{
    "time": 9.997 ,
    "amplitude": 4.34
  },
{
    "time": 10 ,
    "amplitude": 4.43
  },
{
    "time": 10.003 ,
    "amplitude": 4.495
  },
{
    "time": 10.006 ,
    "amplitude": 4.52
  },
{
    "time": 10.008 ,
    "amplitude": 4.545
  },
{
    "time": 10.011 ,
    "amplitude": 4.58
  },
{
    "time": 10.014 ,
    "amplitude": 4.635
  },
{
    "time": 10.017 ,
    "amplitude": 4.685
  },
{
    "time": 10.019 ,
    "amplitude": 4.75
  },
{
    "time": 10.022 ,
    "amplitude": 4.785
  },
{
    "time": 10.025 ,
    "amplitude": 4.785
  },
{
    "time": 10.028 ,
    "amplitude": 4.8
  },
{
    "time": 10.031 ,
    "amplitude": 4.815
  },
{
    "time": 10.033 ,
    "amplitude": 4.815
  },
{
    "time": 10.036 ,
    "amplitude": 4.815
  },
{
    "time": 10.039 ,
    "amplitude": 4.8
  },
{
    "time": 10.042 ,
    "amplitude": 4.79
  },
{
    "time": 10.044 ,
    "amplitude": 4.78
  },
{
    "time": 10.047 ,
    "amplitude": 4.805
  },
{
    "time": 10.05 ,
    "amplitude": 4.83
  },
{
    "time": 10.053 ,
    "amplitude": 4.845
  },
{
    "time": 10.056 ,
    "amplitude": 4.84
  },
{
    "time": 10.058 ,
    "amplitude": 4.825
  },
{
    "time": 10.061 ,
    "amplitude": 4.825
  },
{
    "time": 10.064 ,
    "amplitude": 4.835
  },
{
    "time": 10.067 ,
    "amplitude": 4.85
  },
{
    "time": 10.069 ,
    "amplitude": 4.855
  },
{
    "time": 10.072 ,
    "amplitude": 4.86
  },
{
    "time": 10.075 ,
    "amplitude": 4.845
  },
{
    "time": 10.078 ,
    "amplitude": 4.855
  },
{
    "time": 10.081 ,
    "amplitude": 4.85
  },
{
    "time": 10.083 ,
    "amplitude": 4.845
  },
{
    "time": 10.086 ,
    "amplitude": 4.845
  },
{
    "time": 10.089 ,
    "amplitude": 4.85
  },
{
    "time": 10.092 ,
    "amplitude": 4.85
  },
{
    "time": 10.094 ,
    "amplitude": 4.86
  },
{
    "time": 10.097 ,
    "amplitude": 4.855
  },
{
    "time": 10.1 ,
    "amplitude": 4.865
  },
{
    "time": 10.103 ,
    "amplitude": 4.87
  },
{
    "time": 10.106 ,
    "amplitude": 4.855
  },
{
    "time": 10.108 ,
    "amplitude": 4.85
  },
{
    "time": 10.111 ,
    "amplitude": 4.86
  },
{
    "time": 10.114 ,
    "amplitude": 4.875
  },
{
    "time": 10.117 ,
    "amplitude": 4.865
  },
{
    "time": 10.119 ,
    "amplitude": 4.86
  },
{
    "time": 10.122 ,
    "amplitude": 4.87
  },
{
    "time": 10.125 ,
    "amplitude": 4.87
  },
{
    "time": 10.128 ,
    "amplitude": 4.895
  },
{
    "time": 10.131 ,
    "amplitude": 4.905
  },
{
    "time": 10.133 ,
    "amplitude": 4.905
  },
{
    "time": 10.136 ,
    "amplitude": 4.9
  },
{
    "time": 10.139 ,
    "amplitude": 4.895
  },
{
    "time": 10.142 ,
    "amplitude": 4.9
  },
{
    "time": 10.144 ,
    "amplitude": 4.925
  },
{
    "time": 10.147 ,
    "amplitude": 4.91
  },
{
    "time": 10.15 ,
    "amplitude": 4.91
  },
{
    "time": 10.153 ,
    "amplitude": 4.91
  },
{
    "time": 10.156 ,
    "amplitude": 4.915
  },
{
    "time": 10.158 ,
    "amplitude": 4.91
  },
{
    "time": 10.161 ,
    "amplitude": 4.915
  },
{
    "time": 10.164 ,
    "amplitude": 4.935
  },
{
    "time": 10.167 ,
    "amplitude": 4.94
  },
{
    "time": 10.169 ,
    "amplitude": 4.95
  },
{
    "time": 10.172 ,
    "amplitude": 4.945
  },
{
    "time": 10.175 ,
    "amplitude": 4.94
  },
{
    "time": 10.178 ,
    "amplitude": 4.945
  },
{
    "time": 10.181 ,
    "amplitude": 4.96
  },
{
    "time": 10.183 ,
    "amplitude": 4.965
  },
{
    "time": 10.186 ,
    "amplitude": 4.965
  },
{
    "time": 10.189 ,
    "amplitude": 4.96
  },
{
    "time": 10.192 ,
    "amplitude": 4.965
  },
{
    "time": 10.194 ,
    "amplitude": 4.965
  },
{
    "time": 10.197 ,
    "amplitude": 4.97
  },
{
    "time": 10.2 ,
    "amplitude": 4.975
  },
{
    "time": 10.203 ,
    "amplitude": 4.975
  },
{
    "time": 10.206 ,
    "amplitude": 4.965
  },
{
    "time": 10.208 ,
    "amplitude": 4.955
  },
{
    "time": 10.211 ,
    "amplitude": 4.95
  },
{
    "time": 10.214 ,
    "amplitude": 4.98
  },
{
    "time": 10.217 ,
    "amplitude": 4.99
  },
{
    "time": 10.219 ,
    "amplitude": 4.985
  },
{
    "time": 10.222 ,
    "amplitude": 4.97
  },
{
    "time": 10.225 ,
    "amplitude": 4.955
  },
{
    "time": 10.228 ,
    "amplitude": 4.965
  },
{
    "time": 10.231 ,
    "amplitude": 4.96
  },
{
    "time": 10.233 ,
    "amplitude": 4.95
  },
{
    "time": 10.236 ,
    "amplitude": 4.945
  },
{
    "time": 10.239 ,
    "amplitude": 4.935
  },
{
    "time": 10.242 ,
    "amplitude": 4.92
  },
{
    "time": 10.244 ,
    "amplitude": 4.93
  },
{
    "time": 10.247 ,
    "amplitude": 4.92
  },
{
    "time": 10.25 ,
    "amplitude": 4.92
  },
{
    "time": 10.253 ,
    "amplitude": 4.915
  },
{
    "time": 10.256 ,
    "amplitude": 4.91
  },
{
    "time": 10.258 ,
    "amplitude": 4.895
  },
{
    "time": 10.261 ,
    "amplitude": 4.895
  },
{
    "time": 10.264 ,
    "amplitude": 4.895
  },
{
    "time": 10.267 ,
    "amplitude": 4.905
  },
{
    "time": 10.269 ,
    "amplitude": 4.89
  },
{
    "time": 10.272 ,
    "amplitude": 4.885
  },
{
    "time": 10.275 ,
    "amplitude": 4.87
  },
{
    "time": 10.278 ,
    "amplitude": 4.87
  },
{
    "time": 10.281 ,
    "amplitude": 4.875
  },
{
    "time": 10.283 ,
    "amplitude": 4.875
  },
{
    "time": 10.286 ,
    "amplitude": 4.865
  },
{
    "time": 10.289 ,
    "amplitude": 4.855
  },
{
    "time": 10.292 ,
    "amplitude": 4.84
  },
{
    "time": 10.294 ,
    "amplitude": 4.85
  },
{
    "time": 10.297 ,
    "amplitude": 4.855
  },
{
    "time": 10.3 ,
    "amplitude": 4.87
  },
{
    "time": 10.303 ,
    "amplitude": 4.87
  },
{
    "time": 10.306 ,
    "amplitude": 4.855
  },
{
    "time": 10.308 ,
    "amplitude": 4.84
  },
{
    "time": 10.311 ,
    "amplitude": 4.845
  },
{
    "time": 10.314 ,
    "amplitude": 4.855
  },
{
    "time": 10.317 ,
    "amplitude": 4.86
  },
{
    "time": 10.319 ,
    "amplitude": 4.845
  },
{
    "time": 10.322 ,
    "amplitude": 4.835
  },
{
    "time": 10.325 ,
    "amplitude": 4.83
  },
{
    "time": 10.328 ,
    "amplitude": 4.84
  },
{
    "time": 10.331 ,
    "amplitude": 4.86
  },
{
    "time": 10.333 ,
    "amplitude": 4.865
  },
{
    "time": 10.336 ,
    "amplitude": 4.855
  },
{
    "time": 10.339 ,
    "amplitude": 4.855
  },
{
    "time": 10.342 ,
    "amplitude": 4.85
  },
{
    "time": 10.344 ,
    "amplitude": 4.84
  },
{
    "time": 10.347 ,
    "amplitude": 4.85
  },
{
    "time": 10.35 ,
    "amplitude": 4.865
  },
{
    "time": 10.353 ,
    "amplitude": 4.855
  },
{
    "time": 10.356 ,
    "amplitude": 4.84
  },
{
    "time": 10.358 ,
    "amplitude": 4.835
  },
{
    "time": 10.361 ,
    "amplitude": 4.83
  },
{
    "time": 10.364 ,
    "amplitude": 4.835
  },
{
    "time": 10.367 ,
    "amplitude": 4.845
  },
{
    "time": 10.369 ,
    "amplitude": 4.845
  },
{
    "time": 10.372 ,
    "amplitude": 4.845
  },
{
    "time": 10.375 ,
    "amplitude": 4.84
  },
{
    "time": 10.378 ,
    "amplitude": 4.85
  },
{
    "time": 10.381 ,
    "amplitude": 4.85
  },
{
    "time": 10.383 ,
    "amplitude": 4.85
  },
{
    "time": 10.386 ,
    "amplitude": 4.845
  },
{
    "time": 10.389 ,
    "amplitude": 4.82
  },
{
    "time": 10.392 ,
    "amplitude": 4.83
  },
{
    "time": 10.394 ,
    "amplitude": 4.825
  },
{
    "time": 10.397 ,
    "amplitude": 4.84
  },
{
    "time": 10.4 ,
    "amplitude": 4.84
  },
{
    "time": 10.403 ,
    "amplitude": 4.82
  },
{
    "time": 10.406 ,
    "amplitude": 4.8
  },
{
    "time": 10.408 ,
    "amplitude": 4.8
  },
{
    "time": 10.411 ,
    "amplitude": 4.81
  },
{
    "time": 10.414 ,
    "amplitude": 4.825
  },
{
    "time": 10.417 ,
    "amplitude": 4.82
  },
{
    "time": 10.419 ,
    "amplitude": 4.81
  },
{
    "time": 10.422 ,
    "amplitude": 4.815
  },
{
    "time": 10.425 ,
    "amplitude": 4.8
  },
{
    "time": 10.428 ,
    "amplitude": 4.8
  },
{
    "time": 10.431 ,
    "amplitude": 4.79
  },
{
    "time": 10.433 ,
    "amplitude": 4.795
  },
{
    "time": 10.436 ,
    "amplitude": 4.795
  },
{
    "time": 10.439 ,
    "amplitude": 4.8
  },
{
    "time": 10.442 ,
    "amplitude": 4.775
  },
{
    "time": 10.444 ,
    "amplitude": 4.795
  },
{
    "time": 10.447 ,
    "amplitude": 4.805
  },
{
    "time": 10.45 ,
    "amplitude": 4.81
  },
{
    "time": 10.453 ,
    "amplitude": 4.805
  },
{
    "time": 10.456 ,
    "amplitude": 4.78
  },
{
    "time": 10.458 ,
    "amplitude": 4.785
  },
{
    "time": 10.461 ,
    "amplitude": 4.785
  },
{
    "time": 10.464 ,
    "amplitude": 4.795
  },
{
    "time": 10.467 ,
    "amplitude": 4.795
  },
{
    "time": 10.469 ,
    "amplitude": 4.78
  },
{
    "time": 10.472 ,
    "amplitude": 4.78
  },
{
    "time": 10.475 ,
    "amplitude": 4.77
  },
{
    "time": 10.478 ,
    "amplitude": 4.77
  },
{
    "time": 10.481 ,
    "amplitude": 4.79
  },
{
    "time": 10.483 ,
    "amplitude": 4.8
  },
{
    "time": 10.486 ,
    "amplitude": 4.815
  },
{
    "time": 10.489 ,
    "amplitude": 4.79
  },
{
    "time": 10.492 ,
    "amplitude": 4.78
  },
{
    "time": 10.494 ,
    "amplitude": 4.8
  },
{
    "time": 10.497 ,
    "amplitude": 4.815
  },
{
    "time": 10.5 ,
    "amplitude": 4.82
  },
{
    "time": 10.503 ,
    "amplitude": 4.81
  },
{
    "time": 10.506 ,
    "amplitude": 4.795
  },
{
    "time": 10.508 ,
    "amplitude": 4.795
  },
{
    "time": 10.511 ,
    "amplitude": 4.79
  },
{
    "time": 10.514 ,
    "amplitude": 4.81
  },
{
    "time": 10.517 ,
    "amplitude": 4.825
  },
{
    "time": 10.519 ,
    "amplitude": 4.815
  },
{
    "time": 10.522 ,
    "amplitude": 4.8
  },
{
    "time": 10.525 ,
    "amplitude": 4.775
  },
{
    "time": 10.528 ,
    "amplitude": 4.81
  },
{
    "time": 10.531 ,
    "amplitude": 4.805
  },
{
    "time": 10.533 ,
    "amplitude": 4.805
  },
{
    "time": 10.536 ,
    "amplitude": 4.81
  },
{
    "time": 10.539 ,
    "amplitude": 4.815
  },
{
    "time": 10.542 ,
    "amplitude": 4.805
  },
{
    "time": 10.544 ,
    "amplitude": 4.81
  },
{
    "time": 10.547 ,
    "amplitude": 4.82
  },
{
    "time": 10.55 ,
    "amplitude": 4.825
  },
{
    "time": 10.553 ,
    "amplitude": 4.815
  },
{
    "time": 10.556 ,
    "amplitude": 4.82
  },
{
    "time": 10.558 ,
    "amplitude": 4.8
  },
{
    "time": 10.561 ,
    "amplitude": 4.805
  },
{
    "time": 10.564 ,
    "amplitude": 4.81
  },
{
    "time": 10.567 ,
    "amplitude": 4.825
  },
{
    "time": 10.569 ,
    "amplitude": 4.82
  },
{
    "time": 10.572 ,
    "amplitude": 4.8
  },
{
    "time": 10.575 ,
    "amplitude": 4.8
  },
{
    "time": 10.578 ,
    "amplitude": 4.795
  },
{
    "time": 10.581 ,
    "amplitude": 4.815
  },
{
    "time": 10.583 ,
    "amplitude": 4.83
  },
{
    "time": 10.586 ,
    "amplitude": 4.84
  },
{
    "time": 10.589 ,
    "amplitude": 4.825
  },
{
    "time": 10.592 ,
    "amplitude": 4.81
  },
{
    "time": 10.594 ,
    "amplitude": 4.815
  },
{
    "time": 10.597 ,
    "amplitude": 4.835
  },
{
    "time": 10.6 ,
    "amplitude": 4.84
  },
{
    "time": 10.603 ,
    "amplitude": 4.84
  },
{
    "time": 10.606 ,
    "amplitude": 4.825
  },
{
    "time": 10.608 ,
    "amplitude": 4.81
  },
{
    "time": 10.611 ,
    "amplitude": 4.835
  },
{
    "time": 10.614 ,
    "amplitude": 4.835
  },
{
    "time": 10.617 ,
    "amplitude": 4.855
  },
{
    "time": 10.619 ,
    "amplitude": 4.845
  },
{
    "time": 10.622 ,
    "amplitude": 4.84
  },
{
    "time": 10.625 ,
    "amplitude": 4.835
  },
{
    "time": 10.628 ,
    "amplitude": 4.835
  },
{
    "time": 10.631 ,
    "amplitude": 4.85
  },
{
    "time": 10.633 ,
    "amplitude": 4.86
  },
{
    "time": 10.636 ,
    "amplitude": 4.855
  },
{
    "time": 10.639 ,
    "amplitude": 4.86
  },
{
    "time": 10.642 ,
    "amplitude": 4.865
  },
{
    "time": 10.644 ,
    "amplitude": 4.865
  },
{
    "time": 10.647 ,
    "amplitude": 4.905
  },
{
    "time": 10.65 ,
    "amplitude": 4.91
  },
{
    "time": 10.653 ,
    "amplitude": 4.905
  },
{
    "time": 10.656 ,
    "amplitude": 4.9
  },
{
    "time": 10.658 ,
    "amplitude": 4.9
  },
{
    "time": 10.661 ,
    "amplitude": 4.915
  },
{
    "time": 10.664 ,
    "amplitude": 4.93
  },
{
    "time": 10.667 ,
    "amplitude": 4.95
  },
{
    "time": 10.669 ,
    "amplitude": 4.98
  },
{
    "time": 10.672 ,
    "amplitude": 4.99
  },
{
    "time": 10.675 ,
    "amplitude": 5
  },
{
    "time": 10.678 ,
    "amplitude": 5.02
  },
{
    "time": 10.681 ,
    "amplitude": 5.04
  },
{
    "time": 10.683 ,
    "amplitude": 5.055
  },
{
    "time": 10.686 ,
    "amplitude": 5.06
  },
{
    "time": 10.689 ,
    "amplitude": 5.06
  },
{
    "time": 10.692 ,
    "amplitude": 5.05
  },
{
    "time": 10.694 ,
    "amplitude": 5.06
  },
{
    "time": 10.697 ,
    "amplitude": 5.085
  },
{
    "time": 10.7 ,
    "amplitude": 5.11
  },
{
    "time": 10.703 ,
    "amplitude": 5.085
  },
{
    "time": 10.706 ,
    "amplitude": 5.085
  },
{
    "time": 10.708 ,
    "amplitude": 5.055
  },
{
    "time": 10.711 ,
    "amplitude": 5.01
  },
{
    "time": 10.714 ,
    "amplitude": 4.98
  },
{
    "time": 10.717 ,
    "amplitude": 4.94
  },
{
    "time": 10.719 ,
    "amplitude": 4.92
  },
{
    "time": 10.722 ,
    "amplitude": 4.865
  },
{
    "time": 10.725 ,
    "amplitude": 4.82
  },
{
    "time": 10.728 ,
    "amplitude": 4.805
  },
{
    "time": 10.731 ,
    "amplitude": 4.805
  },
{
    "time": 10.733 ,
    "amplitude": 4.82
  },
{
    "time": 10.736 ,
    "amplitude": 4.815
  },
{
    "time": 10.739 ,
    "amplitude": 4.805
  },
{
    "time": 10.742 ,
    "amplitude": 4.81
  },
{
    "time": 10.744 ,
    "amplitude": 4.815
  },
{
    "time": 10.747 ,
    "amplitude": 4.83
  },
{
    "time": 10.75 ,
    "amplitude": 4.82
  },
{
    "time": 10.753 ,
    "amplitude": 4.805
  },
{
    "time": 10.756 ,
    "amplitude": 4.8
  },
{
    "time": 10.758 ,
    "amplitude": 4.8
  },
{
    "time": 10.761 ,
    "amplitude": 4.8
  },
{
    "time": 10.764 ,
    "amplitude": 4.815
  },
{
    "time": 10.767 ,
    "amplitude": 4.805
  },
{
    "time": 10.769 ,
    "amplitude": 4.8
  },
{
    "time": 10.772 ,
    "amplitude": 4.8
  },
{
    "time": 10.775 ,
    "amplitude": 4.805
  },
{
    "time": 10.778 ,
    "amplitude": 4.815
  },
{
    "time": 10.781 ,
    "amplitude": 4.83
  },
{
    "time": 10.783 ,
    "amplitude": 4.84
  },
{
    "time": 10.786 ,
    "amplitude": 4.82
  },
{
    "time": 10.789 ,
    "amplitude": 4.8
  },
{
    "time": 10.792 ,
    "amplitude": 4.81
  },
{
    "time": 10.794 ,
    "amplitude": 4.825
  },
{
    "time": 10.797 ,
    "amplitude": 4.825
  },
{
    "time": 10.8 ,
    "amplitude": 4.83
  },
{
    "time": 10.803 ,
    "amplitude": 4.82
  },
{
    "time": 10.806 ,
    "amplitude": 4.81
  },
{
    "time": 10.808 ,
    "amplitude": 4.8
  },
{
    "time": 10.811 ,
    "amplitude": 4.815
  },
{
    "time": 10.814 ,
    "amplitude": 4.825
  },
{
    "time": 10.817 ,
    "amplitude": 4.825
  },
{
    "time": 10.819 ,
    "amplitude": 4.81
  },
{
    "time": 10.822 ,
    "amplitude": 4.81
  },
{
    "time": 10.825 ,
    "amplitude": 4.8
  },
{
    "time": 10.828 ,
    "amplitude": 4.825
  },
{
    "time": 10.831 ,
    "amplitude": 4.835
  },
{
    "time": 10.833 ,
    "amplitude": 4.825
  },
{
    "time": 10.836 ,
    "amplitude": 4.8
  },
{
    "time": 10.839 ,
    "amplitude": 4.79
  },
{
    "time": 10.842 ,
    "amplitude": 4.805
  },
{
    "time": 10.844 ,
    "amplitude": 4.84
  },
{
    "time": 10.847 ,
    "amplitude": 4.85
  },
{
    "time": 10.85 ,
    "amplitude": 4.865
  },
{
    "time": 10.853 ,
    "amplitude": 4.85
  },
{
    "time": 10.856 ,
    "amplitude": 4.77
  },
{
    "time": 10.858 ,
    "amplitude": 4.69
  },
{
    "time": 10.861 ,
    "amplitude": 4.625
  },
{
    "time": 10.864 ,
    "amplitude": 4.61
  },
{
    "time": 10.867 ,
    "amplitude": 4.605
  },
{
    "time": 10.869 ,
    "amplitude": 4.605
  },
{
    "time": 10.872 ,
    "amplitude": 4.59
  },
{
    "time": 10.875 ,
    "amplitude": 4.54
  },
{
    "time": 10.878 ,
    "amplitude": 4.5
  },
{
    "time": 10.881 ,
    "amplitude": 4.465
  },
{
    "time": 10.883 ,
    "amplitude": 4.445
  },
{
    "time": 10.886 ,
    "amplitude": 4.4
  },
{
    "time": 10.889 ,
    "amplitude": 4.355
  },
{
    "time": 10.892 ,
    "amplitude": 4.29
  },
{
    "time": 10.894 ,
    "amplitude": 4.27
  },
{
    "time": 10.897 ,
    "amplitude": 4.24
  },
{
    "time": 10.9 ,
    "amplitude": 4.245
  },
{
    "time": 10.903 ,
    "amplitude": 4.235
  },
{
    "time": 10.906 ,
    "amplitude": 4.255
  },
{
    "time": 10.908 ,
    "amplitude": 4.28
  },
{
    "time": 10.911 ,
    "amplitude": 4.335
  },
{
    "time": 10.914 ,
    "amplitude": 4.36
  },
{
    "time": 10.917 ,
    "amplitude": 4.415
  },
{
    "time": 10.919 ,
    "amplitude": 4.49
  },
{
    "time": 10.922 ,
    "amplitude": 4.585
  },
{
    "time": 10.925 ,
    "amplitude": 4.62
  },
{
    "time": 10.928 ,
    "amplitude": 4.675
  },
{
    "time": 10.931 ,
    "amplitude": 4.72
  },
{
    "time": 10.933 ,
    "amplitude": 4.77
  },
{
    "time": 10.936 ,
    "amplitude": 4.82
  },
{
    "time": 10.939 ,
    "amplitude": 4.865
  },
{
    "time": 10.942 ,
    "amplitude": 4.865
  },
{
    "time": 10.944 ,
    "amplitude": 4.895
  },
{
    "time": 10.947 ,
    "amplitude": 4.905
  },
{
    "time": 10.95 ,
    "amplitude": 4.905
  },
{
    "time": 10.953 ,
    "amplitude": 4.915
  },
{
    "time": 10.956 ,
    "amplitude": 4.9
  },
{
    "time": 10.958 ,
    "amplitude": 4.89
  },
{
    "time": 10.961 ,
    "amplitude": 4.91
  },
{
    "time": 10.964 ,
    "amplitude": 4.92
  },
{
    "time": 10.967 ,
    "amplitude": 4.94
  },
{
    "time": 10.969 ,
    "amplitude": 4.94
  },
{
    "time": 10.972 ,
    "amplitude": 4.92
  },
{
    "time": 10.975 ,
    "amplitude": 4.915
  },
{
    "time": 10.978 ,
    "amplitude": 4.925
  },
{
    "time": 10.981 ,
    "amplitude": 4.93
  },
{
    "time": 10.983 ,
    "amplitude": 4.945
  },
{
    "time": 10.986 ,
    "amplitude": 4.945
  },
{
    "time": 10.989 ,
    "amplitude": 4.95
  },
{
    "time": 10.992 ,
    "amplitude": 4.94
  },
{
    "time": 10.994 ,
    "amplitude": 4.95
  },
{
    "time": 10.997 ,
    "amplitude": 4.96
  },
{
    "time": 11 ,
    "amplitude": 4.95
  },
{
    "time": 11.003 ,
    "amplitude": 4.955
  },
{
    "time": 11.006 ,
    "amplitude": 4.955
  },
{
    "time": 11.008 ,
    "amplitude": 4.94
  },
{
    "time": 11.011 ,
    "amplitude": 4.94
  },
{
    "time": 11.014 ,
    "amplitude": 4.935
  },
{
    "time": 11.017 ,
    "amplitude": 4.96
  },
{
    "time": 11.019 ,
    "amplitude": 4.96
  },
{
    "time": 11.022 ,
    "amplitude": 4.965
  },
{
    "time": 11.025 ,
    "amplitude": 4.95
  },
{
    "time": 11.028 ,
    "amplitude": 4.955
  },
{
    "time": 11.031 ,
    "amplitude": 4.96
  },
{
    "time": 11.033 ,
    "amplitude": 4.98
  },
{
    "time": 11.036 ,
    "amplitude": 4.98
  },
{
    "time": 11.039 ,
    "amplitude": 4.98
  },
{
    "time": 11.042 ,
    "amplitude": 4.975
  },
{
    "time": 11.044 ,
    "amplitude": 4.995
  },
{
    "time": 11.047 ,
    "amplitude": 5.01
  },
{
    "time": 11.05 ,
    "amplitude": 5.005
  },
{
    "time": 11.053 ,
    "amplitude": 5.015
  },
{
    "time": 11.056 ,
    "amplitude": 4.995
  },
{
    "time": 11.058 ,
    "amplitude": 4.995
  },
{
    "time": 11.061 ,
    "amplitude": 5.005
  },
{
    "time": 11.064 ,
    "amplitude": 5.025
  },
{
    "time": 11.067 ,
    "amplitude": 5.04
  },
{
    "time": 11.069 ,
    "amplitude": 5.035
  },
{
    "time": 11.072 ,
    "amplitude": 5.025
  },
{
    "time": 11.075 ,
    "amplitude": 5.035
  },
{
    "time": 11.078 ,
    "amplitude": 5.045
  },
{
    "time": 11.081 ,
    "amplitude": 5.065
  },
{
    "time": 11.083 ,
    "amplitude": 5.07
  },
{
    "time": 11.086 ,
    "amplitude": 5.07
  },
{
    "time": 11.089 ,
    "amplitude": 5.05
  },
{
    "time": 11.092 ,
    "amplitude": 5.045
  },
{
    "time": 11.094 ,
    "amplitude": 5.075
  },
{
    "time": 11.097 ,
    "amplitude": 5.08
  },
{
    "time": 11.1 ,
    "amplitude": 5.075
  },
{
    "time": 11.103 ,
    "amplitude": 5.07
  },
{
    "time": 11.106 ,
    "amplitude": 5.075
  },
{
    "time": 11.108 ,
    "amplitude": 5.085
  },
{
    "time": 11.111 ,
    "amplitude": 5.09
  },
{
    "time": 11.114 ,
    "amplitude": 5.11
  },
{
    "time": 11.117 ,
    "amplitude": 5.11
  },
{
    "time": 11.119 ,
    "amplitude": 5.105
  },
{
    "time": 11.122 ,
    "amplitude": 5.09
  },
{
    "time": 11.125 ,
    "amplitude": 5.065
  },
{
    "time": 11.128 ,
    "amplitude": 5.065
  },
{
    "time": 11.131 ,
    "amplitude": 5.08
  },
{
    "time": 11.133 ,
    "amplitude": 5.085
  },
{
    "time": 11.136 ,
    "amplitude": 5.07
  },
{
    "time": 11.139 ,
    "amplitude": 5.06
  },
{
    "time": 11.142 ,
    "amplitude": 5.035
  },
{
    "time": 11.144 ,
    "amplitude": 5.035
  },
{
    "time": 11.147 ,
    "amplitude": 5.055
  },
{
    "time": 11.15 ,
    "amplitude": 5.045
  },
{
    "time": 11.153 ,
    "amplitude": 5.04
  },
{
    "time": 11.156 ,
    "amplitude": 5.025
  },
{
    "time": 11.158 ,
    "amplitude": 5.005
  },
{
    "time": 11.161 ,
    "amplitude": 4.99
  },
{
    "time": 11.164 ,
    "amplitude": 4.99
  },
{
    "time": 11.167 ,
    "amplitude": 4.99
  },
{
    "time": 11.169 ,
    "amplitude": 4.97
  },
{
    "time": 11.172 ,
    "amplitude": 4.965
  },
{
    "time": 11.175 ,
    "amplitude": 4.925
  },
{
    "time": 11.178 ,
    "amplitude": 4.95
  },
{
    "time": 11.181 ,
    "amplitude": 4.955
  },
{
    "time": 11.183 ,
    "amplitude": 4.965
  },
{
    "time": 11.186 ,
    "amplitude": 4.96
  },
{
    "time": 11.189 ,
    "amplitude": 4.945
  },
{
    "time": 11.192 ,
    "amplitude": 4.94
  },
{
    "time": 11.194 ,
    "amplitude": 4.94
  },
{
    "time": 11.197 ,
    "amplitude": 4.935
  },
{
    "time": 11.2 ,
    "amplitude": 4.94
  },
{
    "time": 11.203 ,
    "amplitude": 4.93
  },
{
    "time": 11.206 ,
    "amplitude": 4.93
  },
{
    "time": 11.208 ,
    "amplitude": 4.95
  },
{
    "time": 11.211 ,
    "amplitude": 4.93
  },
{
    "time": 11.214 ,
    "amplitude": 4.93
  },
{
    "time": 11.217 ,
    "amplitude": 4.93
  },
{
    "time": 11.219 ,
    "amplitude": 4.93
  },
{
    "time": 11.222 ,
    "amplitude": 4.915
  },
{
    "time": 11.225 ,
    "amplitude": 4.915
  },
{
    "time": 11.228 ,
    "amplitude": 4.915
  },
{
    "time": 11.231 ,
    "amplitude": 4.925
  },
{
    "time": 11.233 ,
    "amplitude": 4.935
  },
{
    "time": 11.236 ,
    "amplitude": 4.94
  },
{
    "time": 11.239 ,
    "amplitude": 4.93
  },
{
    "time": 11.242 ,
    "amplitude": 4.91
  },
{
    "time": 11.244 ,
    "amplitude": 4.905
  },
{
    "time": 11.247 ,
    "amplitude": 4.92
  },
{
    "time": 11.25 ,
    "amplitude": 4.925
  },
{
    "time": 11.253 ,
    "amplitude": 4.91
  },
{
    "time": 11.256 ,
    "amplitude": 4.91
  },
{
    "time": 11.258 ,
    "amplitude": 4.88
  },
{
    "time": 11.261 ,
    "amplitude": 4.9
  },
{
    "time": 11.264 ,
    "amplitude": 4.91
  },
{
    "time": 11.267 ,
    "amplitude": 4.905
  },
{
    "time": 11.269 ,
    "amplitude": 4.91
  },
{
    "time": 11.272 ,
    "amplitude": 4.895
  },
{
    "time": 11.275 ,
    "amplitude": 4.87
  },
{
    "time": 11.278 ,
    "amplitude": 4.89
  },
{
    "time": 11.281 ,
    "amplitude": 4.895
  },
{
    "time": 11.283 ,
    "amplitude": 4.9
  },
{
    "time": 11.286 ,
    "amplitude": 4.895
  },
{
    "time": 11.289 ,
    "amplitude": 4.89
  },
{
    "time": 11.292 ,
    "amplitude": 4.87
  },
{
    "time": 11.294 ,
    "amplitude": 4.875
  },
{
    "time": 11.297 ,
    "amplitude": 4.88
  },
{
    "time": 11.3 ,
    "amplitude": 4.88
  },
{
    "time": 11.303 ,
    "amplitude": 4.875
  },
{
    "time": 11.306 ,
    "amplitude": 4.87
  },
{
    "time": 11.308 ,
    "amplitude": 4.87
  },
{
    "time": 11.311 ,
    "amplitude": 4.885
  },
{
    "time": 11.314 ,
    "amplitude": 4.9
  },
{
    "time": 11.317 ,
    "amplitude": 4.875
  },
{
    "time": 11.319 ,
    "amplitude": 4.85
  },
{
    "time": 11.322 ,
    "amplitude": 4.85
  },
{
    "time": 11.325 ,
    "amplitude": 4.855
  },
{
    "time": 11.328 ,
    "amplitude": 4.865
  },
{
    "time": 11.331 ,
    "amplitude": 4.875
  },
{
    "time": 11.333 ,
    "amplitude": 4.87
  },
{
    "time": 11.336 ,
    "amplitude": 4.85
  },
{
    "time": 11.339 ,
    "amplitude": 4.815
  },
{
    "time": 11.342 ,
    "amplitude": 4.765
  },
{
    "time": 11.344 ,
    "amplitude": 4.73
  },
{
    "time": 11.347 ,
    "amplitude": 4.705
  },
{
    "time": 11.35 ,
    "amplitude": 4.695
  },
{
    "time": 11.353 ,
    "amplitude": 4.67
  },
{
    "time": 11.356 ,
    "amplitude": 4.66
  },
{
    "time": 11.358 ,
    "amplitude": 4.665
  },
{
    "time": 11.361 ,
    "amplitude": 4.695
  },
{
    "time": 11.364 ,
    "amplitude": 4.73
  },
{
    "time": 11.367 ,
    "amplitude": 4.765
  },
{
    "time": 11.369 ,
    "amplitude": 4.83
  },
{
    "time": 11.372 ,
    "amplitude": 4.895
  },
{
    "time": 11.375 ,
    "amplitude": 4.935
  },
{
    "time": 11.378 ,
    "amplitude": 4.995
  },
{
    "time": 11.381 ,
    "amplitude": 5.055
  },
{
    "time": 11.383 ,
    "amplitude": 5.11
  },
{
    "time": 11.386 ,
    "amplitude": 5.155
  },
{
    "time": 11.389 ,
    "amplitude": 5.185
  },
{
    "time": 11.392 ,
    "amplitude": 5.25
  },
{
    "time": 11.394 ,
    "amplitude": 5.34
  },
{
    "time": 11.397 ,
    "amplitude": 5.375
  },
{
    "time": 11.4 ,
    "amplitude": 5.31
  },
{
    "time": 11.403 ,
    "amplitude": 5.25
  },
{
    "time": 11.406 ,
    "amplitude": 5.265
  },
{
    "time": 11.408 ,
    "amplitude": 5.33
  },
{
    "time": 11.411 ,
    "amplitude": 5.365
  },
{
    "time": 11.414 ,
    "amplitude": 5.325
  },
{
    "time": 11.417 ,
    "amplitude": 5.24
  },
{
    "time": 11.419 ,
    "amplitude": 5.155
  },
{
    "time": 11.422 ,
    "amplitude": 5.09
  },
{
    "time": 11.425 ,
    "amplitude": 4.975
  },
{
    "time": 11.428 ,
    "amplitude": 4.81
  },
{
    "time": 11.431 ,
    "amplitude": 4.64
  },
{
    "time": 11.433 ,
    "amplitude": 4.54
  },
{
    "time": 11.436 ,
    "amplitude": 4.53
  },
{
    "time": 11.439 ,
    "amplitude": 4.595
  },
{
    "time": 11.442 ,
    "amplitude": 4.7
  },
{
    "time": 11.444 ,
    "amplitude": 4.795
  },
{
    "time": 11.447 ,
    "amplitude": 4.835
  },
{
    "time": 11.45 ,
    "amplitude": 4.83
  },
{
    "time": 11.453 ,
    "amplitude": 4.825
  },
{
    "time": 11.456 ,
    "amplitude": 4.805
  },
{
    "time": 11.458 ,
    "amplitude": 4.785
  },
{
    "time": 11.461 ,
    "amplitude": 4.775
  },
{
    "time": 11.464 ,
    "amplitude": 4.795
  },
{
    "time": 11.467 ,
    "amplitude": 4.8
  },
{
    "time": 11.469 ,
    "amplitude": 4.805
  },
{
    "time": 11.472 ,
    "amplitude": 4.79
  },
{
    "time": 11.475 ,
    "amplitude": 4.775
  },
{
    "time": 11.478 ,
    "amplitude": 4.795
  },
{
    "time": 11.481 ,
    "amplitude": 4.79
  },
{
    "time": 11.483 ,
    "amplitude": 4.79
  },
{
    "time": 11.486 ,
    "amplitude": 4.775
  },
{
    "time": 11.489 ,
    "amplitude": 4.785
  },
{
    "time": 11.492 ,
    "amplitude": 4.775
  },
{
    "time": 11.494 ,
    "amplitude": 4.78
  },
{
    "time": 11.497 ,
    "amplitude": 4.79
  },
{
    "time": 11.5 ,
    "amplitude": 4.795
  },
{
    "time": 11.503 ,
    "amplitude": 4.795
  },
{
    "time": 11.506 ,
    "amplitude": 4.775
  },
{
    "time": 11.508 ,
    "amplitude": 4.76
  },
{
    "time": 11.511 ,
    "amplitude": 4.77
  },
{
    "time": 11.514 ,
    "amplitude": 4.78
  },
{
    "time": 11.517 ,
    "amplitude": 4.78
  },
{
    "time": 11.519 ,
    "amplitude": 4.775
  },
{
    "time": 11.522 ,
    "amplitude": 4.755
  },
{
    "time": 11.525 ,
    "amplitude": 4.755
  },
{
    "time": 11.528 ,
    "amplitude": 4.74
  },
{
    "time": 11.531 ,
    "amplitude": 4.755
  },
{
    "time": 11.533 ,
    "amplitude": 4.765
  },
{
    "time": 11.536 ,
    "amplitude": 4.76
  },
{
    "time": 11.539 ,
    "amplitude": 4.75
  },
{
    "time": 11.542 ,
    "amplitude": 4.755
  },
{
    "time": 11.544 ,
    "amplitude": 4.75
  },
{
    "time": 11.547 ,
    "amplitude": 4.775
  },
{
    "time": 11.55 ,
    "amplitude": 4.76
  },
{
    "time": 11.553 ,
    "amplitude": 4.76
  },
{
    "time": 11.556 ,
    "amplitude": 4.76
  },
{
    "time": 11.558 ,
    "amplitude": 4.77
  },
{
    "time": 11.561 ,
    "amplitude": 4.77
  },
{
    "time": 11.564 ,
    "amplitude": 4.785
  },
{
    "time": 11.567 ,
    "amplitude": 4.805
  },
{
    "time": 11.569 ,
    "amplitude": 4.82
  },
{
    "time": 11.572 ,
    "amplitude": 4.815
  },
{
    "time": 11.575 ,
    "amplitude": 4.805
  },
{
    "time": 11.578 ,
    "amplitude": 4.815
  },
{
    "time": 11.581 ,
    "amplitude": 4.835
  },
{
    "time": 11.583 ,
    "amplitude": 4.84
  },
{
    "time": 11.586 ,
    "amplitude": 4.845
  },
{
    "time": 11.589 ,
    "amplitude": 4.845
  },
{
    "time": 11.592 ,
    "amplitude": 4.88
  },
{
    "time": 11.594 ,
    "amplitude": 4.905
  },
{
    "time": 11.597 ,
    "amplitude": 4.935
  },
{
    "time": 11.6 ,
    "amplitude": 4.93
  },
{
    "time": 11.603 ,
    "amplitude": 4.935
  },
{
    "time": 11.606 ,
    "amplitude": 4.94
  },
{
    "time": 11.608 ,
    "amplitude": 4.95
  },
{
    "time": 11.611 ,
    "amplitude": 4.95
  },
{
    "time": 11.614 ,
    "amplitude": 4.945
  },
{
    "time": 11.617 ,
    "amplitude": 4.955
  },
{
    "time": 11.619 ,
    "amplitude": 4.96
  },
{
    "time": 11.622 ,
    "amplitude": 4.965
  },
{
    "time": 11.625 ,
    "amplitude": 4.985
  },
{
    "time": 11.628 ,
    "amplitude": 5
  },
{
    "time": 11.631 ,
    "amplitude": 5
  },
{
    "time": 11.633 ,
    "amplitude": 4.96
  },
{
    "time": 11.636 ,
    "amplitude": 4.91
  },
{
    "time": 11.639 ,
    "amplitude": 4.86
  },
{
    "time": 11.642 ,
    "amplitude": 4.82
  },
{
    "time": 11.644 ,
    "amplitude": 4.81
  },
{
    "time": 11.647 ,
    "amplitude": 4.775
  },
{
    "time": 11.65 ,
    "amplitude": 4.745
  },
{
    "time": 11.653 ,
    "amplitude": 4.7
  },
{
    "time": 11.656 ,
    "amplitude": 4.675
  },
{
    "time": 11.658 ,
    "amplitude": 4.665
  },
{
    "time": 11.661 ,
    "amplitude": 4.695
  },
{
    "time": 11.664 ,
    "amplitude": 4.7
  },
{
    "time": 11.667 ,
    "amplitude": 4.715
  },
{
    "time": 11.669 ,
    "amplitude": 4.705
  },
{
    "time": 11.672 ,
    "amplitude": 4.7
  },
{
    "time": 11.675 ,
    "amplitude": 4.7
  },
{
    "time": 11.678 ,
    "amplitude": 4.695
  },
{
    "time": 11.681 ,
    "amplitude": 4.71
  },
{
    "time": 11.683 ,
    "amplitude": 4.725
  },
{
    "time": 11.686 ,
    "amplitude": 4.725
  },
{
    "time": 11.689 ,
    "amplitude": 4.72
  },
{
    "time": 11.692 ,
    "amplitude": 4.715
  },
{
    "time": 11.694 ,
    "amplitude": 4.725
  },
{
    "time": 11.697 ,
    "amplitude": 4.735
  },
{
    "time": 11.7 ,
    "amplitude": 4.74
  },
{
    "time": 11.703 ,
    "amplitude": 4.74
  },
{
    "time": 11.706 ,
    "amplitude": 4.745
  },
{
    "time": 11.708 ,
    "amplitude": 4.755
  },
{
    "time": 11.711 ,
    "amplitude": 4.755
  },
{
    "time": 11.714 ,
    "amplitude": 4.78
  },
{
    "time": 11.717 ,
    "amplitude": 4.785
  },
{
    "time": 11.719 ,
    "amplitude": 4.785
  },
{
    "time": 11.722 ,
    "amplitude": 4.775
  },
{
    "time": 11.725 ,
    "amplitude": 4.77
  },
{
    "time": 11.728 ,
    "amplitude": 4.775
  },
{
    "time": 11.731 ,
    "amplitude": 4.785
  },
{
    "time": 11.733 ,
    "amplitude": 4.805
  },
{
    "time": 11.736 ,
    "amplitude": 4.795
  },
{
    "time": 11.739 ,
    "amplitude": 4.8
  },
{
    "time": 11.742 ,
    "amplitude": 4.805
  },
{
    "time": 11.744 ,
    "amplitude": 4.8
  },
{
    "time": 11.747 ,
    "amplitude": 4.795
  },
{
    "time": 11.75 ,
    "amplitude": 4.795
  },
{
    "time": 11.753 ,
    "amplitude": 4.81
  },
{
    "time": 11.756 ,
    "amplitude": 4.815
  },
{
    "time": 11.758 ,
    "amplitude": 4.8
  },
{
    "time": 11.761 ,
    "amplitude": 4.805
  },
{
    "time": 11.764 ,
    "amplitude": 4.805
  },
{
    "time": 11.767 ,
    "amplitude": 4.805
  },
{
    "time": 11.769 ,
    "amplitude": 4.805
  },
{
    "time": 11.772 ,
    "amplitude": 4.805
  },
{
    "time": 11.775 ,
    "amplitude": 4.79
  },
{
    "time": 11.778 ,
    "amplitude": 4.795
  },
{
    "time": 11.781 ,
    "amplitude": 4.795
  },
{
    "time": 11.783 ,
    "amplitude": 4.805
  },
{
    "time": 11.786 ,
    "amplitude": 4.8
  },
{
    "time": 11.789 ,
    "amplitude": 4.785
  },
{
    "time": 11.792 ,
    "amplitude": 4.785
  },
{
    "time": 11.794 ,
    "amplitude": 4.8
  },
{
    "time": 11.797 ,
    "amplitude": 4.815
  },
{
    "time": 11.8 ,
    "amplitude": 4.82
  },
{
    "time": 11.803 ,
    "amplitude": 4.825
  },
{
    "time": 11.806 ,
    "amplitude": 4.81
  },
{
    "time": 11.808 ,
    "amplitude": 4.8
  },
{
    "time": 11.811 ,
    "amplitude": 4.81
  },
{
    "time": 11.814 ,
    "amplitude": 4.815
  },
{
    "time": 11.817 ,
    "amplitude": 4.81
  },
{
    "time": 11.819 ,
    "amplitude": 4.81
  },
{
    "time": 11.822 ,
    "amplitude": 4.805
  },
{
    "time": 11.825 ,
    "amplitude": 4.805
  },
{
    "time": 11.828 ,
    "amplitude": 4.815
  },
{
    "time": 11.831 ,
    "amplitude": 4.835
  },
{
    "time": 11.833 ,
    "amplitude": 4.845
  },
{
    "time": 11.836 ,
    "amplitude": 4.84
  },
{
    "time": 11.839 ,
    "amplitude": 4.825
  },
{
    "time": 11.842 ,
    "amplitude": 4.825
  },
{
    "time": 11.844 ,
    "amplitude": 4.82
  },
{
    "time": 11.847 ,
    "amplitude": 4.84
  },
{
    "time": 11.85 ,
    "amplitude": 4.845
  },
{
    "time": 11.853 ,
    "amplitude": 4.84
  },
{
    "time": 11.856 ,
    "amplitude": 4.825
  },
{
    "time": 11.858 ,
    "amplitude": 4.83
  },
{
    "time": 11.861 ,
    "amplitude": 4.835
  },
{
    "time": 11.864 ,
    "amplitude": 4.84
  },
{
    "time": 11.867 ,
    "amplitude": 4.835
  },
{
    "time": 11.869 ,
    "amplitude": 4.855
  },
{
    "time": 11.872 ,
    "amplitude": 4.87
  },
{
    "time": 11.875 ,
    "amplitude": 4.85
  },
{
    "time": 11.878 ,
    "amplitude": 4.84
  },
{
    "time": 11.881 ,
    "amplitude": 4.855
  },
{
    "time": 11.883 ,
    "amplitude": 4.875
  },
{
    "time": 11.886 ,
    "amplitude": 4.855
  },
{
    "time": 11.889 ,
    "amplitude": 4.85
  },
{
    "time": 11.892 ,
    "amplitude": 4.855
  },
{
    "time": 11.894 ,
    "amplitude": 4.865
  },
{
    "time": 11.897 ,
    "amplitude": 4.885
  },
{
    "time": 11.9 ,
    "amplitude": 4.895
  },
{
    "time": 11.903 ,
    "amplitude": 4.875
  },
{
    "time": 11.906 ,
    "amplitude": 4.865
  },
{
    "time": 11.908 ,
    "amplitude": 4.86
  },
{
    "time": 11.911 ,
    "amplitude": 4.875
  },
{
    "time": 11.914 ,
    "amplitude": 4.88
  },
{
    "time": 11.917 ,
    "amplitude": 4.895
  },
{
    "time": 11.919 ,
    "amplitude": 4.88
  },
{
    "time": 11.922 ,
    "amplitude": 4.89
  },
{
    "time": 11.925 ,
    "amplitude": 4.89
  },
{
    "time": 11.928 ,
    "amplitude": 4.895
  },
{
    "time": 11.931 ,
    "amplitude": 4.89
  },
{
    "time": 11.933 ,
    "amplitude": 4.87
  },
{
    "time": 11.936 ,
    "amplitude": 4.855
  },
{
    "time": 11.939 ,
    "amplitude": 4.86
  },
{
    "time": 11.942 ,
    "amplitude": 4.865
  },
{
    "time": 11.944 ,
    "amplitude": 4.885
  },
{
    "time": 11.947 ,
    "amplitude": 4.905
  },
{
    "time": 11.95 ,
    "amplitude": 4.91
  },
{
    "time": 11.953 ,
    "amplitude": 4.895
  },
{
    "time": 11.956 ,
    "amplitude": 4.88
  },
{
    "time": 11.958 ,
    "amplitude": 4.86
  },
{
    "time": 11.961 ,
    "amplitude": 4.88
  },
{
    "time": 11.964 ,
    "amplitude": 4.88
  },
{
    "time": 11.967 ,
    "amplitude": 4.885
  },
{
    "time": 11.969 ,
    "amplitude": 4.89
  },
{
    "time": 11.972 ,
    "amplitude": 4.9
  },
{
    "time": 11.975 ,
    "amplitude": 4.9
  },
{
    "time": 11.978 ,
    "amplitude": 4.89
  },
{
    "time": 11.981 ,
    "amplitude": 4.885
  },
{
    "time": 11.983 ,
    "amplitude": 4.89
  },
{
    "time": 11.986 ,
    "amplitude": 4.89
  },
{
    "time": 11.989 ,
    "amplitude": 4.88
  },
{
    "time": 11.992 ,
    "amplitude": 4.87
  },
{
    "time": 11.994 ,
    "amplitude": 4.875
  },
{
    "time": 11.997 ,
    "amplitude": 4.89
  },
{
    "time": 12 ,
    "amplitude": 4.89
  },
{
    "time": 12.003 ,
    "amplitude": 4.89
  },
{
    "time": 12.006 ,
    "amplitude": 4.885
  },
{
    "time": 12.008 ,
    "amplitude": 4.865
  },
{
    "time": 12.011 ,
    "amplitude": 4.895
  },
{
    "time": 12.014 ,
    "amplitude": 4.89
  },
{
    "time": 12.017 ,
    "amplitude": 4.91
  },
{
    "time": 12.019 ,
    "amplitude": 4.915
  },
{
    "time": 12.022 ,
    "amplitude": 4.91
  },
{
    "time": 12.025 ,
    "amplitude": 4.9
  },
{
    "time": 12.028 ,
    "amplitude": 4.9
  },
{
    "time": 12.031 ,
    "amplitude": 4.925
  },
{
    "time": 12.033 ,
    "amplitude": 4.93
  },
{
    "time": 12.036 ,
    "amplitude": 4.92
  },
{
    "time": 12.039 ,
    "amplitude": 4.92
  },
{
    "time": 12.042 ,
    "amplitude": 4.915
  },
{
    "time": 12.044 ,
    "amplitude": 4.915
  },
{
    "time": 12.047 ,
    "amplitude": 4.915
  },
{
    "time": 12.05 ,
    "amplitude": 4.93
  },
{
    "time": 12.053 ,
    "amplitude": 4.925
  },
{
    "time": 12.056 ,
    "amplitude": 4.93
  },
{
    "time": 12.058 ,
    "amplitude": 4.92
  },
{
    "time": 12.061 ,
    "amplitude": 4.905
  },
{
    "time": 12.064 ,
    "amplitude": 4.91
  },
{
    "time": 12.067 ,
    "amplitude": 4.925
  },
{
    "time": 12.069 ,
    "amplitude": 4.925
  },
{
    "time": 12.072 ,
    "amplitude": 4.92
  },
{
    "time": 12.075 ,
    "amplitude": 4.915
  },
{
    "time": 12.078 ,
    "amplitude": 4.92
  },
{
    "time": 12.081 ,
    "amplitude": 4.93
  },
{
    "time": 12.083 ,
    "amplitude": 4.935
  },
{
    "time": 12.086 ,
    "amplitude": 4.93
  },
{
    "time": 12.089 ,
    "amplitude": 4.935
  },
{
    "time": 12.092 ,
    "amplitude": 4.925
  },
{
    "time": 12.094 ,
    "amplitude": 4.92
  },
{
    "time": 12.097 ,
    "amplitude": 4.915
  },
{
    "time": 12.1 ,
    "amplitude": 4.925
  },
{
    "time": 12.103 ,
    "amplitude": 4.93
  },
{
    "time": 12.106 ,
    "amplitude": 4.94
  },
{
    "time": 12.108 ,
    "amplitude": 4.915
  },
{
    "time": 12.111 ,
    "amplitude": 4.92
  },
{
    "time": 12.114 ,
    "amplitude": 4.92
  },
{
    "time": 12.117 ,
    "amplitude": 4.925
  },
{
    "time": 12.119 ,
    "amplitude": 4.92
  },
{
    "time": 12.122 ,
    "amplitude": 4.915
  },
{
    "time": 12.125 ,
    "amplitude": 4.9
  },
{
    "time": 12.128 ,
    "amplitude": 4.905
  },
{
    "time": 12.131 ,
    "amplitude": 4.925
  },
{
    "time": 12.133 ,
    "amplitude": 4.94
  },
{
    "time": 12.136 ,
    "amplitude": 4.965
  },
{
    "time": 12.139 ,
    "amplitude": 4.965
  },
{
    "time": 12.142 ,
    "amplitude": 4.945
  },
{
    "time": 12.144 ,
    "amplitude": 4.935
  },
{
    "time": 12.147 ,
    "amplitude": 4.94
  },
{
    "time": 12.15 ,
    "amplitude": 4.955
  },
{
    "time": 12.153 ,
    "amplitude": 4.94
  },
{
    "time": 12.156 ,
    "amplitude": 4.92
  },
{
    "time": 12.158 ,
    "amplitude": 4.92
  },
{
    "time": 12.161 ,
    "amplitude": 4.925
  },
{
    "time": 12.164 ,
    "amplitude": 4.93
  },
{
    "time": 12.167 ,
    "amplitude": 4.93
  },
{
    "time": 12.169 ,
    "amplitude": 4.935
  },
{
    "time": 12.172 ,
    "amplitude": 4.94
  },
{
    "time": 12.175 ,
    "amplitude": 4.93
  },
{
    "time": 12.178 ,
    "amplitude": 4.93
  },
{
    "time": 12.181 ,
    "amplitude": 4.925
  },
{
    "time": 12.183 ,
    "amplitude": 4.925
  },
{
    "time": 12.186 ,
    "amplitude": 4.925
  },
{
    "time": 12.189 ,
    "amplitude": 4.925
  },
{
    "time": 12.192 ,
    "amplitude": 4.925
  },
{
    "time": 12.194 ,
    "amplitude": 4.945
  },
{
    "time": 12.197 ,
    "amplitude": 4.95
  },
{
    "time": 12.2 ,
    "amplitude": 4.945
  },
{
    "time": 12.203 ,
    "amplitude": 4.93
  },
{
    "time": 12.206 ,
    "amplitude": 4.93
  },
{
    "time": 12.208 ,
    "amplitude": 4.925
  },
{
    "time": 12.211 ,
    "amplitude": 4.93
  },
{
    "time": 12.214 ,
    "amplitude": 4.93
  },
{
    "time": 12.217 ,
    "amplitude": 4.94
  },
{
    "time": 12.219 ,
    "amplitude": 4.935
  },
{
    "time": 12.222 ,
    "amplitude": 4.925
  },
{
    "time": 12.225 ,
    "amplitude": 4.925
  },
{
    "time": 12.228 ,
    "amplitude": 4.935
  },
{
    "time": 12.231 ,
    "amplitude": 4.94
  },
{
    "time": 12.233 ,
    "amplitude": 4.94
  },
{
    "time": 12.236 ,
    "amplitude": 4.95
  },
{
    "time": 12.239 ,
    "amplitude": 4.935
  },
{
    "time": 12.242 ,
    "amplitude": 4.935
  },
{
    "time": 12.244 ,
    "amplitude": 4.945
  },
{
    "time": 12.247 ,
    "amplitude": 4.95
  },
{
    "time": 12.25 ,
    "amplitude": 4.96
  },
{
    "time": 12.253 ,
    "amplitude": 4.935
  },
{
    "time": 12.256 ,
    "amplitude": 4.94
  },
{
    "time": 12.258 ,
    "amplitude": 4.91
  },
{
    "time": 12.261 ,
    "amplitude": 4.915
  },
{
    "time": 12.264 ,
    "amplitude": 4.94
  },
{
    "time": 12.267 ,
    "amplitude": 4.935
  },
{
    "time": 12.269 ,
    "amplitude": 4.94
  },
{
    "time": 12.272 ,
    "amplitude": 4.93
  },
{
    "time": 12.275 ,
    "amplitude": 4.935
  },
{
    "time": 12.278 ,
    "amplitude": 4.94
  },
{
    "time": 12.281 ,
    "amplitude": 4.95
  },
{
    "time": 12.283 ,
    "amplitude": 4.945
  },
{
    "time": 12.286 ,
    "amplitude": 4.945
  },
{
    "time": 12.289 ,
    "amplitude": 4.94
  },
{
    "time": 12.292 ,
    "amplitude": 4.94
  },
{
    "time": 12.294 ,
    "amplitude": 4.945
  },
{
    "time": 12.297 ,
    "amplitude": 4.94
  },
{
    "time": 12.3 ,
    "amplitude": 4.915
  },
{
    "time": 12.303 ,
    "amplitude": 4.94
  },
{
    "time": 12.306 ,
    "amplitude": 4.92
  },
{
    "time": 12.308 ,
    "amplitude": 4.925
  },
{
    "time": 12.311 ,
    "amplitude": 4.935
  },
{
    "time": 12.314 ,
    "amplitude": 4.94
  },
{
    "time": 12.317 ,
    "amplitude": 4.95
  },
{
    "time": 12.319 ,
    "amplitude": 4.95
  },
{
    "time": 12.322 ,
    "amplitude": 4.94
  },
{
    "time": 12.325 ,
    "amplitude": 4.94
  },
{
    "time": 12.328 ,
    "amplitude": 4.955
  },
{
    "time": 12.331 ,
    "amplitude": 4.96
  },
{
    "time": 12.333 ,
    "amplitude": 4.945
  },
{
    "time": 12.336 ,
    "amplitude": 4.93
  },
{
    "time": 12.339 ,
    "amplitude": 4.93
  },
{
    "time": 12.342 ,
    "amplitude": 4.93
  },
{
    "time": 12.344 ,
    "amplitude": 4.93
  },
{
    "time": 12.347 ,
    "amplitude": 4.945
  },
{
    "time": 12.35 ,
    "amplitude": 4.95
  },
{
    "time": 12.353 ,
    "amplitude": 4.945
  },
{
    "time": 12.356 ,
    "amplitude": 4.935
  },
{
    "time": 12.358 ,
    "amplitude": 4.92
  },
{
    "time": 12.361 ,
    "amplitude": 4.93
  },
{
    "time": 12.364 ,
    "amplitude": 4.95
  },
{
    "time": 12.367 ,
    "amplitude": 4.95
  },
{
    "time": 12.369 ,
    "amplitude": 4.96
  },
{
    "time": 12.372 ,
    "amplitude": 4.95
  },
{
    "time": 12.375 ,
    "amplitude": 4.925
  },
{
    "time": 12.378 ,
    "amplitude": 4.935
  },
{
    "time": 12.381 ,
    "amplitude": 4.945
  },
{
    "time": 12.383 ,
    "amplitude": 4.945
  },
{
    "time": 12.386 ,
    "amplitude": 4.95
  },
{
    "time": 12.389 ,
    "amplitude": 4.95
  },
{
    "time": 12.392 ,
    "amplitude": 4.925
  },
{
    "time": 12.394 ,
    "amplitude": 4.915
  },
{
    "time": 12.397 ,
    "amplitude": 4.93
  },
{
    "time": 12.4 ,
    "amplitude": 4.945
  },
{
    "time": 12.403 ,
    "amplitude": 4.93
  },
{
    "time": 12.406 ,
    "amplitude": 4.93
  },
{
    "time": 12.408 ,
    "amplitude": 4.93
  },
{
    "time": 12.411 ,
    "amplitude": 4.935
  },
{
    "time": 12.414 ,
    "amplitude": 4.935
  },
{
    "time": 12.417 ,
    "amplitude": 4.96
  },
{
    "time": 12.419 ,
    "amplitude": 4.945
  },
{
    "time": 12.422 ,
    "amplitude": 4.935
  },
{
    "time": 12.425 ,
    "amplitude": 4.935
  },
{
    "time": 12.428 ,
    "amplitude": 4.945
  },
{
    "time": 12.431 ,
    "amplitude": 4.95
  },
{
    "time": 12.433 ,
    "amplitude": 4.96
  },
{
    "time": 12.436 ,
    "amplitude": 4.955
  },
{
    "time": 12.439 ,
    "amplitude": 4.95
  },
{
    "time": 12.442 ,
    "amplitude": 4.94
  },
{
    "time": 12.444 ,
    "amplitude": 4.94
  },
{
    "time": 12.447 ,
    "amplitude": 4.935
  },
{
    "time": 12.45 ,
    "amplitude": 4.955
  },
{
    "time": 12.453 ,
    "amplitude": 4.945
  },
{
    "time": 12.456 ,
    "amplitude": 4.93
  },
{
    "time": 12.458 ,
    "amplitude": 4.94
  },
{
    "time": 12.461 ,
    "amplitude": 4.935
  },
{
    "time": 12.464 ,
    "amplitude": 4.95
  },
{
    "time": 12.467 ,
    "amplitude": 4.95
  },
{
    "time": 12.469 ,
    "amplitude": 4.95
  },
{
    "time": 12.472 ,
    "amplitude": 4.95
  },
{
    "time": 12.475 ,
    "amplitude": 4.945
  },
{
    "time": 12.478 ,
    "amplitude": 4.96
  },
{
    "time": 12.481 ,
    "amplitude": 4.955
  },
{
    "time": 12.483 ,
    "amplitude": 4.95
  },
{
    "time": 12.486 ,
    "amplitude": 4.935
  },
{
    "time": 12.489 ,
    "amplitude": 4.925
  },
{
    "time": 12.492 ,
    "amplitude": 4.935
  },
{
    "time": 12.494 ,
    "amplitude": 4.935
  },
{
    "time": 12.497 ,
    "amplitude": 4.945
  },
{
    "time": 12.5 ,
    "amplitude": 4.945
  },
{
    "time": 12.503 ,
    "amplitude": 4.955
  },
{
    "time": 12.506 ,
    "amplitude": 4.935
  },
{
    "time": 12.508 ,
    "amplitude": 4.945
  },
{
    "time": 12.511 ,
    "amplitude": 4.955
  },
{
    "time": 12.514 ,
    "amplitude": 4.95
  },
{
    "time": 12.517 ,
    "amplitude": 4.965
  },
{
    "time": 12.519 ,
    "amplitude": 4.945
  },
{
    "time": 12.522 ,
    "amplitude": 4.93
  },
{
    "time": 12.525 ,
    "amplitude": 4.925
  },
{
    "time": 12.528 ,
    "amplitude": 4.95
  },
{
    "time": 12.531 ,
    "amplitude": 4.98
  },
{
    "time": 12.533 ,
    "amplitude": 5.015
  },
{
    "time": 12.536 ,
    "amplitude": 5.005
  },
{
    "time": 12.539 ,
    "amplitude": 5
  },
{
    "time": 12.542 ,
    "amplitude": 5.01
  },
{
    "time": 12.544 ,
    "amplitude": 5.02
  },
{
    "time": 12.547 ,
    "amplitude": 5.035
  },
{
    "time": 12.55 ,
    "amplitude": 5.045
  },
{
    "time": 12.553 ,
    "amplitude": 5.055
  },
{
    "time": 12.556 ,
    "amplitude": 5.07
  },
{
    "time": 12.558 ,
    "amplitude": 5.08
  },
{
    "time": 12.561 ,
    "amplitude": 5.1
  },
{
    "time": 12.564 ,
    "amplitude": 5.13
  },
{
    "time": 12.567 ,
    "amplitude": 5.14
  },
{
    "time": 12.569 ,
    "amplitude": 5.145
  },
{
    "time": 12.572 ,
    "amplitude": 5.145
  },
{
    "time": 12.575 ,
    "amplitude": 5.145
  },
{
    "time": 12.578 ,
    "amplitude": 5.155
  },
{
    "time": 12.581 ,
    "amplitude": 5.165
  },
{
    "time": 12.583 ,
    "amplitude": 5.185
  },
{
    "time": 12.586 ,
    "amplitude": 5.185
  },
{
    "time": 12.589 ,
    "amplitude": 5.19
  },
{
    "time": 12.592 ,
    "amplitude": 5.185
  },
{
    "time": 12.594 ,
    "amplitude": 5.195
  },
{
    "time": 12.597 ,
    "amplitude": 5.16
  },
{
    "time": 12.6 ,
    "amplitude": 5.115
  },
{
    "time": 12.603 ,
    "amplitude": 5.065
  },
{
    "time": 12.606 ,
    "amplitude": 5.005
  },
{
    "time": 12.608 ,
    "amplitude": 4.975
  },
{
    "time": 12.611 ,
    "amplitude": 4.94
  },
{
    "time": 12.614 ,
    "amplitude": 4.915
  },
{
    "time": 12.617 ,
    "amplitude": 4.905
  },
{
    "time": 12.619 ,
    "amplitude": 4.895
  },
{
    "time": 12.622 ,
    "amplitude": 4.89
  },
{
    "time": 12.625 ,
    "amplitude": 4.9
  },
{
    "time": 12.628 ,
    "amplitude": 4.905
  },
{
    "time": 12.631 ,
    "amplitude": 4.915
  },
{
    "time": 12.633 ,
    "amplitude": 4.915
  },
{
    "time": 12.636 ,
    "amplitude": 4.895
  },
{
    "time": 12.639 ,
    "amplitude": 4.895
  },
{
    "time": 12.642 ,
    "amplitude": 4.88
  },
{
    "time": 12.644 ,
    "amplitude": 4.89
  },
{
    "time": 12.647 ,
    "amplitude": 4.9
  },
{
    "time": 12.65 ,
    "amplitude": 4.915
  },
{
    "time": 12.653 ,
    "amplitude": 4.905
  },
{
    "time": 12.656 ,
    "amplitude": 4.885
  },
{
    "time": 12.658 ,
    "amplitude": 4.875
  },
{
    "time": 12.661 ,
    "amplitude": 4.88
  },
{
    "time": 12.664 ,
    "amplitude": 4.905
  },
{
    "time": 12.667 ,
    "amplitude": 4.9
  },
{
    "time": 12.669 ,
    "amplitude": 4.89
  },
{
    "time": 12.672 ,
    "amplitude": 4.875
  },
{
    "time": 12.675 ,
    "amplitude": 4.88
  },
{
    "time": 12.678 ,
    "amplitude": 4.89
  },
{
    "time": 12.681 ,
    "amplitude": 4.91
  },
{
    "time": 12.683 ,
    "amplitude": 4.905
  },
{
    "time": 12.686 ,
    "amplitude": 4.9
  },
{
    "time": 12.689 ,
    "amplitude": 4.895
  },
{
    "time": 12.692 ,
    "amplitude": 4.885
  },
{
    "time": 12.694 ,
    "amplitude": 4.895
  },
{
    "time": 12.697 ,
    "amplitude": 4.895
  },
{
    "time": 12.7 ,
    "amplitude": 4.915
  },
{
    "time": 12.703 ,
    "amplitude": 4.91
  },
{
    "time": 12.706 ,
    "amplitude": 4.905
  },
{
    "time": 12.708 ,
    "amplitude": 4.885
  },
{
    "time": 12.711 ,
    "amplitude": 4.88
  },
{
    "time": 12.714 ,
    "amplitude": 4.895
  },
{
    "time": 12.717 ,
    "amplitude": 4.92
  },
{
    "time": 12.719 ,
    "amplitude": 4.94
  },
{
    "time": 12.722 ,
    "amplitude": 4.945
  },
{
    "time": 12.725 ,
    "amplitude": 4.93
  },
{
    "time": 12.728 ,
    "amplitude": 4.945
  },
{
    "time": 12.731 ,
    "amplitude": 4.93
  },
{
    "time": 12.733 ,
    "amplitude": 4.855
  },
{
    "time": 12.736 ,
    "amplitude": 4.765
  },
{
    "time": 12.739 ,
    "amplitude": 4.71
  },
{
    "time": 12.742 ,
    "amplitude": 4.7
  },
{
    "time": 12.744 ,
    "amplitude": 4.7
  },
{
    "time": 12.747 ,
    "amplitude": 4.69
  },
{
    "time": 12.75 ,
    "amplitude": 4.675
  },
{
    "time": 12.753 ,
    "amplitude": 4.64
  },
{
    "time": 12.756 ,
    "amplitude": 4.58
  },
{
    "time": 12.758 ,
    "amplitude": 4.55
  },
{
    "time": 12.761 ,
    "amplitude": 4.53
  },
{
    "time": 12.764 ,
    "amplitude": 4.49
  },
{
    "time": 12.767 ,
    "amplitude": 4.46
  },
{
    "time": 12.769 ,
    "amplitude": 4.435
  },
{
    "time": 12.772 ,
    "amplitude": 4.41
  },
{
    "time": 12.775 ,
    "amplitude": 4.375
  },
{
    "time": 12.778 ,
    "amplitude": 4.365
  },
{
    "time": 12.781 ,
    "amplitude": 4.355
  },
{
    "time": 12.783 ,
    "amplitude": 4.34
  },
{
    "time": 12.786 ,
    "amplitude": 4.335
  },
{
    "time": 12.789 ,
    "amplitude": 4.36
  },
{
    "time": 12.792 ,
    "amplitude": 4.38
  },
{
    "time": 12.794 ,
    "amplitude": 4.395
  },
{
    "time": 12.797 ,
    "amplitude": 4.395
  },
{
    "time": 12.8 ,
    "amplitude": 4.435
  },
{
    "time": 12.803 ,
    "amplitude": 4.525
  },
{
    "time": 12.806 ,
    "amplitude": 4.625
  },
{
    "time": 12.808 ,
    "amplitude": 4.69
  },
{
    "time": 12.811 ,
    "amplitude": 4.735
  },
{
    "time": 12.814 ,
    "amplitude": 4.76
  },
{
    "time": 12.817 ,
    "amplitude": 4.77
  },
{
    "time": 12.819 ,
    "amplitude": 4.815
  },
{
    "time": 12.822 ,
    "amplitude": 4.855
  },
{
    "time": 12.825 ,
    "amplitude": 4.905
  },
{
    "time": 12.828 ,
    "amplitude": 4.93
  },
{
    "time": 12.831 ,
    "amplitude": 4.945
  },
{
    "time": 12.833 ,
    "amplitude": 4.965
  },
{
    "time": 12.836 ,
    "amplitude": 4.995
  },
{
    "time": 12.839 ,
    "amplitude": 4.975
  },
{
    "time": 12.842 ,
    "amplitude": 4.955
  },
{
    "time": 12.844 ,
    "amplitude": 4.955
  },
{
    "time": 12.847 ,
    "amplitude": 4.965
  },
{
    "time": 12.85 ,
    "amplitude": 4.98
  },
{
    "time": 12.853 ,
    "amplitude": 4.99
  },
{
    "time": 12.856 ,
    "amplitude": 4.995
  },
{
    "time": 12.858 ,
    "amplitude": 4.985
  },
{
    "time": 12.861 ,
    "amplitude": 4.985
  },
{
    "time": 12.864 ,
    "amplitude": 4.995
  },
{
    "time": 12.867 ,
    "amplitude": 4.995
  },
{
    "time": 12.869 ,
    "amplitude": 4.99
  },
{
    "time": 12.872 ,
    "amplitude": 4.995
  },
{
    "time": 12.875 ,
    "amplitude": 4.99
  },
{
    "time": 12.878 ,
    "amplitude": 4.995
  },
{
    "time": 12.881 ,
    "amplitude": 5
  },
{
    "time": 12.883 ,
    "amplitude": 5
  },
{
    "time": 12.886 ,
    "amplitude": 4.985
  },
{
    "time": 12.889 ,
    "amplitude": 4.99
  },
{
    "time": 12.892 ,
    "amplitude": 4.975
  },
{
    "time": 12.894 ,
    "amplitude": 4.985
  },
{
    "time": 12.897 ,
    "amplitude": 4.99
  },
{
    "time": 12.9 ,
    "amplitude": 4.99
  },
{
    "time": 12.903 ,
    "amplitude": 4.995
  },
{
    "time": 12.906 ,
    "amplitude": 4.99
  },
{
    "time": 12.908 ,
    "amplitude": 4.975
  },
{
    "time": 12.911 ,
    "amplitude": 4.98
  },
{
    "time": 12.914 ,
    "amplitude": 4.995
  },
{
    "time": 12.917 ,
    "amplitude": 5.005
  },
{
    "time": 12.919 ,
    "amplitude": 4.995
  },
{
    "time": 12.922 ,
    "amplitude": 4.975
  },
{
    "time": 12.925 ,
    "amplitude": 4.98
  },
{
    "time": 12.928 ,
    "amplitude": 4.99
  },
{
    "time": 12.931 ,
    "amplitude": 4.99
  },
{
    "time": 12.933 ,
    "amplitude": 4.99
  },
{
    "time": 12.936 ,
    "amplitude": 4.995
  },
{
    "time": 12.939 ,
    "amplitude": 4.995
  },
{
    "time": 12.942 ,
    "amplitude": 5.005
  },
{
    "time": 12.944 ,
    "amplitude": 5.02
  },
{
    "time": 12.947 ,
    "amplitude": 5.04
  },
{
    "time": 12.95 ,
    "amplitude": 5.05
  },
{
    "time": 12.953 ,
    "amplitude": 5.05
  },
{
    "time": 12.956 ,
    "amplitude": 5.045
  },
{
    "time": 12.958 ,
    "amplitude": 5.035
  },
{
    "time": 12.961 ,
    "amplitude": 5.025
  },
{
    "time": 12.964 ,
    "amplitude": 5.04
  },
{
    "time": 12.967 ,
    "amplitude": 5.06
  },
{
    "time": 12.969 ,
    "amplitude": 5.06
  },
{
    "time": 12.972 ,
    "amplitude": 5.05
  },
{
    "time": 12.975 ,
    "amplitude": 5.045
  },
{
    "time": 12.978 ,
    "amplitude": 5.04
  },
{
    "time": 12.981 ,
    "amplitude": 5.03
  },
{
    "time": 12.983 ,
    "amplitude": 5.035
  },
{
    "time": 12.986 ,
    "amplitude": 5.05
  },
{
    "time": 12.989 ,
    "amplitude": 5.065
  },
{
    "time": 12.992 ,
    "amplitude": 5.075
  },
{
    "time": 12.994 ,
    "amplitude": 5.07
  },
{
    "time": 12.997 ,
    "amplitude": 5.07
  },
{
    "time": 13 ,
    "amplitude": 5.075
  },
{
    "time": 13.003 ,
    "amplitude": 5.075
  },
{
    "time": 13.006 ,
    "amplitude": 5.08
  },
{
    "time": 13.008 ,
    "amplitude": 5.08
  },
{
    "time": 13.011 ,
    "amplitude": 5.09
  },
{
    "time": 13.014 ,
    "amplitude": 5.1
  },
{
    "time": 13.017 ,
    "amplitude": 5.1
  },
{
    "time": 13.019 ,
    "amplitude": 5.08
  },
{
    "time": 13.022 ,
    "amplitude": 5.075
  },
{
    "time": 13.025 ,
    "amplitude": 5.065
  },
{
    "time": 13.028 ,
    "amplitude": 5.08
  },
{
    "time": 13.031 ,
    "amplitude": 5.095
  },
{
    "time": 13.033 ,
    "amplitude": 5.1
  },
{
    "time": 13.036 ,
    "amplitude": 5.1
  },
{
    "time": 13.039 ,
    "amplitude": 5.08
  },
{
    "time": 13.042 ,
    "amplitude": 5.075
  },
{
    "time": 13.044 ,
    "amplitude": 5.06
  },
{
    "time": 13.047 ,
    "amplitude": 5.075
  },
{
    "time": 13.05 ,
    "amplitude": 5.08
  },
{
    "time": 13.053 ,
    "amplitude": 5.065
  },
{
    "time": 13.056 ,
    "amplitude": 5.07
  },
{
    "time": 13.058 ,
    "amplitude": 5.065
  },
{
    "time": 13.061 ,
    "amplitude": 5.075
  },
{
    "time": 13.064 ,
    "amplitude": 5.09
  },
{
    "time": 13.067 ,
    "amplitude": 5.075
  },
{
    "time": 13.069 ,
    "amplitude": 5.065
  },
{
    "time": 13.072 ,
    "amplitude": 5.06
  },
{
    "time": 13.075 ,
    "amplitude": 5.05
  },
{
    "time": 13.078 ,
    "amplitude": 5.065
  },
{
    "time": 13.081 ,
    "amplitude": 5.065
  },
{
    "time": 13.083 ,
    "amplitude": 5.065
  },
{
    "time": 13.086 ,
    "amplitude": 5.06
  },
{
    "time": 13.089 ,
    "amplitude": 5.05
  },
{
    "time": 13.092 ,
    "amplitude": 5.055
  },
{
    "time": 13.094 ,
    "amplitude": 5.05
  },
{
    "time": 13.097 ,
    "amplitude": 5.05
  },
{
    "time": 13.1 ,
    "amplitude": 5.045
  },
{
    "time": 13.103 ,
    "amplitude": 5.03
  },
{
    "time": 13.106 ,
    "amplitude": 5.025
  },
{
    "time": 13.108 ,
    "amplitude": 5.01
  },
{
    "time": 13.111 ,
    "amplitude": 5.015
  },
{
    "time": 13.114 ,
    "amplitude": 5.035
  },
{
    "time": 13.117 ,
    "amplitude": 5.03
  },
{
    "time": 13.119 ,
    "amplitude": 5.02
  },
{
    "time": 13.122 ,
    "amplitude": 5.005
  },
{
    "time": 13.125 ,
    "amplitude": 4.99
  },
{
    "time": 13.128 ,
    "amplitude": 5.01
  },
{
    "time": 13.131 ,
    "amplitude": 4.995
  },
{
    "time": 13.133 ,
    "amplitude": 5.02
  },
{
    "time": 13.136 ,
    "amplitude": 5.01
  },
{
    "time": 13.139 ,
    "amplitude": 5.005
  },
{
    "time": 13.142 ,
    "amplitude": 5.005
  },
{
    "time": 13.144 ,
    "amplitude": 5.005
  },
{
    "time": 13.147 ,
    "amplitude": 5.015
  },
{
    "time": 13.15 ,
    "amplitude": 5.01
  },
{
    "time": 13.153 ,
    "amplitude": 5
  },
{
    "time": 13.156 ,
    "amplitude": 4.995
  },
{
    "time": 13.158 ,
    "amplitude": 4.98
  },
{
    "time": 13.161 ,
    "amplitude": 4.99
  },
{
    "time": 13.164 ,
    "amplitude": 5.005
  },
{
    "time": 13.167 ,
    "amplitude": 5.005
  },
{
    "time": 13.169 ,
    "amplitude": 5
  },
{
    "time": 13.172 ,
    "amplitude": 4.99
  },
{
    "time": 13.175 ,
    "amplitude": 5
  },
{
    "time": 13.178 ,
    "amplitude": 4.995
  },
{
    "time": 13.181 ,
    "amplitude": 5.005
  },
{
    "time": 13.183 ,
    "amplitude": 4.995
  },
{
    "time": 13.186 ,
    "amplitude": 4.99
  },
{
    "time": 13.189 ,
    "amplitude": 4.975
  },
{
    "time": 13.192 ,
    "amplitude": 4.97
  },
{
    "time": 13.194 ,
    "amplitude": 4.975
  },
{
    "time": 13.197 ,
    "amplitude": 4.985
  },
{
    "time": 13.2 ,
    "amplitude": 5
  },
{
    "time": 13.203 ,
    "amplitude": 5
  },
{
    "time": 13.206 ,
    "amplitude": 4.99
  },
{
    "time": 13.208 ,
    "amplitude": 4.98
  },
{
    "time": 13.211 ,
    "amplitude": 4.98
  },
{
    "time": 13.214 ,
    "amplitude": 5
  },
{
    "time": 13.217 ,
    "amplitude": 5.01
  },
{
    "time": 13.219 ,
    "amplitude": 4.99
  },
{
    "time": 13.222 ,
    "amplitude": 4.98
  },
{
    "time": 13.225 ,
    "amplitude": 4.975
  },
{
    "time": 13.228 ,
    "amplitude": 4.99
  },
{
    "time": 13.231 ,
    "amplitude": 5
  },
{
    "time": 13.233 ,
    "amplitude": 4.99
  },
{
    "time": 13.236 ,
    "amplitude": 4.97
  },
{
    "time": 13.239 ,
    "amplitude": 4.97
  },
{
    "time": 13.242 ,
    "amplitude": 4.965
  },
{
    "time": 13.244 ,
    "amplitude": 4.985
  },
{
    "time": 13.247 ,
    "amplitude": 4.985
  },
{
    "time": 13.25 ,
    "amplitude": 4.975
  },
{
    "time": 13.253 ,
    "amplitude": 4.965
  },
{
    "time": 13.256 ,
    "amplitude": 4.955
  },
{
    "time": 13.258 ,
    "amplitude": 4.955
  },
{
    "time": 13.261 ,
    "amplitude": 4.94
  },
{
    "time": 13.264 ,
    "amplitude": 4.95
  },
{
    "time": 13.267 ,
    "amplitude": 4.945
  },
{
    "time": 13.269 ,
    "amplitude": 4.935
  },
{
    "time": 13.272 ,
    "amplitude": 4.93
  },
{
    "time": 13.275 ,
    "amplitude": 4.915
  },
{
    "time": 13.278 ,
    "amplitude": 4.91
  },
{
    "time": 13.281 ,
    "amplitude": 4.9
  },
{
    "time": 13.283 ,
    "amplitude": 4.9
  },
{
    "time": 13.286 ,
    "amplitude": 4.895
  },
{
    "time": 13.289 ,
    "amplitude": 4.895
  },
{
    "time": 13.292 ,
    "amplitude": 4.905
  },
{
    "time": 13.294 ,
    "amplitude": 4.91
  },
{
    "time": 13.297 ,
    "amplitude": 4.91
  },
{
    "time": 13.3 ,
    "amplitude": 4.895
  },
{
    "time": 13.303 ,
    "amplitude": 4.885
  },
{
    "time": 13.306 ,
    "amplitude": 4.88
  },
{
    "time": 13.308 ,
    "amplitude": 4.865
  },
{
    "time": 13.311 ,
    "amplitude": 4.885
  },
{
    "time": 13.314 ,
    "amplitude": 4.9
  },
{
    "time": 13.317 ,
    "amplitude": 4.9
  },
{
    "time": 13.319 ,
    "amplitude": 4.905
  },
{
    "time": 13.322 ,
    "amplitude": 4.885
  },
{
    "time": 13.325 ,
    "amplitude": 4.86
  },
{
    "time": 13.328 ,
    "amplitude": 4.865
  },
{
    "time": 13.331 ,
    "amplitude": 4.88
  },
{
    "time": 13.333 ,
    "amplitude": 4.875
  },
{
    "time": 13.336 ,
    "amplitude": 4.875
  },
{
    "time": 13.339 ,
    "amplitude": 4.865
  },
{
    "time": 13.342 ,
    "amplitude": 4.88
  },
{
    "time": 13.344 ,
    "amplitude": 4.91
  },
{
    "time": 13.347 ,
    "amplitude": 4.91
  },
{
    "time": 13.35 ,
    "amplitude": 4.91
  },
{
    "time": 13.353 ,
    "amplitude": 4.91
  },
{
    "time": 13.356 ,
    "amplitude": 4.9
  },
{
    "time": 13.358 ,
    "amplitude": 4.89
  },
{
    "time": 13.361 ,
    "amplitude": 4.895
  },
{
    "time": 13.364 ,
    "amplitude": 4.905
  },
{
    "time": 13.367 ,
    "amplitude": 4.925
  },
{
    "time": 13.369 ,
    "amplitude": 4.935
  },
{
    "time": 13.372 ,
    "amplitude": 4.94
  },
{
    "time": 13.375 ,
    "amplitude": 4.94
  },
{
    "time": 13.378 ,
    "amplitude": 4.945
  },
{
    "time": 13.381 ,
    "amplitude": 4.945
  },
{
    "time": 13.383 ,
    "amplitude": 4.935
  },
{
    "time": 13.386 ,
    "amplitude": 4.925
  },
{
    "time": 13.389 ,
    "amplitude": 4.92
  },
{
    "time": 13.392 ,
    "amplitude": 4.92
  },
{
    "time": 13.394 ,
    "amplitude": 4.92
  },
{
    "time": 13.397 ,
    "amplitude": 4.93
  },
{
    "time": 13.4 ,
    "amplitude": 4.92
  },
{
    "time": 13.403 ,
    "amplitude": 4.925
  },
{
    "time": 13.406 ,
    "amplitude": 4.935
  },
{
    "time": 13.408 ,
    "amplitude": 4.935
  },
{
    "time": 13.411 ,
    "amplitude": 4.93
  },
{
    "time": 13.414 ,
    "amplitude": 4.94
  },
{
    "time": 13.417 ,
    "amplitude": 4.94
  },
{
    "time": 13.419 ,
    "amplitude": 4.94
  },
{
    "time": 13.422 ,
    "amplitude": 4.94
  },
{
    "time": 13.425 ,
    "amplitude": 4.95
  },
{
    "time": 13.428 ,
    "amplitude": 4.96
  },
{
    "time": 13.431 ,
    "amplitude": 4.955
  },
{
    "time": 13.433 ,
    "amplitude": 4.94
  },
{
    "time": 13.436 ,
    "amplitude": 4.945
  },
{
    "time": 13.439 ,
    "amplitude": 4.94
  },
{
    "time": 13.442 ,
    "amplitude": 4.93
  },
{
    "time": 13.444 ,
    "amplitude": 4.945
  },
{
    "time": 13.447 ,
    "amplitude": 4.955
  },
{
    "time": 13.45 ,
    "amplitude": 4.97
  },
{
    "time": 13.453 ,
    "amplitude": 4.955
  },
{
    "time": 13.456 ,
    "amplitude": 4.94
  },
{
    "time": 13.458 ,
    "amplitude": 4.93
  },
{
    "time": 13.461 ,
    "amplitude": 4.945
  },
{
    "time": 13.464 ,
    "amplitude": 4.95
  },
{
    "time": 13.467 ,
    "amplitude": 4.955
  },
{
    "time": 13.469 ,
    "amplitude": 4.945
  },
{
    "time": 13.472 ,
    "amplitude": 4.945
  },
{
    "time": 13.475 ,
    "amplitude": 4.94
  },
{
    "time": 13.478 ,
    "amplitude": 4.95
  },
{
    "time": 13.481 ,
    "amplitude": 4.955
  },
{
    "time": 13.483 ,
    "amplitude": 4.945
  },
{
    "time": 13.486 ,
    "amplitude": 4.95
  },
{
    "time": 13.489 ,
    "amplitude": 4.945
  },
{
    "time": 13.492 ,
    "amplitude": 4.935
  },
{
    "time": 13.494 ,
    "amplitude": 4.935
  },
{
    "time": 13.497 ,
    "amplitude": 4.94
  },
{
    "time": 13.5 ,
    "amplitude": 4.95
  },
{
    "time": 13.503 ,
    "amplitude": 4.96
  },
{
    "time": 13.506 ,
    "amplitude": 4.975
  },
{
    "time": 13.508 ,
    "amplitude": 4.975
  },
{
    "time": 13.511 ,
    "amplitude": 4.98
  },
{
    "time": 13.514 ,
    "amplitude": 4.98
  },
{
    "time": 13.517 ,
    "amplitude": 4.975
  },
{
    "time": 13.519 ,
    "amplitude": 4.965
  },
{
    "time": 13.522 ,
    "amplitude": 4.96
  },
{
    "time": 13.525 ,
    "amplitude": 4.965
  },
{
    "time": 13.528 ,
    "amplitude": 4.98
  },
{
    "time": 13.531 ,
    "amplitude": 5.015
  },
{
    "time": 13.533 ,
    "amplitude": 4.995
  },
{
    "time": 13.536 ,
    "amplitude": 5.01
  },
{
    "time": 13.539 ,
    "amplitude": 5.015
  },
{
    "time": 13.542 ,
    "amplitude": 5.015
  },
{
    "time": 13.544 ,
    "amplitude": 5.035
  },
{
    "time": 13.547 ,
    "amplitude": 5.04
  },
{
    "time": 13.55 ,
    "amplitude": 5.05
  },
{
    "time": 13.553 ,
    "amplitude": 5.055
  },
{
    "time": 13.556 ,
    "amplitude": 5.065
  },
{
    "time": 13.558 ,
    "amplitude": 5.07
  },
{
    "time": 13.561 ,
    "amplitude": 5.085
  },
{
    "time": 13.564 ,
    "amplitude": 5.105
  },
{
    "time": 13.567 ,
    "amplitude": 5.13
  },
{
    "time": 13.569 ,
    "amplitude": 5.175
  },
{
    "time": 13.572 ,
    "amplitude": 5.175
  },
{
    "time": 13.575 ,
    "amplitude": 5.175
  },
{
    "time": 13.578 ,
    "amplitude": 5.18
  },
{
    "time": 13.581 ,
    "amplitude": 5.175
  },
{
    "time": 13.583 ,
    "amplitude": 5.165
  },
{
    "time": 13.586 ,
    "amplitude": 5.175
  },
{
    "time": 13.589 ,
    "amplitude": 5.165
  },
{
    "time": 13.592 ,
    "amplitude": 5.16
  },
{
    "time": 13.594 ,
    "amplitude": 5.155
  },
{
    "time": 13.597 ,
    "amplitude": 5.155
  },
{
    "time": 13.6 ,
    "amplitude": 5.17
  },
{
    "time": 13.603 ,
    "amplitude": 5.14
  },
{
    "time": 13.606 ,
    "amplitude": 5.095
  },
{
    "time": 13.608 ,
    "amplitude": 5.055
  },
{
    "time": 13.611 ,
    "amplitude": 5.02
  },
{
    "time": 13.614 ,
    "amplitude": 4.98
  },
{
    "time": 13.617 ,
    "amplitude": 4.945
  },
{
    "time": 13.619 ,
    "amplitude": 4.9
  },
{
    "time": 13.622 ,
    "amplitude": 4.875
  },
{
    "time": 13.625 ,
    "amplitude": 4.89
  },
{
    "time": 13.628 ,
    "amplitude": 4.915
  },
{
    "time": 13.631 ,
    "amplitude": 4.94
  },
{
    "time": 13.633 ,
    "amplitude": 4.94
  },
{
    "time": 13.636 ,
    "amplitude": 4.925
  },
{
    "time": 13.639 ,
    "amplitude": 4.915
  },
{
    "time": 13.642 ,
    "amplitude": 4.91
  },
{
    "time": 13.644 ,
    "amplitude": 4.915
  },
{
    "time": 13.647 ,
    "amplitude": 4.925
  },
{
    "time": 13.65 ,
    "amplitude": 4.93
  },
{
    "time": 13.653 ,
    "amplitude": 4.915
  },
{
    "time": 13.656 ,
    "amplitude": 4.905
  },
{
    "time": 13.658 ,
    "amplitude": 4.905
  },
{
    "time": 13.661 ,
    "amplitude": 4.93
  },
{
    "time": 13.664 ,
    "amplitude": 4.925
  },
{
    "time": 13.667 ,
    "amplitude": 4.92
  },
{
    "time": 13.669 ,
    "amplitude": 4.915
  },
{
    "time": 13.672 ,
    "amplitude": 4.9
  },
{
    "time": 13.675 ,
    "amplitude": 4.905
  },
{
    "time": 13.678 ,
    "amplitude": 4.905
  },
{
    "time": 13.681 ,
    "amplitude": 4.91
  },
{
    "time": 13.683 ,
    "amplitude": 4.92
  },
{
    "time": 13.686 ,
    "amplitude": 4.9
  },
{
    "time": 13.689 ,
    "amplitude": 4.9
  },
{
    "time": 13.692 ,
    "amplitude": 4.9
  },
{
    "time": 13.694 ,
    "amplitude": 4.91
  },
{
    "time": 13.697 ,
    "amplitude": 4.905
  },
{
    "time": 13.7 ,
    "amplitude": 4.905
  },
{
    "time": 13.703 ,
    "amplitude": 4.91
  },
{
    "time": 13.706 ,
    "amplitude": 4.92
  },
{
    "time": 13.708 ,
    "amplitude": 4.935
  },
{
    "time": 13.711 ,
    "amplitude": 4.925
  },
{
    "time": 13.714 ,
    "amplitude": 4.925
  },
{
    "time": 13.717 ,
    "amplitude": 4.915
  },
{
    "time": 13.719 ,
    "amplitude": 4.915
  },
{
    "time": 13.722 ,
    "amplitude": 4.905
  },
{
    "time": 13.725 ,
    "amplitude": 4.92
  },
{
    "time": 13.728 ,
    "amplitude": 4.91
  },
{
    "time": 13.731 ,
    "amplitude": 4.89
  },
{
    "time": 13.733 ,
    "amplitude": 4.87
  },
{
    "time": 13.736 ,
    "amplitude": 4.87
  },
{
    "time": 13.739 ,
    "amplitude": 4.895
  },
{
    "time": 13.742 ,
    "amplitude": 4.925
  },
{
    "time": 13.744 ,
    "amplitude": 4.955
  },
{
    "time": 13.747 ,
    "amplitude": 4.96
  },
{
    "time": 13.75 ,
    "amplitude": 4.945
  },
{
    "time": 13.753 ,
    "amplitude": 4.91
  },
{
    "time": 13.756 ,
    "amplitude": 4.83
  },
{
    "time": 13.758 ,
    "amplitude": 4.745
  },
{
    "time": 13.761 ,
    "amplitude": 4.715
  },
{
    "time": 13.764 ,
    "amplitude": 4.69
  },
{
    "time": 13.767 ,
    "amplitude": 4.695
  },
{
    "time": 13.769 ,
    "amplitude": 4.695
  },
{
    "time": 13.772 ,
    "amplitude": 4.68
  },
{
    "time": 13.775 ,
    "amplitude": 4.645
  },
{
    "time": 13.778 ,
    "amplitude": 4.61
  },
{
    "time": 13.781 ,
    "amplitude": 4.57
  },
{
    "time": 13.783 ,
    "amplitude": 4.55
  },
{
    "time": 13.786 ,
    "amplitude": 4.5
  },
{
    "time": 13.789 ,
    "amplitude": 4.48
  },
{
    "time": 13.792 ,
    "amplitude": 4.44
  },
{
    "time": 13.794 ,
    "amplitude": 4.435
  },
{
    "time": 13.797 ,
    "amplitude": 4.41
  },
{
    "time": 13.8 ,
    "amplitude": 4.37
  },
{
    "time": 13.803 ,
    "amplitude": 4.33
  },
{
    "time": 13.806 ,
    "amplitude": 4.295
  },
{
    "time": 13.808 ,
    "amplitude": 4.285
  },
{
    "time": 13.811 ,
    "amplitude": 4.315
  },
{
    "time": 13.814 ,
    "amplitude": 4.365
  },
{
    "time": 13.817 ,
    "amplitude": 4.395
  },
{
    "time": 13.819 ,
    "amplitude": 4.41
  },
{
    "time": 13.822 ,
    "amplitude": 4.435
  },
{
    "time": 13.825 ,
    "amplitude": 4.51
  },
{
    "time": 13.828 ,
    "amplitude": 4.6
  },
{
    "time": 13.831 ,
    "amplitude": 4.675
  },
{
    "time": 13.833 ,
    "amplitude": 4.725
  },
{
    "time": 13.836 ,
    "amplitude": 4.75
  },
{
    "time": 13.839 ,
    "amplitude": 4.785
  },
{
    "time": 13.842 ,
    "amplitude": 4.82
  },
{
    "time": 13.844 ,
    "amplitude": 4.875
  },
{
    "time": 13.847 ,
    "amplitude": 4.925
  },
{
    "time": 13.85 ,
    "amplitude": 4.945
  },
{
    "time": 13.853 ,
    "amplitude": 4.965
  },
{
    "time": 13.856 ,
    "amplitude": 4.98
  },
{
    "time": 13.858 ,
    "amplitude": 4.975
  },
{
    "time": 13.861 ,
    "amplitude": 4.99
  },
{
    "time": 13.864 ,
    "amplitude": 4.995
  },
{
    "time": 13.867 ,
    "amplitude": 5.015
  },
{
    "time": 13.869 ,
    "amplitude": 5.005
  },
{
    "time": 13.872 ,
    "amplitude": 5
  },
{
    "time": 13.875 ,
    "amplitude": 4.99
  },
{
    "time": 13.878 ,
    "amplitude": 4.99
  },
{
    "time": 13.881 ,
    "amplitude": 5
  },
{
    "time": 13.883 ,
    "amplitude": 4.995
  },
{
    "time": 13.886 ,
    "amplitude": 5
  },
{
    "time": 13.889 ,
    "amplitude": 5.005
  },
{
    "time": 13.892 ,
    "amplitude": 5.01
  },
{
    "time": 13.894 ,
    "amplitude": 5.025
  },
{
    "time": 13.897 ,
    "amplitude": 5.04
  },
{
    "time": 13.9 ,
    "amplitude": 5.04
  },
{
    "time": 13.903 ,
    "amplitude": 5.03
  },
{
    "time": 13.906 ,
    "amplitude": 5.02
  },
{
    "time": 13.908 ,
    "amplitude": 5.01
  },
{
    "time": 13.911 ,
    "amplitude": 5.02
  },
{
    "time": 13.914 ,
    "amplitude": 5.045
  },
{
    "time": 13.917 ,
    "amplitude": 5.04
  },
{
    "time": 13.919 ,
    "amplitude": 5.03
  },
{
    "time": 13.922 ,
    "amplitude": 5.015
  },
{
    "time": 13.925 ,
    "amplitude": 5.015
  },
{
    "time": 13.928 ,
    "amplitude": 5.025
  },
{
    "time": 13.931 ,
    "amplitude": 5.03
  },
{
    "time": 13.933 ,
    "amplitude": 5.025
  },
{
    "time": 13.936 ,
    "amplitude": 5.025
  },
{
    "time": 13.939 ,
    "amplitude": 5.03
  },
{
    "time": 13.942 ,
    "amplitude": 5.025
  },
{
    "time": 13.944 ,
    "amplitude": 5.045
  },
{
    "time": 13.947 ,
    "amplitude": 5.05
  },
{
    "time": 13.95 ,
    "amplitude": 5.04
  },
{
    "time": 13.953 ,
    "amplitude": 5.03
  },
{
    "time": 13.956 ,
    "amplitude": 5.01
  },
{
    "time": 13.958 ,
    "amplitude": 5.01
  },
{
    "time": 13.961 ,
    "amplitude": 5.035
  },
{
    "time": 13.964 ,
    "amplitude": 5.065
  },
{
    "time": 13.967 ,
    "amplitude": 5.08
  },
{
    "time": 13.969 ,
    "amplitude": 5.07
  },
{
    "time": 13.972 ,
    "amplitude": 5.065
  },
{
    "time": 13.975 ,
    "amplitude": 5.065
  },
{
    "time": 13.978 ,
    "amplitude": 5.06
  },
{
    "time": 13.981 ,
    "amplitude": 5.08
  },
{
    "time": 13.983 ,
    "amplitude": 5.085
  },
{
    "time": 13.986 ,
    "amplitude": 5.09
  },
{
    "time": 13.989 ,
    "amplitude": 5.085
  },
{
    "time": 13.992 ,
    "amplitude": 5.08
  },
{
    "time": 13.994 ,
    "amplitude": 5.095
  },
{
    "time": 13.997 ,
    "amplitude": 5.115
  },
{
    "time": 14 ,
    "amplitude": 5.12
  },
{
    "time": 14.003 ,
    "amplitude": 5.115
  },
{
    "time": 14.006 ,
    "amplitude": 5.1
  },
{
    "time": 14.008 ,
    "amplitude": 5.105
  },
{
    "time": 14.011 ,
    "amplitude": 5.125
  },
{
    "time": 14.014 ,
    "amplitude": 5.135
  },
{
    "time": 14.017 ,
    "amplitude": 5.13
  },
{
    "time": 14.019 ,
    "amplitude": 5.13
  },
{
    "time": 14.022 ,
    "amplitude": 5.115
  },
{
    "time": 14.025 ,
    "amplitude": 5.115
  },
{
    "time": 14.028 ,
    "amplitude": 5.13
  },
{
    "time": 14.031 ,
    "amplitude": 5.14
  },
{
    "time": 14.033 ,
    "amplitude": 5.15
  },
{
    "time": 14.036 ,
    "amplitude": 5.14
  },
{
    "time": 14.039 ,
    "amplitude": 5.14
  },
{
    "time": 14.042 ,
    "amplitude": 5.125
  },
{
    "time": 14.044 ,
    "amplitude": 5.135
  },
{
    "time": 14.047 ,
    "amplitude": 5.16
  },
{
    "time": 14.05 ,
    "amplitude": 5.17
  },
{
    "time": 14.053 ,
    "amplitude": 5.16
  },
{
    "time": 14.056 ,
    "amplitude": 5.155
  },
{
    "time": 14.058 ,
    "amplitude": 5.15
  },
{
    "time": 14.061 ,
    "amplitude": 5.145
  },
{
    "time": 14.064 ,
    "amplitude": 5.165
  },
{
    "time": 14.067 ,
    "amplitude": 5.155
  },
{
    "time": 14.069 ,
    "amplitude": 5.155
  },
{
    "time": 14.072 ,
    "amplitude": 5.125
  },
{
    "time": 14.075 ,
    "amplitude": 5.13
  },
{
    "time": 14.078 ,
    "amplitude": 5.145
  },
{
    "time": 14.081 ,
    "amplitude": 5.155
  },
{
    "time": 14.083 ,
    "amplitude": 5.155
  },
{
    "time": 14.086 ,
    "amplitude": 5.145
  },
{
    "time": 14.089 ,
    "amplitude": 5.12
  },
{
    "time": 14.092 ,
    "amplitude": 5.11
  },
{
    "time": 14.094 ,
    "amplitude": 5.115
  },
{
    "time": 14.097 ,
    "amplitude": 5.13
  },
{
    "time": 14.1 ,
    "amplitude": 5.115
  },
{
    "time": 14.103 ,
    "amplitude": 5.1
  },
{
    "time": 14.106 ,
    "amplitude": 5.09
  },
{
    "time": 14.108 ,
    "amplitude": 5.08
  },
{
    "time": 14.111 ,
    "amplitude": 5.08
  },
{
    "time": 14.114 ,
    "amplitude": 5.09
  },
{
    "time": 14.117 ,
    "amplitude": 5.075
  },
{
    "time": 14.119 ,
    "amplitude": 5.065
  },
{
    "time": 14.122 ,
    "amplitude": 5.05
  },
{
    "time": 14.125 ,
    "amplitude": 5.025
  },
{
    "time": 14.128 ,
    "amplitude": 5.035
  },
{
    "time": 14.131 ,
    "amplitude": 5.04
  },
{
    "time": 14.133 ,
    "amplitude": 5.02
  },
{
    "time": 14.136 ,
    "amplitude": 5.01
  },
{
    "time": 14.139 ,
    "amplitude": 5.01
  },
{
    "time": 14.142 ,
    "amplitude": 5.02
  },
{
    "time": 14.144 ,
    "amplitude": 5.025
  },
{
    "time": 14.147 ,
    "amplitude": 5.03
  },
{
    "time": 14.15 ,
    "amplitude": 5.02
  },
{
    "time": 14.153 ,
    "amplitude": 5.005
  },
{
    "time": 14.156 ,
    "amplitude": 4.995
  },
{
    "time": 14.158 ,
    "amplitude": 4.985
  },
{
    "time": 14.161 ,
    "amplitude": 4.985
  },
{
    "time": 14.164 ,
    "amplitude": 5
  },
{
    "time": 14.167 ,
    "amplitude": 4.995
  },
{
    "time": 14.169 ,
    "amplitude": 4.985
  },
{
    "time": 14.172 ,
    "amplitude": 4.99
  },
{
    "time": 14.175 ,
    "amplitude": 4.97
  },
{
    "time": 14.178 ,
    "amplitude": 4.97
  },
{
    "time": 14.181 ,
    "amplitude": 4.98
  },
{
    "time": 14.183 ,
    "amplitude": 4.98
  },
{
    "time": 14.186 ,
    "amplitude": 4.96
  },
{
    "time": 14.189 ,
    "amplitude": 4.965
  },
{
    "time": 14.192 ,
    "amplitude": 4.955
  },
{
    "time": 14.194 ,
    "amplitude": 4.98
  },
{
    "time": 14.197 ,
    "amplitude": 5
  },
{
    "time": 14.2 ,
    "amplitude": 4.985
  },
{
    "time": 14.203 ,
    "amplitude": 4.975
  },
{
    "time": 14.206 ,
    "amplitude": 4.965
  },
{
    "time": 14.208 ,
    "amplitude": 4.955
  },
{
    "time": 14.211 ,
    "amplitude": 4.965
  },
{
    "time": 14.214 ,
    "amplitude": 4.975
  },
{
    "time": 14.217 ,
    "amplitude": 4.975
  },
{
    "time": 14.219 ,
    "amplitude": 4.975
  },
{
    "time": 14.222 ,
    "amplitude": 4.95
  },
{
    "time": 14.225 ,
    "amplitude": 4.935
  },
{
    "time": 14.228 ,
    "amplitude": 4.955
  },
{
    "time": 14.231 ,
    "amplitude": 4.96
  },
{
    "time": 14.233 ,
    "amplitude": 4.96
  },
{
    "time": 14.236 ,
    "amplitude": 4.935
  },
{
    "time": 14.239 ,
    "amplitude": 4.935
  },
{
    "time": 14.242 ,
    "amplitude": 4.935
  },
{
    "time": 14.244 ,
    "amplitude": 4.95
  },
{
    "time": 14.247 ,
    "amplitude": 4.96
  },
{
    "time": 14.25 ,
    "amplitude": 4.95
  },
{
    "time": 14.253 ,
    "amplitude": 4.935
  },
{
    "time": 14.256 ,
    "amplitude": 4.93
  },
{
    "time": 14.258 ,
    "amplitude": 4.93
  },
{
    "time": 14.261 ,
    "amplitude": 4.935
  },
{
    "time": 14.264 ,
    "amplitude": 4.935
  },
{
    "time": 14.267 ,
    "amplitude": 4.92
  },
{
    "time": 14.269 ,
    "amplitude": 4.925
  },
{
    "time": 14.272 ,
    "amplitude": 4.925
  },
{
    "time": 14.275 ,
    "amplitude": 4.935
  },
{
    "time": 14.278 ,
    "amplitude": 4.93
  },
{
    "time": 14.281 ,
    "amplitude": 4.93
  },
{
    "time": 14.283 ,
    "amplitude": 4.92
  },
{
    "time": 14.286 ,
    "amplitude": 4.91
  },
{
    "time": 14.289 ,
    "amplitude": 4.91
  },
{
    "time": 14.292 ,
    "amplitude": 4.91
  },
{
    "time": 14.294 ,
    "amplitude": 4.905
  },
{
    "time": 14.297 ,
    "amplitude": 4.895
  },
{
    "time": 14.3 ,
    "amplitude": 4.885
  },
{
    "time": 14.303 ,
    "amplitude": 4.9
  },
{
    "time": 14.306 ,
    "amplitude": 4.885
  },
{
    "time": 14.308 ,
    "amplitude": 4.88
  },
{
    "time": 14.311 ,
    "amplitude": 4.89
  },
{
    "time": 14.314 ,
    "amplitude": 4.905
  },
{
    "time": 14.317 ,
    "amplitude": 4.89
  },
{
    "time": 14.319 ,
    "amplitude": 4.895
  },
{
    "time": 14.322 ,
    "amplitude": 4.895
  },
{
    "time": 14.325 ,
    "amplitude": 4.87
  },
{
    "time": 14.328 ,
    "amplitude": 4.88
  },
{
    "time": 14.331 ,
    "amplitude": 4.9
  },
{
    "time": 14.333 ,
    "amplitude": 4.9
  },
{
    "time": 14.336 ,
    "amplitude": 4.9
  },
{
    "time": 14.339 ,
    "amplitude": 4.885
  },
{
    "time": 14.342 ,
    "amplitude": 4.87
  },
{
    "time": 14.344 ,
    "amplitude": 4.885
  },
{
    "time": 14.347 ,
    "amplitude": 4.885
  },
{
    "time": 14.35 ,
    "amplitude": 4.895
  },
{
    "time": 14.353 ,
    "amplitude": 4.89
  },
{
    "time": 14.356 ,
    "amplitude": 4.87
  },
{
    "time": 14.358 ,
    "amplitude": 4.865
  },
{
    "time": 14.361 ,
    "amplitude": 4.885
  },
{
    "time": 14.364 ,
    "amplitude": 4.915
  },
{
    "time": 14.367 ,
    "amplitude": 4.915
  },
{
    "time": 14.369 ,
    "amplitude": 4.92
  },
{
    "time": 14.372 ,
    "amplitude": 4.915
  },
{
    "time": 14.375 ,
    "amplitude": 4.905
  },
{
    "time": 14.378 ,
    "amplitude": 4.905
  },
{
    "time": 14.381 ,
    "amplitude": 4.9
  },
{
    "time": 14.383 ,
    "amplitude": 4.91
  },
{
    "time": 14.386 ,
    "amplitude": 4.905
  },
{
    "time": 14.389 ,
    "amplitude": 4.89
  },
{
    "time": 14.392 ,
    "amplitude": 4.895
  },
{
    "time": 14.394 ,
    "amplitude": 4.91
  },
{
    "time": 14.397 ,
    "amplitude": 4.925
  },
{
    "time": 14.4 ,
    "amplitude": 4.915
  },
{
    "time": 14.403 ,
    "amplitude": 4.9
  },
{
    "time": 14.406 ,
    "amplitude": 4.89
  },
{
    "time": 14.408 ,
    "amplitude": 4.89
  },
{
    "time": 14.411 ,
    "amplitude": 4.915
  },
{
    "time": 14.414 ,
    "amplitude": 4.925
  },
{
    "time": 14.417 ,
    "amplitude": 4.915
  },
{
    "time": 14.419 ,
    "amplitude": 4.91
  },
{
    "time": 14.422 ,
    "amplitude": 4.905
  },
{
    "time": 14.425 ,
    "amplitude": 4.885
  },
{
    "time": 14.428 ,
    "amplitude": 4.895
  },
{
    "time": 14.431 ,
    "amplitude": 4.905
  },
{
    "time": 14.433 ,
    "amplitude": 4.92
  },
{
    "time": 14.436 ,
    "amplitude": 4.92
  },
{
    "time": 14.439 ,
    "amplitude": 4.925
  },
{
    "time": 14.442 ,
    "amplitude": 4.92
  },
{
    "time": 14.444 ,
    "amplitude": 4.935
  },
{
    "time": 14.447 ,
    "amplitude": 4.935
  },
{
    "time": 14.45 ,
    "amplitude": 4.94
  },
{
    "time": 14.453 ,
    "amplitude": 4.925
  },
{
    "time": 14.456 ,
    "amplitude": 4.915
  },
{
    "time": 14.458 ,
    "amplitude": 4.92
  },
{
    "time": 14.461 ,
    "amplitude": 4.925
  },
{
    "time": 14.464 ,
    "amplitude": 4.935
  },
{
    "time": 14.467 ,
    "amplitude": 4.935
  },
{
    "time": 14.469 ,
    "amplitude": 4.935
  },
{
    "time": 14.472 ,
    "amplitude": 4.915
  },
{
    "time": 14.475 ,
    "amplitude": 4.915
  },
{
    "time": 14.478 ,
    "amplitude": 4.925
  },
{
    "time": 14.481 ,
    "amplitude": 4.93
  },
{
    "time": 14.483 ,
    "amplitude": 4.93
  },
{
    "time": 14.486 ,
    "amplitude": 4.925
  },
{
    "time": 14.489 ,
    "amplitude": 4.92
  },
{
    "time": 14.492 ,
    "amplitude": 4.925
  },
{
    "time": 14.494 ,
    "amplitude": 4.92
  },
{
    "time": 14.497 ,
    "amplitude": 4.935
  },
{
    "time": 14.5 ,
    "amplitude": 4.925
  },
{
    "time": 14.503 ,
    "amplitude": 4.935
  },
{
    "time": 14.506 ,
    "amplitude": 4.92
  },
{
    "time": 14.508 ,
    "amplitude": 4.935
  },
{
    "time": 14.511 ,
    "amplitude": 4.93
  },
{
    "time": 14.514 ,
    "amplitude": 4.94
  },
{
    "time": 14.517 ,
    "amplitude": 4.945
  },
{
    "time": 14.519 ,
    "amplitude": 4.935
  },
{
    "time": 14.522 ,
    "amplitude": 4.93
  },
{
    "time": 14.525 ,
    "amplitude": 4.905
  },
{
    "time": 14.528 ,
    "amplitude": 4.92
  },
{
    "time": 14.531 ,
    "amplitude": 4.94
  },
{
    "time": 14.533 ,
    "amplitude": 4.94
  },
{
    "time": 14.536 ,
    "amplitude": 4.93
  },
{
    "time": 14.539 ,
    "amplitude": 4.915
  },
{
    "time": 14.542 ,
    "amplitude": 4.905
  },
{
    "time": 14.544 ,
    "amplitude": 4.92
  },
{
    "time": 14.547 ,
    "amplitude": 4.925
  },
{
    "time": 14.55 ,
    "amplitude": 4.95
  },
{
    "time": 14.553 ,
    "amplitude": 4.93
  },
{
    "time": 14.556 ,
    "amplitude": 4.925
  },
{
    "time": 14.558 ,
    "amplitude": 4.915
  },
{
    "time": 14.561 ,
    "amplitude": 4.91
  },
{
    "time": 14.564 ,
    "amplitude": 4.945
  },
{
    "time": 14.567 ,
    "amplitude": 4.95
  },
{
    "time": 14.569 ,
    "amplitude": 4.945
  },
{
    "time": 14.572 ,
    "amplitude": 4.925
  },
{
    "time": 14.575 ,
    "amplitude": 4.92
  },
{
    "time": 14.578 ,
    "amplitude": 4.915
  },
{
    "time": 14.581 ,
    "amplitude": 4.925
  },
{
    "time": 14.583 ,
    "amplitude": 4.94
  },
{
    "time": 14.586 ,
    "amplitude": 4.945
  },
{
    "time": 14.589 ,
    "amplitude": 4.94
  },
{
    "time": 14.592 ,
    "amplitude": 4.965
  },
{
    "time": 14.594 ,
    "amplitude": 4.99
  },
{
    "time": 14.597 ,
    "amplitude": 5.005
  },
{
    "time": 14.6 ,
    "amplitude": 5.02
  },
{
    "time": 14.603 ,
    "amplitude": 5.01
  },
{
    "time": 14.606 ,
    "amplitude": 5
  },
{
    "time": 14.608 ,
    "amplitude": 5
  },
{
    "time": 14.611 ,
    "amplitude": 5.015
  },
{
    "time": 14.614 ,
    "amplitude": 5.05
  },
{
    "time": 14.617 ,
    "amplitude": 5.06
  },
{
    "time": 14.619 ,
    "amplitude": 5.07
  },
{
    "time": 14.622 ,
    "amplitude": 5.085
  },
{
    "time": 14.625 ,
    "amplitude": 5.095
  },
{
    "time": 14.628 ,
    "amplitude": 5.115
  },
{
    "time": 14.631 ,
    "amplitude": 5.13
  },
{
    "time": 14.633 ,
    "amplitude": 5.145
  },
{
    "time": 14.636 ,
    "amplitude": 5.14
  },
{
    "time": 14.639 ,
    "amplitude": 5.135
  },
{
    "time": 14.642 ,
    "amplitude": 5.115
  },
{
    "time": 14.644 ,
    "amplitude": 5.13
  },
{
    "time": 14.647 ,
    "amplitude": 5.16
  },
{
    "time": 14.65 ,
    "amplitude": 5.16
  },
{
    "time": 14.653 ,
    "amplitude": 5.155
  },
{
    "time": 14.656 ,
    "amplitude": 5.11
  },
{
    "time": 14.658 ,
    "amplitude": 5.07
  },
{
    "time": 14.661 ,
    "amplitude": 5.035
  },
{
    "time": 14.664 ,
    "amplitude": 5.01
  },
{
    "time": 14.667 ,
    "amplitude": 4.97
  },
{
    "time": 14.669 ,
    "amplitude": 4.935
  },
{
    "time": 14.672 ,
    "amplitude": 4.87
  },
{
    "time": 14.675 ,
    "amplitude": 4.83
  },
{
    "time": 14.678 ,
    "amplitude": 4.83
  },
{
    "time": 14.681 ,
    "amplitude": 4.86
  },
{
    "time": 14.683 ,
    "amplitude": 4.885
  },
{
    "time": 14.686 ,
    "amplitude": 4.88
  },
{
    "time": 14.689 ,
    "amplitude": 4.87
  },
{
    "time": 14.692 ,
    "amplitude": 4.86
  },
{
    "time": 14.694 ,
    "amplitude": 4.87
  },
{
    "time": 14.697 ,
    "amplitude": 4.875
  },
{
    "time": 14.7 ,
    "amplitude": 4.865
  },
{
    "time": 14.703 ,
    "amplitude": 4.855
  },
{
    "time": 14.706 ,
    "amplitude": 4.84
  },
{
    "time": 14.708 ,
    "amplitude": 4.85
  },
{
    "time": 14.711 ,
    "amplitude": 4.88
  },
{
    "time": 14.714 ,
    "amplitude": 4.895
  },
{
    "time": 14.717 ,
    "amplitude": 4.87
  },
{
    "time": 14.719 ,
    "amplitude": 4.85
  },
{
    "time": 14.722 ,
    "amplitude": 4.84
  },
{
    "time": 14.725 ,
    "amplitude": 4.855
  },
{
    "time": 14.728 ,
    "amplitude": 4.87
  },
{
    "time": 14.731 ,
    "amplitude": 4.87
  },
{
    "time": 14.733 ,
    "amplitude": 4.885
  },
{
    "time": 14.736 ,
    "amplitude": 4.865
  },
{
    "time": 14.739 ,
    "amplitude": 4.845
  },
{
    "time": 14.742 ,
    "amplitude": 4.85
  },
{
    "time": 14.744 ,
    "amplitude": 4.865
  },
{
    "time": 14.747 ,
    "amplitude": 4.86
  },
{
    "time": 14.75 ,
    "amplitude": 4.865
  },
{
    "time": 14.753 ,
    "amplitude": 4.855
  },
{
    "time": 14.756 ,
    "amplitude": 4.845
  },
{
    "time": 14.758 ,
    "amplitude": 4.855
  },
{
    "time": 14.761 ,
    "amplitude": 4.865
  },
{
    "time": 14.764 ,
    "amplitude": 4.88
  },
{
    "time": 14.767 ,
    "amplitude": 4.875
  },
{
    "time": 14.769 ,
    "amplitude": 4.87
  },
{
    "time": 14.772 ,
    "amplitude": 4.855
  },
{
    "time": 14.775 ,
    "amplitude": 4.85
  },
{
    "time": 14.778 ,
    "amplitude": 4.84
  },
{
    "time": 14.781 ,
    "amplitude": 4.85
  },
{
    "time": 14.783 ,
    "amplitude": 4.835
  },
{
    "time": 14.786 ,
    "amplitude": 4.8
  },
{
    "time": 14.789 ,
    "amplitude": 4.785
  },
{
    "time": 14.792 ,
    "amplitude": 4.77
  },
{
    "time": 14.794 ,
    "amplitude": 4.785
  },
{
    "time": 14.797 ,
    "amplitude": 4.81
  },
{
    "time": 14.8 ,
    "amplitude": 4.81
  },
{
    "time": 14.803 ,
    "amplitude": 4.81
  },
{
    "time": 14.806 ,
    "amplitude": 4.8
  },
{
    "time": 14.808 ,
    "amplitude": 4.755
  },
{
    "time": 14.811 ,
    "amplitude": 4.67
  },
{
    "time": 14.814 ,
    "amplitude": 4.6
  },
{
    "time": 14.817 ,
    "amplitude": 4.575
  },
{
    "time": 14.819 ,
    "amplitude": 4.58
  },
{
    "time": 14.822 ,
    "amplitude": 4.595
  },
{
    "time": 14.825 ,
    "amplitude": 4.58
  },
{
    "time": 14.828 ,
    "amplitude": 4.58
  },
{
    "time": 14.831 ,
    "amplitude": 4.555
  },
{
    "time": 14.833 ,
    "amplitude": 4.495
  },
{
    "time": 14.836 ,
    "amplitude": 4.44
  },
{
    "time": 14.839 ,
    "amplitude": 4.4
  },
{
    "time": 14.842 ,
    "amplitude": 4.385
  },
{
    "time": 14.844 ,
    "amplitude": 4.375
  },
{
    "time": 14.847 ,
    "amplitude": 4.37
  },
{
    "time": 14.85 ,
    "amplitude": 4.33
  },
{
    "time": 14.853 ,
    "amplitude": 4.265
  },
{
    "time": 14.856 ,
    "amplitude": 4.235
  },
{
    "time": 14.858 ,
    "amplitude": 4.235
  },
{
    "time": 14.861 ,
    "amplitude": 4.23
  },
{
    "time": 14.864 ,
    "amplitude": 4.26
  },
{
    "time": 14.867 ,
    "amplitude": 4.295
  },
{
    "time": 14.869 ,
    "amplitude": 4.355
  },
{
    "time": 14.872 ,
    "amplitude": 4.375
  },
{
    "time": 14.875 ,
    "amplitude": 4.395
  },
{
    "time": 14.878 ,
    "amplitude": 4.455
  },
{
    "time": 14.881 ,
    "amplitude": 4.555
  },
{
    "time": 14.883 ,
    "amplitude": 4.625
  },
{
    "time": 14.886 ,
    "amplitude": 4.675
  },
{
    "time": 14.889 ,
    "amplitude": 4.705
  },
{
    "time": 14.892 ,
    "amplitude": 4.745
  },
{
    "time": 14.894 ,
    "amplitude": 4.795
  },
{
    "time": 14.897 ,
    "amplitude": 4.865
  },
{
    "time": 14.9 ,
    "amplitude": 4.89
  },
{
    "time": 14.903 ,
    "amplitude": 4.91
  },
{
    "time": 14.906 ,
    "amplitude": 4.915
  },
{
    "time": 14.908 ,
    "amplitude": 4.92
  },
{
    "time": 14.911 ,
    "amplitude": 4.935
  },
{
    "time": 14.914 ,
    "amplitude": 4.94
  },
{
    "time": 14.917 ,
    "amplitude": 4.95
  },
{
    "time": 14.919 ,
    "amplitude": 4.935
  },
{
    "time": 14.922 ,
    "amplitude": 4.935
  },
{
    "time": 14.925 ,
    "amplitude": 4.935
  },
{
    "time": 14.928 ,
    "amplitude": 4.955
  },
{
    "time": 14.931 ,
    "amplitude": 4.965
  },
{
    "time": 14.933 ,
    "amplitude": 4.965
  },
{
    "time": 14.936 ,
    "amplitude": 4.96
  },
{
    "time": 14.939 ,
    "amplitude": 4.965
  },
{
    "time": 14.942 ,
    "amplitude": 4.975
  },
{
    "time": 14.944 ,
    "amplitude": 4.965
  },
{
    "time": 14.947 ,
    "amplitude": 4.98
  },
{
    "time": 14.95 ,
    "amplitude": 4.97
  },
{
    "time": 14.953 ,
    "amplitude": 4.97
  },
{
    "time": 14.956 ,
    "amplitude": 4.98
  },
{
    "time": 14.958 ,
    "amplitude": 4.97
  },
{
    "time": 14.961 ,
    "amplitude": 4.98
  },
{
    "time": 14.964 ,
    "amplitude": 4.995
  },
{
    "time": 14.967 ,
    "amplitude": 4.97
  },
{
    "time": 14.969 ,
    "amplitude": 4.97
  },
{
    "time": 14.972 ,
    "amplitude": 4.96
  },
{
    "time": 14.975 ,
    "amplitude": 4.97
  },
{
    "time": 14.978 ,
    "amplitude": 4.99
  },
{
    "time": 14.981 ,
    "amplitude": 5.015
  },
{
    "time": 14.983 ,
    "amplitude": 5.015
  },
{
    "time": 14.986 ,
    "amplitude": 4.995
  },
{
    "time": 14.989 ,
    "amplitude": 5
  },
{
    "time": 14.992 ,
    "amplitude": 4.985
  },
{
    "time": 14.994 ,
    "amplitude": 4.995
  },
{
    "time": 14.997 ,
    "amplitude": 5.015
  }
]

# Create Analyzer
rWaveNotch = 4.9 # amplitude
thresholdForFeatureCount = 14 # number of features in buffer that indicate abnormality
timeSpan = .3 # seconds in between r-wave peaks that would indicate abnormality 
bufferLength = 60 # number of records in to check for features
RWaveAnalyzer = RWaveAnalysis(rWaveNotch, thresholdForFeatureCount, timeSpan, bufferLength)


def main():
  index = 0
  while index < len(sampleData):
    RWaveAnalyzer.analyze(sampleData[index])
    index+=1

main() 