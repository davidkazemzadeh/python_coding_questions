#(self,symbol,type_,par_value,price,last_dividend=0,fixed_dividend=None)
# Adding stocks
stock1 = Stock("AAA", "Common",100,175,8)
stock_market.add_stock(stock1)

stock2 = Stock("BBB", "Common",100,150,4)
stock_market.add_stock(stock2)

stock3 = Stock("CCC", "Common",100,149,3.75)
stock_market.add_stock(stock3)

# Calculate dividend yield and P/E ratio
price = 50

dividend_yield = stock1.calc_common_div_yield(price) if stock1.type == "Common" else stock1.calc_preferred_div_yield(price)

pe_ratio = stock1.calc_p_e_ratio(price)
print(f"Dividend Yield: {dividend_yield}")
print(f"P/E Ratio: {pe_ratio}")

# Record a trade
quantity = 100
indicator = "Buy"
price = 175
stock1.record_trade(quantity, indicator, price)

# Record a trade
quantity = 110
indicator = "Buy"
price = 150
stock2.record_trade(quantity, indicator, price)

# Record a trade
quantity = 115
indicator = "Buy"
price = 149
stock3.record_trade(quantity, indicator, price)

# Calculate Volume Weighted Stock Price
volume_weighted_price = stock1.calc_volume_weighted_stock_price()
print(f"Volume Weighted Stock Price: {volume_weighted_price}")

# Calculate GBCE All Share Index
gbce_index = stock_market.calc_gbce_all_share_index()
print(f"GBCE All Share Index: {gbce_index}")