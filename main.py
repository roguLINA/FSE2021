from sklearn.ensemble import RandomForestRegressor

def main_function(X, y):
    rfr = RandomForestRegressor()
    rfr.fit(X, y)
    return rfr

