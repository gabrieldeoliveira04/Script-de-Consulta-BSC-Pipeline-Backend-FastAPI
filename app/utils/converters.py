def format_balance(balance, decimals=4):
    """
    Formata números para exibição amigável
    """

    return f"{float(balance):,.{decimals}f}"