from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from negocio.models import Comentario


class ComentarioTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='secret123',
            email='test@example.com',
        )

    def test_crear_comentario_usa_usuario_logueado(self):
        self.client.login(username='testuser', password='secret123')
        response = self.client.post(
            reverse('crear_comentario'),
            {
                'comentario': 'Este comentario tiene mas de veinticinco caracteres para pasar la validacion.',
            },
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        comentario = Comentario.objects.latest('id')
        self.assertEqual(comentario.username, 'testuser')
        self.assertEqual(comentario.correo, 'test@example.com')