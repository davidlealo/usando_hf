from transformers import pipeline

def main():
    print("Hola, Hugging Face")

    # Cargar el modelo de resumen
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

    # Generar resumen
    prompt = "El aprendizaje basado en proyectos ayuda a los estudiantes a desarrollar habilidades prácticas y colaborativas."
    print("Generando resumen...")
    result = summarizer(prompt, max_length=50, min_length=25, do_sample=False)
    
    print("Resumen generado:")
    print(result[0]['summary_text'])

if __name__ == "__main__":
    import os
    os.environ["TOKENIZERS_PARALLELISM"] = "false"  # Evita conflictos con tokenizers
    main()
