from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("general-ocr-theory")
model = AutoModelForSeq2SeqLM.from_pretrained("general-ocr-theory")