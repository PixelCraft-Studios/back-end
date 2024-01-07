from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.models import Card
from api.serializers import CardSerializer
from api.utils import random_card


@api_view(['GET'])
def get_ping():
  return Response({"message": "pong!"})


@api_view(['GET'])
def get_cards(request):
  cards = Card.objects.all()

  Card.objects.filter(chosen=True).update(chosen=False)

  random_cards = random_card(cards)
  random_cards.save()

  serializer = CardSerializer(cards, many=True)
    
  return Response(serializer.data)

@api_view(['POST'])
def create_card(request):
  serializer = CardSerializer(data=request.data)
  if serializer.is_valid():      
    serializer.save()
    return Response(serializer.data)
  
  return Response(serializer.errors)

@api_view(['GET'])
def select_card(request, card_id):
  try:
    card = Card.objects.get(id=card_id)
    serializer = CardSerializer(card).data
      
    if not card.chosen:
      return Response({"error": "wrong card"}, status=404)

    return Response(serializer)
  except Card.DoesNotExist:
    return Response({"error": "Card not found"}, status=404)
