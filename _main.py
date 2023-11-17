import pandas as pd

class main_fit:
    def __init__(self) -> None:
        data = pd.read_csv('dls_resources.csv')
        self.x = data.iloc[:,:-1].values
        self.y = data.iloc[:,-1].values

    
    def test_train(self):
        from sklearn.model_selection import train_test_split
        self.x_train,self.x_test,self.y_train,self.y_test = train_test_split(self.x,self.y,test_size=0.2,random_state=1)

    def regressor(self):
        from sklearn.tree import DecisionTreeRegressor
        self.regressor = DecisionTreeRegressor(random_state=0)
        self.regressor.fit(self.x_train,self.y_train)
    
    def predict(self,score,resources):
        self.T_score = score
        self.resources = resources
        self.dls_score = self.T_score*self.regressor.predict(self.resources)/100
        return self.dls_score
    