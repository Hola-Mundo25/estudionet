from database import Database
from models.enrollment import Enrollment

class EnrollmentController:
    def __init__(self):
        self.db = Database()
    
    def enroll_user(self, user_id, course_id):
        """Inscribe un usuario a un curso"""
        try:
            # Verificar que el usuario no esté ya inscrito
            existing = self.get_enrollment(user_id, course_id)
            if existing:
                print("⚠️ El usuario ya está inscrito en este curso")
                return False
            
            # Crear la inscripción
            enrollment = Enrollment(
                user_id=user_id,
                course_id=course_id,
                status='active',
                payment_status='pending'
            )
            
            query = """
                INSERT INTO enrollments (user_id, course_id, status, payment_status)
                VALUES (%s, %s, %s, %s)
            """
            params = (
                enrollment.user_id,
                enrollment.course_id,
                enrollment.status,
                enrollment.payment_status
            )
            
            self.db.execute_query(query, params)
            return True
            
        except Exception as e:
            print(f"❌ Error al inscribir usuario: {e}")
            return False
    
    def get_enrollment(self, user_id, course_id):
        """Obtiene una inscripción específica de un usuario a un curso"""
        query = """
            SELECT * FROM enrollments 
            WHERE user_id = %s AND course_id = %s
        """
        result = self.db.execute_query(query, (user_id, course_id))
        return result[0] if result else None
    
    def get_user_enrollments(self, user_id):
        """Obtiene todas las inscripciones de un usuario con información del curso"""
        query = """
            SELECT 
                e.*,
                c.title as course_title,
                c.description as course_description,
                c.price as course_price,
                c.duration as course_duration,
                c.level as course_level,
                c.instructor as course_instructor,
                c.category as course_category
            FROM enrollments e
            JOIN courses c ON e.course_id = c.id
            WHERE e.user_id = %s
            ORDER BY e.enrollment_date DESC
        """
        return self.db.execute_query(query, (user_id,))
    
    def get_course_enrollments(self, course_id):
        """Obtiene todos los usuarios inscritos en un curso"""
        query = """
            SELECT 
                e.*,
                u.username,
                u.email,
                u.full_name
            FROM enrollments e
            JOIN users u ON e.user_id = u.id
            WHERE e.course_id = %s
            ORDER BY e.enrollment_date DESC
        """
        return self.db.execute_query(query, (course_id,))
    
    def get_all_enrollments(self):
        """Obtiene todas las inscripciones con información de usuarios y cursos"""
        query = """
            SELECT 
                e.*,
                u.username,
                u.full_name,
                c.title as course_title,
                c.price as course_price
            FROM enrollments e
            JOIN users u ON e.user_id = u.id
            JOIN courses c ON e.course_id = c.id
            ORDER BY e.enrollment_date DESC
        """
        return self.db.execute_query(query)
    
    def update_enrollment_status(self, enrollment_id, new_status):
        """Actualiza el estado de una inscripción"""
        try:
            # Validar estado
            if not Enrollment.validate_status(new_status):
                print(f"❌ Estado inválido. Debe ser: {', '.join(Enrollment.get_valid_statuses())}")
                return False
            
            query = "UPDATE enrollments SET status = %s WHERE id = %s"
            self.db.execute_query(query, (new_status.lower(), enrollment_id))
            return True
            
        except Exception as e:
            print(f"❌ Error al actualizar estado: {e}")
            return False
    
    def update_payment_status(self, enrollment_id, new_payment_status):
        """Actualiza el estado de pago de una inscripción"""
        try:
            # Validar estado de pago
            if not Enrollment.validate_payment_status(new_payment_status):
                print(f"❌ Estado de pago inválido. Debe ser: {', '.join(Enrollment.get_valid_payment_statuses())}")
                return False
            
            query = "UPDATE enrollments SET payment_status = %s WHERE id = %s"
            self.db.execute_query(query, (new_payment_status.lower(), enrollment_id))
            return True
            
        except Exception as e:
            print(f"❌ Error al actualizar estado de pago: {e}")
            return False
    
    def cancel_enrollment(self, enrollment_id):
        """Cancela una inscripción"""
        try:
            query = "UPDATE enrollments SET status = 'cancelled' WHERE id = %s"
            self.db.execute_query(query, (enrollment_id,))
            return True
        except Exception as e:
            print(f"❌ Error al cancelar inscripción: {e}")
            return False
    
    def delete_enrollment(self, enrollment_id):
        """Elimina una inscripción (usar con cuidado)"""
        try:
            query = "DELETE FROM enrollments WHERE id = %s"
            self.db.execute_query(query, (enrollment_id,))
            return True
        except Exception as e:
            print(f"❌ Error al eliminar inscripción: {e}")
            return False
    
    def get_active_enrollments_by_user(self, user_id):
        """Obtiene solo las inscripciones activas de un usuario"""
        query = """
            SELECT 
                e.*,
                c.title as course_title,
                c.instructor as course_instructor
            FROM enrollments e
            JOIN courses c ON e.course_id = c.id
            WHERE e.user_id = %s AND e.status = 'active'
            ORDER BY e.enrollment_date DESC
        """
        return self.db.execute_query(query, (user_id,))
    
    def get_completed_enrollments_by_user(self, user_id):
        """Obtiene los cursos completados por un usuario"""
        query = """
            SELECT 
                e.*,
                c.title as course_title,
                c.instructor as course_instructor
            FROM enrollments e
            JOIN courses c ON e.course_id = c.id
            WHERE e.user_id = %s AND e.status = 'completed'
            ORDER BY e.enrollment_date DESC
        """
        return self.db.execute_query(query, (user_id,))
    
    def get_enrollment_stats(self):
        """Obtiene estadísticas generales de inscripciones"""
        query = """
            SELECT 
                COUNT(*) as total_enrollments,
                COUNT(CASE WHEN status = 'active' THEN 1 END) as active_count,
                COUNT(CASE WHEN status = 'completed' THEN 1 END) as completed_count,
                COUNT(CASE WHEN status = 'cancelled' THEN 1 END) as cancelled_count,
                COUNT(CASE WHEN payment_status = 'paid' THEN 1 END) as paid_count,
                COUNT(CASE WHEN payment_status = 'pending' THEN 1 END) as pending_count
            FROM enrollments
        """
        result = self.db.execute_query(query)
        return result[0] if result else None