"""Super Simple Stocks Assignment """
from datetime import datetime, timedelta
from functools import reduce
from math import pow
from typing import Union

class Stock:
    """object to represent a given stock"""
    def __init__(self,symbol: str,type_: str,par_value: Union[float,int],price: Union[float,int],last_dividend=0,fixed_dividend=None):
        self.symbol=symbol
        self.type=type_ 
        self.par_value=par_value
        self.price=price
        self.last_dividend=last_dividend if last_dividend != 0 else 0 
        self.fixed_dividend=fixed_dividend if fixed_dividend != None else None  
        self.trades = []
    """calculate the common dividend yield for a stock"""
    def calc_common_div_yield(self,price):
        return self.last_dividend / price
    """calculate the preferred dividend yield for a stock"""
    def calc_preferred_div_yield(self,price):
        return (self.fixed_dividend*self.par_value) / price
    """calculate the price to earning ratio for a stock"""
    def calc_p_e_ratio(self,price):
        if self.type == "Common":
            result = price / self.calc_common_div_yield(price)
        elif self.type == "Preferred":
            result = price / self.calc_preferred_div_yield(price)
        return result
    def record_trade(self, quantity, indicator, price):
        timestamp = datetime.now()
        self.timestamp=timestamp
        trade = Trade(timestamp, quantity, indicator, price)
        self.trades.append(trade)

    def calc_volume_weighted_stock_price(self):
        five_minutes_ago = datetime.now() - timedelta(minutes=5)
        recent_trades = [trade for trade in self.trades if trade.timestamp >= five_minutes_ago]
        total_price_quantity = sum([trade.price * trade.quantity for trade in recent_trades])
        total_quantity = sum([trade.quantity for trade in recent_trades])
        
        if total_quantity == 0:
            return 0
        
        return total_price_quantity / total_quantity

class Trade:
    """object representing a trade"""
    def __init__(self, timestamp: datetime, quantity: Union[float, int], indicator: str, price: Union[float, int]):
        self.timestamp = timestamp
        self.quantity = quantity
        self.indicator = indicator
        self.price = price

class StockMarket():
    """object representing all stocks"""
    def __init__(self):
        self.stocks = []

    def add_stock(self, stock):
        self.stocks.append(stock)

    def calc_gbce_all_share_index(self):
        stock_prices = [stock.calc_volume_weighted_stock_price() for stock in self.stocks]
        filtered_prices = list(filter(lambda price: price > 0, stock_prices))
        if not filtered_prices:
            return 0
        
        product = reduce(lambda x, y: x * y, filtered_prices)
        return pow(product, 1 / len(filtered_prices))