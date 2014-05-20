'''
Created on May 18, 2014

@author ardhani
'''
import urllib2

class GoogleFinance(object):

    def __init__(self, symbol=None):
        """
        Consutructor for GoogleFinance. 
        Here 'symbol' is optional.
        """
        self.symbol = symbol
    
    def __requestUrl__(self, symbol, interval, period):
        """
        Prepares the url required for fetching the data from google.
        """
        url = 'https://www.google.com/finance/getprices?q=%s&x=NSE&i=%s&p=%s&f=d,c,v,o,h,l' %(symbol, interval, period)
        return url
    
    def getQuote(self, symbol=None, interval=61, period="15m"):
        """
        getQuote method fetches the quotes of a symbol for the given amount 
        of time with a given interval.
        """
        if not self.symbol and not symbol:
            raise TypeError("symbol can't be null")

        if self.symbol:
            symbol = self.symbol
        elif symbol:
            self.symbol = symbol

        url = self.__requestUrl__(symbol, interval, period)
        print(url)
        try:
            data = urllib2.urlopen(url).read()
            data = data.split("\n")
            data = data[7:-1]
            if  data:
                fileHandler = open(symbol+".csv",'a')
                for quoteLine in data:
                    fileHandler.write(quoteLine)
                    fileHandler.write("\n")
                fileHandler.close()
                return True
            else:
                return False
        except Exception, err:
            print(err)
