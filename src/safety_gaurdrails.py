def apply_safety_checks(response):
    banned_phrases = ["guaranteed", "100% fix", "definitely"]

    for phrase in banned_phrases:
        if phrase in response.lower():
            response = response.replace(phrase, "")

    return response
