from logging import debug
from flask import Flask,render_template,request
from transformers import pipeline
import os

bart_summarizer= pipeline('summarization',model=os.path.join(os.curdir,os.path.join('models','bart-model')))
t5_summarizer=pipeline('summarization',model=os.path.join(os.curdir,os.path.join('models','custom-t5-model')))

app=Flask(__name__)

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/displaysummary',methods=['GET','POST'])
def renderDisplayForm():
    if request.method=='GET':
        return f'The url /data is accessed directly'
    if request.method=='POST':
        form_data=request.form
        
        
        bart_summary=bart_summarizer(form_data['inputText'])[0]['summary_text']
        t5_summary=t5_summarizer(form_data['inputText'])[0]['summary_text']
        # return form_data
        return render_template('index.html',bart_summary=bart_summary,t5_summary=t5_summary)

if __name__=='__main__':
    app.run(debug=True)
    