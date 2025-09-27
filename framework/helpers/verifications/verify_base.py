from framework.fields.base_field import BaseField


class VerifyBase:
    def __init__(self, field: 'BaseField'):
        self.field = field
        self.element = field.get_element()
    def exists(self):
        """Verifies that the element exists."""
        element = self.field.get_element()
        assert element.is_displayed(), "Element is not displayed and should be."
    def not_exists(self):
        """Verifies that the element does not exist."""
        element = self.field.get_element()
        assert not element.is_displayed(), "Element is displayed and should not be."
