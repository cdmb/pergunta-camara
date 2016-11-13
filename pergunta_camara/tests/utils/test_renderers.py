from pergunta_camara.tests.base import MinimalTestCase
from pergunta_camara.utils.renderers import CustomRendererException
from pergunta_camara.utils.renderers import ModelToJson


class FakeModel:

    def __str__(self):
        return 'FakeModel()'

    def __repr__(self):
        return 'FakeModel()'


class ModelToJsonTestCase(MinimalTestCase):

    def test_exception_when_attributes_to_ignore_dont_exists(self):

        theobject = FakeModel()

        with self.assertRaises(CustomRendererException) as cm:
            ModelToJson(theobject).render(ignore=['id'])

        exception = cm.exception

        self.assertEqual(
            str(exception),
            'The object {!r} does not have an attribute {!r}'.format(
                theobject, 'id'
            )
        )

    def test_use_dunder_json_if_the_object_implement_it(self):

        theobject = FakeModel()

        # If the model implement a __json__, we can just return it
        theobject.__json__ = lambda **kwargs: {'foo': 'bar', 'bar': 'foo'}

        mtj = ModelToJson(theobject)

        self.assertDictEqual(mtj.render(), {'foo': 'bar', 'bar': 'foo'})
