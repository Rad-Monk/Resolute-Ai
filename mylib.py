import transformers
import fitz # install using: pip install PyMuPDF
from transformers import BartTokenizer, TFBartForConditionalGeneration
import math


def extract_text_from_pdf(pdf_file):
    text = ""
    
    # Open the PDF file from the file-like object
    pdf_document = fitz.open(stream=pdf_file.read(), filetype="pdf")
    
    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]
        text += page.get_text()
    
    return text


tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
model = TFBartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')


def summarize_text(text, chunk_size=1024, summary_max_length=600, summary_min_length=400):
    tokens = tokenizer(text, return_tensors='tf', max_length=chunk_size, truncation=True).input_ids
    num_chunks = math.ceil(tokens.shape[1] / chunk_size)
    
    summaries = []
    for i in range(num_chunks):
        chunk = tokens[:, i*chunk_size:(i+1)*chunk_size]
        summary_ids = model.generate(chunk, max_length=summary_max_length, min_length=summary_min_length, do_sample=False)
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        summaries.append(summary)
    
    return ' '.join(summaries)


def get_summary(pdf):
    pdf_text = extract_text_from_pdf(pdf)
    summary = summarize_text(pdf_text)
    return summary