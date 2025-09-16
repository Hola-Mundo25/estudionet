from database import Database
from models.user import User
from controllers.auth_controller import AuthController
from controllers.user_controller import UserController

def main():
    print(" ESTUDIONET - Sistema de Autenticación")
    print("=" * 40)
    
    auth = AuthController()
    user_controller = UserController()