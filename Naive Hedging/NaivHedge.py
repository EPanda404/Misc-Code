import sys
import math

class MarketData():
    def __init__(self, price, quantity):
        self.quantity = int(quantity)
        self.price = float(price)

class TradeRequest():
    def __init__(self, tradeRequestTokens):
        self.qty = int(tradeRequestTokens[0])
        self.riskPerQty = float(tradeRequestTokens[1])

    def ParseMarketData(mdLine):
        tokens = mdLine.split()
        return [MarketData(price, size) for price, size in zip(tokens[1::2], tokens[::2])]

class Hedger():
    def __init__(self, bids, offers):
        self.bids = bids
        self.offers = offers
        self.risk = 0

    def PassTrade(self, tradeRequest):
        self.risk = self.risk + (tradeRequest.qty * tradeRequest.riskPerQty)
        ret = ''
        riskQuant = abs(int(self.risk))

        if -1 < self.risk < 1:
            return None
        
        elif self.risk >= 1:
            ret = f'{riskQuant * -1} '
            
            orders = {}
            for i in self.bids:
                if riskQuant <= 0:
                    break
                if i.quantity <= 0:
                    next()
                
                if i.quantity < riskQuant:
                    orders.update({i.price: i.quantity})
                    riskQuant = riskQuant - i.quantity
                    i.quantity = 0
                    
                if i.quantity >= riskQuant:
                    orders.update({i.price: riskQuant})
                    i.quantity = i.quantity - riskQuant
                    riskQuant = 0
            
        elif self.risk <= -1:
            ret = f'{riskQuant} '
            
            orders = {}
            for i in self.offers:
                if riskQuant <= 0:
                    break
                if i.quantity <= 0:
                    next()
                
                if i.quantity < riskQuant:
                    orders.update({i.price: i.quantity})
                    riskQuant = riskQuant - i.quantity
                    i.quantity = 0
                    
                if i.quantity >= riskQuant:
                    orders.update({i.price: riskQuant})
                    i.quantity = i.quantity - riskQuant
                    riskQuant = 0
        
        sumnum = 0
        count = 0
        for i in orders:
            sumnum = sumnum + orders.get(i) * i
            count = orders.get(i)
                
        avg = sumnum / count
          
        ret = ret + f'{avg:.2f}'
            
        self.risk = self.risk % 1
        return ret
  
linesParsed=0

hedger = None
for line in sys.stdin:
    if linesParsed == 0:
        offers = TradeRequest.ParseMarketData(line)
        linesParsed += 1
    elif linesParsed == 1:
        bids = TradeRequest.ParseMarketData(line)
        hedger = Hedger(bids, offers)
        linesParsed += 1
        
    else:
        if hedger is None:
            raise Exception('no good')
        tradeRequest = TradeRequest(line.split())
        res = hedger.PassTrade(tradeRequest)
        if res is not None:
            print(res)
        linesParsed += 1