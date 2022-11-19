

class Model:

    def __init__(self, name: str):
        self.name = name
        self.blocks = []
        self.last_port_id = 0

    def add_block(self, block):
        self.blocks.append(block)

    def create_port_id(self) -> int:
        self.last_port_id += 1

        return self.last_port_id