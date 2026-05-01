from src.rag_retriever import retrieve_context


def get_var(var_name, prompt, other_vars):
    if var_name != "context":
        return {"output": ""}

    inquiry = other_vars.get("inquiry", "")

    retrieval_result = retrieve_context(inquiry, max_documents=2)

    context_text = retrieval_result["context"]
    sources = retrieval_result["sources"]

    if sources:
        source_text = "Retrieved Sources: " + ", ".join(sources)
    else:
        source_text = "Retrieved Sources: none"

    return {
        "output": f"{source_text}\n\n{context_text}"
    }