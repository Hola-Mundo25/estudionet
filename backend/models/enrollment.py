class Enrollment:
    def __init__(self, user_id, course_id, status='active', payment_status='pending', 
                 id=None, enrollment_date=None):
        """
        Modelo de Inscripción para EstudioNet
        
        Args:
            user_id (int): ID del usuario inscrito
            course_id (int): ID del curso
            status (str): Estado de la inscripción (active, completed, cancelled)
            payment_status (str): Estado del pago (pending, paid, refunded)
            id (int, optional): ID de la inscripción en la base de datos
            enrollment_date (datetime, optional): Fecha de inscripción
        """
        self.id = id
        self.user_id = user_id
        self.course_id = course_id
        self.enrollment_date = enrollment_date
        self.status = status
        self.payment_status = payment_status
    
    def __repr__(self):
        """Representación del objeto Enrollment"""
        return f"<Enrollment(id={self.id}, user_id={self.user_id}, course_id={self.course_id}, status='{self.status}')>"
    
    def to_dict(self):
        """Convierte el objeto Enrollment a diccionario"""
        return {
            'id': self.id,
            'user_id': self.user_id,
            'course_id': self.course_id,
            'enrollment_date': self.enrollment_date,
            'status': self.status,
            'payment_status': self.payment_status
        }
    
    def is_active(self):
        """Verifica si la inscripción está activa"""
        return self.status == 'active'
    
    def is_completed(self):
        """Verifica si el curso fue completado"""
        return self.status == 'completed'
    
    def is_cancelled(self):
        """Verifica si la inscripción fue cancelada"""
        return self.status == 'cancelled'
    
    def is_paid(self):
        """Verifica si el pago fue realizado"""
        return self.payment_status == 'paid'
    
    def is_pending_payment(self):
        """Verifica si el pago está pendiente"""
        return self.payment_status == 'pending'
    
    def mark_as_completed(self):
        """Marca la inscripción como completada"""
        self.status = 'completed'
    
    def mark_as_cancelled(self):
        """Marca la inscripción como cancelada"""
        self.status = 'cancelled'
    
    def mark_as_paid(self):
        """Marca el pago como realizado"""
        self.payment_status = 'paid'
    
    def mark_as_refunded(self):
        """Marca el pago como reembolsado"""
        self.payment_status = 'refunded'
    
    @staticmethod
    def validate_status(status):
        """Valida que el estado sea correcto"""
        valid_statuses = ['active', 'completed', 'cancelled']
        return status.lower() in valid_statuses
    
    @staticmethod
    def validate_payment_status(payment_status):
        """Valida que el estado de pago sea correcto"""
        valid_payment_statuses = ['pending', 'paid', 'refunded']
        return payment_status.lower() in valid_payment_statuses
    
    @staticmethod
    def get_valid_statuses():
        """Retorna lista de estados válidos"""
        return ['active', 'completed', 'cancelled']
    
    @staticmethod
    def get_valid_payment_statuses():
        """Retorna lista de estados de pago válidos"""
        return ['pending', 'paid', 'refunded']