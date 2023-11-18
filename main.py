import os.path
import random

def neuron(input, layer, index):
    weight = loadWeight('weight'+layer+'-'+str(index))
    bias = loadBias('bias'+layer+'-'+str(index))

    output = relu(input * weight + bias)
    return output

def loadWeight(name):
    location = './files/weights/'+name+'.txt'
    if(os.path.isfile(location)):
        w = open(file='./files/weights/'+name+'.txt', mode='r')
        weight = w.read()
    else:
        weight = random.uniform(-1, 1)
        w = open(file='./files/weights/'+name+'.txt', mode='w')
        w.write(str(weight))
    return float(weight)

def loadBias(name):
    location = './files/baises/'+name+'.txt'
    if(os.path.isfile(location)):
        w = open(file='./files/baises/'+name+'.txt', mode='r')
        bias = w.read()
    else:
        bias = random.uniform(-1, 1)
        w = open(file='./files/weights/'+name+'.txt', mode='w')
        w.write(str(bias))
    return float(bias)

def relu(input):
    if input > 0:
        return input
    else:
        return 0

inputData = [1, 2, 3, 4, 5]
inputNeurons = 5
outputNeurons = 2

hiddenLayers = 3
neuronsPerHiddenLayer = 5

# Process the input layer
inputlayerOutputs = []

for i in range(inputNeurons):
    inputlayerOutputs.append(neuron(inputData[i], 'input', i))

# Process the hidden layer
hiddenLayerOutputs = []
layer_input = inputlayerOutputs

for layer in range(hiddenLayers):
    layer_outputs = []

    for nueronOn in range(neuronsPerHiddenLayer):
        inputOn = 0
        for input_value in layer_input:
            output = neuron(input_value, 'middle', str(layer)+'-'+str(nueronOn)+'-'+str(inputOn))
            inputOn = inputOn + inputOn
        layer_outputs.append(output)
    
    layer_input = layer_outputs
    
    hiddenLayerOutputs.append(layer_outputs)

# Process the output layer
output_layer = []
for theRange in range(outputNeurons):
    outputOn = 0
    for input_value in layer_input:
        output = neuron(input_value, 'output', str(theRange)+'-'+str(outputOn))
        outputOn = outputOn + outputOn
    output_layer.append(output)

output_layer_output = output_layer

print("Final Output:", output_layer_output)
print("Network decision", output_layer_output.index(max(output_layer_output)))