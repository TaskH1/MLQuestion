def format_answer_text(answer_text):
    # Split the text by the bullet point simbol
    paragraphs = answer_text.split("•")
    # Wrap each segment in <p> tags
    formatted_paragraphs = [f"<p>{para.strip()}</p>" for para in paragraphs if para.strip()]
    # Join the paragraphs back together as a single string
    return "".join(formatted_paragraphs)