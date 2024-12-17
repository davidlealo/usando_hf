from transformers import pipeline

print("Hola, Hugging Face")

# Cargar el modelo ligero DistilGPT2
generator = pipeline("text-generation", model="distilgpt2")

# Generar texto
prompt = "Qué piensas del aprendizaje basado en proyectos?"
print("Generando texto...")
result = generator(prompt, max_length=50, num_return_sequences=1)

# Mostrar el resultado
print("Texto generado:")
print(result[0]['generated_text'])
