# EduNomad

## Plataforma educativa para el aprendizaje de la escritura morfosintáctica del castellano

**EduNomad** es una plataforma educativa digital desarrollada en **Django**, orientada al aprendizaje progresivo, ético y pedagógicamente fundamentado de la **escritura morfosintáctica del español** como lengua meta. Está diseñada para estudiantes cuya lengua materna pertenece a las **diez lenguas más habladas del mundo**, así como para docentes, investigadores y autodidactas.

El proyecto integra principios de **lingüística aplicada**, **pedagogía contrastiva**, **tecnología educativa** y **desarrollo de software académico**, con una proyección futura hacia la integración responsable de **inteligencia artificial educativa**.

---

## 🎯 Objetivos del proyecto

### Objetivo general

Desarrollar una plataforma digital que facilite el aprendizaje consciente y progresivo de la escritura en lengua castellana, con énfasis en la morfosintaxis, respetando la diversidad lingüística y cultural de los estudiantes.

### Objetivos específicos

* Ofrecer cursos estructurados por niveles (A1–C2) centrados en la escritura.
* Proporcionar ejercicios morfosintácticos guiados y evaluables.
* Visualizar el progreso individual del estudiante mediante métricas claras.
* Implementar un modelo de acceso ético (FREE / PREMIUM).
* Preparar la base técnica para futuras integraciones de IA educativa.

---

## 🧠 Fundamentación pedagógica

EduNomad se apoya en los siguientes principios:

* **Aprendizaje progresivo**: de estructuras simples a complejas.
* **Corrección explicada**: el error como oportunidad de aprendizaje.
* **Escritura contrastiva**: comparación entre el español y la lengua materna.
* **Autonomía del estudiante**: la IA como apoyo, no sustitución cognitiva.
* **Contextualización cultural**: ejemplos adaptados al entorno del aprendiz.

---

## 🏗️ Arquitectura del proyecto

El proyecto sigue una arquitectura modular basada en Django:

```
EduNomad/
├── config/           # Configuración global (settings, urls, wsgi)
├── core/             # Usuarios, perfiles, roles, dashboard
├── courses/          # Cursos, lecciones, niveles
├── practice/         # Ejercicios y prácticas morfosintácticas
├── solver/           # Lógica de resolución y corrección
├── subscription/     # Suscripciones y control de acceso (paywall)
├── media/            # Archivos subidos por usuarios
├── manage.py
├── requirements.txt
└── README.md
```

---

## 📚 Modelo académico de aprendizaje

### Cursos

* Organizados por nivel (A1–C2)
* Cada curso contiene lecciones progresivas
* Ejemplo inicial: **Castellano A1 – Escritura básica**

### Lecciones

* Introducción teórica breve
* Ejemplos guiados
* Acceso gratuito a contenidos esenciales

### Ejercicios (Practice)

* Ejercicios morfosintácticos manuales
* Respuesta escrita o selección guiada
* Corrección inmediata o diferida

### Progreso

* Seguimiento individual por curso y lección
* Métricas de avance claras
* Base para análisis longitudinal

---

## 🔐 Monetización ética (Paywall)

EduNomad implementa un modelo de monetización ética mediante **decoradores de acceso**:

* **FREE**: acceso completo al aprendizaje esencial
* **PREMIUM**: herramientas avanzadas (análisis, feedback extendido, IA)

Este enfoque garantiza que **ningún estudiante quede excluido del aprendizaje básico**.

---

## 🤖 Integración futura de Inteligencia Artificial

La IA será incorporada progresivamente con fines pedagógicos:

* Análisis de errores morfosintácticos frecuentes
* Retroalimentación personalizada
* Ejercicios adaptativos según lengua materna
* Asistencia en reescritura guiada

La IA **no reemplaza al estudiante**, sino que acompaña su proceso cognitivo.

---

## 🌍 Proyección intercultural y multilingüe

El diseño contempla estudiantes cuya lengua materna sea:

* Mandarín
* Inglés
* Hindi
* Español
* Árabe
* Bengalí
* Portugués
* Ruso
* Urdu
* Francés

El enfoque contrastivo permitirá adaptar explicaciones y ejemplos.

---

## 🧪 Estado del proyecto

* ✅ Arquitectura base implementada
* ✅ Modelos académicos definidos
* ✅ Primer curso estructurado
* ✅ Control de versiones en GitHub
* 🚧 Integración IA (fase futura)
* 🚧 Despliegue en producción

---

## 👤 Autor

**Hernán Acevedo Mar**
Proyecto académico-tecnológico en desarrollo
Investigación en educación, lenguaje y software

---

## 📜 Licencia

Este proyecto se publica con fines educativos y de investigación. La licencia específica será definida en fases posteriores del desarrollo.

---

> EduNomad no es solo una plataforma: es un laboratorio pedagógico para la escritura consciente en lengua castellana.

