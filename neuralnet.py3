class NNet:
    def _ini_(self,x,y,):
        self.input =x
        self.weights1 =np.random.rand(self.input.shape[1],4)
        self.weights2 =np.random.rand(4,1)
        self.y        =y
        self.output   =np.zeroes(y.shape)

    def feedforward(self):
        self.layer1 = sigmoid(np.dot(self.input, self.weights1))
        self.output =sigmoid(np.dot(self.layer1, self.weights2))

    def backprop(self):
        #Apply chain rule to determine derivative of loss function with respect to weights[x]
        d_weights2 =np.dot(self.layer1.T, (2*(self.y-self.output)*sigmoid_derivative(self.output)))
        d_weights1=np.dot(self.input.T, (np.dot(2*(self.y-self.output)*sigmoid_derivative(self.output),self.weights2.T)*sigmoid_derivative(self.layer1)))

        #update weights with derivative of loss function.
        self.weights1+=d_weights1
        self.weights2+=d_weights2
