from domain.models.payment import Payment
from domain.repositories.payment_repository import PaymentRepository
from application.interfaces.payment_gateway_interface import PaymentGatewayInterface

class ProcessPaymentUseCase:
    def __init__(self, payment_repository: PaymentRepository, payment_gateway: PaymentGatewayInterface):
        self.payment_repository = payment_repository
        self.payment_gateway = payment_gateway

    def execute(self, payment_info):
        
        payment_result = self.payment_gateway.process_payment(payment_info['amount'], payment_info)
        
        if payment_result['success']:
            payment = Payment(
                id=None,  
                reservation_id=payment_info['reservation_id'],
                amount=payment_info['amount'],
                date=payment_info['date'] 
            )
            saved_payment = self.payment_repository.save(payment)
            return saved_payment
        else:
            raise ValueError("El pago no pudo ser procesado")

