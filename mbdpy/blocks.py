from .model import Model

class Block:

    def __init__(self):
        pass
    
    def connect_output(self, input_id) -> None:
        self.output_to = input_id


class Add(Block):

    def __init__(self, n_input, model: Model):
        self.input_id = []
        self.output_to = None

        for _ in range(n_input):
            self.input_id.append(model.create_port_id())


class Constant(Block):

    def __init__(self, value):
        self.value = value
        self.output_to = None