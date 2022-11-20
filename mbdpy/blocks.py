from .model import Model

import numpy as np

class Block:
    """
    Base block class.
    """
    def __init__(self):
        pass
    
    def connect_output(self, input_id) -> None:
        self.output_to = input_id

    def evaluate(self, input: list[float]) -> None:
        pass

    def move(self, coord: tuple[int, int]) -> None:
        self.coord = coord


class Constant(Block):
    """
    Block that raise a constant value.
    """
    def __init__(self, value: float):
        self.input_id = []
        self.input_buffer = [None]
        self.value = value
        self.output_to = None

    def evaluate(self, inputs: list) -> float:

        return self.value


class Terminator(Block):
    """
    Block without output to terminate a signal.
    """
    def __init__(self, model: Model):
        self.input_id = [model.create_port_id()]
        self.input_buffer = [None]
        self.output_to = None


class Sum(Block):
    """
    Block that sum multiple inputs.
    """
    def __init__(self, n_input, model: Model):
        self.input_id = []
        self.input_buffer = []
        self.output_to = None

        for _ in range(n_input):
            self.input_id.append(model.create_port_id())
            self.input_buffer.append(None)

    def evaluate(self, inputs: list[float]) -> float:

        return np.sum(np.array(inputs))
