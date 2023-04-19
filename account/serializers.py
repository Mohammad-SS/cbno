from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import ContactForm


class TwoSumSerializer(serializers.Serializer):
    """
    Serializer class for validating and serializing data for the TwoSumAPIView.

    num1: Integer field for accepting the first integer value.
    num2: Integer field for accepting the second integer value.

    get_sum: Method to calculate the sum of two integer values.
    """

    num1 = serializers.IntegerField()
    num2 = serializers.IntegerField()

    def get_sum(self, validated_data):
        try:
            return validated_data.get("num1") + validated_data.get("num2")
        except Exception as e:
            print(e)
            raise ValidationError(detail="data is not valid")


class ContactFormSerializer(serializers.ModelSerializer):
    """
    Serializer class for validating and serializing data for creating a new contact.

    Meta:
        model: Model class for the serializer.
        fields: List of fields to be included in the serialized output.
    """

    class Meta:
        model = ContactForm
        fields = "__all__"
