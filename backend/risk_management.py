def apply_risk_management(adjusted_amount, my_balance):
    max_trade_percentage = 0.1  # Max 10% of wallet balance
    max_trade_amount = my_balance * max_trade_percentage
    return min(adjusted_amount, max_trade_amount)
