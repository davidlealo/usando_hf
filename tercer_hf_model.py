from transformers import pipeline

sentiment = pipeline("sentiment-analysis")
result = sentiment("Hugging Face es genial y fácil de usar, pero me pongo nervioso porque es demasiado lo que necesito aprender.")
print(result)

print('_________________________________________________')
print('===================================================')


summarizer = pipeline("summarization")
result = summarizer("Tu texto largo aquí", max_length=50, min_length=25, do_sample=False)
print(result[0]['summary_text'])

print('_________________________________________________')
print('===================================================')


translator = pipeline("translation_en_to_fr")
result = translator("Hugging Face is awesome!")
print(result[0]['translation_text'])
