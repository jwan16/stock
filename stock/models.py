from django.db import models
import django_tables2 as tables

class Company(models.Model):
    COM_StockCode = models.CharField(max_length=10)
    COM_Name = models.CharField(max_length=30)
    COM_LatestUpdate = models.DateTimeField(auto_created=True, auto_now=True)
    COM_IssuedShare = models.CharField(max_length=30)
    COM_ParCurrency = models.CharField(max_length=30)
    COM_ParValue = models.CharField(max_length=30)
    COM_Industry = models.CharField(max_length=30)
    COM_Profile = models.CharField(max_length=30000)
    COM_ListingDate = models.CharField(max_length=30)
    COM_AuthCapital = models.CharField(max_length=30)
    COM_IssuedCapital = models.CharField(max_length=30)
    COM_BoardLot = models.CharField(max_length=30)

    def __str__(self):
        return self.COM_StockCode

class CompanyTable(tables.Table):
    class Meta:
        model = Company
        exclude = ('COM_Profile')

class Technical(models.Model):
    TEC_COM_StockCode = models.CharField(max_length=10)
    TEC_LatestUpdate = models.DateTimeField(auto_created=True, auto_now=True)
    TEC_ClosingPrice = models.CharField(max_length=30)
    TEC_1MonthChange = models.CharField(max_length=30)
    TEC_3MonthChange = models.CharField(max_length=30)
    TEC_52WeekChange = models.CharField(max_length=30)
    TEC_1MonthHSIRelative = models.CharField(max_length=30)
    TEC_3MonthHSIRelative = models.CharField(max_length=30)
    TEC_52WeekHSIRelative = models.CharField(max_length=30)
    TEC_MarketCapital = models.CharField(max_length=30)
    TEC_52WeekHigh = models.CharField(max_length=30)
    TEC_52WeekLow = models.CharField(max_length=30)
    TEC_1MonthAvgVol = models.CharField(max_length=30)
    TEC_3MonthAvgVol = models.CharField(max_length=30)
    TEC_10DayMovingAvg = models.CharField(max_length=30)
    TEC_50DayMovingAvg = models.CharField(max_length=30)
    TEC_90DayMovingAvg = models.CharField(max_length=30)
    TEC_250DayMovingAvg = models.CharField(max_length=30)
    TEC_14DayRSI = models.CharField(max_length=30)

    def __str__(self):
        return self.TEC_COM_StockCode

class Ratio(models.Model):
    RAT_COM_StockCode = models.CharField(max_length=10)
    RAT_LatestUpdate = models.DateTimeField(auto_created=True, auto_now=True)
    RAT_Year = models.DateField()
    RAT_CurrentRatio = models.FloatField(null=True)
    RAT_QuickRatio = models.FloatField(null=True)
    RAT_LTDebtEquity = models.FloatField(null=True)
    RAT_TotalDebtEquity = models.FloatField(null=True)
    RAT_TotalDebtCapital = models.FloatField(null=True)
    RAT_ROE = models.FloatField(null=True)
    RAT_ROC = models.FloatField(null=True)
    RAT_ROTA = models.FloatField(null=True)
    RAT_OPM = models.FloatField(null=True)
    RAT_PreTaxPM = models.FloatField(null=True)
    RAT_NetPM = models.FloatField(null=True)
    RAT_InventoryTurnover = models.FloatField(null=True)
    RAT_DividendPayout = models.FloatField(null=True)
    RAT_NP = models.FloatField(null=True)
    RAT_NPG = models.FloatField(null=True)
    RAT_EPS = models.FloatField(null=True)
    RAT_EPSGrowth = models.FloatField(null=True)
    RAT_DPS = models.FloatField(null=True)
    RAT_PE = models.FloatField(null=True)
    RAT_Yield = models.FloatField(null=True)
    RAT_NAV = models.FloatField(null=True)
    RAT_Currency = models.FloatField(null=True)

    def __str__(self):
        return self.RAT_COM_StockCode

class Historical_Price(models.Model):
    HIS_COM_StockCode = models.IntegerField()
    HIS_Date = models.DateField()
    HIS_Open = models.IntegerField()
    HIS_Low = models.IntegerField()
    HIS_Close = models.IntegerField()
    HIS_Adj_Close = models.IntegerField()
    HIS_Volume = models.IntegerField()