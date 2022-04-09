from transformers import pipeline
import os

## Loading pretrained BART-large-xsum-samsum model from HuggingFace Hub and saving it locally

summarizer=pipeline('summarization',model="lidiya/bart-large-xsum-samsum")
summarizer.save_pretrained(os.path.join(os.curdir,os.path.join('models','bart-model')))


## Loading custom trained t5-model from HuggingFace Hub and saving it locally

summarizer=pipeline('summarization',model='anegi/t5smallmodel')
summarizer.save_pretrained(os.path.join(os.curdir,os.path.join('models','custom-t5-model')))
