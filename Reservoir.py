import math

import matplotlib.pyplot as plt


class Reservoir:

    def __init__(self, reservoir_size, weights):
        self.reservoir_size = reservoir_size
        self.weights = weights
        self.outputs = [0.0] * self.reservoir_size
        self.biases = [-3.37, 0.125]

    def forward(self):
        activities = [0.0] * self.reservoir_size
        for neuron1 in range(self.reservoir_size):
            for neuron2 in range(self.reservoir_size):
                activities[neuron1] += self.weights[neuron2][neuron1] * self.outputs[neuron2]
            activities[neuron1] += self.biases[neuron1]
        for neuron1 in range(self.reservoir_size):
            self.outputs[neuron1] = math.tanh(activities[neuron1])

    def visualize(self):
        output1 = []
        output2 = []
        for activations in range(100):
            self.forward()
            output1.append(self.outputs[0])
            output2.append(self.outputs[1])
        plt.plot(range(100), output1)
        plt.xlabel("activations")
        plt.ylabel("activity")
        plt.plot(range(100), output2)
        plt.show()


if __name__ == '__main__':
    chaoticReservoir = Reservoir(2, [[-4, -1.5], [1.5, 0]])
    chaoticReservoir.visualize()

    # fixReservoir = Reservoir(2, [[-1.2, -0.45], [0.45, 0]])
    # fixReservoir.visualize()
