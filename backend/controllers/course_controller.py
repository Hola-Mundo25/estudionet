from database import Database
from models.course import Course

class CourseController:
    def __init__(self):
        self.db = Database()
    
    def get_all_courses(self):
        """Obtiene todos los cursos de la base de datos"""
        query = "SELECT * FROM courses ORDER BY id DESC"
        return self.db.execute_query(query)
    
    def get_course_by_id(self, course_id):
        """Obtiene un curso por su ID"""
        query = "SELECT * FROM courses WHERE id = %s"
        result = self.db.execute_query(query, (course_id,))
        return result[0] if result else None
    
    def create_course(self, title, description, price, duration, level, instructor, category):
        """Crea un nuevo curso"""
        try:
            # Validar campos requeridos
            if not title or not description:
                print("❌ Título y descripción son obligatorios")
                return False
            
            # Validar precio
            try:
                price = float(price)
                if price < 0:
                    print("❌ El precio no puede ser negativo")
                    return False
            except ValueError:
                print("❌ Precio inválido")
                return False
            
            # Validar duración
            try:
                duration = int(duration)
                if duration <= 0:
                    print("❌ La duración debe ser mayor a 0")
                    return False
            except ValueError:
                print("❌ Duración inválida")
                return False
            
            # Validar nivel
            niveles_validos = ['basico', 'intermedio', 'avanzado']
            if level.lower() not in niveles_validos:
                print(f"❌ Nivel inválido. Debe ser: {', '.join(niveles_validos)}")
                return False
            
            # Crear el curso
            curso = Course(
                title=title,
                description=description,
                price=price,
                duration=duration,
                level=level.lower(),
                instructor=instructor,
                category=category
            )
            
            query = """
                INSERT INTO courses (title, description, price, duration, level, instructor, category)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            params = (
                curso.title,
                curso.description,
                curso.price,
                curso.duration,
                curso.level,
                curso.instructor,
                curso.category
            )
            
            self.db.execute_query(query, params)
            return True
            
        except Exception as e:
            print(f"❌ Error al crear curso: {e}")
            return False
    
    def update_course(self, course_id, title=None, description=None, price=None, 
                     duration=None, level=None, instructor=None, category=None):
        """Actualiza un curso existente"""
        try:
            # Obtener datos actuales del curso
            curso_actual = self.get_course_by_id(course_id)
            if not curso_actual:
                print("❌ Curso no encontrado")
                return False
            
            # Preparar datos para actualizar (mantener actuales si no se proporciona nuevo valor)
            nuevo_title = title if title else curso_actual['title']
            nuevo_description = description if description else curso_actual['description']
            nuevo_price = float(price) if price else curso_actual['price']
            nuevo_duration = int(duration) if duration else curso_actual['duration']
            nuevo_level = level.lower() if level else curso_actual['level']
            nuevo_instructor = instructor if instructor else curso_actual['instructor']
            nuevo_category = category if category else curso_actual['category']
            
            # Validar nivel si se proporciona
            if level:
                niveles_validos = ['basico', 'intermedio', 'avanzado']
                if nuevo_level not in niveles_validos:
                    print(f"❌ Nivel inválido. Debe ser: {', '.join(niveles_validos)}")
                    return False
            
            # Validar precio si se proporciona
            if price and nuevo_price < 0:
                print("❌ El precio no puede ser negativo")
                return False
            
            # Validar duración si se proporciona
            if duration and nuevo_duration <= 0:
                print("❌ La duración debe ser mayor a 0")
                return False
            
            # Actualizar en la base de datos
            query = """
                UPDATE courses 
                SET title = %s, description = %s, price = %s, duration = %s,
                    level = %s, instructor = %s, category = %s
                WHERE id = %s
            """
            params = (
                nuevo_title,
                nuevo_description,
                nuevo_price,
                nuevo_duration,
                nuevo_level,
                nuevo_instructor,
                nuevo_category,
                course_id
            )
            
            self.db.execute_query(query, params)
            return True
            
        except ValueError as e:
            print(f"❌ Error de validación: {e}")
            return False
        except Exception as e:
            print(f"❌ Error al actualizar curso: {e}")
            return False
    
    def delete_course(self, course_id):
        """Elimina un curso"""
        try:
            # Verificar que el curso existe
            curso = self.get_course_by_id(course_id)
            if not curso:
                print("❌ Curso no encontrado")
                return False
            
            query = "DELETE FROM courses WHERE id = %s"
            self.db.execute_query(query, (course_id,))
            return True
            
        except Exception as e:
            print(f"❌ Error al eliminar curso: {e}")
            return False
    
    def search_courses(self, keyword):
        """Busca cursos por palabra clave en título o descripción"""
        query = """
            SELECT * FROM courses 
            WHERE title LIKE %s OR description LIKE %s OR category LIKE %s
            ORDER BY id DESC
        """
        search_term = f"%{keyword}%"
        return self.db.execute_query(query, (search_term, search_term, search_term))
    
    def get_courses_by_level(self, level):
        """Obtiene cursos filtrados por nivel"""
        query = "SELECT * FROM courses WHERE level = %s ORDER BY id DESC"
        return self.db.execute_query(query, (level,))
    
    def get_courses_by_category(self, category):
        """Obtiene cursos filtrados por categoría"""
        query = "SELECT * FROM courses WHERE category = %s ORDER BY id DESC"
        return self.db.execute_query(query, (category,))