import re
import random


class ChatBot:
    def __init__(self):
        self.respuestas = [
            {
                'respuesta_bot': '¡Hola! ¿En qué puedo ayudarte?',
                'palabras_clave': ['hola', 'buenas', 'saludos'],
                'respuesta_sencilla': True
            },
            {
                'respuesta_bot': 'Estoy bien, ¿y tú?',
                'palabras_clave': ['estás', 'sientes'],
                'palabras_obligatorias': ['cómo']
            },
            {
                'respuesta_bot': 'Cada persona tiene sus propias preferencias en cuanto a jugadores de fútbol. Personalmente, tengo una inclinación por Messi, pero respeto cualquier otra preferencia que puedas tener. ¡El fútbol nos brinda una diversidad de talentos para admirar!',
                'palabras_clave': ['messi', 'ronaldo'],
                'respuesta_sencilla': True
            },
            {
                'respuesta_bot': 'Hasta luego, ¡que tengas un buen día!',
                'palabras_clave': ['adios', 'chau'],
                'respuesta_sencilla': True
            },
            {
                'respuesta_bot': 'Estoy aquí para ayudarte. ¿En qué necesitas?',
                'palabras_clave': ['ayuda', 'ayúdame'],
                'respuesta_sencilla': True
            },
            {
                'respuesta_bot': '¡Me encanta charlar contigo!',
                'palabras_clave': ['conversar', 'charla'],
                'respuesta_sencilla': True
            },
            {
                'respuesta_bot': 'La tecnología es fascinante. ¿Tienes alguna opinión sobre ello?',
                'palabras_clave': ['tecnología', 'opinión'],
                'respuesta_sencilla': True
            },
            {
                'respuesta_bot': '¡Esa es una idea genial! ¿Tienes más ideas que quieras compartir?',
                'palabras_clave': ['idea', 'propuesta'],
                'respuesta_sencilla': True
            },
            {
                'respuesta_bot': 'Estamos ubicados en SENATI - Independencia.',
                'palabras_clave': ['ubicación', 'estás'],
                'respuesta_sencilla': True
            },
            {
                'respuesta_bot': 'La ingeniería de software es una rama de las ciencias de la computación que se enfoca en la creación de software confiable y de calidad, utilizando métodos y técnicas de ingeniería para su desarrollo y mantenimiento.',
                'palabras_clave': ['explicame', 'software'],
                'palabras_obligatorias': ['ing', 'de', 'software']
            }

        ]

        self.respuesta_desconocida = [
            'Puedes decirlo de nuevo?', 'No estoy seguro de lo que quieres', 'Lamento no saber la respuesta a eso']

    def obtener_respuesta(self, mensaje_usuario):
        mensaje_entrada = re.split(r'\s|[,;.:!?-_]\s', mensaje_usuario.lower())
        respuesta_bot = self.elegir_respuesta(mensaje_entrada)
        return respuesta_bot

    def calcular_probabilidad_mensaje(self, mensaje_usuario, palabras_clave, respuestas_sencillas=False, palabras_obligatorias=[]):
        mensajes_especificos = sum(
            1 for palabra in mensaje_usuario if palabra in palabras_clave)
        palabras_requeridas = all(
            palabra in mensaje_usuario for palabra in palabras_obligatorias)
        porcentaje = mensajes_especificos / len(palabras_clave)

        if palabras_requeridas or respuestas_sencillas:
            return int(porcentaje * 100)
        else:
            return 0

    def elegir_respuesta(self, mensaje_entrada):
        probabilidad_respuesta = {}

        for respuesta_info in self.respuestas:
            self.agregar_probabilidad(
                respuesta_info, mensaje_entrada, probabilidad_respuesta)

        mejor_probabilidad = max(
            probabilidad_respuesta, key=probabilidad_respuesta.get)

        return random.choice(self.respuesta_desconocida) if probabilidad_respuesta[mejor_probabilidad] < 1 else mejor_probabilidad

    def agregar_probabilidad(self, respuesta_info, mensaje_entrada, propabilidad_repsuesta):
        respuesta_bot = respuesta_info['respuesta_bot']
        palabras_clave = respuesta_info['palabras_clave']
        respuesta_sencilla = respuesta_info.get('respuesta_sencilla', False)
        palabras_obligatorias = respuesta_info.get(
            'palabras_obligatorias', [])

        probabilidad = self.calcular_probabilidad_mensaje(
            mensaje_entrada, palabras_clave, respuesta_sencilla, palabras_obligatorias)
        propabilidad_repsuesta[respuesta_bot] = probabilidad
