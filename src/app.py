from src.response_generator import generate_response
from src.safety_gaurdrails import apply_safety_checks

def handle_query(user_query):
    response = generate_response(user_query)
    safe_response = apply_safety_checks(response)
    return safe_response
