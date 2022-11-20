from .model import Model

import numpy as np

class Block:

    def __init__(self):
        pass
    
    def connect_output(self, input_id) -> None:
        self.output_to = input_id


class Constant(Block):

    def __init__(self, value: float):
        self.input_id = []
        self.input_buffer = [None]
        self.value = value
        self.output_to = None

    def evaluate(self, inputs: list) -> float:

        return self.value


class Terminator(Block):

    def __init__(self, model: Model):
        self.input_id = [model.create_port_id()]
        self.input_buffer = [None]
        self.output_to = None

    def evaluate(self, input: list[float]) -> None:
        pass

class Add(Block):

    def __init__(self, n_input, model: Model):
        self.input_id = []
        self.input_buffer = []
        self.output_to = None

        for _ in range(n_input):
            self.input_id.append(model.create_port_id())
            self.input_buffer.append(None)

    def evaluate(self, inputs: list[float]) -> float:

        return np.sum(np.array(inputs))
