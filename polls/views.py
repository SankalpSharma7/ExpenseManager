from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from polls.models import Transaction
from polls.serializers import TransactionSerializer


def update_parents(parent_id, amount):
    if parent_id != -1:
        transactions = Transaction.objects.filter(transaction_id__exact=parent_id).first()

        if transactions:
            transactions.tree_sum = transactions.tree_sum + amount
            transactions.save()
            update_parents(transactions.parent_id, amount)


def get_all_transactions(request):
    transactions = Transaction.objects.all()

    transactions_serializer = TransactionSerializer(transactions, many=True)
    return JsonResponse(transactions_serializer.data, safe=False)


@api_view(['GET', 'PUT', 'POST'])
def transaction(request, transaction_id):
    if request.method == 'GET':

        transactions = Transaction.objects.all()
        transactions = transactions.filter(transaction_id__exact=transaction_id)

        transactions_serializer = TransactionSerializer(transactions, many=True)

        return JsonResponse(transactions_serializer.data, safe=False)
    elif request.method == 'PUT':
        transaction_data = JSONParser().parse(request)
        transaction_data['transaction_id'] = transaction_id
        transaction_data['tree_sum'] = transaction_data['amount']

        if 'parent_id' in transaction_data:
            update_parents(transaction_data['parent_id'], transaction_data['amount'])

        transaction_serializer = TransactionSerializer(data=transaction_data)

        if transaction_serializer.is_valid():
            transaction_serializer.save()
            return JsonResponse(transaction_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(transaction_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def get_transaction_by_type(request, type):
    transactions = Transaction.objects.all()
    transactions = transactions.filter(type__exact=type)
    if transactions:
        transactions_serializer = TransactionSerializer(transactions, many=True)

        transactions_list = transactions_serializer.data
        transactions_ids = [d['transaction_id'] for d in transactions_list]

        return JsonResponse(transactions_ids, safe=False)
    else:
        return JsonResponse('No Matching Data Found', safe=False)


def sum_transactions(request, transaction_id):
    transactions = Transaction.objects.all()
    transactions = transactions.filter(transaction_id__exact=transaction_id)

    if transactions:
        transactions_serializer = TransactionSerializer(transactions, many=True)

        transactions_list = transactions_serializer.data

        result = transactions_list[0]['tree_sum']

        return JsonResponse(result, safe=False)
    else:
        return JsonResponse('No Matching Data Found', safe=False)
