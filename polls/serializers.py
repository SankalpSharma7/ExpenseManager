from rest_framework import serializers
from polls.models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('transaction_id',
                  'amount',
                  'type',
                  'parent_id',
                  'tree_sum')