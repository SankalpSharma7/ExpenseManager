# ExpenseManager
A project which can help you manage your expense and further will allow to do some analytics over it 

#steps to setup

1) setup python and django 
2) Clone the project and go to the root directory of project and run "python manage.py runserver" 
3) Server will be hosted and link will be mentioned in your terminal


#API Spec:
PUT /transactionservice/transaction/$transaction_id Body: { "amount":double,"type":string,"parent_id":long } where:
• transaction id is a long specifying a new transaction • amount is a double specifying the amount
• type is a string specifying a type of the transaction.
• parent id is an optional long that may specify the parent transaction of this transaction.

GET /transactionservice/transaction/$transaction_id Returns: { "amount":double,"type":string,"parent_id":long }

GET /transactionservice/types/$type Returns: [long, long, ... ] A json list of all transaction ids that share the same type $type.

GET /transactionservice/sum/$transaction_id Returns: { "sum": double } A sum of all transactions that are transitively linked by their parent_id to $transaction_id.( If A is parent of B andC, andCisparentofDandE.sum(A)=B+C+D+
E -- note: not just immediate child transactions.)
