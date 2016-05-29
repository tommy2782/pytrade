
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author hongbin@youzan.com
import os,sys
import talib

local_path = os.path.dirname(__file__)
root = os.path.join(local_path, '..')
sys.path.append(root)

import strategy_mining.model_base as base

def diff(df, key, shink, shift=1):
    df["ta_diff_%s_%d_%d" % (key, shink, shift)] = (df[key]/df[key].shift(shift)).shift(shink)
    return df


def adx(df, timeperiod = 14):
    """
    ADX(high, low, close[, timeperiod=?])
    Average Directional Movement Index (Momentum Indicators)
    Inputs:
        prices: ['high', 'low', 'close']
    Parameters:
        timeperiod: 14
    Outputs:
        real
    """
    npAdx = talib.ADX(df.high.values, df.low.values, df.close.values, timeperiod)
    df["ta_adx_" + str(timeperiod)] = npAdx
    npAdxr = talib.ADXR(df.high.values, df.low.values, df.close.values, timeperiod)
    df["ta_adxr_" + str(timeperiod)] = npAdx
    npMdi = talib.MINUS_DI(df.high.values, df.low.values, df.close.values, timeperiod)
    df["ta_mdi_" + str(timeperiod)] = npMdi
    npMdi = talib.PLUS_DI(df.high.values, df.low.values, df.close.values, timeperiod)
    df["ta_pdi_" + str(timeperiod)] = npMdi
    return df

def apo(df, fastperiod=12, slowperiod=26, matype=0):
    """
    Absolute Price Oscillator (Momentum Indicators)

    """
    npApo = talib.APO(df.close.values, fastperiod, slowperiod, matype)
    df['ta_apo_%d_%d_%d'%(fastperiod, slowperiod, matype)] = npApo
    return df

def aroon(df, timeperiod=14):
    """
    Aroon (Momentum Indicators)
    """
    npUp, npDown = talib.AROON(df.high.values, df.low.values, timeperiod)
    df["ta_aroon_up_" + str(timeperiod)] = npUp 
    df["ta_aroon_down_" + str(timeperiod)] = npDown
    df['ta_aroonosc_' + str(timeperiod)] = talib.AROONOSC(df.high.values, df.low.values, timeperiod) 
    return df

def ad(df):
    """
    Chaikin A/D Line (Volume Indicators)
    """
    npAd = talib.AD(df.high.values, df.low.values, df.close.values, df.volume.values)
    df["ta_ad"] = npAd
    return df
def adosc(df, fastperiod = 3, slowperiod = 10):
    """
    Chaikin A/D Oscillator (Volume Indicators)
    """
    npAdosc = talib.ADOSC(df.high.values, df.low.values, df.close.values, df.volume.values, fastperiod, slowperiod)
    df["ta_adsoc"] = npAdosc
    return df

def obv(df, fastperiod = 3, slowperiod = 10):
    """
    On Balance Volume (Volume Indicators)
    """
    df["ta_obv"] = talib.OBV(df.close.values, df.volume.values)
    return df

def atr(df, timeperiod = 14):
    """
    Average True Range (Volatility Indicators)
    """
    df["ta_atr_" + str(timeperiod)] = talib.ATR(df.high.values, df.low.values, df.close.values, timeperiod)
    return df

def natr(df, timeperiod = 14):
    """
    Normalized Average True Range (Volatility Indicators)
    """
    df["ta_natr_" + str(timeperiod)] = talib.NATR(df.high.values, df.low.values, df.close.values, timeperiod)
    return df

def trange(df):
    """
    True Range (Volatility Indicators)
    """
    df["ta_trange"] = talib.TRANGE(df.high.values, df.low.values, df.close.values)
    return df



def CEIL(df): # real signature unknown; restored from __doc__
    """
    CEIL(real)

        Vector Ceil (Math Transform)

        Inputs:
            real: (any ndarray)
        Outputs:
            real
    """
    df["ta_CEIL"] = talib.CEIL(df.close.values)
    return df

def CMO(df, timeperiod=14): # real signature unknown; NOTE: unreliably restored from __doc__
    """
    CMO(real[, timeperiod=?])

        Chande Momentum Oscillator (Momentum Indicators)

        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 14
        Outputs:
            real
    """
    df["ta_CMO"] = talib.CMO(df.close.values, timeperiod=14)
    return df

def DEMA(real, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
    """
    DEMA(real[, timeperiod=?])

        Double Exponential Moving Average (Overlap Studies)

        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 30
        Outputs:
            real
    """
    df["ta_DEMA"] = talib.DEMA(df.close.values, timeperiod = 30)
    return df

def DX(high, low, close, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
    """
    DX(high, low, close[, timeperiod=?])

        Directional Movement Index (Momentum Indicators)

        Inputs:
            prices: ['high', 'low', 'close']
        Parameters:
            timeperiod: 14
        Outputs:
            real
    """
    pass

def EMA(real, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
    """
    EMA(real[, timeperiod=?])

        Exponential Moving Average (Overlap Studies)

        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 30
        Outputs:
            real
    """
    pass

def EXP(real): # real signature unknown; restored from __doc__
    """
    EXP(real)

        Vector Arithmetic Exp (Math Transform)

        Inputs:
            real: (any ndarray)
        Outputs:
            real
    """
    pass

def FLOOR(real): # real signature unknown; restored from __doc__
    """
    FLOOR(real)

        Vector Floor (Math Transform)

        Inputs:
            real: (any ndarray)
        Outputs:
            real
    """
    pass

def HT_DCPERIOD(real): # real signature unknown; restored from __doc__
    """
    HT_DCPERIOD(real)

        Hilbert Transform - Dominant Cycle Period (Cycle Indicators)

        Inputs:
            real: (any ndarray)
        Outputs:
            real
    """
    pass

def HT_DCPHASE(real): # real signature unknown; restored from __doc__
    """
    HT_DCPHASE(real)

        Hilbert Transform - Dominant Cycle Phase (Cycle Indicators)

        Inputs:
            real: (any ndarray)
        Outputs:
            real
    """
    pass

def HT_PHASOR(real): # real signature unknown; restored from __doc__
    """
    HT_PHASOR(real)

        Hilbert Transform - Phasor Components (Cycle Indicators)

        Inputs:
            real: (any ndarray)
        Outputs:
            inphase
            quadrature
    """
    pass

def HT_SINE(real): # real signature unknown; restored from __doc__
    """
    HT_SINE(real)

        Hilbert Transform - SineWave (Cycle Indicators)

        Inputs:
            real: (any ndarray)
        Outputs:
            sine
            leadsine
    """
    pass

def HT_TRENDLINE(real): # real signature unknown; restored from __doc__
    """
    HT_TRENDLINE(real)

        Hilbert Transform - Instantaneous Trendline (Overlap Studies)

        Inputs:
            real: (any ndarray)
        Outputs:
            real
    """
    pass

def HT_TRENDMODE(real): # real signature unknown; restored from __doc__
    """
    HT_TRENDMODE(real)

        Hilbert Transform - Trend vs Cycle Mode (Cycle Indicators)

        Inputs:
            real: (any ndarray)
        Outputs:
            integer (values are -100, 0 or 100)
    """
    pass

def KAMA(real, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
    """
    KAMA(real[, timeperiod=?])

        Kaufman Adaptive Moving Average (Overlap Studies)

        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 30
        Outputs:
            real
    """
    pass

def LINEARREG(real, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
    """
    LINEARREG(real[, timeperiod=?])

        Linear Regression (Statistic Functions)

        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 14
        Outputs:
            real
    """
    pass

def LINEARREG_ANGLE(real, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
    """
    LINEARREG_ANGLE(real[, timeperiod=?])

        Linear Regression Angle (Statistic Functions)

        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 14
        Outputs:
            real
    """
    pass

def LINEARREG_INTERCEPT(real, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
    """
    LINEARREG_INTERCEPT(real[, timeperiod=?])

        Linear Regression Intercept (Statistic Functions)

        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 14
        Outputs:
            real
    """
    pass

def LINEARREG_SLOPE(real, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
    """
    LINEARREG_SLOPE(real[, timeperiod=?])

        Linear Regression Slope (Statistic Functions)

        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 14
        Outputs:
            real
    """
    pass

def LN(real): # real signature unknown; restored from __doc__
    """
    LN(real)

        Vector Log Natural (Math Transform)

        Inputs:
            real: (any ndarray)
        Outputs:
            real
    """
    pass

def LOG10(real): # real signature unknown; restored from __doc__
    """
    LOG10(real)

        Vector Log10 (Math Transform)

        Inputs:
            real: (any ndarray)
        Outputs:
            real
    """
    pass

def MA(real, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
    """
    MA(real[, timeperiod=?, matype=?])

        Moving average (Overlap Studies)

        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 30
            matype: 0 (Simple Moving Average)
        Outputs:
            real
    """
    pass

def MACD(real, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
    """
    MACD(real[, fastperiod=?, slowperiod=?, signalperiod=?])

        Moving Average Convergence/Divergence (Momentum Indicators)

        Inputs:
            real: (any ndarray)
        Parameters:
            fastperiod: 12
            slowperiod: 26
            signalperiod: 9
        Outputs:
            macd
            macdsignal
            macdhist
    """
    pass

def MACDEXT(real, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
    """
    MACDEXT(real[, fastperiod=?, fastmatype=?, slowperiod=?, slowmatype=?, signalperiod=?, signalmatype=?])

        MACD with controllable MA type (Momentum Indicators)

        Inputs:
            real: (any ndarray)
        Parameters:
            fastperiod: 12
            fastmatype: 0
            slowperiod: 26
            slowmatype: 0
            signalperiod: 9
            signalmatype: 0
        Outputs:
            macd
            macdsignal
            macdhist
    """
    pass

def MACDFIX(real, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
    """
    MACDFIX(real[, signalperiod=?])

        Moving Average Convergence/Divergence Fix 12/26 (Momentum Indicators)

        Inputs:
            real: (any ndarray)
        Parameters:
            signalperiod: 9
        Outputs:
            macd
            macdsignal
            macdhist
    """
    pass

def MAMA(real, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
    """
    MAMA(real[, fastlimit=?, slowlimit=?])

        MESA Adaptive Moving Average (Overlap Studies)

        Inputs:
            real: (any ndarray)
        Parameters:
            fastlimit: 0.5
            slowlimit: 0.05
        Outputs:
            mama
            fama
    """
    pass

def MAVP(real, periods, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
    """
    MAVP(real, periods[, minperiod=?, maxperiod=?, matype=?])

        Moving average with variable period (Overlap Studies)

        Inputs:
            real: (any ndarray)
            periods: (any ndarray)
        Parameters:
            minperiod: 2
            maxperiod: 30
            matype: 0 (Simple Moving Average)
        Outputs:
            real
    """
    pass

def MAX(real, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
    """
    MAX(real[, timeperiod=?])

        Highest value over a specified period (Math Operators)

        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 30
        Outputs:
            real
    """
    pass

def MAXINDEX(real, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
    """
    MAXINDEX(real[, timeperiod=?])

        Index of highest value over a specified period (Math Operators)

        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 30
        Outputs:
            integer (values are -100, 0 or 100)
    """
    pass

def MEDPRICE(high, low): # real signature unknown; restored from __doc__
    """
    MEDPRICE(high, low)

        Median Price (Price Transform)

        Inputs:
            prices: ['high', 'low']
        Outputs:
            real
    """
    pass

def MFI(high, low, close, volume, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
    """
    MFI(high, low, close, volume[, timeperiod=?])

        Money Flow Index (Momentum Indicators)

        Inputs:
            prices: ['high', 'low', 'close', 'volume']
        Parameters:
            timeperiod: 14
        Outputs:
            real
    """
    pass

def MIDPOINT(real, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
    """
    MIDPOINT(real[, timeperiod=?])

        MidPoint over period (Overlap Studies)

        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 14
        Outputs:
            real
    """
    pass

def MIDPRICE(high, low, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
    """
    MIDPRICE(high, low[, timeperiod=?])

        Midpoint Price over period (Overlap Studies)

        Inputs:
            prices: ['high', 'low']
        Parameters:
            timeperiod: 14
        Outputs:
            real
    """
    pass

def MIN(real, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
    """
    MIN(real[, timeperiod=?])

        Lowest value over a specified period (Math Operators)

        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 30
        Outputs:
            real
    """
    pass

def MININDEX(real, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
    """
    MININDEX(real[, timeperiod=?])

        Index of lowest value over a specified period (Math Operators)

        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 30
        Outputs:
            integer (values are -100, 0 or 100)
    """
    pass

def MINMAX(real, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
    """
    MINMAX(real[, timeperiod=?])

        Lowest and highest values over a specified period (Math Operators)

        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 30
        Outputs:
            min
            max
    """
    pass

def MINMAXINDEX(real, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
    """
    MINMAXINDEX(real[, timeperiod=?])

        Indexes of lowest and highest values over a specified period (Math Operators)

        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 30
        Outputs:
            minidx
            maxidx
    """
    pass

def MINUS_DI(high, low, close, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
    """
    MINUS_DI(high, low, close[, timeperiod=?])

        Minus Directional Indicator (Momentum Indicators)

        Inputs:
            prices: ['high', 'low', 'close']
        Parameters:
            timeperiod: 14
        Outputs:
            real
    """
    pass

def MINUS_DM(high, low, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
    """
    MINUS_DM(high, low[, timeperiod=?])

        Minus Directional Movement (Momentum Indicators)

        Inputs:
            prices: ['high', 'low']
        Parameters:
            timeperiod: 14
        Outputs:
            real
    """
    pass

def MOM(real, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
    """
    MOM(real[, timeperiod=?])

        Momentum (Momentum Indicators)

        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 10
        Outputs:
            real
    """
    pass

def MULT(real0, real1): # real signature unknown; restored from __doc__
    """
    MULT(real0, real1)

        Vector Arithmetic Mult (Math Operators)

        Inputs:
            real0: (any ndarray)
            real1: (any ndarray)
        Outputs:
            real
    """
    pass

def NATR(high, low, close, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
    """
    NATR(high, low, close[, timeperiod=?])

        Normalized Average True Range (Volatility Indicators)

        Inputs:
            prices: ['high', 'low', 'close']
        Parameters:
            timeperiod: 14
        Outputs:
            real
    """
    pass

def OBV(real, volume): # real signature unknown; restored from __doc__
    """
    OBV(real, volume)

        On Balance Volume (Volume Indicators)

        Inputs:
            real: (any ndarray)
            prices: ['volume']
        Outputs:
            real
    """
    pass

def PLUS_DI(high, low, close, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
    """
    PLUS_DI(high, low, close[, timeperiod=?])

        Plus Directional Indicator (Momentum Indicators)

        Inputs:
            prices: ['high', 'low', 'close']
        Parameters:
            timeperiod: 14
        Outputs:
            real
    """
    pass

def PLUS_DM(high, low, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
    """
    PLUS_DM(high, low[, timeperiod=?])

        Plus Directional Movement (Momentum Indicators)

        Inputs:
            prices: ['high', 'low']
        Parameters:
            timeperiod: 14
        Outputs:
            real
    """
    pass

def PPO(real, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
    """
    PPO(real[, fastperiod=?, slowperiod=?, matype=?])

        Percentage Price Oscillator (Momentum Indicators)

        Inputs:
            real: (any ndarray)
        Parameters:
            fastperiod: 12
            slowperiod: 26
            matype: 0 (Simple Moving Average)
        Outputs:
            real
    """
    pass

def ROC(real, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
    """
    ROC(real[, timeperiod=?])

        Rate of change : ((real/prevPrice)-1)*100 (Momentum Indicators)

        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 10
        Outputs:
            real
    """
    pass

def ROCP(real, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
    """
    ROCP(real[, timeperiod=?])

        Rate of change Percentage: (real-prevPrice)/prevPrice (Momentum Indicators)

        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 10
        Outputs:
            real
    """
    pass

def ROCR(real, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
    """
    ROCR(real[, timeperiod=?])

        Rate of change ratio: (real/prevPrice) (Momentum Indicators)

        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 10
        Outputs:
            real
    """
    pass

def ROCR100(real, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
    """
    ROCR100(real[, timeperiod=?])

        Rate of change ratio 100 scale: (real/prevPrice)*100 (Momentum Indicators)

        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 10
        Outputs:
            real
    """
    pass

def RSI(real, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
    """
    RSI(real[, timeperiod=?])

        Relative Strength Index (Momentum Indicators)

        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 14
        Outputs:
            real
    """
    pass

def SAR(high, low, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
    """
    SAR(high, low[, acceleration=?, maximum=?])

        Parabolic SAR (Overlap Studies)

        Inputs:
            prices: ['high', 'low']
        Parameters:
            acceleration: 0.02
            maximum: 0.2
        Outputs:
            real
    """
    pass

def SAREXT(high, low, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
    """
    SAREXT(high, low[, startvalue=?, offsetonreverse=?, accelerationinitlong=?, accelerationlong=?, accelerationmaxlong=?, accelerationinitshort=?, accelerationshort=?, accelerationmaxshort=?])

        Parabolic SAR - Extended (Overlap Studies)

        Inputs:
            prices: ['high', 'low']
        Parameters:
            startvalue: 0
            offsetonreverse: 0
            accelerationinitlong: 0.02
            accelerationlong: 0.02
            accelerationmaxlong: 0.2
            accelerationinitshort: 0.02
            accelerationshort: 0.02
            accelerationmaxshort: 0.2
        Outputs:
            real
    """
    pass

def SIN(real): # real signature unknown; restored from __doc__
    """
    SIN(real)

        Vector Trigonometric Sin (Math Transform)

        Inputs:
            real: (any ndarray)
        Outputs:
            real
    """
    pass

def SINH(real): # real signature unknown; restored from __doc__
    """
    SINH(real)

        Vector Trigonometric Sinh (Math Transform)

        Inputs:
            real: (any ndarray)
        Outputs:
            real
    """
    pass

def SMA(real, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
    """
    SMA(real[, timeperiod=?])

        Simple Moving Average (Overlap Studies)

        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 30
        Outputs:
            real
    """
    pass

def SQRT(real): # real signature unknown; restored from __doc__
    """
    SQRT(real)

        Vector Square Root (Math Transform)

        Inputs:
            real: (any ndarray)
        Outputs:
            real
    """
    pass

def STDDEV(real, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
    """
    STDDEV(real[, timeperiod=?, nbdev=?])

        Standard Deviation (Statistic Functions)

        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 5
            nbdev: 1
        Outputs:
            real
    """
    pass

def STOCH(high, low, close, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
    """
    STOCH(high, low, close[, fastk_period=?, slowk_period=?, slowk_matype=?, slowd_period=?, slowd_matype=?])

        Stochastic (Momentum Indicators)

        Inputs:
            prices: ['high', 'low', 'close']
        Parameters:
            fastk_period: 5
            slowk_period: 3
            slowk_matype: 0
            slowd_period: 3
            slowd_matype: 0
        Outputs:
            slowk
            slowd
    """
    pass

def STOCHF(high, low, close, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
    """
    STOCHF(high, low, close[, fastk_period=?, fastd_period=?, fastd_matype=?])

        Stochastic Fast (Momentum Indicators)

        Inputs:
            prices: ['high', 'low', 'close']
        Parameters:
            fastk_period: 5
            fastd_period: 3
            fastd_matype: 0
        Outputs:
            fastk
            fastd
    """
    pass

def STOCHRSI(real, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
    """
    STOCHRSI(real[, timeperiod=?, fastk_period=?, fastd_period=?, fastd_matype=?])

        Stochastic Relative Strength Index (Momentum Indicators)

        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 14
            fastk_period: 5
            fastd_period: 3
            fastd_matype: 0
        Outputs:
            fastk
            fastd
    """
    pass

def SUB(real0, real1): # real signature unknown; restored from __doc__
    """
    SUB(real0, real1)

        Vector Arithmetic Substraction (Math Operators)

        Inputs:
            real0: (any ndarray)
            real1: (any ndarray)
        Outputs:
            real
    """
    pass

def SUM(real, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
    """
    SUM(real[, timeperiod=?])

        Summation (Math Operators)

        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 30
        Outputs:
            real
    """
    pass

def T3(real, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
    """
    T3(real[, timeperiod=?, vfactor=?])

        Triple Exponential Moving Average (T3) (Overlap Studies)

        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 5
            vfactor: 0.7
        Outputs:
            real
    """
    pass

def TAN(real): # real signature unknown; restored from __doc__
    """
    TAN(real)

        Vector Trigonometric Tan (Math Transform)

        Inputs:
            real: (any ndarray)
        Outputs:
            real
    """
    pass

def TANH(real): # real signature unknown; restored from __doc__
    """
    TANH(real)

        Vector Trigonometric Tanh (Math Transform)

        Inputs:
            real: (any ndarray)
        Outputs:
            real
    """
    pass

def TEMA(real, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
    """
    TEMA(real[, timeperiod=?])

        Triple Exponential Moving Average (Overlap Studies)

        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 30
        Outputs:
            real
    """
    pass

def TRANGE(high, low, close): # real signature unknown; restored from __doc__
    """
    TRANGE(high, low, close)

        True Range (Volatility Indicators)

        Inputs:
            prices: ['high', 'low', 'close']
        Outputs:
            real
    """
    pass

def TRIMA(real, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
    """
    TRIMA(real[, timeperiod=?])

        Triangular Moving Average (Overlap Studies)

        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 30
        Outputs:
            real
    """
    pass

def TRIX(real, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
    """
    TRIX(real[, timeperiod=?])

        1-day Rate-Of-Change (ROC) of a Triple Smooth EMA (Momentum Indicators)

        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 30
        Outputs:
            real
    """
    pass

def TSF(real, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
    """
    TSF(real[, timeperiod=?])

        Time Series Forecast (Statistic Functions)

        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 14
        Outputs:
            real
    """
    pass

def TYPPRICE(high, low, close): # real signature unknown; restored from __doc__
    """
    TYPPRICE(high, low, close)

        Typical Price (Price Transform)

        Inputs:
            prices: ['high', 'low', 'close']
        Outputs:
            real
    """
    pass

def ULTOSC(high, low, close, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
    """
    ULTOSC(high, low, close[, timeperiod1=?, timeperiod2=?, timeperiod3=?])

        Ultimate Oscillator (Momentum Indicators)

        Inputs:
            prices: ['high', 'low', 'close']
        Parameters:
            timeperiod1: 7
            timeperiod2: 14
            timeperiod3: 28
        Outputs:
            real
    """
    pass

def VAR(real, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
    """
    VAR(real[, timeperiod=?, nbdev=?])

        Variance (Statistic Functions)

        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 5
            nbdev: 1
        Outputs:
            real
    """
    pass

def WCLPRICE(high, low, close): # real signature unknown; restored from __doc__
    """
    WCLPRICE(high, low, close)

        Weighted Close Price (Price Transform)

        Inputs:
            prices: ['high', 'low', 'close']
        Outputs:
            real
    """
    pass

def WILLR(high, low, close, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
    """
    WILLR(high, low, close[, timeperiod=?])

        Williams' %R (Momentum Indicators)

        Inputs:
            prices: ['high', 'low', 'close']
        Parameters:
            timeperiod: 14
        Outputs:
            real
    """
    pass

def WMA(real, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__
    """
    WMA(real[, timeperiod=?])

        Weighted Moving Average (Overlap Studies)

        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 30
        Outputs:
            real
    """
    pass


def cdl(df):
    open = df.open.values
    high = df.high.values
    low = df.low.values
    close = df.close.values
    df["ta_cdl3blackcrows"] = talib.CDL3BLACKCROWS(open, high, low, close)
    df["ta_cdl3inside"] = talib.CDL3INSIDE(open, high, low, close)
    df["ta_cdl3linestrike"] = talib.CDL3LINESTRIKE(open, high, low, close)
    df["ta_cdl3outside"] = talib.CDL3OUTSIDE(open, high, low, close)
    df["ta_cdl3starsinsouth"] = talib.CDL3STARSINSOUTH(open, high, low, close)
    df["ta_cdl3whitesoldiers"] = talib.CDL3WHITESOLDIERS(open, high, low, close)
    df["ta_cdladandonedbaby"] = talib.CDLABANDONEDBABY(open, high, low, close) #? penetration
    df["ta_CDLADVANCEBLOCK"] = talib.CDLADVANCEBLOCK(open, high, low, close)
    df["ta_CDLBELTHOLD"] = talib.CDLBELTHOLD(open, high, low, close)
    df["ta_CDLBREAKAWAY"] = talib.CDLBREAKAWAY(open, high, low, close)
    df["ta_CDLCLOSINGMARUBOZU"] = talib.CDLCLOSINGMARUBOZU(open, high, low, close)
    df["ta_CDLCONCEALBABYSWALL"] = talib.CDLCONCEALBABYSWALL(open, high, low, close)
    df["ta_CDLCOUNTERATTACK"] = talib.CDLCOUNTERATTACK(open, high, low, close)
    df["ta_CDLDARKCLOUDCOVER"] = talib.CDLDARKCLOUDCOVER(open, high, low, close) #? penetration
    df["ta_CDLDARKCLOUDCOVER"] = talib.CDLDARKCLOUDCOVER(open, high, low, close) #? penetration
    df["ta_CDLDOJI"] = talib.CDLDOJI(open, high, low, close)
    df["ta_CDLDOJISTAR"] = talib.CDLDOJISTAR(open, high, low, close)
    df["ta_CDLDRAGONFLYDOJI"] = talib.CDLDRAGONFLYDOJI(open, high, low, close)
    df["ta_CDLENGULFING"] = talib.CDLENGULFING(open, high, low, close)
    df["ta_CDLEVENINGDOJISTAR"] = talib.CDLEVENINGDOJISTAR(open, high, low, close) #? penetration
    df["ta_CDLEVENINGSTAR"] = talib.CDLEVENINGSTAR(open, high, low, close) #? penetration
    df["ta_CDLGAPSIDESIDEWHITE"] = talib.CDLGAPSIDESIDEWHITE(open, high, low, close)
    df["ta_CDLGRAVESTONEDOJI"] = talib.CDLGRAVESTONEDOJI(open, high, low, close)
    df["ta_CDLHAMMER"] = talib.CDLHAMMER(open, high, low, close)
    df["ta_CDLHANGINGMAN"] = talib.CDLHANGINGMAN(open, high, low, close)
    df["ta_CDLHARAMI"] = talib.CDLHARAMI(open, high, low, close)
    df["ta_CDLHARAMICROSS"] = talib.CDLHARAMICROSS(open, high, low, close)
    df["ta_CDLHIGHWAVE"] = talib.CDLHIGHWAVE(open, high, low, close)
    df["ta_CDLHIKKAKE"] = talib.CDLHIKKAKE(open, high, low, close)
    df["ta_CDLHIKKAKEMOD"] = talib.CDLHIKKAKEMOD(open, high, low, close)
    df["ta_CDLHOMINGPIGEON"] = talib.CDLHOMINGPIGEON(open, high, low, close)
    df["ta_CDLIDENTICAL3CROWS"] = talib.CDLIDENTICAL3CROWS(open, high, low, close)
    df["ta_CDLINNECK"] = talib.CDLINNECK(open, high, low, close)
    df["ta_CDLINVERTEDHAMMER"] = talib.CDLINVERTEDHAMMER(open, high, low, close)
    df["ta_CDLKICKING"] = talib.CDLKICKING(open, high, low, close)
    df["ta_CDLKICKINGBYLENGTH"] = talib.CDLKICKINGBYLENGTH(open, high, low, close)
    df["ta_CDLLADDERBOTTOM"] = talib.CDLLADDERBOTTOM(open, high, low, close)
    df["ta_CDLLONGLEGGEDDOJI"] = talib.CDLLONGLEGGEDDOJI(open, high, low, close)
    df["ta_CDLLONGLINE"] = talib.CDLLONGLINE(open, high, low, close)
    df["ta_CDLMARUBOZU"] = talib.CDLMARUBOZU(open, high, low, close)
    df["ta_CDLMATCHINGLOW"] = talib.CDLMATCHINGLOW(open, high, low, close)
    df["ta_CDLMATHOLD"] = talib.CDLMATHOLD(open, high, low, close) #? penetration
    df["ta_CDLMORNINGDOJISTAR"] = talib.CDLMORNINGDOJISTAR(open, high, low, close) #? penetration
    df["ta_CDLMORNINGSTAR"] = talib.CDLMORNINGSTAR(open, high, low, close) #? penetration
    df["ta_CDLONNECK"] = talib.CDLONNECK(open, high, low, close)
    df["ta_CDLPIERCING"] = talib.CDLPIERCING(open, high, low, close)
    df["ta_CDLRICKSHAWMAN"] = talib.CDLRICKSHAWMAN(open, high, low, close)
    df["ta_CDLRISEFALL3METHODS"] = talib.CDLRISEFALL3METHODS(open, high, low, close)
    df["ta_CDLSEPARATINGLINES"] = talib.CDLSEPARATINGLINES(open, high, low, close)
    df["ta_CDLSHOOTINGSTAR"] = talib.CDLSHOOTINGSTAR(open, high, low, close)
    df["ta_CDLSHORTLINE"] = talib.CDLSHORTLINE(open, high, low, close)
    df["ta_CDLSPINNINGTOP"] = talib.CDLSPINNINGTOP(open, high, low, close)
    df["ta_CDLSTALLEDPATTERN"] = talib.CDLSTALLEDPATTERN(open, high, low, close)
    df["ta_CDLSTICKSANDWICH"] = talib.CDLSTICKSANDWICH(open, high, low, close)
    df["ta_CDLTAKURI"] = talib.CDLTAKURI(open, high, low, close)
    df["ta_CDLTASUKIGAP"] = talib.CDLTASUKIGAP(open, high, low, close)
    df["ta_CDLTHRUSTING"] = talib.CDLTHRUSTING(open, high, low, close)
    df["ta_CDLTRISTAR"] = talib.CDLTRISTAR(open, high, low, close)
    df["ta_CDLUNIQUE3RIVER"] = talib.CDLUNIQUE3RIVER(open, high, low, close)
    df["ta_CDLUPSIDEGAP2CROWS"] = talib.CDLUPSIDEGAP2CROWS(open, high, low, close)
    df["ta_CDLXSIDEGAP3METHODS"] = talib.CDLXSIDEGAP3METHODS(open, high, low, close)
    return df


def cal_all(df):
    df = adx(df, timeperiod = 14)
    for i in range(14):
        df = diff(df, "ta_adx_14", i, 1)
    for i in range(14):
        df = diff(df, "ta_mdi_14", i, 1)
    for i in range(14):
        df = diff(df, "ta_pdi_14", i, 1)
    for i in range(14):
        df = diff(df, "close", i, 1)
    #df = diff(df, 0,1) 
    #df = diff(df, 1,1) 
    #df = diff(df, 2,1) 
    #df = diff(df, 3,1) 
    df = apo(df, 12, 26, 0)
    df = aroon(df, 14)
    df = ad(df)
    df = adosc(df)
    df = obv(df)
    df = atr(df, timeperiod = 14)
    df = natr(df, timeperiod = 14)
    df = trange(df)
    return df

def call2(df):
    df = cdl(df)
    return df

if __name__ == '__main__':
    df = base.get_stock_data_pd("A")
    print cal_all(df).head(10)
    #print adx(df).tail(1)