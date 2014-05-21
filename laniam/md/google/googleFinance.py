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

        url = self.__requestUrl__(self.symbol, interval, period)
        try:
            data = urllib2.urlopen(url).read()
            data = data.split("\n")
            data = data[7:-1]
            if  data:
                for i  in range(len(data)):
                    data[i] = data[i][1:]
                return data
            else:
                return []
        except Exception, err:
            print(err)

    def writeQuoteToFile(self, symbol=None, interval=61, period="15m"):
        """
        """
        if self.symbol or symbol:
            if not self.symbol:
                self.symbol = symbol
        else:
            raise TypeError("symbol can't be null")
        
        lastIndex = self.__getLastIndex()
        data = self.getQuote(self.symbol, interval, period)
        file_handler = open(self.symbol+".csv", "a")
        for row in data:
            rowValues = row.split(',') 
            index = int(rowValues[0])
            if index > lastIndex:
                file_handler.write(row+'\n')
        file_handler.close()

    def __getLastIndex(self):
        """
        """
        try:
            file_handler  = open(self.symbol+".csv")
            file_content  = file_handler.read()
            splitLines    = file_content.split('\n')
            lastIndexLine = splitLines[-2] 
            lastIndex     = int(lastIndexLine.split(',')[0])
            file_handler.close()
        except:
            lastIndex     = 0
        return lastIndex 
