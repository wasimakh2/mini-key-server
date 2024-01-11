# keyserv/utils.py

import random
import string

from flask import request
from keyserv.keymanager import Origin
from keyserv.models import Application


def generate_token():
    """Generate a random activation token for key activation."""
    token_length = 16
    token = ''.join(random.choices(string.ascii_uppercase + string.digits, k=token_length))
    return token

def validate_machine(machine):
    """Validate the machine information provided during key activation."""
    # Add validation logic here
    return True

def validate_user(user):
    """Validate the user information provided during key activation."""
    # Add validation logic here
    return True

def validate_hwid(hwid):
    """Validate the hardware ID provided during key activation."""
    # Add validation logic here
    return True

def get_remaining_activations(app_id, token):
    """Retrieve the remaining activations for a given key."""
    # Add logic to retrieve remaining activations
    return 0

def log_activation_attempt(app_id, token, origin, result):
    """Log the key activation attempt, regardless of success or failure."""
    # Add logic to log activation attempt

def log_key_check_attempt(app_id, token, origin, result):
    """Log the key check attempt, regardless of success or failure."""
    # Add logic to log key check attempt

def get_support_message(app_id):
    """Retrieve the support message for a given application."""
    # Add logic to retrieve support message
