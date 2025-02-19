
from fastapi import HTTPException, File, UploadFile
from storeApi.models.summarize import TextInput
from storeApi.services.extractText import extract_text_pdf, extract_text_docx
from typing import Optional

async def input_handle(
    input: Optional[TextInput] = None,
    file: Optional[UploadFile] = File(None)
):
    if input and input.text:
        text = input.text
    elif file:
        if file.content_type == "application/pdf":
            text = await extract_text_pdf(file)
        elif file.content_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            text = await extract_text_docx(file)
        else:
            raise HTTPException(status_code=400, detail="Unsupported file format")
    else:
        raise HTTPException(status_code=400, detail="No input provided")
    return text