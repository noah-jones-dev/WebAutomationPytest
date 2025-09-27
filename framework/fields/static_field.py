from framework.fields.base_field import BaseField
from framework.helpers.verifications.verify_static import VerifyStatic

class StaticField(BaseField):
    @property
    def verify(self) -> VerifyStatic:
        """Returns a verification object for this static field"""
        return VerifyStatic(self)