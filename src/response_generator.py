from src.intent_classifier import predict_intent

def generate_response(query):
    intent = predict_intent(query)

    if intent == "damp_issue":
        return (
            "Thanks for sharing the issue. Dampness or wet patches, especially "
            "after rainfall, may be caused by moisture seepage or external "
            "water exposure.\n\n"
            "To understand the situation better, could you please share:\n"
            "• Is the affected wall exposed to the outside?\n"
            "• Do you notice any cracks, discoloration, or peeling paint nearby?\n"
            "• Does the dampness appear only after heavy rain or remain constant?\n\n"
            "Monitoring the area and arranging a professional inspection may help "
            "identify the root cause and suitable next steps."
        )

    elif intent == "crack_issue":
        return (
            "Thank you for informing us about the cracks on the wall. Wall cracks "
            "can occur due to factors such as material aging, minor structural "
            "movement, or environmental changes.\n\n"
            "To assess this better, could you please clarify:\n"
            "• Are the cracks thin (hairline) or wide and deep?\n"
            "• Have you noticed the cracks increasing in size over time?\n"
            "• Are the cracks located near doors, windows, or ceilings?\n\n"
            "Based on these details, a professional inspection may be recommended "
            "to determine whether any repair or monitoring is required."
        )

    elif intent == "paint_issue":
        return (
            "Thanks for reaching out regarding the paint damage. Peeling, bubbling, "
            "or discoloration of paint can sometimes be linked to moisture, surface "
            "preparation issues, or aging of the paint layer.\n\n"
            "To help us assist you better, could you share:\n"
            "• Is the affected area exposed to moisture or humidity?\n"
            "• How old is the current paint work?\n"
            "• Are there any signs of dampness or seepage beneath the paint?\n\n"
            "Identifying the underlying cause is important before repainting, "
            "and a professional assessment may help ensure a long-lasting solution."
        )

    elif intent == "general_query":
        return (
            "Thank you for contacting us. We would be happy to assist you with your "
            "home maintenance concern.\n\n"
            "Could you please provide more details about the issue, such as:\n"
            "• The specific area of the house affected\n"
            "• When the problem started\n"
            "• Any visible signs or changes you have noticed\n\n"
            "Once we have this information, we can guide you with appropriate next steps."
        )

    else:
        return (
            "Thank you for reaching out. Could you please provide more details "
            "about the issue so we can assist you more accurately?"
        )
