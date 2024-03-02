from datetime import datetime
from application.interfaces.payment_gateway_interface import PaymentGatewayInterface

class PaymentGatewayImpl(PaymentGatewayInterface):
    def process_payment(self, amount: float, payment_details: dict):
        required_fields = ['card_number', 'expiry_date', 'cvc', 'amount']
        
        for field in required_fields:
            if field not in payment_details or not payment_details[field]:
                return {
                    "success": False,
                    "message": f"Falta el campo requerido: {field}"
                }
        
        if not payment_details['card_number'].isdigit() or len(payment_details['card_number']) != 16:
            return {
                "success": False,
                "message": "Número de tarjeta inválido"
            }
        
        expiry_date = payment_details['expiry_date']
        exp_month, exp_year = map(int, expiry_date.split('/'))
        current_month, current_year = datetime.now().month, datetime.now().year % 100
        
        payment_success = exp_year > current_year or (exp_year == current_year and exp_month >= current_month)
        
        if not payment_success:
            return {
                "success": False,
                "message": "El pago no pudo ser procesado. Tarjeta expirada."
            }
        
        return {
            "success": True,
            "transaction_id": "simulated_transaction_id",
            "message": "Pago procesado exitosamente"
        }
