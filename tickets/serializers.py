from rest_framework import serializers
from .models import Ticket, Screening


class ScreeningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Screening
        fields = ['movie', 'screening_time', 'price']


class TicketSerializer(serializers.ModelSerializer):
    screening = ScreeningSerializer

    class Meta:
        model = Ticket
        fields = ['name', 'phone_number', 'email', 'screening', 'seat', 'discount']

    def create(self, validated_data):
        request = self.context["request"]

        return Ticket.objects.create(**validated_data)


class BookedSeats(serializers.BaseSerializer):

    def to_representation(self, instance):
        booked = [ticket.seat for ticket in instance]

        return {
            'booked': booked
        }
