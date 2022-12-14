import json
import numpy as np

from .blocks import get_block_class


class Model:
    """
    Model class.
    """
    def __init__(self, name='blank_model'):
        self.name = name
        self.blocks = []
        self.last_port_id = 0

    def add_block(self, block) -> None:
        """
        Add a block to the model.
        Args:
            block (Block): instance of a block.
        """
        self.blocks.append(block)

    def create_port_id(self) -> int:
        """
        Create a new port id.
        Returns:
            port_id (int): new port id created
        """
        self.last_port_id += 1

        return self.last_port_id
    
    def save_json(self) -> None:
        """
        Convert and save the model into a json file.
        """
        model = self

        for i, block in enumerate(model.blocks):
            model.blocks[i] = vars(block)
        
        model_dict = vars(model)

        with open('models/' + model.name + '.json', 'w') as model_file:
            json.dump(model_dict, model_file, indent=4)

    def load_json(self, filename: str):
        """
        Load a json file and convert the data into an instance of the class.
        """
        with open(filename) as json_file:
            json_model = json.load(json_file)

        for key in json_model:
            setattr(self, key, json_model[key])

        for i, block in enumerate(self.blocks):
            block_class = get_block_class(block['type'])

            if block['type'] == 'Constant':
                block_class = block_class(block['value'])
            if block['type'] == 'Terminator':
                block_class = block_class(self)
            if block['type'] == 'Sum':
                block_class = block_class(len(block['input_id']), self)
            
            for key in block:
                setattr(block_class, key, block[key])

            self.blocks[i] = block_class
            del block_class
            
        return self

    def run(self, time: float, dt: float) -> None:
        """
        Run the model.
        Args:
            time (float): total simulation time in sec.
            dt (float): timestep of the simulation in sec.
        """
        new_blocks = []
        self.outputs = []
        self.outputs_to = []
        self.time = list(np.linspace(0, time, int((time + dt)/dt), dtype=float))

        for block in self.blocks:
            self.outputs.append([])

            if not block.input_id:
                new_blocks.insert(0, block)
            else:
                new_blocks.append(block)

        self.blocks = new_blocks

        for block in self.blocks:
            self.outputs_to.append(block.output_to)
        
        for t in self.time:
            for i, block in enumerate(self.blocks):
                output = block.evaluate(block.input_buffer)
                output_to = block.output_to
                self.outputs[i].append(output)

                for target_block in self.blocks:
                    if len(target_block.input_id) > 1:
                        for j, input_id in enumerate(target_block.input_id):
                            if output_to == input_id:
                                target_block.input_buffer[j] = output

