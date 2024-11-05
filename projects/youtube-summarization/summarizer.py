from youtube_transcript_api import YouTubeTranscriptApi
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

def Summarizer(link, model):
  
  video_id = link.split("=")[1]

  try:
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    FinalTranscript = ' '.join([i['text'] for i in transcript])
    
    if model == "Pegasus":
      checkpoint = "google/pegasus-large"
    elif model == "mT5":
      checkpoint = "csebuetnlp/mT5_multilingual_XLSum"
    elif model == "BART":
      checkpoint = "sshleifer/distilbart-cnn-12-6"
      
    tokenizer = AutoTokenizer.from_pretrained(checkpoint)
    model = AutoModelForSeq2SeqLM.from_pretrained(checkpoint)


    inputs = tokenizer(FinalTranscript, 
                    max_length=1024, 
                    truncation=True,
                    return_tensors="pt")
    
    summary_ids = model.generate(inputs["input_ids"])
    summary = tokenizer.batch_decode(summary_ids, 
                                  skip_special_tokens=True, 
                                  clean_up_tokenization_spaces=False)
    

    return summary[0]
  except Exception as e:
    return "TranscriptsDisabled: Transcript is not available \nTry another video"  
