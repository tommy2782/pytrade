#!/usr/bin/env python2.7

import os, sys
import finsymbols
import pandas as pd
local_path = os.path.dirname(__file__)
root = os.path.join(local_path, '..')
sys.path.append(root)
from yeod import daily_bars_getter as sp500
from ta import build as tabuild
from ta import merged as tamerge
from pred import pred

def main(argv):
    sp500.main(["",10])
    assert 0 == sp500.main(["",10])
    tabuild.main1(["",10])
    tamerge.main(["", "ta1"])
    #pred.main(["","ta1_GBCv1n1000md3_l5_s2000e2009", "ta1", "2016-06-09" ])
    
if __name__ == '__main__':
    main(sys.argv)



