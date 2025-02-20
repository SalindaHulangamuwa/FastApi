from storeApi.models.summarize import TextInput


text_table = {}

def summarize_text(text: TextInput):
    data=text.dict()
    last_record_id=len(text_table)
    new_text={**data,"id":last_record_id}
    text_table[last_record_id]=new_text
    return new_text
    