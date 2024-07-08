class Transaction:

    transactions = []
    
    def __init__(self,ref_paiement,code_emmeteur,code_recepteur,date_transaction,montant,canal):

        self.ref = ref_paiement
        self.issuer_id = code_emmeteur
        self.recipient_id = code_recepteur
        self.transaction_date = date_transaction
        self.amount = montant
        self.method = canal