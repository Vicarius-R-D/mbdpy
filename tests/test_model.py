from mbdpy.model import Model
from mbdpy.blocks import Block

class TestModel:
    def test_init_model(self):
        model = Model('test model')

        assert model.name == 'test model'
        assert isinstance(model.blocks, list)
        assert not model.blocks
        assert model.last_port_id == 0

    def test_add_block(self):
        model = Model('test model')
        model.add_block(Block())

        assert len(model.blocks) == 1
        assert isinstance(model.blocks[0], Block)

    def test_create_input_id(self):
        model = Model('test model')
        new_id = model.create_port_id()

        assert new_id == 1
        assert new_id == model.last_port_id
