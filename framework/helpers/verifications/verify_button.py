from framework.helpers.verifications.verify_base import VerifyBase

class VerifyButton(VerifyBase):
    def color_is(self, expected_rgb_color: str):
        """Verify that the button color is equal to the expected color."""
        assert expected_rgb_color == self.element.value_of_css_property('background-color'), f"The actual color '{self.element.value_of_css_property('background-color')}' did not match '{expected_rgb_color}'"