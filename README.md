# **Usando Hugging Face 🚀**

Este proyecto explora las funcionalidades básicas de la biblioteca **Hugging Face Transformers** utilizando modelos preentrenados en diversas tareas de NLP como generación de texto, análisis de sentimientos, traducción y resumen de texto.

---

## **Descripción General**

Este repositorio contiene ejemplos prácticos usando **Hugging Face** para aplicar modelos de lenguaje preentrenados. Es ideal para aprender a interactuar con **pipelines** de Hugging Face de manera sencilla y eficiente.

### **Tareas Implementadas**

1. **Generación de texto** con `GPT-2` y `DistilGPT2`.
2. **Análisis de sentimientos** con `DistilBERT`.
3. **Traducción de texto** (Inglés a Francés).
4. **Resumen de texto** con `DistilBART`.

---

## **Requisitos Previos**

Asegúrate de tener instaladas las siguientes dependencias:

- **Python**: 3.9+
- **Pip**: Última versión
- Librerías principales:
   - `transformers`
   - `torch`
   - `datasets`

---

## **Instalación**

1. **Clona el repositorio**:

   ```bash
   git clone https://github.com/davidlealo/usando_hf.git
   cd usando_hf
   ```

2. **Crea un entorno virtual** (recomendado):

   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

3. **Instala las dependencias**:

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

---

## **Ejecución de Scripts**

### **1. Generación de texto**
Ejecuta `primer_hf_model.py` para generar texto usando **DistilGPT2**:

```bash
python3 primer_hf_model.py
```

**Descripción del script**:  
Se utiliza el modelo `distilgpt2` para generar texto a partir de un prompt específico.

---

### **2. Generación de texto avanzada**
Ejecuta `segundo_hf_model.py` para usar el modelo **GPT-2**:

```bash
python3 segundo_hf_model.py
```

**Descripción del script**:  
Genera texto más amplio basado en el prompt "La inteligencia artificial en el futuro".

---

### **3. Análisis de sentimientos, resumen y traducción**
Ejecuta `tercer_hf_model.py` para realizar múltiples tareas:

```bash
python3 tercer_hf_model.py
```

**Tareas incluidas**:
- **Análisis de sentimiento**: Clasifica un texto como positivo o negativo.
- **Resumen de texto**: Resume un texto largo en una versión corta.
- **Traducción**: Traduce texto de inglés a francés.

---

### **4. Resumen de texto**
Ejecuta `cuarto_hf_model.py` para resumir texto usando **DistilBART**:

```bash
python3 cuarto_hf_model.py
```

**Descripción del script**:  
Se utiliza el modelo `sshleifer/distilbart-cnn-12-6` para resumir textos.

---

## **Estructura del Proyecto**

```plaintext
usando_hf/
│
├── primer_hf_model.py      # Generación de texto con DistilGPT2
├── segundo_hf_model.py     # Generación de texto con GPT-2
├── tercer_hf_model.py      # Análisis de sentimientos, resumen y traducción
├── cuarto_hf_model.py      # Resumen de texto con DistilBART
├── README.md               # Documentación del proyecto
├── requirements.txt        # Dependencias del proyecto
└── LICENSE                 # Licencia MIT
```

---

## **Dependencias Principales**

- **transformers**: Interactuar con modelos preentrenados.
- **torch**: Biblioteca para operaciones con tensores y entrenamiento.
- **datasets**: Manejo eficiente de datasets.

---

## **Ejemplo de Ejecución**

Aquí un ejemplo de salida de `primer_hf_model.py`:

```plaintext
Hola, Hugging Face
Generando texto...
Texto generado:
Qué piensas del aprendizaje basado en proyectos? Es una excelente manera de desarrollar habilidades prácticas y colaborativas...
```

---

## **Licencia**

Este proyecto está bajo la licencia **MIT**.

---

## **Contacto**

Si tienes preguntas o sugerencias, puedes contactarme:

- **GitHub**: [https://github.com/davidlealo](https://github.com/davidlealo)
- **LinkedIn**: [https://linkedin.com/in/davidlealo/](https://linkedin.com/in/davidlealo/)
- **Email**: [davidlealo@gmail.com](mailto:davidlealo@gmail.com)

---

¡Explora, contribuye y aprende con Hugging Face! 😊🚀
