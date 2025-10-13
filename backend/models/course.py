class Course:
    def __init__(self, title, description, price, duration, level, instructor, category, id=None, created_at=None):
        """
        Modelo de Curso para EstudioNet
        
        Args:
            title (str): Título del curso
            description (str): Descripción detallada del curso
            price (float): Precio del curso en ARS
            duration (int): Duración en minutos
            level (str): Nivel del curso (basico, intermedio, avanzado)
            instructor (str): Nombre del instructor
            category (str): Categoría del curso (ej: programacion, diseño, marketing)
            id (int, optional): ID del curso en la base de datos
            created_at (datetime, optional): Fecha de creación
        """
        self.id = id
        self.title = title
        self.description = description
        self.price = price
        self.duration = duration
        self.level = level
        self.instructor = instructor
        self.category = category
        self.created_at = created_at
    
    def __repr__(self):
        """Representación del objeto Course"""
        return f"<Course(id={self.id}, title='{self.title}', price={self.price}, level='{self.level}')>"
    
    def to_dict(self):
        """Convierte el objeto Course a diccionario"""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'price': self.price,
            'duration': self.duration,
            'level': self.level,
            'instructor': self.instructor,
            'category': self.category,
            'created_at': self.created_at
        }
    
    def get_duration_hours(self):
        """Retorna la duración convertida a horas"""
        return round(self.duration / 60, 2)
    
    def get_price_formatted(self):
        """Retorna el precio formateado con separador de miles"""
        return f"${self.price:,.2f}"
    
    def is_free(self):
        """Verifica si el curso es gratuito"""
        return self.price == 0
    
    @staticmethod
    def validate_level(level):
        """Valida que el nivel sea correcto"""
        valid_levels = ['basico', 'intermedio', 'avanzado']
        return level.lower() in valid_levels
    
    @staticmethod
    def get_valid_levels():
        """Retorna lista de niveles válidos"""
        return ['basico', 'intermedio', 'avanzado']