from transformers import pipeline

# Cargar un modelo de texto (GPT-2 por defecto)
generator = pipeline("text-generation", model="gpt2")

# Generar texto a partir de una frase
prompt = "La inteligencia artificial en el futuro"
result = generator(prompt, max_length=50, num_return_sequences=1)

# Mostrar el resultado
print("Texto generado:")
print(result[0]['generated_text'])
