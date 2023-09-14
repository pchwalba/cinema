from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .serializers import TicketSerializer, ScreeningSerializer, BookedSeats
from .models import Ticket


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def list(self, request, **kwargs):
        """get the list of occupied seats for chosen screening."""
        sc_pk = self.kwargs.get('sc_pk')
        queryset = Ticket.objects.filter(screening__pk=sc_pk)
        serializer = BookedSeats(queryset)
        serializer.data['screening'] = sc_pk
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.perform_create(serializer)
        response_data = serializer.data
        response_data['id'] = instance.id
        headers = self.get_success_headers(serializer.data)
        return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        instance = serializer.save()
        return instance
