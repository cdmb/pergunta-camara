class CustomRendererException(Exception):
    pass


class ModelToJson:

    def __init__(self, _object):
        self._object = _object

    def render(self, ignore=None):

        ignore = ignore or []

        if ignore:

            invalid_attribute = next(
                (attr for attr in ignore if not hasattr(self._object, attr)),
                None
            )

            if invalid_attribute:
                raise CustomRendererException(
                    'The object {!r} does not have an attribute {!r}'.format(
                        self._object, 'id'
                    )
                )

        if hasattr(self._object, '__json__'):
            return self._object.__json__(ignore=ignore)
