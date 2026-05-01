def get_var(var_name, prompt, other_vars):
    if var_name != "context":
        return {"output": ""}

    inquiry = other_vars.get("inquiry", "").lower()

    if "return" in inquiry or "refund" in inquiry:
        return {
            "output": (
                "Return Policy:\n"
                "- Customers can return eligible items within 30 days of delivery.\n"
                "- A return label will be emailed to the customer after the return request is initiated.\n"
                "- Returned items must be unused and in original packaging.\n"
                "- The assistant must clearly mention the return label in the response."
            )
        }

    if "damaged" in inquiry or "package" in inquiry:
        return {
            "output": (
                "Damaged Package Support Policy:\n"
                "- Apologize politely for the damaged package.\n"
                "- Ask the customer to describe the issue and share order details.\n"
                "- Do not assume the cause of damage.\n"
                "- Escalate to order support if needed."
            )
        }

    if "order" in inquiry:
        return {
            "output": (
                "Order Support Policy:\n"
                "- Ask the customer to briefly describe the issue with the order.\n"
                "- Be polite and empathetic.\n"
                "- Do not assume the exact problem unless it is provided by the customer."
            )
        }

    if "account" in inquiry or "password" in inquiry:
        return {
            "output": (
                "Account Support Policy:\n"
                "- Always confirm the Account ID before giving next steps.\n"
                "- Do not ask for passwords or sensitive credentials.\n"
                "- The assistant must never ask the user to share their password.\n"
                "- Guide the user through secure account-support steps."
            )
        }

    return {
        "output": (
            "General Knowledge Boundary:\n"
            "- If the answer is not present in the provided context, the assistant must say exactly: I don't know.\n"
            "- The assistant must not invent unsupported facts."
        )
    }