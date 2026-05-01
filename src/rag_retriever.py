from pathlib import Path
from typing import List, Dict


KNOWLEDGE_BASE_DIR = Path("data/knowledge_base")


KEYWORD_MAP = {
    "return": ["return", "refund", "unused", "label", "opened", "product"],
    "order": ["order", "package", "delivery", "delayed", "missing", "incorrect"],
    "account": ["account", "password", "username", "login", "reset", "credential"],
    "damaged": ["damaged", "damage", "broken", "package", "photos"],
    "security": ["ignore", "system prompt", "hidden", "instructions", "override", "own knowledge"],
}


DOCUMENT_MAP = {
    "return": "return_policy.txt",
    "order": "order_support_policy.txt",
    "account": "account_security_policy.txt",
    "damaged": "damaged_package_policy.txt",
    "security": "security_policy.txt",
}


def load_document(file_name: str) -> str:
    file_path = KNOWLEDGE_BASE_DIR / file_name
    if not file_path.exists():
        return ""
    return file_path.read_text(encoding="utf-8")


def detect_relevant_categories(query: str) -> List[str]:
    query_lower = query.lower()
    matched_categories = []

    for category, keywords in KEYWORD_MAP.items():
        if any(keyword in query_lower for keyword in keywords):
            matched_categories.append(category)

    return matched_categories


def retrieve_context(query: str, max_documents: int = 2) -> Dict[str, object]:
    categories = detect_relevant_categories(query)

    if not categories:
        return {
            "context": (
                "General Knowledge Boundary:\n"
                "The available knowledge base does not contain information related to this query.\n"
                "If the answer is not present in the retrieved context, the assistant must say exactly: I don't know."
            ),
            "sources": []
        }

    selected_categories = categories[:max_documents]
    retrieved_contexts = []
    sources = []

    for category in selected_categories:
        file_name = DOCUMENT_MAP.get(category)
        if file_name:
            document_text = load_document(file_name)
            if document_text:
                retrieved_contexts.append(document_text)
                sources.append(file_name)

    if not retrieved_contexts:
        return {
            "context": (
                "General Knowledge Boundary:\n"
                "No relevant document was retrieved from the knowledge base.\n"
                "If the answer is not present in the retrieved context, the assistant must say exactly: I don't know."
            ),
            "sources": []
        }

    return {
        "context": "\n\n---\n\n".join(retrieved_contexts),
        "sources": sources
    }


if __name__ == "__main__":
    sample_query = "I want to return my widget"
    result = retrieve_context(sample_query)
    print("Retrieved Sources:", result["sources"])
    print("\nRetrieved Context:\n")
    print(result["context"])