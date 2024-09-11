# Desarrollo de un Tutor Virtual basado en ChatGPT para la Asignatura de Sistemas Inteligentes en la ESII-AB

> Este proyecto corresponde al Trabajo Fin de Grado realizado por Iván Fernández García.


## Sobre el proyecto 📝

El aprendizaje autónomo y las tutorías personalizadas son componentes esenciales del proceso educativo moderno. Sin embargo, no siempre es posible contar con un tutor humano disponible para resolver dudas al momento. Un tutor virtual puede complementar la enseñanza tradicional, ofreciendo respuestas inmediatas, adaptabilidad a distintos ritmos de aprendizaje y disponibilidad a todas horas.

El avance de la inteligencia artificial ha permitido el surgimiento de herramientas capaces de entender a los humanos e interactuar con ellos en lenguaje natural. Una de estas herramientas, ChatGPT, ha mostrado ser particularmente efectiva en diversas aplicaciones. En el ámbito educativo, hay un potencial aún no explotado para el uso de esta tecnología como tutor virtual en asignaturas específicas.

El objetivo de este Trabajo Fin de Grado ha sido desarrollar un tutor virtual basado en ChatGPT que adapte sus respuestas al contenido y a las metodologías de la asignatura de Sistemas Inteligentes, impartida en el tercer curso del Grado en Ingeniería Informática en la Escuela Superior de Ingeniería Informática de Albacete.

Para ello, se ha integrado la API de OpenAI en un chatbot y se ha optimizado el comportamiento del tutor virtual con el fin de obtener respuestas más afines que ChatGPT frente a preguntas relacionadas con la asignatura. Ha sido un proyecto marcado por el estudio de tecnologías emergentes que evolucionan constantemente, las cuales nos permiten mejorar el rendimiento de ChatGPT respecto al caso de uso específico que queremos explotar.


## Introducción 👋🏼

El proyecto se divide en dos partes claramente diferenciadas:

- **Desarrollo de la aplicación.** Se ha integrado la API de OpenAI (más concretamente, Assistants API) en un chatbot.
- **Optimización del tutor virtual.** Se han adaptado las respuestas del asistente anterior al contenido de la asignatura.

El código referente al desarrollo de la aplicación se encuentra en este repositorio, que incluye tanto la integración del chatbot de Voiceflow en una aplicación web como la integración de Assistants API para generar las respuestas utilizando un GPT como modelo base. Independientemente de su integración en la aplicación, la implementación del chatbot en Voiceflow no requiere código y la lógica conversacional utilizada se puede apreciar en la memoria del trabajo.

Por otra parte, la optimización del comportamiento del asistente se ha realizado a través de la propia plataforma de OpenAI sin necesidad de código. Las instrucciones y archivos utilizados, así como la evolución de este proceso, se puede apreciar en la memoria del trabajo. Por lo tanto, no se ha proporcionado ningún archivo de código relacionado con esta tarea.

Para comprender en profundidad la arquitectura del proyecto y las posibilidades que nos ofrece Assistants API, se recomienda encarecidamente leer la memoria del trabajo antes de comenzar a trabajar con el código.


## Estructura 📂

- ``Memoria_ChatGPT-SSII.pdf``: Memoria del trabajo.
- ``Presentacion_ChatGPT-SSII.pdf``: Diapositivas utilizadas para la defensa del trabajo.
- ``app-chatbot``: Carpeta que contiene el código correspondiente a la aplicación web principal a través de la que se puede interactuar con el chatbot. Contiene el archivo ``app.py`` y una plantilla ``index.html`` ubicada en la carpeta ``templates``.
- ``gpt-to-web``: Carpeta que contiene el código correspondiente a la aplicación web en la que se ha integrado OpenAI API y actúa como puente entre el chatbot de Voiceflow y la API. Contiene un único archivo ``main.py`` con todo lo necesario.


## Objetivo y motivación 🎯

El objetivo de este repositorio no es proporcionar la posibilidad de interactuar con el tutor virtual, sino los recursos necesarios para poder crear fácilmente nuevas herramientas basadas en ChatGPT que estén orientadas a casos de uso específicos.

Una de las mayores ventajas de las tecnologías y herramientas utilizadas para llevar a cabo el proyecto es que su implementación es en mayor medida reutilizable para cualquier caso de uso que se nos presente, ya que actuar como un tutor virtual para una asignatura específica es simplemente una posibilidad más.

Assistants API nos permite personalizar las respuestas de un modelo GPT base a través de instrucciones y archivos de utilidad con información adicional. Este proceso para optimizar el comportamiento del asistente se puede realizar directamente desde la plataforma de OpenAI, por lo que el desarrollo de la aplicación se ha realizado de manera independiente y para que las respuestas las genere un asistente ya optimizado basta con utilizar el identificador correspondiente.

Este proyecto involucra información sensible que no ha sido directamente proporcionada:
- **OpenAI API Key.** La clave de la API nos permite acceder a los servicios de OpenAI como cliente a través de Python.
- **Assistant ID.** Este identificador nos permite gestionar qué asistente es el encargado de generar las respuestas cuando el chatbot responda a las consultas del usuario.
- **Voiceflow Project ID.** Este identificador nos permite gestionar qué chatbot implementado en un proyecto de Voiceflow es integrado como chat web en la aplicación.

Por lo tanto, para crear una herramienta como la de este proyecto será necesario que cada desarrollador utilice estos valores secretos y los proteja correctamente.


## Cómo crear tu propio asistente 🤖

Antes de comenzar, es importante aclarar que la integración de OpenAI API que se ha realizado se corresponde con la lógica del chatbot. En caso de realizar modificaciones en su implementación, se debe tener en cuenta que esto podría requerir cambios adicionales en el código para cubrir todas las funcionalidades deseadas. En este proyecto se ha trabajado con un flujo simple en el que se crea un hilo por conversación y las respuestas las genera un único asistente. También es fundamental trabajar con una versión reciente de la librería de OpenAI. Más concretamente, en este proyecto se ha utilizado la versión 1.34.0.

#### Paso 1: Personalizar la clave de OpenAI API
- Acceder a la plataforma de [OpenAI API](https://platform.openai.com/).
- Iniciar sesión o registrarse.
- Crear una nueva clave secreta (Settings > Your profile > User API keys > Create new secret key).
- Utilizar este valor en el archivo ``gpt-to-web/main.py``. Se recomienda protegerlo y acceder a él en lugar de escribirlo directamente.

#### Paso 2: Personalizar el identificador del asistente
- Acceder a la plataforma de [OpenAI API](https://platform.openai.com/).
- Iniciar sesión o registrarse.
- Crear un nuevo asistente de Assistants API (Dashboard > Assistants > Create).
- Utilizar su identificador (tendrá formato "asst_...") en el archivo ``gpt-to-web/main.py``. Se recomienda protegerlo y acceder a él en lugar de escribirlo directamente.

#### Paso 3: Personalizar el chatbot de Voiceflow
- Acceder a [Voiceflow](https://www.voiceflow.com/)
- Crear un nuevo agente con la lógica conversacional que se muestra en la memoria.
- Adaptar los mensajes de bienvenida del asistente al caso de uso.
- Utilizar la URL de la aplicación web del archivo ``gpt-to-web/main.py``, seguida de la ruta ``/start`` para la creación del hilo y ``/chat`` para la generación de respuestas.
- Personalizar la integración del chat web (Nombre, colores, iconos, etc.).
- Utilizar el identificador del proyecto de Voiceflow en el archivo ``app-chatbot/templates/index.html``. Se recomienda protegerlo y acceder a él en lugar de escribirlo directamente.

#### Paso 4: Comprobar el correcto funcionamiento
- Ejecutar la aplicación web del archivo ``app-chatbot/app.py``. La aplicación web del archivo ``gpt-to-web/main.py`` debe estar también en funcionamiento.
- Interactuar con el asistente y comprobar que la lógica conversacional funciona correctamente. Debemos recordar que las respuestas del asistente que estamos utilizando todavía no se han adaptado al caso de uso específico.

#### Paso 5: Optimizar el comportamiento del asistente
- Acceder a la plataforma de [OpenAI API](https://platform.openai.com/).
- Iniciar sesión o registrarse.
- Acceder a la configuración del asistente creado en el paso 3 (Dashboard > Assistants).
- Personalizar el comportamiento del asistente a través de instrucciones y de las herramientas que proporciona Assistants API. El modelo GPT base y los parámetros utilizados dependerán del proyecto, pero es fundamental barajar diferentes alternativas en función de los costes y la complejidad del caso de uso concreto. Es recomendable comprobar las respuestas proporcionadas directamente desde la herramienta Playground de OpenAI, y no interactuando en la aplicación. Por último, el código cubre el uso de la búsqueda en archivos y el intérprete de código, aunque no es necesario tener las herramientas activadas para que funcione correctamente. Sin embargo, se deben aprovechar para sacar el máximo partido a este servicio de OpenAI, puesto que en caso contrario se podría haber optado por una opción más sencilla.

## Contacto 📩

Si tienes alguna pregunta, no dudes en contactarme.

- **Correo electrónico**: [fdez.garcia.ivan@gmail.com](mailto:fdez.garcia.ivan@gmail.com)
- **LinkedIn**: [Iván Fernández García](linkedin.com/in/ivan-fdez-garcia)

También puedes abrir un nuevo asunto a través de [GitHub Issues](https://github.com/ivan-fdez-garcia/ChatGPT-SSII/issues) para reportar problemas o sugerencias.
