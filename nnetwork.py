#neursal network class definition
import numpy
import scipy.special
class neuralNetwork:
    #initialise the neural network
    def _inif_(self,inputnodes,hiddennodes,outputnodes,learningrate):
        #set number of nodes in each input hidden output layer
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes
        #learning rate
        self.lr = learningrate
        #link wight matrices wih an who
        #weights inside the arry are W_i_j where link is from node i to nodej in the next layer
        #w11 w21
        #w12 w22 etc
        self.wih=(numpy.random.rand(self.hnodes,self.inodes)-0.5)
        self.who=(numpy.random.rand(self.onodes,self.hnodes)-0.5)
        #activation function
        self.activation_function = lambda x:scipy.special.expit(x)
        pass

    #train the neural network
    def train(self,inputs_list,targets_list):
        inputs = numpy.array(inputs_list,ndmin=2).T
        targets = numpy.array(targets_list,ndmin=2).T
        hidden_inputs = numpy.dot(self.wih,inputs)
        hidden_outputs = self.activation_function(hidden_inputs)
        final_inputs= numpy.dot(self.who,hidden_outputs)
        final_outputs= self.activation_function(final_inputs)

        output_errors = targets-final_outputs
        hidden_errors = numpy.dot(self.who.T,output_errors)

        self.who += self.lr*numpy.dot((output_errors*final_outputs*(1.0-final_outputs)),numpy.transpose(hidden_outputs))
        self.wih += self.lr*numpy.dot((hidden_errors*hidden_outputs*(1.0-hidden_outputs)),numpy.transpose*(inputs))
        pass

    #query the neural network
    def query(self,inputs_list):
        inputs = numpy.array(inputs_list,ndmin=2).T
        hidden_inputs = numpy.dot(self.wih,inputs)
        hidden_outputs = self.activation_function(hidden_inputs)
        final_inputs = numpy.dot(self.who,hidden_outputs)
        final_outputs = self.activation_function(final_inputs)
        return final_outputs
        pass


