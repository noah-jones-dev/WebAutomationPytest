from framework.helpers.verifications.verify_button import VerifyBase

class VerifyLink(VerifyBase):
    def text_is(self, expected_text: str):
        '''Verify that the link text is equal to the expected text.'''
        assert expected_text == self.element.text, f"The actual text '{self.element.text}' did not match '{expected_text}'"
    def text_contains(self, expected_partial_text: str):
        '''Verify that the link text contains the expected text.'''
        assert expected_partial_text in self.element.text, f"The actual text {self.element.text} did not contain '{expected_partial_text}'"