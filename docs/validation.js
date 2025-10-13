// ============================================
// VALIDACIONES PARA LOGIN.HTML
// ============================================

// Credenciales hardcodeadas (como solicitado en el sprint)
const VALID_CREDENTIALS = {
    username: 'admin',
    password: 'admin123'
};

// Función para validar el formulario de login
function validateLoginForm() {
    const loginForm = document.getElementById('loginForm');
    
    if (!loginForm) return; // Si no estamos en la página de login, salir

    loginForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const username = document.getElementById('username').value.trim();
        const password = document.getElementById('password').value;
        
        // Limpiar mensajes de error previos
        clearErrors();
        
        let isValid = true;

        // Validar campo username
        if (username === '') {
            showError('usernameError', 'El usuario es requerido');
            markInvalid('username');
            isValid = false;
        } else if (username.length < 3) {
            showError('usernameError', 'El usuario debe tener al menos 3 caracteres');
            markInvalid('username');
            isValid = false;
        } else {
            markValid('username');
        }

        // Validar campo password
        if (password === '') {
            showError('passwordError', 'La contraseña es requerida');
            markInvalid('password');
            isValid = false;
        } else if (password.length < 6) {
            showError('passwordError', 'La contraseña debe tener al menos 6 caracteres');
            markInvalid('password');
            isValid = false;
        } else {
            markValid('password');
        }

        // Si las validaciones HTML/JS pasan, verificar credenciales
        if (isValid) {
            if (username === VALID_CREDENTIALS.username && password === VALID_CREDENTIALS.password) {
                // Credenciales correctas - redirigir a landing page
                alert('¡Inicio de sesión exitoso! Bienvenido ' + username);
                window.location.href = 'index.html';
            } else {
                // Credenciales incorrectas
                showError('passwordError', 'Usuario o contraseña incorrectos');
                markInvalid('username');
                markInvalid('password');
            }
        }
    });

    // Validación en tiempo real
    const usernameInput = document.getElementById('username');
    const passwordInput = document.getElementById('password');

    if (usernameInput) {
        usernameInput.addEventListener('input', function() {
            if (this.value.trim().length >= 3) {
                markValid('username');
                hideError('usernameError');
            }
        });
    }

    if (passwordInput) {
        passwordInput.addEventListener('input', function() {
            if (this.value.length >= 6) {
                markValid('password');
                hideError('passwordError');
            }
        });
    }
}

// ============================================
// VALIDACIONES PARA REGISTER.HTML
// ============================================

function validateRegisterForm() {
    const registerForm = document.getElementById('registerForm');
    
    if (!registerForm) return; // Si no estamos en la página de registro, salir

    // Establecer fecha máxima (18 años atrás)
    const fechaNacimiento = document.getElementById('fechaNacimiento');
    if (fechaNacimiento) {
        const today = new Date();
        const maxDate = new Date(today.getFullYear() - 18, today.getMonth(), today.getDate());
        fechaNacimiento.max = maxDate.toISOString().split('T')[0];
    }

    // Validación de fortaleza de contraseña en tiempo real
    const passwordInput = document.getElementById('password');
    if (passwordInput) {
        passwordInput.addEventListener('input', function() {
            checkPasswordStrength(this.value);
        });
    }

    // Validación de confirmación de contraseña en tiempo real
    const confirmPasswordInput = document.getElementById('confirmPassword');
    if (confirmPasswordInput) {
        confirmPasswordInput.addEventListener('input', function() {
            validatePasswordMatch();
        });
    }

    // También validar cuando se cambia la contraseña principal
    if (passwordInput) {
        passwordInput.addEventListener('input', function() {
            if (confirmPasswordInput.value !== '') {
                validatePasswordMatch();
            }
        });
    }

    // Validación del formulario completo al enviar
    registerForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        clearErrors();
        
        let isValid = true;

        // Validar nombre
        const nombre = document.getElementById('nombre').value.trim();
        if (nombre === '') {
            showError('nombreError', 'El nombre es requerido');
            markInvalid('nombre');
            isValid = false;
        } else if (nombre.length < 2) {
            showError('nombreError', 'El nombre debe tener al menos 2 caracteres');
            markInvalid('nombre');
            isValid = false;
        } else {
            markValid('nombre');
        }

        // Validar apellido
        const apellido = document.getElementById('apellido').value.trim();
        if (apellido === '') {
            showError('apellidoError', 'El apellido es requerido');
            markInvalid('apellido');
            isValid = false;
        } else if (apellido.length < 2) {
            showError('apellidoError', 'El apellido debe tener al menos 2 caracteres');
            markInvalid('apellido');
            isValid = false;
        } else {
            markValid('apellido');
        }

        // Validar username
        const username = document.getElementById('username').value.trim();
        const usernamePattern = /^[a-zA-Z0-9_]+$/;
        if (username === '') {
            showError('usernameError', 'El usuario es requerido');
            markInvalid('username');
            isValid = false;
        } else if (username.length < 3) {
            showError('usernameError', 'El usuario debe tener al menos 3 caracteres');
            markInvalid('username');
            isValid = false;
        } else if (!usernamePattern.test(username)) {
            showError('usernameError', 'Solo se permiten letras, números y guión bajo');
            markInvalid('username');
            isValid = false;
        } else {
            markValid('username');
        }

        // Validar email
        const email = document.getElementById('email').value.trim();
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (email === '') {
            showError('emailError', 'El email es requerido');
            markInvalid('email');
            isValid = false;
        } else if (!emailPattern.test(email)) {
            showError('emailError', 'Ingrese un email válido');
            markInvalid('email');
            isValid = false;
        } else {
            markValid('email');
        }

        // Validar DNI
        const dni = document.getElementById('dni').value;
        if (dni === '') {
            showError('dniError', 'El DNI es requerido');
            markInvalid('dni');
            isValid = false;
        } else if (dni < 1000000 || dni > 99999999) {
            showError('dniError', 'Ingrese un DNI válido (entre 1.000.000 y 99.999.999)');
            markInvalid('dni');
            isValid = false;
        } else {
            markValid('dni');
        }

        // Validar fecha de nacimiento
        const fechaNac = document.getElementById('fechaNacimiento').value;
        if (fechaNac === '') {
            showError('fechaNacimientoError', 'La fecha de nacimiento es requerida');
            markInvalid('fechaNacimiento');
            isValid = false;
        } else {
            const birthDate = new Date(fechaNac);
            const today = new Date();
            const age = today.getFullYear() - birthDate.getFullYear();
            
            if (age < 18) {
                showError('fechaNacimientoError', 'Debes ser mayor de 18 años');
                markInvalid('fechaNacimiento');
                isValid = false;
            } else {
                markValid('fechaNacimiento');
            }
        }

        // Validar contraseña
        const password = document.getElementById('password').value;
        if (password === '') {
            showError('passwordError', 'La contraseña es requerida');
            markInvalid('password');
            isValid = false;
        } else if (password.length < 6) {
            showError('passwordError', 'La contraseña debe tener al menos 6 caracteres');
            markInvalid('password');
            isValid = false;
        } else {
            markValid('password');
        }

        // Validar confirmación de contraseña (CRÍTICO - como solicitado en el sprint)
        const confirmPassword = document.getElementById('confirmPassword').value;
        if (confirmPassword === '') {
            showError('confirmPasswordError', 'Debe confirmar la contraseña');
            markInvalid('confirmPassword');
            isValid = false;
        } else if (password !== confirmPassword) {
            showError('confirmPasswordError', 'Las contraseñas no coinciden');
            markInvalid('confirmPassword');
            hideSuccess('confirmPasswordSuccess');
            isValid = false;
        } else {
            markValid('confirmPassword');
            showSuccess('confirmPasswordSuccess');
        }

        // Validar términos y condiciones
        const terms = document.getElementById('terms');
        if (!terms.checked) {
            showError('termsError', 'Debe aceptar los términos y condiciones');
            isValid = false;
        }

        // Si todo es válido, redirigir a login
        if (isValid) {
            alert('¡Registro exitoso! Redirigiendo al inicio de sesión...');
            window.location.href = 'login.html';
        }
    });
}

// ============================================
// FUNCIONES AUXILIARES
// ============================================

// Mostrar mensaje de error
function showError(elementId, message) {
    const errorElement = document.getElementById(elementId);
    if (errorElement) {
        errorElement.textContent = message;
        errorElement.classList.add('show');
    }
}

// Ocultar mensaje de error
function hideError(elementId) {
    const errorElement = document.getElementById(elementId);
    if (errorElement) {
        errorElement.classList.remove('show');
    }
}

// Mostrar mensaje de éxito
function showSuccess(elementId) {
    const successElement = document.getElementById(elementId);
    if (successElement) {
        successElement.classList.add('show');
    }
}

// Ocultar mensaje de éxito
function hideSuccess(elementId) {
    const successElement = document.getElementById(elementId);
    if (successElement) {
        successElement.classList.remove('show');
    }
}

// Marcar campo como inválido
function markInvalid(fieldId) {
    const field = document.getElementById(fieldId);
    if (field) {
        field.classList.remove('is-valid');
        field.classList.add('is-invalid');
    }
}

// Marcar campo como válido
function markValid(fieldId) {
    const field = document.getElementById(fieldId);
    if (field) {
        field.classList.remove('is-invalid');
        field.classList.add('is-valid');
    }
}

// Limpiar todos los errores
function clearErrors() {
    const errorMessages = document.querySelectorAll('.error-message');
    errorMessages.forEach(error => error.classList.remove('show'));
    
    const inputs = document.querySelectorAll('.form-control');
    inputs.forEach(input => {
        input.classList.remove('is-invalid', 'is-valid');
    });
}

// Verificar fortaleza de contraseña
function checkPasswordStrength(password) {
    const strengthBar = document.getElementById('strengthBar');
    if (!strengthBar) return;

    strengthBar.className = 'password-strength-bar';

    if (password.length === 0) {
        strengthBar.style.width = '0';
        return;
    }

    let strength = 0;
    
    if (password.length >= 6) strength++;
    if (password.length >= 10) strength++;
    if (/[a-z]/.test(password) && /[A-Z]/.test(password)) strength++;
    if (/[0-9]/.test(password)) strength++;
    if (/[^a-zA-Z0-9]/.test(password)) strength++;

    if (strength <= 2) {
        strengthBar.classList.add('strength-weak');
    } else if (strength <= 3) {
        strengthBar.classList.add('strength-medium');
    } else {
        strengthBar.classList.add('strength-strong');
    }
}

// Validar coincidencia de contraseñas
function validatePasswordMatch() {
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirmPassword').value;
    
    if (confirmPassword === '') return;
    
    if (password === confirmPassword) {
        markValid('confirmPassword');
        hideError('confirmPasswordError');
        showSuccess('confirmPasswordSuccess');
    } else {
        markInvalid('confirmPassword');
        showError('confirmPasswordError', 'Las contraseñas no coinciden');
        hideSuccess('confirmPasswordSuccess');
    }
}

// ============================================
// INICIALIZACIÓN
// ============================================

// Ejecutar cuando el DOM esté completamente cargado
document.addEventListener('DOMContentLoaded', function() {
    validateLoginForm();
    validateRegisterForm();
});